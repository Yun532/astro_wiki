# 01 Ingest source 通用流程

当我提供一个 source 文件或 URL 时，请按此流程执行。

## 流程

1. 识别 source 类型。
2. 确认 raw source 是否已保存；如果没有保存，先保存到合适位置。
3. 读取 source。
4. 提取 key claims、关键数值、公式、图表、数据产品、仪器、天体源、模型、假设、限制、open questions。
5. 更新相关 wiki 页面。
6. 更新 `index.md`、`log.md`、`wiki/90_元信息/literature-index.md`。
7. 若有冲突，更新 `wiki/90_元信息/contradictions.md`。
8. 若有未解决问题，更新 `wiki/90_元信息/open-questions.md`。
9. 运行 lint 和 graph。

## 写作规则

- 默认中文。
- 论文标题、仪器名、模型名、公式保留英文。
- 观测事实和模型解释分开。
- 不要过度推断。
- 每条关键 claim 必须有来源。

## 输出报告

报告新建页面、修改页面、key claims、新增公式或模型内容、新增图像索引、open questions、contradictions、lint / graph 结果、下一步建议。
