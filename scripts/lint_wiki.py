#!/usr/bin/env python3
"""Basic wiki lint."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
WIKI=ROOT/'wiki'
REPORT=WIKI/'90_元信息'/'lint-report.md'
REQ=['title','type','status','last_updated','tags','source_count','confidence','related']
files=sorted(WIKI.rglob('*.md')) if WIKI.exists() else []
missing_fm=[]; missing_fields=[]; todos=[]; needs=[]; orphan=[]
for p in files:
    txt=p.read_text(encoding='utf-8',errors='ignore')
    if not txt.startswith('---'):
        missing_fm.append(p); continue
    fm=txt.split('---',2)[1] if txt.count('---')>=2 else ''
    miss=[k for k in REQ if not re.search(rf'^{re.escape(k)}\s*:', fm, re.M)]
    if miss: missing_fields.append((p,miss))
    if 'TODO: add source' in txt: todos.append(p)
    if re.search(r'^status:\s*needs-source', fm, re.M): needs.append(p)
    if '[[' not in txt and '](' not in txt and p.name not in ('index.md','lint-report.md'):
        orphan.append(p)
REPORT.parent.mkdir(parents=True,exist_ok=True)
lines=['---','title: Lint report','type: report','status: seed','last_updated: 2026-05-09','tags: []','source_count: 0','confidence: low','related: []','---','','# Lint report','',f'- pages: {len(files)}',f'- missing_frontmatter: {len(missing_fm)}',f'- missing_fields: {len(missing_fields)}',f'- orphan_like: {len(orphan)}',f'- needs_source: {len(needs)}',f'- TODO source placeholders: {len(todos)}','']
if missing_fm: lines += ['## Missing frontmatter','']+[f'- {p.relative_to(ROOT)}' for p in missing_fm]+['']
if missing_fields: lines += ['## Missing fields','']+[f'- {p.relative_to(ROOT)}: {miss}' for p,miss in missing_fields]+['']
if orphan: lines += ['## Orphan-like pages','']+[f'- {p.relative_to(ROOT)}' for p in orphan]+['']
if todos: lines += ['## TODO source placeholders','']+[f'- {p.relative_to(ROOT)}' for p in todos[:200]]
REPORT.write_text('\n'.join(lines),encoding='utf-8')
print(f"[OK] lint pages={len(files)} missing_frontmatter={len(missing_fm)} missing_fields={len(missing_fields)} orphan_like={len(orphan)} needs_source={len(needs)} todo_source={len(todos)}")
