# 05 Figure Asset Agent

用于论文图像、图表和可视化结果的资产登记、提取和 provenance 管理。读图说明和正文使用建议交给 `13_figure_reading_agent.md`。

## 核心原则

1. 先检查已有资产，再决定是否提取。
2. 优先复用已有图片提取工具和已有网页资产。
3. arXiv source 包中的原始 figure 优先于 PDF crop。
4. 不覆盖已有图片文件；如果需要保留多个版本，用来源后缀区分。
5. 图像不是数据文件；除非用户明确要求，不从图像数字化数据。

## 图像来源优先级

1. 已有 wiki / site / `site/public/figures/` 资产。
2. arXiv source 包中的原始 PDF / PNG / EPS / JPG。
3. 用户已有图片提取工具输出，例如 `E:\paper_figure_extractor`。
4. PDF page-render crop，仅在前面方式不可用时使用。

## 资产登记字段

每张 figure asset 至少登记：

- figure id / source file。
- 来源论文、arXiv / DOI。
- 本地路径或外部链接。
- provenance：source package / existing asset / extractor output / PDF crop。
- 分辨率或文件类型。
- 是否已有更高质量或重复资产。

## 与数据 Agent 的关系

- Figure Asset Agent 负责图像文件和 provenance。
- Figure Reading Agent 负责 caption、科学用途和正文使用建议。
- Data Agent 负责真实数据入口、表格、CSV 和 provenance。
- 如果 figure caption 或论文正文给出 data URL，必须把线索转交给 Data Agent 规则处理。
- 如果只有图，没有数值表，默认只登记图，不 digitize。

## 禁止事项

- 不重复提取已有资产，除非 provenance 或质量明显更好。
- 不覆盖已有图片文件；需要变体时添加来源后缀。
- 不把 PDF crop 当作原始 figure，必须标注 crop provenance。
