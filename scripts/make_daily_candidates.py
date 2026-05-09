#!/usr/bin/env python3
from pathlib import Path
from datetime import date
ROOT=Path(__file__).resolve().parents[1]
out=ROOT/'wiki'/'90_元信息'/'daily-candidates'/f'{date.today().isoformat()}.md'
out.parent.mkdir(parents=True,exist_ok=True)
content = f"""---
title: 每日文献候选 {date.today().isoformat()}
type: meta
status: seed
last_updated: {date.today().isoformat()}
tags: [daily-candidates]
source_count: 0
confidence: low
related: []
---

# 每日文献候选

TODO: add source

## must read

## relevant

## maybe

## not relevant
"""
out.write_text(content,encoding='utf-8')
print(f'[OK] wrote {out}')
