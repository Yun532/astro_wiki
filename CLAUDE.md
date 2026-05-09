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

## 公式规则

公式和推导要 source-backed。每个公式模块包含 equation、变量定义、推导步骤、物理意义、假设条件、适用范围、常见误区、来源、应用链接。

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
