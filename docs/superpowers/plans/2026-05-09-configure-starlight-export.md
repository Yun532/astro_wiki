# Configure Starlight Export Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Configure `site/` as an Astro Starlight site that renders the Chinese-first `wiki/` content without making `site/` the knowledge source.

**Architecture:** Use Astro's official Starlight template to create the site project. Keep `wiki/` authoritative and use `scripts/prepare_starlight_site.py` to mirror wiki Markdown into `site/src/content/docs/`, copy graph data to `site/public/`, and add a standalone `/graph/` page from the existing blueprint.

**Tech Stack:** Astro, Starlight, npm, Python export scripts, GitHub Pages workflow already present.

---

## File Structure

- Create/modify `site/package.json`, `site/package-lock.json`, `site/astro.config.mjs`, `site/src/`, and related Astro template files via official npm scaffolding.
- Create `site/src/pages/graph.astro` from `site_blueprint/graph.astro`.
- Modify `scripts/prepare_starlight_site.py` only if needed for Starlight compatibility discovered during build.
- Keep `wiki/` unchanged except generated source content remains outside it.

### Task 1: Scaffold Astro Starlight site

**Files:**
- Create: `site/package.json`
- Create: `site/package-lock.json`
- Create: `site/astro.config.mjs`
- Create: `site/src/`

- [ ] **Step 1: Run official scaffold**

Run from repository root:

```powershell
npm create astro@latest "E:\astro_wiki_cn\site" -- --template starlight --install --yes
```

Expected: `site/package.json` and `site/astro.config.mjs` exist, dependencies are installed, and the command exits successfully.

### Task 2: Configure Chinese Starlight site

**Files:**
- Modify: `site/astro.config.mjs`
- Modify: `site/package.json` if scripts need adjustment

- [ ] **Step 1: Configure title, locale, sidebar, and graph link**

Set Starlight config to a Chinese title, Chinese default locale, Chinese social/edit options omitted, and a sidebar organized around the wiki's top-level sections.

Expected: Starlight config parses successfully during build.

### Task 3: Add knowledge graph page

**Files:**
- Create: `site/src/pages/graph.astro`

- [ ] **Step 1: Copy existing graph blueprint**

Copy `site_blueprint/graph.astro` to `site/src/pages/graph.astro`.

Expected: `/graph/` route is available in the Astro build and fetches `/knowledge_graph.json`.

### Task 4: Export wiki content into Starlight

**Files:**
- Execute: `scripts/build_graph.py`
- Execute: `scripts/prepare_starlight_site.py`
- Generated: `site/src/content/docs/**/*.md`
- Generated: `site/public/knowledge_graph.json`

- [ ] **Step 1: Build graph**

Run:

```powershell
python "E:\astro_wiki_cn\scripts\build_graph.py"
```

Expected: output includes `[OK] graph nodes=55 edges=54` or a higher node/edge count if more pages were added.

- [ ] **Step 2: Mirror wiki into site content**

Run:

```powershell
python "E:\astro_wiki_cn\scripts\prepare_starlight_site.py"
```

Expected: output includes `[OK] exported pages:` and `[OK] copied graph:`.

### Task 5: Verify build and local preview

**Files:**
- No source changes unless verification identifies a concrete compatibility issue.

- [ ] **Step 1: Build site**

Run:

```powershell
npm run build --prefix "E:\astro_wiki_cn\site"
```

Expected: Astro build exits successfully and creates `site/dist/`.

- [ ] **Step 2: Start dev server for UI preview**

Run:

```powershell
npm run dev --prefix "E:\astro_wiki_cn\site"
```

Expected: dev server starts and serves the Starlight docs and `/graph/` route. If browser access is unavailable, report that limitation explicitly.

### Task 6: Report results

**Files:**
- No additional file changes.

- [ ] **Step 1: Summarize exact status**

Report scaffold status, export status, build status, graph route status, and any preview limitation.

---

## Self-Review

- Spec coverage: covers official npm scaffold, Chinese Starlight config, graph page, wiki export, build verification, and preview requirement.
- Placeholder scan: no plan placeholders remain.
- Scope check: focused on Starlight export flow only; source ingest remains excluded.
