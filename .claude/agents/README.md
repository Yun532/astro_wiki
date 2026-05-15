# Project Claude Code agents

本目录保存本项目可共享的 Claude Code subagent 配置。

## 分工

- `paper-reader`：阅读论文和 raw source，提取 source-backed claims、公式、数值、图表和 caveat，不直接改 wiki。
- `knowledge-integrator`：把阅读结果整合进 `wiki/` 的模型、仪器、理论、比较和元信息页面。
- `event-curator`：维护 `wiki/20_天体源/`，为 GRB 等事件建立正式事件节点。
- `course-planner`：维护 `wiki_textbook/`，规划课程 / review 式理论逻辑，补基础知识并写详细推导。
- `site-maintainer`：维护 Astro Starlight、导航、导出、知识图谱页面和 GitHub Pages 路由。
- `code-maintainer`：维护脚本、lint、graph builder、export automation 和 CI。

## 推荐流水线

```text
paper-reader
→ knowledge-integrator
→ event-curator（若涉及具体天体源 / 事件）
→ course-planner（若涉及公式、推导或基础理论链条）
→ site-maintainer
→ code-maintainer（若工具链需要变化）
→ 主 agent 最终验证、提交、部署
```

主 agent 负责调度和最终一致性，避免多个 agent 同时修改同一文件。
