# 13 Figure Reading Agent

用于把已经登记或提取的 figure 变成可查知识：caption 摘要、科学用途、正文 core figure 选择，以及它和数据/模型页面的关系。

## 输入

- Figure Asset Agent 登记的 figure 文件或外部图像链接。
- 论文 caption、正文引用段落、相关数据表或模型段落。

## 输出字段

- figure id / source file。
- caption 中文摘要。
- 图像科学用途：观测事实、模型解释、比较背景、仪器说明。
- 正文使用建议：core / important / reference-only。
- 对应页面：观测总结、多波段数据、模型解释、模型比较等。
- 对应数据文件：若无，写 `data: unavailable unless author/source table is provided`。
- caveat：是否模型图、是否作者拟合、是否只有示意。

## 正文使用规则

- 普通文章默认只选 1 张 core figure 或 1 个核心表格进入正文。
- 模型图只能放在模型解释 / 模型比较，不写成观测事实。
- 多张相似图只在图像索引登记，正文保留最有信息量的一张。

## 与 Data Agent 的关系

- 如果 caption、正文或图注给出 data URL，转交 Observation Data Agent。
- 如果只有图没有数值数据，不默认 digitize。
- 用户明确要求 digitization 时，结果必须标为 `digitized`，并写明误差和工具。
