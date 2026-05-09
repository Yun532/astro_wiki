# First Ingest LHAASO GRB 221009A Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ingest the LHAASO Collaboration Science/arXiv paper on the TeV afterglow of GRB 221009A as the first formal source-backed wiki entry.

**Architecture:** Keep `raw/` as the source evidence layer, update `wiki/` as the knowledge layer, and let `site/` remain generated output. Separate observation facts from model interpretation: LHAASO photon counts, timing, and light-curve behavior go into GRB 221009A observation/instrument pages; narrow-jet interpretation goes into model pages and comparison pages with explicit attribution.

**Tech Stack:** Markdown wiki, Python lint/graph/export scripts, Astro Starlight, Git.

---

## File Structure

- Create: `raw/arxiv/2306.06372/metadata.md`
- Download: `raw/arxiv/2306.06372/2306.06372.pdf`
- Download: `raw/arxiv/2306.06372/2306.06372-source.tar.gz`
- Modify: `wiki/20_天体源/grb/grb-221009a/观测总结.md`
- Modify: `wiki/20_天体源/grb/grb-221009a/时间线.md`
- Modify: `wiki/20_天体源/grb/grb-221009a/余辉.md`
- Modify: `wiki/20_天体源/grb/grb-221009a/仪器结果.md`
- Modify: `wiki/20_天体源/grb/grb-221009a/光变曲线.md`
- Modify: `wiki/20_天体源/grb/grb-221009a/模型解释.md`
- Modify: `wiki/20_天体源/grb/grb-221009a/图像索引.md`
- Modify: `wiki/30_仪器/lhaaso/代表性结果.md`
- Modify: `wiki/30_仪器/lhaaso/相关文献.md`
- Modify: `wiki/40_综合比较/模型比较/grb-221009a-model-comparison.md`
- Modify: `wiki/40_综合比较/源类比较/vhe-grb-detections.md`
- Modify: `wiki/90_元信息/literature-index.md`
- Modify: `wiki/90_元信息/open-questions.md`
- Modify: `wiki/90_元信息/source-quality.md`
- Modify: `wiki/90_元信息/update-log.md`

### Task 1: Save raw source metadata

**Files:**
- Create: `raw/arxiv/2306.06372/metadata.md`
- Download: `raw/arxiv/2306.06372/2306.06372.pdf`
- Download: `raw/arxiv/2306.06372/2306.06372-source.tar.gz`

- [ ] **Step 1: Create raw source directory**

Run:

```powershell
New-Item -ItemType Directory -Force "E:\astro_wiki_cn\raw\arxiv\2306.06372"
```

Expected: directory exists.

- [ ] **Step 2: Download PDF and source package**

Run:

```powershell
Invoke-WebRequest -Uri "https://arxiv.org/pdf/2306.06372" -OutFile "E:\astro_wiki_cn\raw\arxiv\2306.06372\2306.06372.pdf"
Invoke-WebRequest -Uri "https://arxiv.org/e-print/2306.06372" -OutFile "E:\astro_wiki_cn\raw\arxiv\2306.06372\2306.06372-source.tar.gz"
```

Expected: both files exist and are non-empty.

- [ ] **Step 3: Write source metadata**

Create `metadata.md` with title, source type, arXiv ID, Science DOI, raw file paths, and key source-backed claims.

### Task 2: Update GRB 221009A observation pages

**Files:**
- Modify: `wiki/20_天体源/grb/grb-221009a/观测总结.md`
- Modify: `wiki/20_天体源/grb/grb-221009a/时间线.md`
- Modify: `wiki/20_天体源/grb/grb-221009a/余辉.md`
- Modify: `wiki/20_天体源/grb/grb-221009a/仪器结果.md`
- Modify: `wiki/20_天体源/grb/grb-221009a/光变曲线.md`

- [ ] **Step 1: Add LHAASO observation facts**

Add sourced facts only: field-of-view serendipitous observation, >64,000 photons above 0.2 TeV in first 3000 s, delayed TeV onset several minutes after trigger, peak about 10 s after onset, post-peak decay, faster decay about 650 s after peak.

- [ ] **Step 2: Update frontmatter**

Set status to `growing`, source_count to at least `1`, confidence to `medium`, and related pages to include LHAASO / relevant model pages.

### Task 3: Update model and comparison pages

**Files:**
- Modify: `wiki/20_天体源/grb/grb-221009a/模型解释.md`
- Modify: `wiki/40_综合比较/模型比较/grb-221009a-model-comparison.md`
- Modify: `wiki/40_综合比较/源类比较/vhe-grb-detections.md`

- [ ] **Step 1: Add attributed interpretation**

Record that the LHAASO paper models the emission with a relativistic jet half-opening angle about 0.8°, consistent with a structured-jet core and proposed as an explanation for the unusually high isotropic energy.

- [ ] **Step 2: Preserve observation/model boundary**

Do not state the narrow jet as an established fact outside model sections; mark it as the paper's interpretation.

### Task 4: Update LHAASO instrument and metadata pages

**Files:**
- Modify: `wiki/30_仪器/lhaaso/代表性结果.md`
- Modify: `wiki/30_仪器/lhaaso/相关文献.md`
- Modify: `wiki/90_元信息/literature-index.md`
- Modify: `wiki/90_元信息/source-quality.md`
- Modify: `wiki/90_元信息/open-questions.md`
- Modify: `wiki/90_元信息/update-log.md`

- [ ] **Step 1: Register source and quality**

Add the Science/arXiv source to literature and source-quality indexes, with high value for TeV afterglow observations and caveat that model interpretation remains interpretation.

- [ ] **Step 2: Add open questions**

Add source-backed open questions around TeV onset, break around 650 s, and relation between narrow-core interpretation and multiwavelength modeling.

### Task 5: Update figure index without embedding figures yet

**Files:**
- Modify: `wiki/20_天体源/grb/grb-221009a/图像索引.md`

- [ ] **Step 1: Register figure extraction plan**

Record that figures should be extracted first from arXiv source package, then via `E:\paper_figure_extractor` if needed, and only PDF crop as last resort. Do not embed figures in content until exact figure files and captions are verified.

### Task 6: Verify and commit

**Files:**
- Generated but ignored: `site/src/content/docs/`, `site/public/knowledge_graph.json`, `site/dist/`

- [ ] **Step 1: Run verification**

Run:

```powershell
python scripts/lint_wiki.py
python scripts/build_graph.py
python scripts/prepare_starlight_site.py
npm.cmd run build --prefix site
```

Expected: lint has zero missing frontmatter and fields; graph builds; Astro build exits 0.

- [ ] **Step 2: Commit**

Run:

```powershell
git add docs/superpowers/plans/2026-05-10-first-ingest-lhaaso-grb221009a.md raw/arxiv/2306.06372 wiki
 git commit -m "Ingest LHAASO GRB 221009A TeV afterglow source"
```

Expected: commit succeeds.

---

## Self-Review

- Spec coverage: covers raw source preservation, observation/model separation, LHAASO instrument pages, literature/source quality metadata, open questions, image policy, lint/graph/site verification, and commit.
- Placeholder scan: no implementation placeholders remain; content pages may retain `TODO: add source` only where seed claims are still intentionally unsourced.
- Safety: no raw source mutation after download; generated site outputs remain ignored.
