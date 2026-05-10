# 中文高能天体物理知识库 Claude Code 启动包

这是一个给 Claude Code 使用的完整项目启动包，用来构建一个中文优先、source-centered、model-centered、instrument-centered 的个人高能天体物理 Wiki。

核心目标：

- 用 `raw/` 保存原始来源；
- 用 `wiki/` 保存中文 Markdown 知识库；
- 用 `wiki_textbook/` 保存长篇理论推导、公式链条和课程教材式章节；
- 用 `site/` 生成 Astro Starlight 网页；
- 用 `/graph/` 显示动态可交互知识星图；
- 用脚本维护 lint、知识图谱、网页导出、图片提取计划；
- 每次 ingest 不只是生成论文摘要，而是更新源、仪器、模型、理论、综合比较和元信息。

## 第一次使用

解压到项目根目录后启动 Claude Code：

```powershell
claude
```

对 Claude Code 说：

```text
请先阅读 CLAUDE.md 和 prompts/00_初始化中文知识库.md，然后初始化这个中文优先的高能天体物理知识库。初始化完成后不要 ingest，先报告目录、seed pages、lint 和 graph 结果。
```

## 重要约定

- 默认中文写作。
- 目录尽量中文化。
- `prompt emission` 写成“瞬时辐射”。
- `afterglow` 写成“余辉”。
- `light curve` 写成“光变曲线”。
- `spectral evolution` 写成“能谱演化”。
- 论文标题、仪器名、模型名、变量、公式保留英文。
- 网页 UI 和星图 UI 使用中文。
- 图片提取优先使用 arXiv source；如需本地工具，优先检查 `E:\paper_figure_extractor` 下的图片提取工具。
- 长篇公式推导和理论主线写入 `wiki_textbook/`；`wiki/` 页面只保留摘要式结论和链接。

## 包含内容

```text
CLAUDE.md
prompts/
templates/
scripts/
docs/
site_blueprint/
.claude/skills/
.github/workflows/
```
