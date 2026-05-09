# Prepare Git Push Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Prepare the local project for a first push to `https://github.com/Yun532/astro_wiki.git` without pushing.

**Architecture:** Make the project root the only Git repository, keep `site/` as a normal tracked subdirectory, and ignore generated/dependency artifacts. Initialize the root repository on `main`, connect the remote, and verify that `git status` excludes `site/node_modules`, `site/dist`, and nested Git metadata.

**Tech Stack:** Git, PowerShell, Astro/Starlight generated site files.

---

## File Structure

- Create `E:\astro_wiki_cn\.gitignore` for root-level ignore rules.
- Remove `E:\astro_wiki_cn\site\.git` so `site/` is not a nested repository.
- Initialize root Git metadata at `E:\astro_wiki_cn\.git`.
- Add remote `origin` pointing to `https://github.com/Yun532/astro_wiki.git`.

### Task 1: Add root ignore rules

**Files:**
- Create: `E:\astro_wiki_cn\.gitignore`

- [ ] **Step 1: Write root `.gitignore`**

Write rules for generated artifacts and local-only files:

```gitignore
# Dependencies
site/node_modules/

# Astro build output and cache
site/dist/
site/.astro/

# Nested scaffold repository metadata
site/.git/

# Logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*

# Environment variables
.env
.env.*

# Python cache
__pycache__/
*.py[cod]

# OS files
.DS_Store
Thumbs.db
```

Expected: root `.gitignore` exists before root Git initialization.

### Task 2: Remove nested site Git metadata

**Files:**
- Remove: `E:\astro_wiki_cn\site\.git`

- [ ] **Step 1: Delete nested `.git` directory**

Run:

```powershell
Remove-Item -Recurse -Force "E:\astro_wiki_cn\site\.git"
```

Expected: `Test-Path "E:\astro_wiki_cn\site\.git"` returns `False`.

### Task 3: Initialize root Git repository

**Files:**
- Create: `E:\astro_wiki_cn\.git`

- [ ] **Step 1: Initialize root repository on main**

Run:

```powershell
git -C "E:\astro_wiki_cn" init -b main
```

Expected: `git -C "E:\astro_wiki_cn" branch --show-current` prints `main`.

### Task 4: Add GitHub remote without pushing

**Files:**
- Modify: root Git config under `.git/config`

- [ ] **Step 1: Add remote origin**

Run:

```powershell
git -C "E:\astro_wiki_cn" remote add origin "https://github.com/Yun532/astro_wiki.git"
```

Expected: `git -C "E:\astro_wiki_cn" remote -v` shows `origin` fetch and push URLs.

### Task 5: Verify push readiness without staging or pushing

**Files:**
- No source changes.

- [ ] **Step 1: Check status**

Run:

```powershell
git -C "E:\astro_wiki_cn" status --short
```

Expected: source files are untracked for first commit, but `site/node_modules/`, `site/dist/`, `site/.astro/`, and `site/.git/` do not appear.

- [ ] **Step 2: Dry-run add**

Run:

```powershell
git -C "E:\astro_wiki_cn" add --dry-run .
```

Expected: dry-run lists project source files and does not list generated dependency/build folders.

---

## Self-Review

- Spec coverage: covers root ignore rules, nested Git removal, root initialization, remote connection, no push, and readiness verification.
- Placeholder scan: no placeholders remain.
- Safety: destructive action is limited to `site/.git`, which the user explicitly approved by accepting the proposed preparation plan.
