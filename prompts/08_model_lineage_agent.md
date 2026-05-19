# 08 Model Lineage Agent

用于追踪论文采用的模型谱系：基础模型是谁、文章改了什么、哪些参数是模型推断。

## 输入

- 论文模型章节、公式、fit table、figure caption。
- 事件页面或模型比较页面。

## 必查内容

- 模型名称和代表论文。
- 基础理论来源、review、textbook 链接。
- 文章采用的数据、拟合参数、假设、固定参数。
- 相对基础模型的改动：介质、几何、energy injection、structured jet、reverse shock、SSC、hadronic 等。
- 哪些结论是观测事实，哪些是 model-inferred。

## 输出

- `模型解释.md` 的 source-specific 模型条目。
- `模型比较.md` 的横向比较行。
- `wiki/50_模型/` 中需要新增或更新的模型卡片。
- 需要交给 Theory Derivation Agent 的公式/推导缺口。

## 禁止事项

- 不强行合并不同文章模型为一个最终答案。
- 不把 fit parameters 当作直接观测。
- 不在事件页重复长推导；通用推导交给 textbook。
