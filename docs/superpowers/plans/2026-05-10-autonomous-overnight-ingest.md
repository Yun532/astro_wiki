# Autonomous Overnight Ingest Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Run an autonomous, source-backed overnight ingest across GRB 221009A, two-component gamma-ray bursts, IACT principles/reconstruction methods, and optical interferometry for Cherenkov telescopes.

**Architecture:** Work in small source batches. Each batch saves raw source metadata under `raw/`, updates Chinese-first `wiki/` pages with observation/model/instrument boundaries preserved, runs lint/graph/site verification, commits, pushes, and checks deployment. Stop only for hard blockers such as inaccessible full text/source metadata, failed verification that cannot be fixed locally, or source ambiguity that would risk fabrication.

**Tech Stack:** Markdown wiki, arXiv/DOI metadata, PDF/source package downloads where available, Python lint/graph/export scripts, Astro Starlight, GitHub Actions Pages deployment.

---

## File Structure

- Create raw source folders under `raw/arxiv/<arxiv-id>/` when arXiv exists.
- Create raw source folders under `raw/papers/<slug>/` when source has DOI but no arXiv package.
- Modify existing topic pages in `wiki/20_天体源/`, `wiki/30_仪器/`, `wiki/40_综合比较/`, `wiki/50_模型/`, and `wiki/90_元信息/`.
- Create new pages only when a topic has no suitable existing page:
  - `wiki/10_理论/切伦科夫辐射.md`
  - `wiki/30_仪器/iact/index.md`
  - `wiki/30_仪器/iact/成像原理.md`
  - `wiki/30_仪器/iact/重建方法.md`
  - `wiki/30_仪器/iact/相关文献.md`
  - `wiki/50_模型/grb模型/two-component-jet.md`
  - `wiki/40_综合比较/模型比较/two-component-grb-models.md`
  - `wiki/40_综合比较/仪器比较/cherenkov-telescope-interferometry.md`

### Task 1: Build source queue

**Files:**
- Create: `raw/source-queue-2026-05-10.md`

- [ ] **Step 1: Search sources per topic**

Use web/arXiv searches to identify 3-5 candidate sources per topic. Prefer peer-reviewed papers, arXiv versions, instrument collaboration papers, and review/method papers.

- [ ] **Step 2: Write source queue**

Write `raw/source-queue-2026-05-10.md` with columns: topic, priority, source title, arXiv/DOI/URL, source type, why ingest, target pages.

### Task 2: Batch A — GRB 221009A continuation

**Files:**
- Modify: `wiki/20_天体源/grb/grb-221009a/多波段数据.md`
- Modify: `wiki/20_天体源/grb/grb-221009a/能谱演化.md`
- Modify: `wiki/20_天体源/grb/grb-221009a/相关文献.md`
- Modify: `wiki/90_元信息/literature-index.md`
- Modify: `wiki/90_元信息/update-log.md`

- [ ] **Step 1: Ingest one GRB 221009A multiwavelength or spectral source**

Save raw metadata and PDF/source when available. Update only claims directly supported by the source.

- [ ] **Step 2: Verify and commit**

Run:

```powershell
python scripts/lint_wiki.py
python scripts/build_graph.py
python scripts/prepare_starlight_site.py
npm.cmd run build --prefix site
```

Expected: zero missing frontmatter/fields/orphans, graph builds, Astro build exits 0.

Commit message:

```text
Ingest GRB 221009A multiwavelength source
```

### Task 3: Batch B — two-component GRB models

**Files:**
- Create/modify: `wiki/50_模型/grb模型/two-component-jet.md`
- Create/modify: `wiki/40_综合比较/模型比较/two-component-grb-models.md`
- Modify: `wiki/20_天体源/grb/grb-221009a/模型解释.md`
- Modify: `wiki/90_元信息/literature-index.md`
- Modify: `wiki/90_元信息/open-questions.md`
- Modify: `wiki/90_元信息/update-log.md`

- [ ] **Step 1: Ingest one foundational or review source on two-component GRB jets**

Separate model assumptions from observational diagnostics. Do not over-apply generic two-component models to GRB 221009A unless the source specifically does so.

- [ ] **Step 2: Verify and commit**

Run full verification and commit:

```text
Ingest two-component GRB jet model source
```

### Task 4: Batch C — IACT principles and reconstruction methods

**Files:**
- Create/modify: `wiki/30_仪器/iact/index.md`
- Create/modify: `wiki/30_仪器/iact/成像原理.md`
- Create/modify: `wiki/30_仪器/iact/重建方法.md`
- Create/modify: `wiki/30_仪器/iact/相关文献.md`
- Create/modify: `wiki/10_理论/切伦科夫辐射.md`
- Modify: `wiki/90_元信息/literature-index.md`
- Modify: `wiki/90_元信息/update-log.md`

- [ ] **Step 1: Ingest one IACT overview/method source**

Cover atmospheric Cherenkov light, imaging camera, Hillas parameters, stereoscopic reconstruction, gamma/hadron separation, energy reconstruction, and caveats.

- [ ] **Step 2: Verify and commit**

Run full verification and commit:

```text
Ingest IACT principles and reconstruction source
```

### Task 5: Batch D — optical interferometry for Cherenkov telescopes

**Files:**
- Create/modify: `wiki/40_综合比较/仪器比较/cherenkov-telescope-interferometry.md`
- Modify: `wiki/30_仪器/iact/index.md`
- Modify: `wiki/30_仪器/iact/相关文献.md`
- Modify: `wiki/90_元信息/literature-index.md`
- Modify: `wiki/90_元信息/open-questions.md`
- Modify: `wiki/90_元信息/update-log.md`

- [ ] **Step 1: Ingest one source on intensity interferometry / Cherenkov telescope arrays**

Distinguish optical intensity interferometry from standard IACT gamma-ray reconstruction. Record use cases, angular resolution motivation, hardware/data acquisition implications, and limitations.

- [ ] **Step 2: Verify and commit**

Run full verification and commit:

```text
Ingest Cherenkov telescope interferometry source
```

### Task 6: Deployment check after each pushed commit

**Files:**
- No source changes.

- [ ] **Step 1: Push each batch**

Run:

```powershell
git push origin main
```

- [ ] **Step 2: Check GitHub Actions and key URLs**

Use GitHub CLI to check latest workflow success and test key pages for HTTP 200.

---

## Self-Review

- Spec coverage: covers all four requested topic areas and defines autonomous source-backed batches.
- Placeholder scan: no placeholder claims are embedded; exact scientific claim text will be taken only from selected sources during execution.
- Type consistency: paths follow existing wiki frontmatter and directory conventions.
- Scope note: this is intentionally split into independent commits per batch so partial overnight progress remains usable even if later source discovery or verification blocks.
