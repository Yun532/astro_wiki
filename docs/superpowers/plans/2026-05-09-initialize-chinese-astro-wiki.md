# Initialize Chinese Astro Wiki Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Initialize the Chinese-first high-energy astrophysics Markdown wiki without ingesting any scientific sources.

**Architecture:** Preserve existing project files and fill only the missing knowledge-base structure. Seed pages contain metadata, page purpose, future content scope, related links, and `TODO: add source`, but no scientific claims.

**Tech Stack:** Markdown wiki files, Python utility scripts already present in `scripts/`, PowerShell for local verification.

---

## File Structure

- Create directories under `raw/`, `wiki/`, and `site/` according to `prompts/00_初始化中文知识库.md`.
- Create the specified seed Markdown files under `wiki/`.
- Reuse existing `CLAUDE.md`, `templates/`, `scripts/`, `prompts/`, and `docs/` files without overwriting them.
- Run existing `scripts/lint_wiki.py` and `scripts/build_graph.py` after initialization.

### Task 1: Create initialization directories

**Files:**
- Create: `raw/papers/`, `raw/webpages/`, `raw/data/`, `raw/images/`, `raw/notes/`
- Create: all requested `wiki/` category and subcategory directories
- Create: `site/`

- [ ] **Step 1: Create directories with PowerShell**

Run a PowerShell script that creates only missing directories using `New-Item -ItemType Directory -Force`.

Expected: command exits successfully and no existing files are overwritten.

### Task 2: Create seed pages

**Files:**
- Create: all seed pages listed in `prompts/00_初始化中文知识库.md:94-154`

- [ ] **Step 1: Generate seed page content**

Each page must include this frontmatter shape:

```yaml
---
title: <中文或页面标题>
type: seed
status: seed
last_updated: 2026-05-09
tags: []
source_count: 0
confidence: low
related: []
---
```

Each body must include Chinese sections for page purpose, future content, related pages, and `TODO: add source`.

Expected: all requested seed files exist and contain no scientific conclusions.

### Task 3: Run verification

**Files:**
- Execute: `scripts/lint_wiki.py`
- Execute: `scripts/build_graph.py`

- [ ] **Step 1: Run lint**

Run: `python "E:\astro_wiki_cn\scripts\lint_wiki.py"`

Expected: record exact stdout/stderr and exit status.

- [ ] **Step 2: Run graph build**

Run: `python "E:\astro_wiki_cn\scripts\build_graph.py"`

Expected: record exact stdout/stderr and exit status.

### Task 4: Report initialization result

**Files:**
- No additional file changes.

- [ ] **Step 1: Summarize results**

Report created directory groups, seed page count, lint result, graph result, whether ingest was skipped, and whether site setup can continue.

---

## Self-Review

- Spec coverage: covers directory creation, seed pages, no ingest, lint, graph, and reporting.
- Placeholder scan: no implementation placeholders remain; `TODO: add source` is required page content, not an unfinished plan item.
- Scope check: focused on initialization only; source ingest is explicitly excluded.
