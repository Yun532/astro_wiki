#!/usr/bin/env python3
"""Build a simple knowledge graph from Markdown links in wiki/."""
from __future__ import annotations
from pathlib import Path
import json, re, csv

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
OUT_DIR = WIKI / "90_元信息"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OBSIDIAN = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
MDLINK = re.compile(r"\[[^\]]+\]\(([^)]+\.md(?:#[^)]+)?)\)")

def node_type(path: Path) -> str:
    s = str(path).replace('\\','/')
    if '00_总览' in s: return '总览'
    if '10_理论' in s: return '理论'
    if '20_天体源' in s: return '天体源'
    if '30_仪器' in s: return '仪器'
    if '40_综合比较' in s: return '综合比较'
    if '50_模型' in s: return '模型'
    if '90_元信息' in s: return '元信息'
    return 'unknown'

def title_of(text: str, path: Path) -> str:
    m = re.search(r"^title:\s*['\"]?(.+?)['\"]?\s*$", text, re.M)
    if m and m.group(1).strip(): return m.group(1).strip()
    h = re.search(r"^#\s+(.+)$", text, re.M)
    if h: return h.group(1).strip()
    return path.stem

files = [p for p in sorted(WIKI.rglob('*.md')) if p.name != 'lint-report.md'] if WIKI.exists() else []
by_stem = {p.stem.lower(): p for p in files}
by_name = {p.name.lower(): p for p in files}
by_rel = {p.relative_to(WIKI).as_posix().lower(): p for p in files}
nodes=[]; edges=[]
for p in files:
    text=p.read_text(encoding='utf-8', errors='ignore')
    rel=p.relative_to(WIKI).as_posix()
    nodes.append({'id': rel, 'title': title_of(text,p), 'path': rel, 'type': node_type(p), 'degree':0})
    targets=[]
    for link in OBSIDIAN.findall(text):
        key=link.strip().lower()
        target=by_stem.get(key) or by_name.get(key+'.md') or by_rel.get(key) or by_rel.get(key+'.md')
        if target: targets.append(target.relative_to(WIKI).as_posix())
    for href in MDLINK.findall(text):
        href=href.split('#')[0]
        candidate=(p.parent / href).resolve()
        try:
            if candidate.exists() and WIKI.resolve() in candidate.parents:
                targets.append(candidate.relative_to(WIKI.resolve()).as_posix())
        except Exception:
            pass
    for t in sorted(set(targets)):
        if t != rel: edges.append({'source': rel, 'target': t})

deg={n['id']:0 for n in nodes}
for e in edges:
    deg[e['source']]=deg.get(e['source'],0)+1
    deg[e['target']]=deg.get(e['target'],0)+1
for n in nodes: n['degree']=deg.get(n['id'],0)
(OUT_DIR/'knowledge_graph.json').write_text(json.dumps({'nodes':nodes,'edges':edges},ensure_ascii=False,indent=2),encoding='utf-8')
with (OUT_DIR/'knowledge_graph_edges.csv').open('w',newline='',encoding='utf-8') as f:
    wr=csv.DictWriter(f,fieldnames=['source','target']); wr.writeheader(); wr.writerows(edges)
print(f"[OK] graph nodes={len(nodes)} edges={len(edges)}")
