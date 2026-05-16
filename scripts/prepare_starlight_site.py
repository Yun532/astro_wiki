#!/usr/bin/env python3
"""Mirror wiki/ and wiki_textbook/ into an Astro Starlight content directory."""
from pathlib import Path
import shutil, re
ROOT=Path(__file__).resolve().parents[1]
BASE_PATH='/astro_wiki'
WIKI=ROOT/'wiki'; TEXTBOOK=ROOT/'wiki_textbook'; SITE=ROOT/'site'; DOCS=SITE/'src'/'content'/'docs'; PUBLIC=SITE/'public'; FIGPUB=PUBLIC/'figures'
DOCS.mkdir(parents=True,exist_ok=True); PUBLIC.mkdir(parents=True,exist_ok=True)
if DOCS.exists(): shutil.rmtree(DOCS)
DOCS.mkdir(parents=True,exist_ok=True)
wiki_files=sorted(WIKI.rglob('*.md')) if WIKI.exists() else []
textbook_files=sorted(TEXTBOOK.rglob('*.md')) if TEXTBOOK.exists() else []
files=wiki_files+textbook_files
by_stem={p.stem.lower():p for p in files}

def frontmatter_fix(txt,p):
    if not txt.startswith('---'): return f'---\ntitle: "{p.stem}"\n---\n\n'+txt
    parts=txt.split('---',2); fm=parts[1]; body=parts[2]
    if not re.search(r'^title\s*:', fm, re.M): fm=f'title: "{p.stem}"\n'+fm
    return '---'+fm+'---'+body

def content_rel(target):
    target=target.resolve()
    if WIKI.resolve() in target.parents:
        return target.relative_to(WIKI)
    if TEXTBOOK.resolve() in target.parents:
        return Path('textbook')/target.relative_to(TEXTBOOK)
    raise ValueError(f'not a content file: {target}')

def link_for(target):
    rel=content_rel(target).with_suffix('').as_posix()
    if rel.endswith('/index'): rel=rel[:-6]
    return f'{BASE_PATH}/{rel}/'

def convert_links(txt,src_file):
    def obsidian_repl(m):
        raw=m.group(1); label=raw
        if '|' in raw: raw,label=raw.split('|',1)
        key=raw.split('#')[0].strip().lower(); target=by_stem.get(Path(key).stem.lower())
        return f'[{label}]({link_for(target)})' if target else label
    txt=re.sub(r'\[\[([^\]]+)\]\]', obsidian_repl, txt)
    def markdown_repl(m):
        label,href=m.group(1),m.group(2)
        if href.startswith(('http://','https://','/')) or not href.split('#')[0].endswith('.md'):
            return m.group(0)
        href_path,fragment=(href.split('#',1)+[''])[:2] if '#' in href else (href,'')
        target=(src_file.parent/href_path).resolve()
        try:
            if target.exists() and (WIKI.resolve() in target.parents or TEXTBOOK.resolve() in target.parents):
                link=link_for(target)
                if fragment: link=f'{link}#{fragment}'
                return f'[{label}]({link})'
        except Exception:
            pass
        return m.group(0)
    return re.sub(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)', markdown_repl, txt)

def convert_images(txt,src_file):
    def repl(m):
        alt,path=m.group(1),m.group(2)
        if path.startswith('http') or path.startswith('/'): return m.group(0)
        img=(src_file.parent/path).resolve()
        try:
            if img.exists() and (WIKI.resolve() in img.parents or TEXTBOOK.resolve() in img.parents):
                rel=content_rel(img).as_posix(); out=FIGPUB/rel; out.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(img,out)
                return f'![{alt}](/figures/{rel})'
        except Exception: pass
        return m.group(0)
    return re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', repl, txt)
count=0
for p in files:
    out=DOCS/content_rel(p); out.parent.mkdir(parents=True,exist_ok=True)
    txt=convert_images(convert_links(frontmatter_fix(p.read_text(encoding='utf-8',errors='ignore'),p),p),p)
    out.write_text(txt,encoding='utf-8'); count+=1
graph=WIKI/'90_元信息'/'knowledge_graph.json'
if graph.exists(): shutil.copy2(graph, PUBLIC/'knowledge_graph.json')
print(f'[OK] wrote Starlight docs mirror: {DOCS}')
print(f'[OK] exported pages: {count}')
if graph.exists(): print('[OK] copied graph: site/public/knowledge_graph.json')
