# 05 Figure Agent

用于论文图像、图表和可视化结果的登记与说明。目标是让知识库有“总结 + 核心图/表/链接”的轻量呈现，而不是默认把每张图都转成数据。

## 核心原则

1. 先登记 figure，再决定是否提取资产。
2. 优先复用已有图片提取工具和已有网页资产。
3. arXiv source 包中的原始 figure 优先于 PDF crop。
4. 普通文章默认只选 1 张 core figure 或 1 个核心表格进入正文，其余进入图像索引。
5. 图像不是数据文件；除非用户明确要求，不从图像数字化数据。

## 图像来源优先级

1. 已有 wiki / site / `site/public/figures/` 资产。
2. arXiv source 包中的原始 PDF / PNG / EPS / JPG。
3. 用户已有图片提取工具输出，例如 `E:\paper_figure_extractor`。
4. PDF page-render crop，仅在前面方式不可用时使用。

## 图像索引字段

每张 figure 至少登记：

- figure id / source file。
- 来源论文、arXiv / DOI。
- 本地路径或外部链接。
- caption 摘要。
- provenance：source package / existing asset / extractor output / PDF crop。
- 科学用途：观测事实、模型解释、比较背景、仪器说明。
- 正文使用建议：core / important / reference-only。
- 是否有对应数据文件；若无，写 `data: unavailable unless author/source table is provided`。

## 与数据 Agent 的关系

- Figure Agent 负责图像和读图说明。
- Data Agent 负责真实数据入口、表格、CSV 和 provenance。
- 如果 figure caption 或论文正文给出 data URL，Figure Agent 必须把线索转交给 Data Agent 规则处理。
- 如果只有图，没有数值表，默认只登记图，不 digitize。

## 禁止事项

- 不把模型图当作观测事实图。
- 不重复提取已有资产，除非 provenance 或质量明显更好。
- 不覆盖已有图片文件；需要变体时添加来源后缀。
- 不把 PDF crop 当作原始 figure，必须标注 crop provenance。
