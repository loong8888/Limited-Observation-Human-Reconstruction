'use strict';
const data = window.CATALOGUE;
const $ = id => document.getElementById(id);
const escapeHTML = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let tab='papers';
const names=Object.fromEntries(data.inventories.map(g=>[g.id,g.title]));
const shortNames={template:'Template fitting',feature:'Feature alignment',temporal:'Temporal aggregation',priorguided:'Prior-guided',feedforward:'Feed-forward',condgen:'Conditional generation',datasets:'Dataset source'};
const paperMap=Object.fromEntries(data.papers.map(p=>[p.id,p]));
const context=new Map();
for(const g of data.inventories) for(const row of g.rows) for(const id of row.citations) context.set(id,(context.get(id)||'')+' '+row.cells.join(' '));
for(const g of data.inventories) $('family').add(new Option(g.title,g.id));
for(const year of [...new Set(data.papers.map(p=>p.year))].sort().reverse()) $('year').add(new Option(year,year));
const external=(url,label)=>'<a href="'+escapeHTML(url)+'" target="_blank" rel="noopener noreferrer">'+escapeHTML(label)+'</a>';
function render(){
 const query=$('query').value.toLowerCase().trim();
 const terms=query.split(/\s+/).filter(Boolean);
 const matches=s=>terms.every(t=>s.toLowerCase().includes(t));
 for(const id of ['family-label','year-label','sort-label']) $(id).hidden=tab!=='papers';
 $('results').setAttribute('aria-labelledby',tab+'-tab');
 document.querySelectorAll('[data-tab]').forEach(b=>{b.setAttribute('aria-selected',String(b.dataset.tab===tab));b.tabIndex=b.dataset.tab===tab?0:-1;});
 if(tab==='papers'){
  const filtered=data.papers.filter(p=>(!$('family').value||p.inventory_groups.includes($('family').value))&&(!$('year').value||p.year===$('year').value)&&matches([p.title,p.authors,p.venue,p.id,context.get(p.id)||''].join(' ')));
  filtered.sort((a,b)=>$('sort').value==='title'?a.title.localeCompare(b.title):($('sort').value==='oldest'?a.year.localeCompare(b.year):b.year.localeCompare(a.year))||a.title.localeCompare(b.title));
  $('count').textContent=filtered.length+' paper'+(filtered.length===1?'':'s');
  $('scope').textContent='Explore our method families and related foundations; hybrid systems may span several families.';
  $('results').innerHTML=filtered.map(p=>'<article class="entry"><div class="year">'+escapeHTML(p.year)+'</div><div><h2>'+(p.url?external(p.url,p.title):escapeHTML(p.title))+'</h2><p class="meta">'+escapeHTML(p.authors)+'</p><p class="venue">'+escapeHTML(p.venue||'Venue not specified')+'</p><div class="badges">'+(p.inventory_groups.length?p.inventory_groups.map(g=>'<span class="badge '+g+'">'+escapeHTML(shortNames[g])+'</span>').join(''):'<span class="badge">Foundations / context</span>')+'</div></div><div class="links">'+(p.url?external(p.url,'Paper ↗'):'<span>No direct link</span>')+'<button type="button" data-copy="'+escapeHTML(p.id)+'">Copy BibTeX</button><a href="../resources/papers.md#'+encodeURIComponent(p.id)+'">Record</a></div></article>').join('');
 } else if(tab==='datasets'){
  const g=data.inventories.find(g=>g.id==='datasets');const rows=g.rows.filter(r=>matches(r.cells.join(' ')));
  $('count').textContent=rows.length+' datasets';$('scope').textContent='Scans, fitted bodies, held-out views, and generated supervision are not interchangeable references.';
  $('results').innerHTML=rows.map(r=>'<article class="dataset"><h2>'+escapeHTML(r.name)+'</h2><dl class="facts">'+r.cells.slice(1).map((c,i)=>'<div><dt>'+escapeHTML(g.headers[i+1])+'</dt><dd>'+escapeHTML(c)+'</dd></div>').join('')+'</dl><p class="meta">'+r.citations.map(id=>paperMap[id].url?external(paperMap[id].url,'Source paper'):'<a href="../resources/papers.md#'+id+'">Reference</a>').join(' · ')+'</p></article>').join('');
 } else {
  const rows=data.tools.filter(t=>matches([t.name,t.category,t.purpose,t.caveat].join(' ')));
  $('count').textContent=rows.length+' resources';$('scope').textContent='Reusable tools and complementary collections; follow each project for setup, data access, and licensing.';
  $('results').innerHTML=rows.map(t=>'<article class="tool"><small>'+escapeHTML(t.category)+'</small><h2>'+external(t.url,t.name)+'</h2><p>'+escapeHTML(t.purpose)+'</p><p class="meta">'+escapeHTML(t.caveat)+'</p></article>').join('');
 }
 if(tab==='papers') for(const button of document.querySelectorAll('[data-copy]')){
  const record=data.paper_links[button.dataset.copy];
  if(record) for(const [field,label] of [['pdf_url','PDF'],['project_url','Project'],['code_url','Code']]){
   if(!record[field])continue;
   const a=document.createElement('a');a.href=record[field];a.textContent=label+' ↗';a.title=label;a.target='_blank';a.rel='noopener noreferrer';button.parentElement.appendChild(a);
  }
 }
 if(!$('results').children.length) $('results').innerHTML='<p class="empty">No matching entries.</p>';
}
$('query').addEventListener('input',render);
for(const id of ['family','year','sort']) $(id).addEventListener('change',render);
$('reset').addEventListener('click',()=>{$('query').value='';$('family').value='';$('year').value='';$('sort').value='newest';render();});
document.querySelectorAll('[data-tab]').forEach(b=>{b.addEventListener('click',()=>{tab=b.dataset.tab;render();});b.addEventListener('keydown',e=>{const tabs=[...document.querySelectorAll('[data-tab]')];let i=tabs.indexOf(b);if(e.key==='ArrowRight') i=(i+1)%tabs.length;else if(e.key==='ArrowLeft') i=(i+tabs.length-1)%tabs.length;else return;e.preventDefault();tabs[i].click();tabs[i].focus();});});
$('results').addEventListener('click',async e=>{
 const button=e.target.closest('[data-copy]'); if(!button)return;
 const text=paperMap[button.dataset.copy].bibtex;
 try {await navigator.clipboard.writeText(text);button.textContent='Copied';}
 catch {const box=document.createElement('textarea');box.value=text;box.style.position='fixed';box.style.left='-9999px';document.body.appendChild(box);box.select();let ok=false;try{ok=document.execCommand('copy');}catch{}box.remove();button.textContent=ok?'Copied':'See record';}
 setTimeout(()=>{if(button.isConnected)button.textContent='Copy BibTeX';},1800);
});
render();
