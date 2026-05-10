# Wiki Textbook Rules Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an independent long-form theoretical derivation layer (`wiki_textbook/`) to the astro wiki rules without disrupting the existing `wiki/` knowledge-card structure.

**Architecture:** Keep `wiki/` as the source/card/model/instrument knowledge layer and introduce `wiki_textbook/` as a separate book-like derivation layer. Rule documents define when formulas are merged into existing derivation chains, when new textbook chapters are created, and how ordinary ingest pages link to long derivations without duplicating them.

**Tech Stack:** Markdown rules (`CLAUDE.md`, `README.md`, `prompts/*.md`), source-backed wiki/textbook content, Python lint/graph/export verification.

---

## File Structure

- Modify: `CLAUDE.md`
  - Add `wiki_textbook/` as an independent long-form theory derivation layer.
  - Add textbook source priority, formula merge rules, chapter template, formula block template, and ingest decision flow.
- Modify: `README.md`
  - Add a concise user-facing description of `wiki_textbook/`.
- Modify: `prompts/01_ingest_source.md`
  - Add formula/textbook ingest rule so future source ingest checks `wiki_textbook/` before writing duplicate derivations.
- Modify: `prompts/02_ingest_arxiv_paper.md`
  - Add arXiv-specific formula extraction and textbook update behavior.
- Create: `wiki_textbook/index.md`
  - Create the long-form textbook root and explain how it differs from `wiki/`.
- Create: `wiki_textbook/grb-afterglow/index.md`
  - Create the starter outline for the GRB afterglow textbook route.
- Create: `wiki_textbook/grb-afterglow/公式索引.md`
  - Create an index template for formula names, equations, assumptions, and source-backed derivation locations.
- Create: `wiki_textbook/grb-afterglow/符号表.md`
  - Create a symbol table starter for GRB afterglow derivations.
- Create: `wiki_textbook/grb-afterglow/来源脉络.md`
  - Create a source genealogy starter distinguishing review/book foundations from model/event papers.

## Task 1: Add `wiki_textbook/` rules to project instructions

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Insert independent layer rule after directory organization**

Add this section after the existing `## 目录组织` block:

```markdown
## 长篇理论教材层

`wiki_textbook/` 是独立于 `wiki/` 的长篇理论推导层，用于写成类似课程教材、lecture notes 或毕业论文理论章节的连续文本。它不替代 `wiki/`：

- `wiki/` 保存知识卡片、具体源、仪器、模型、比较和元信息。
- `wiki_textbook/` 保存从基础物理到论文结论的系统推导链。
- 普通 `wiki/` 页面只写公式结论、变量含义、适用范围和链接，不重复长推导。
- 长篇推导按“基础物理 → 标准模型 → 模型扩展 → 事件应用”的逻辑组织，不按单篇论文组织。
```

- [ ] **Step 2: Replace formula rule with expanded textbook-aware formula rule**

Replace the existing `## 公式规则` section with:

```markdown
## 公式和理论推导规则

公式和推导要 source-backed。短公式卡片可保留在 `wiki/10_理论/` 或 `wiki/50_模型/`，但完整推导优先进入 `wiki_textbook/`。

每个完整公式模块至少包含：

1. equation：原始公式和常用变体。
2. 变量定义：所有符号、单位、参考系和归一化约定。
3. 推导步骤：从前置假设到目标结论的主要中间式。
4. 物理意义：该公式说明什么物理图像。
5. 假设条件：几何、动力学、辐射机制、介质、参考系、近似阶数。
6. 适用范围：能段、时间段、光深、Lorentz factor、regime、事件类型。
7. 常见误区：容易混淆的变量、错误外推、观测量和模型量混用。
8. 来源：review/book、模型论文、事件论文分别列出。
9. 应用链接：对应 `wiki/` 中的模型页、事件页、仪器页和综合比较页。

新 source 中出现公式、标度律或推导时：

- 若已有相同理论链条，不重复写完整推导；更新已有 `wiki_textbook/` 章节的来源、变体、caveat 或应用。
- 若是已有公式的 source-specific form，加入同一章的“变体 / 参数化 / caveat”。
- 若引入新的理论环节或不可合并的假设，才新建 `wiki_textbook/` 章节。
- 若只是事件拟合参数，写入具体事件或模型页面，不进入长推导，除非它改变或检验理论形式。
```

- [ ] **Step 3: Add source priority rule**

Add this subsection under formula rules:

```markdown
### 理论教材 source 优先级

- 基础推导优先使用 review、book、lecture notes 或经典教材，例如 GRB/afterglow review、Zhang Bing GRB book/review、Piran review、Mészáros review 等。
- 标准模型公式使用原始模型论文和高权重综述共同支持，例如 fireball、external shock、synchrotron afterglow、jet break。
- 模型扩展使用对应模型论文，例如 structured jet、two-component jet、refreshed shock、energy injection。
- 事件应用使用具体事件论文，例如 GRB 030329、GRB 080319B、GRB 221009A。
- 不同 source 的定义或参数化不一致时，记录为“符号约定差异”或“模型假设差异”，不要强行统一。
```

## Task 2: Update ingest prompts

**Files:**
- Modify: `prompts/01_ingest_source.md`
- Modify: `prompts/02_ingest_arxiv_paper.md`

- [ ] **Step 1: Update generic ingest workflow**

In `prompts/01_ingest_source.md`, after workflow step 4, add:

```markdown
5. 如果 source 含有公式、标度律、推导或模型变体，先检查 `wiki_textbook/` 是否已有对应推导链：已有则合并来源/变体/caveat；没有且值得长篇推导时才新建 textbook 章节。
```

Then renumber later steps so the final lint/graph step remains last.

- [ ] **Step 2: Add generic writing rule**

In `prompts/01_ingest_source.md` under `## 写作规则`, add:

```markdown
- 长推导写入 `wiki_textbook/`；普通 `wiki/` 页面只保留结论、适用范围和到 textbook 的链接，避免重复。
- 同一模型或理论的相似公式不要重复开页，优先更新已有推导链。
```

- [ ] **Step 3: Update arXiv ingest requirements**

In `prompts/02_ingest_arxiv_paper.md`, replace the final line of `## Ingest 要求` with:

```markdown
不要只写 paper summary。更新具体源、仪器、模型、理论、综合比较和元信息页面。公式需要变量定义、假设和来源；如果公式属于可持续扩展的理论链条，优先更新 `wiki_textbook/`，并在普通 `wiki/` 页面链接到对应推导章节。图像需要图像索引。
```

## Task 3: Add user-facing README rule

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Add textbook layer to core goals**

After the bullet `用 wiki/ 保存中文 Markdown 知识库；`, add:

```markdown
- 用 `wiki_textbook/` 保存长篇理论推导、公式链条和课程教材式章节；
```

- [ ] **Step 2: Add important convention**

After the existing image extraction convention, add:

```markdown
- 长篇公式推导和理论主线写入 `wiki_textbook/`；`wiki/` 页面只保留摘要式结论和链接。
```

## Task 4: Create textbook starter pages

**Files:**
- Create: `wiki_textbook/index.md`
- Create: `wiki_textbook/grb-afterglow/index.md`
- Create: `wiki_textbook/grb-afterglow/公式索引.md`
- Create: `wiki_textbook/grb-afterglow/符号表.md`
- Create: `wiki_textbook/grb-afterglow/来源脉络.md`

- [ ] **Step 1: Create `wiki_textbook/index.md`**

```markdown
# 理论教材层

`wiki_textbook/` 是长篇理论推导层，用于把高能天体物理主题整理成类似课程教材、lecture notes 或毕业论文理论章节的连续文本。

## 和 `wiki/` 的分工

- `wiki/`：知识卡片、具体天体源、仪器、模型、比较、元信息。
- `wiki_textbook/`：从基础物理到论文结论的连续推导链。

普通 `wiki/` 页面应链接到这里的推导章节，而不是重复长推导。

## 当前教材主线

- [GRB 余辉理论教材](grb-afterglow/index.md)

## 写作原则

1. 中文解释优先，变量、模型名、公式名保留英文。
2. 从基础假设开始推导，不按单篇论文堆摘要。
3. 每个关键公式标明变量定义、参考系、适用范围和来源。
4. 新 source 优先合并进已有推导链，避免重复章节。
5. 有争议或不同约定时保留 source-specific form。
```

- [ ] **Step 2: Create `wiki_textbook/grb-afterglow/index.md`**

```markdown
# GRB 余辉理论教材

本教材主线目标是从相对论基础和辐射过程出发，逐步推导 GRB fireball / external shock / afterglow / jet structure 的常用公式，并连接到 GRB 030329、GRB 080319B、GRB 221009A 等事件应用。

## 推荐阅读路线

1. 相对论基础：Lorentz factor、Doppler factor、arrival time、beaming。
2. 观测量与参考系变换：频率、时间、强度、luminosity、isotropic-equivalent quantities。
3. Fireball model：compactness、初始加速、coasting、deceleration。
4. External shock dynamics：Blandford-McKee scaling、deceleration time、介质密度剖面。
5. Synchrotron afterglow spectrum：特征频率、peak flux、cooling regimes。
6. Light curve closure relations：spectral index 与 temporal index 的关系。
7. Jet break and beaming correction：opening angle、beaming fraction、true energy。
8. Energy injection and refreshed shock：late shells、plateau、bump。
9. Structured jet：angular energy profile、viewing angle、core/wings。
10. Two-component jet：narrow / wide component、component transition、事件应用。
11. Event applications：GRB 030329、GRB 080319B、GRB 221009A。

## 辅助索引

- [公式索引](公式索引.md)
- [符号表](符号表.md)
- [来源脉络](来源脉络.md)
```

- [ ] **Step 3: Create `wiki_textbook/grb-afterglow/公式索引.md`**

```markdown
# GRB 余辉公式索引

| 公式 / 标度律 | 章节 | 核心变量 | 适用范围 | 主要来源 |
| --- | --- | --- | --- | --- |
| Doppler factor | 待建：相对论基础 | Γ, β, θ, δ | relativistic beaming | TODO: add source |
| arrival time relation | 待建：观测量与参考系变换 | R, Γ, z, t_obs | on-axis / small-angle approximation | TODO: add source |
| deceleration time | 待建：external shock dynamics | E, n/A_*, Γ_0, z | ISM / wind external shock | TODO: add source |
| jet break condition | 待建：jet break and beaming correction | Γ, θ_j, t_j | collimated outflow | TODO: add source |
| beaming fraction | 待建：jet break and beaming correction | f_b, θ_j, E_iso | small-angle jet correction | TODO: add source |
| two-component transition | 待建：two-component jet | t_dec,w, t_jet,n, E_w/E_n | narrow/wide jet model | Peng et al. 2005; Berger et al. 2003 |
```

- [ ] **Step 4: Create `wiki_textbook/grb-afterglow/符号表.md`**

```markdown
# GRB 余辉符号表

| 符号 | 含义 | 常用单位 / 归一化 | 注意事项 |
| --- | --- | --- | --- |
| Γ | bulk Lorentz factor | dimensionless | 注意区分 initial Γ_0、shock Γ、component Γ。 |
| β | v/c | dimensionless | β = sqrt(1 - Γ^-2)。 |
| δ | Doppler factor | dimensionless | 依赖 viewing angle 和 Γ。 |
| θ_j | jet opening half-angle | rad 或 degree | small-angle approximation 下 f_b ≈ θ_j^2/2。 |
| E_iso | isotropic-equivalent energy | erg | 观测推断量，不等于 true energy。 |
| E | beaming-corrected / true energy | erg | 依赖几何和模型假设。 |
| n | ISM number density | cm^-3 | wind medium 中通常改用 A 或 A_*。 |
| t_obs | observer-frame time | s, d | 通常含 redshift factor (1+z)。 |
```

- [ ] **Step 5: Create `wiki_textbook/grb-afterglow/来源脉络.md`**

```markdown
# GRB 余辉理论来源脉络

## 基础 / review / book

- Zhang Bing GRB review / book：计划用于 GRB 基础、相对论变换、fireball model、afterglow framework。TODO: add exact source.
- Piran review：计划用于 fireball 与 afterglow 基础。TODO: add exact source.
- Mészáros review：计划用于 GRB prompt / afterglow 物理图像。TODO: add exact source.

## 标准模型论文

- Sari, Piran & Narayan afterglow spectrum / dynamics：TODO: add source.
- Sari, Piran & Halpern jet break：TODO: add source.
- Chevalier & Li wind afterglow：TODO: add source.

## 模型扩展

- Peng, Königl & Granot 2005 two-component jet：narrow / wide component、t_dec,w 与 t_jet,n、jet-break masking。
- Berger et al. 2003 GRB 030329 calorimetry：事件级 two-component explosion 解释。

## 事件应用

- GRB 030329：radio calorimetry、5° narrow component、17° wide component、SN 2003dh subtraction caveat。
- GRB 080319B：naked-eye burst、prompt optical/gamma mismatch、narrow core / wide jet interpretation。TODO: complete source ingest.
- GRB 221009A：structured jet、TeV afterglow、radio-to-GeV afterglow、model comparison。
```

## Task 5: Verify and commit

**Files:**
- Verify changed Markdown and repository state.

- [ ] **Step 1: Run wiki verification**

Run:

```powershell
python scripts/lint_wiki.py; if ($?) { python scripts/build_graph.py }; if ($?) { python scripts/prepare_starlight_site.py }; if ($?) { npm.cmd run build --prefix site }
```

Expected:

```text
[OK] lint ... missing_frontmatter=0 missing_fields=0 orphan_like=0
[OK] graph ...
[OK] exported pages: ...
[build] Complete!
```

Note: `wiki_textbook/` is intentionally outside current `wiki/` export/lint unless future site export support is added.

- [ ] **Step 2: Commit rule update**

Run:

```powershell
git add CLAUDE.md README.md prompts/01_ingest_source.md prompts/02_ingest_arxiv_paper.md wiki_textbook/index.md wiki_textbook/grb-afterglow/index.md wiki_textbook/grb-afterglow/公式索引.md wiki_textbook/grb-afterglow/符号表.md wiki_textbook/grb-afterglow/来源脉络.md docs/superpowers/plans/2026-05-10-wiki-textbook-rules.md
git commit -m @'
Add independent theory textbook rules
'@
```

Expected: commit succeeds with changed rule and starter textbook files.

## Self-Review

- Spec coverage: directory purpose, source priority, chapter purpose, formula block requirements, ingest decision flow, and GRB afterglow starter outline are covered.
- Placeholder scan: `TODO: add source` appears intentionally only as source-quality uncertainty markers in starter source genealogy/index files; no implementation placeholder is left in rules.
- Type consistency: the independent layer is consistently named `wiki_textbook/`; ordinary wiki remains `wiki/`; site layer remains `site/`.
