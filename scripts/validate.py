"""Offline consistency checks; no claim of remote or bibliographic verification."""
from pathlib import Path
import json, re
from urllib.parse import unquote

ROOT=Path(__file__).resolve().parents[1]
errors=[]
papers=json.loads((ROOT/'data/papers.json').read_text())
paper_links=json.loads((ROOT/'data/paper_links.json').read_text())
if len(paper_links)!=len(papers) or any(not r.get('source_url') for r in paper_links): errors.append('Missing per-paper source URL')
groups=json.loads((ROOT/'data/inventories.json').read_text())
ids={p['id'] for p in papers}; gids={g['id'] for g in groups}
code_links=json.loads((ROOT/'data/code_links.json').read_text())
if not set(code_links)<=ids: errors.append('Unknown code-link citation')
if len(ids)!=len(papers): errors.append('Duplicate citation IDs')
bib=(ROOT/'data/references.bib').read_text()
bibids=set(re.findall(r'@\w+\s*\{\s*([^,\s]+)',bib))
if ids!=bibids: errors.append('Bibliography and paper JSON IDs differ')
for p in papers:
    if not p['title'] or not p['year']: errors.append('Incomplete record: '+p['id'])
    if not set(p['inventory_groups'])<=gids: errors.append('Unknown group: '+p['id'])
    if p['url'] and not p['url'].startswith(('https://','http://')): errors.append('Invalid URL: '+p['id'])
    expected={g['id'] for g in groups if any(p['id'] in r['citations'] for r in g['rows'])}
    if set(p['inventory_groups'])!=expected: errors.append('Inconsistent memberships: '+p['id'])
for g in groups:
    for r in g['rows']:
        if len(r['cells'])!=len(g['headers']): errors.append('Column mismatch: '+r['name'])
        if not set(r['citations'])<=ids: errors.append('Unknown citation: '+r['name'])
        if any('\\' in c for c in r['cells']): errors.append('Residual TeX: '+r['name'])
for f in list(ROOT.rglob('*.md'))+list((ROOT/'homepage').glob('*.html')):
    text=f.read_text()
    links=re.findall(r'\]\(([^)]+)\)',text)+re.findall(r'(?:href|src)="([^"]+)"',text)
    for link in links:
        if link.startswith(('http:','https:','mailto:','#','data:')): continue
        path,_,anchor=link.partition('#')
        dest=(f.parent/unquote(path)).resolve()
        if not dest.exists(): errors.append(f'{f.relative_to(ROOT)}: missing {link}')
        elif anchor and dest.name=='papers.md' and anchor not in ids and not anchor.startswith('year-'):
            errors.append('Unknown paper anchor: '+anchor)
bundle=(ROOT/'homepage/catalogue.js').read_text()
actual=json.loads(bundle.removeprefix('window.CATALOGUE = ').strip().removesuffix(';'))
if actual['papers']!=papers or actual['inventories']!=groups or actual['code_links']!=code_links or actual['tools']!=json.loads((ROOT/'data/tools.json').read_text()): errors.append('Stale homepage bundle')
if errors: raise SystemExit('\n'.join(errors))
print(f'PASS: {len(papers)} references; {len(groups)} inventories; row widths, memberships, local paths, citation anchors, and browser data checked.')
