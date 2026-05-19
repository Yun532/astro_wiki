# Agent Roster

本目录中的 agent prompt 用于把论文 ingest 拆成稳定分工。普通 ingest 先读 `01_ingest_source.md` 或 `02_ingest_arxiv_paper.md`，再按任务调用对应 agent。

这些 prompt 是 GRB / 天文知识库扩展层的独立规则文件，不是 Codex UI 里的运行时 subagent，也不会自动接管原项目 agent。若需要并行执行，应在当前任务和当前分支中单独启动，明确每个 agent 的输入、输出和写入范围；不要修改或替换原有项目 agent 配置。

## 当前 Agent

| agent | prompt | 主要职责 | 主要输出 |
| --- | --- | --- | --- |
| 文献索引 Agent | `06_literature_index_agent.md` | 拆论文、列 claim/table/figure/model/formula 清单 | 文献卡片、source-to-page 更新计划 |
| 观测数据 Agent | `04_observation_data_agent.md` | 找真实数据入口、抽公开表格、登记 external/access-needed | `数据文件索引.md`、CSV sidecar |
| 图像提取 Agent | `05_figure_agent.md` | 查找/提取 figure asset、比对已有资产、记录 provenance | figure 文件、asset provenance |
| 图像说明 / 读图 Agent | `13_figure_reading_agent.md` | caption 中文说明、科学用途、正文 core figure 选择 | `图像索引.md`、正文图像说明 |
| 数据清洗 / 单位 Agent | `07_data_cleaning_units_agent.md` | 单位、时间零点、upper limit、model-ready 规则 | cleaned CSV/JSON、列定义 |
| 模型谱系 Agent | `08_model_lineage_agent.md` | 追溯基础模型、文章变体、model-inferred 参数 | `模型解释.md`、`模型比较.md` |
| 公式推导 Agent | `09_theory_derivation_agent.md` | 从假设到观测量的推导链 | `wiki_textbook/`、符号表、公式索引 |
| 代码实现 Agent | `10_code_reproduction_agent.md` | 按理论页实现通用函数和事件脚本 | `reproduce/grb/core/`、`models/`、`events/` |
| 复现验证 Agent | `11_reproduction_validation_agent.md` | 检查代码是否复现理论或论文数量级 | `reproduce/grb/validation/` |
| 知识库质检 Agent | `12_quality_graph_agent.md` | 检查链接、来源、事实/模型边界、open questions | 元信息页、lint/graph 建议 |

## 分工原则

- 这些 agent 只做补充和局部修订；原知识库已有页面、已有 agent 和已有 workflow 继续保留。
- 每次运行前必须说明该 agent 的目标页面 / 数据目录 / 输出文件；任务结束后关闭或收束，不长期挂在原项目里。
- 文献索引 Agent 只拆解任务，不替其他 agent 完成抽表、抽图或模型推导。
- 观测数据 Agent 只处理真实数据入口和表格，不把模型拟合参数写成观测事实。
- 图像提取 Agent 只处理 asset 和 provenance；图像说明 Agent 负责读图和正文使用；二者都不默认 digitize。
- 模型谱系和公式推导分开：前者管“文章用了哪个模型”，后者管“模型从假设怎么推到公式”。
- 代码实现和复现验证分开：前者写代码，后者检查是否可信。
