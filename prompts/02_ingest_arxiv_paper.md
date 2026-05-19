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

图像工作按 `prompts/05_figure_agent.md` 执行。

不要把所有图片插入正文。建立图像索引，正文只使用 core / important figures。

## 数据规则

观测数据工作按 `prompts/04_observation_data_agent.md` 执行。不要只看 arXiv source 包中的 LaTeX 表；必须检查 Data Availability、supplement、caption、appendix、作者仓库、Zenodo/Figshare、CDS/VizieR、HEASARC/MAST/仪器 archive、GCN 和用户给定链接。若没有机器可读数据，则登记为 unavailable 或 external-linked/access-needed，不默认 digitize。

## Ingest 要求

不要只写 paper summary。更新具体源、仪器、模型、理论、综合比较和元信息页面。公式需要变量定义、假设和来源；如果公式属于可持续扩展的理论链条，优先更新 `wiki_textbook/`，并在普通 `wiki/` 页面链接到对应推导章节。图像需要图像索引。
