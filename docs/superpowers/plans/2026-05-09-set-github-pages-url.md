# Set GitHub Pages URL Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Configure the Astro Starlight site for the GitHub Pages project URL `https://yun532.github.io/astro_wiki/`.

**Architecture:** Set Astro's `site` and `base` options for a project Pages deployment. Make generated wiki links and the custom graph page respect `/astro_wiki/` so docs, graph JSON, and node navigation work under the project subpath.

**Tech Stack:** Astro Starlight, Python export script, static GitHub Pages deployment.

---

## File Structure

- Modify `site/astro.config.mjs` to set `site: 'https://yun532.github.io'` and `base: '/astro_wiki'`.
- Modify `site/src/pages/graph.astro` to use Astro's `import.meta.env.BASE_URL` for JSON fetch and node navigation.
- Modify `scripts/prepare_starlight_site.py` so generated wiki links include a configurable base path, defaulting to `/astro_wiki`.

### Task 1: Configure Astro Pages URL

**Files:**
- Modify: `site/astro.config.mjs`

- [ ] **Step 1: Add site and base**

Update the `defineConfig` object to include:

```js
site: 'https://yun532.github.io',
base: '/astro_wiki',
```

Expected: `astro.config.mjs` remains valid JavaScript and Starlight config is unchanged except for deployment URL settings.

### Task 2: Make graph route base-safe

**Files:**
- Modify: `site/src/pages/graph.astro`

- [ ] **Step 1: Use BASE_URL in client script**

Add a base URL constant from Astro frontmatter and use it in the inline script:

```astro
---
const baseUrl = import.meta.env.BASE_URL;
---
```

Use `const BASE_URL = ${JSON.stringify(baseUrl)};` in the script, fetch `${BASE_URL}knowledge_graph.json`, and navigate nodes to `${BASE_URL}${path}/`.

Expected: graph page works at `/astro_wiki/graph/` and loads `/astro_wiki/knowledge_graph.json`.

### Task 3: Make exported wiki links base-safe

**Files:**
- Modify: `scripts/prepare_starlight_site.py`

- [ ] **Step 1: Add export base path**

Add:

```python
BASE_PATH = '/astro_wiki'
```

Update `link_for()` so absolute generated links are prefixed with `BASE_PATH`.

Expected: generated docs contain links like `/astro_wiki/00_总览/` rather than `/00_总览/`.

### Task 4: Verify export and build

**Files:**
- Execute: `scripts/build_graph.py`
- Execute: `scripts/prepare_starlight_site.py`
- Execute: `npm.cmd run build --prefix site`

- [ ] **Step 1: Rebuild graph, export docs, and build site**

Run:

```powershell
python "E:\astro_wiki_cn\scripts\build_graph.py"
python "E:\astro_wiki_cn\scripts\prepare_starlight_site.py"
npm.cmd run build --prefix "E:\astro_wiki_cn\site"
```

Expected: graph builds, export reports copied graph, Astro build completes with sitemap warning resolved.

- [ ] **Step 2: Verify generated URLs**

Run local dev server and request:

```text
http://127.0.0.1:4321/astro_wiki/00_%E6%80%BB%E8%A7%88/
http://127.0.0.1:4321/astro_wiki/graph/
http://127.0.0.1:4321/astro_wiki/knowledge_graph.json
```

Expected: all return HTTP 200.

---

## Self-Review

- Spec coverage: covers Astro deployment URL, graph route base path, exported wiki links, build verification, and local route verification.
- Placeholder scan: no placeholders remain.
- Type consistency: paths and variables are consistent across Astro and Python changes.
