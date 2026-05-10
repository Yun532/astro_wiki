# 02 Ingest arXiv paper

## 推荐 raw 结构

```text
raw/papers/
├── YYYY-short-title.pdf
├── YYYY-short-title.md
└── YYYY-short-title_src/
```

metadata `.md` 需要包含 title、source_type、arxiv、doi、url、pdf、source_url、status、related_source。

## 图片规则

1. 优先从 arXiv source 包提取原始图片。
2. 若 arXiv source 不可用，检查本地工具目录：`E:\paper_figure_extractor`。
3. 若只能从 PDF 裁图，必须标明 provenance: PDF page-render crop。

不要把所有图片插入正文。建立图像索引，正文只使用 core / important figures。

## Ingest 要求

不要只写 paper summary。更新具体源、仪器、模型、理论、综合比较和元信息页面。公式需要变量定义、假设和来源；如果公式属于可持续扩展的理论链条，优先更新 `wiki_textbook/`，并在普通 `wiki/` 页面链接到对应推导章节。图像需要图像索引。
