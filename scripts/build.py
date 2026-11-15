"""Build Markdown inventories and the offline browser data from local JSON."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
def load(name):
    return json.loads((ROOT / 'data' / name).read_text())
def md(s):
    return str(s).replace('|', '\\|').replace('\n', ' ')
def table(headers, rows):
    return '| ' + ' | '.join(headers) + ' |\n|' + '|'.join([' --- ']*len(headers)) + '|\n' + ''.join('| '+' | '.join(md(c) for c in row)+' |\n' for row in rows)
def write(path, text):
    (ROOT / path).write_text(text.rstrip()+'\n')

papers=load('papers.json'); inventories=load('inventories.json'); tools=load('tools.json')
code_links=load('code_links.json')
paper_links={r['id']:r for r in load('paper_links.json')}
byid={p['id']:p for p in papers}
for g in inventories:
    text=f"# {g['title']}\n[Back to repository](../README.md) · Manuscript Section {g['section']}\n\n{g['summary']}\n\n> {g['caveat']}\n\n"
    text+='We summarize representative work reviewed in our survey below. PA = pixel alignment; VA = voxel alignment; SDS = score distillation. A dash indicates information not reported in the cited source.\n\n'
    groups=list(dict.fromkeys(r['group'] for r in g['rows']))
    for group in groups:
        if group: text+='## '+group+'\n\n'
        rows=[]
        for r in g['rows']:
            if r['group']!=group: continue
            cells=list(r['cells'])
            links=[]
            for key in r['citations']:
                p=byid[key]
                links.append(f"[Reference](papers.md#{key})")
                if key in code_links: links.append(f"[Code]({code_links[key]['url']})")
            cells.append(' · '.join(links) or 'Not cited in source table')
            rows.append(cells)
        text+=table(g['headers']+['Source'],rows)+'\n'
    write('resources/'+g['id']+'.md',text)

text='# Paper Index\n[Back to repository](../README.md) · [BibTeX](../data/references.bib) · [Searchable catalogue](../homepage/index.html)\n\n'
text+='We collect the methods, datasets, and foundational studies discussed in our survey. Follow each title to the paper source, and use the PDF, project, and code links where available. Category links connect papers to our mechanism-based taxonomy; hybrid methods may appear in more than one inventory. Earlier titles are retained as aliases where relevant.\n\n'
years=sorted({p['year'] for p in papers},reverse=True)
text+='Years: '+' · '.join(f'[{y}](#year-{y})' for y in years)+'\n\n'
for y in years:
    text+=f'<a id="year-{y}"></a>\n## {y}\n\n'
    for p in sorted((p for p in papers if p['year']==y),key=lambda p:p['title'].lower()):
        title=f"[{p['title']}]({p['url']})" if p['url'] else p['title']
        text+=f'<a id="{p["id"]}"></a>\n### {title}\n\n{p["authors"]}. **{p["venue"] or "Venue not specified"}**, {p["year"]}.\n\n'
        if p.get('aliases'): text+='Earlier title / alias: '+'; '.join(p['aliases'])+'.\n\n'
        if p['inventory_groups']:
            text+='Inventory: '+' · '.join(f'[{next(g["title"] for g in inventories if g["id"]==i)}]({i}.md)' for i in p['inventory_groups'])+'\n\n'
        else: text+='Related foundations and context for our survey.\n\n'
        if not p['url']: text+='No direct identifier supplied in the bibliography. Locate the work by its full title; no URL has been guessed.\n\n'
        link=paper_links[p['id']]
        for field,label in [('pdf_url','PDF'),('project_url','Project'),('code_url','Code')]:
            if link[field]: text+=f"[{label}]({link[field]}) · "
        text=text.rstrip(' · ')+'\n\n'
        text+='<details><summary>BibTeX</summary>\n\n```bibtex\n'+p['bibtex'].strip()+'\n```\n</details>\n\n'
write('resources/papers.md',text)
text='# Models and Tools\n[Back to repository](../README.md)\n\nWe collect reusable components for body modeling, camera estimation, differentiable rendering, generative guidance, and evaluation. These tools complement the methods reviewed in our survey; they are not a benchmark ranking. Please consult each project for installation instructions, model access, and licensing terms.\n\n'
for category in dict.fromkeys(t['category'] for t in tools):
    text+='## '+category+'\n\n'
    for t in tools:
        if t['category']==category: text+=f'### [{t["name"]}]({t["url"]})\n\n{t["purpose"]}\n\n**Caution:** {t["caveat"]}\n\n'
write('resources/tools.md',text)
bundle={'papers':papers,'inventories':inventories,'tools':tools,'code_links':code_links,'paper_links':paper_links}
text='# Implementation Entry Points\n[Back to repository](../README.md)\n\nWe highlight official implementations spanning the main reconstruction mechanisms. Additional project and code links are available in the [paper index](papers.md). Please cite the corresponding papers and follow each implementation\'s licensing and data-access requirements.\n\n'
text+=table(['Paper','Official code'],[[f"[{byid[k]['title']}](papers.md#{k})",f"[Repository]({v['url']})"] for k,v in code_links.items()])
write('resources/implementations.md',text)
write('homepage/catalogue.js','window.CATALOGUE = '+json.dumps(bundle,ensure_ascii=False).replace('</','<\\/')+';')
print(f'Built {len(papers)} paper records, {sum(len(g["rows"]) for g in inventories)} inventory rows, and {len(tools)} resources.')
