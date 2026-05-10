# CLAUDE.md

本项目是一个**中文优先**的个人高能天体物理知识库。目标是建立一个长期维护、持续增长、可部署为网页的 Markdown Wiki。

## 最高原则

1. 默认中文写作。
2. `raw/` 是原始资料层，不要修改原始来源。
3. `wiki/` 是知识层，由 LLM 维护。
4. `site/` 是网页渲染层，不是知识源。
5. 不要只写论文摘要，要把新 source 整合进已有知识结构。
6. 论文是证据，不是主结构。
7. 数据跟随具体源或仪器，不单独堆在全局目录。
8. 观测事实和模型解释必须分开。
9. 所有重要 claim 必须有来源。
10. 不确定就写 `TODO: add source` 或明确 uncertainty，不要编造。

## 语言规则

- 正文中文。
- 页面标题中文优先。
- 导航中文。
- 图注解释中文。
- open questions / contradictions 中文。
- 论文标题、GCN title、arXiv title 保留英文。
- 仪器名、模型名、变量、公式保留英文。
- 术语可中英混合，但以中文可读性为第一原则。

推荐翻译：

- prompt emission → 瞬时辐射
- afterglow → 余辉
- light curve → 光变曲线
- spectral evolution → 能谱演化
- multiwavelength data → 多波段数据
- model interpretation → 模型解释
- observation summary → 观测总结
- instrument results → 仪器结果
- open questions → 未解决问题
- figure index → 图像索引

## 目录组织

- `00_总览/`: 入口、研究地图、术语表。
- `10_理论/`: 基础理论、公式、推导。
- `20_天体源/`: 具体源、具体事件、源类。
- `30_仪器/`: 仪器性能、数据产品、代表性结果。
- `40_综合比较/`: 跨源、跨模型、跨仪器比较。
- `50_模型/`: 物理模型和现象学模型。
- `90_元信息/`: 文献索引、未解决问题、矛盾、日志、图谱。

## 长篇理论教材层

`wiki_textbook/` 是独立于 `wiki/` 的长篇理论推导层，用于写成类似课程教材、lecture notes 或毕业论文理论章节的连续文本。它不替代 `wiki/`：

- `wiki/` 保存知识卡片、具体源、仪器、模型、比较和元信息。
- `wiki_textbook/` 保存从基础物理到论文结论的系统推导链。
- 普通 `wiki/` 页面只写公式结论、变量含义、适用范围和链接，不重复长推导。
- 长篇推导按“基础物理 → 标准模型 → 模型扩展 → 事件应用”的逻辑组织，不按单篇论文组织。

## 页面 frontmatter

每个 wiki 页面必须包含：

```yaml
---
title:
type:
status:
last_updated:
tags: []
source_count:
confidence:
related: []
---
```

状态可选：`seed`、`growing`、`reviewed`、`needs-source`、`outdated`、`superseded`、`controversial`。

置信度可选：`high`、`medium`、`low`。

## Ingest 规则

每次 ingest 新 source 时：

1. 识别 source 类型。
2. 保存 raw source。
3. 读取 source。
4. 提取 key claims、数值、公式、图表、数据、假设、限制。
5. 更新相关具体源页面。
6. 更新相关仪器页面。
7. 更新相关模型 / 理论页面。
8. 更新综合比较页面。
9. 更新文献索引。
10. 更新 open questions / contradictions。
11. 更新 index.md 和 log.md。
12. 运行 lint 和 graph。

## 观测和模型分离

观测事实写入：观测总结、时间线、瞬时辐射、余辉、光变曲线、能谱演化、多波段数据、仪器结果。

模型解释写入：模型解释、`50_模型/`、`40_综合比较/模型比较/`。

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

### 理论教材 source 优先级

- 基础推导优先使用 review、book、lecture notes 或经典教材，例如 GRB/afterglow review、Zhang Bing GRB book/review、Piran review、Mészáros review 等。
- 标准模型公式使用原始模型论文和高权重综述共同支持，例如 fireball、external shock、synchrotron afterglow、jet break。
- 模型扩展使用对应模型论文，例如 structured jet、two-component jet、refreshed shock、energy injection。
- 事件应用使用具体事件论文，例如 GRB 030329、GRB 080319B、GRB 221009A。
- 不同 source 的定义或参数化不一致时，记录为“符号约定差异”或“模型假设差异”，不要强行统一。

## 图片规则

采用三层策略：raw 层保存原始图片；图像索引登记所有 main / supplement figures；正文只嵌入 core / important figures。

优先级：

1. 优先从 arXiv source 包提取原始图片。
2. 如果 arXiv source 不可用或图片难以对应，检查本地工具目录 `E:\paper_figure_extractor`。
3. 如只能从 PDF page-render crop 提图，必须在图像索引中标注 provenance。

## GCN 规则

GCN 用于 trigger、localization、瞬时辐射、fluence、redshift、follow-up、caveat。不要用 GCN 支持复杂模型解释，除非 GCN 明确说明并标注为初步结果。

## 网站规则

使用 Astro Starlight。`wiki/` 是源，`site/` 是渲染层。不要为适配网页修改 wiki 原文。使用 `scripts/prepare_starlight_site.py` 导出。保持中文导航和中文 UI。提供 `/graph/` 知识星图页面。
