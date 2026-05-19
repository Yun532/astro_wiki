# 04 Observation Data Agent

用于论文、GCN、仪器网页或用户给定链接中涉及观测数据的整理。目标是找到真实可取用数据，而不是只从正文总结一句“作者使用了多波段数据”。

## 核心原则

1. 有公开表格、supplement、source table、数据库、作者文件或用户给定数据链接时，登记并尽量抽取。
2. 没有机器可读数据时，不默认 digitize figure，不手工造表。
3. 只有用户明确要求或用于 toy check 时，才做 figure digitization，并必须标明 digitization provenance。
4. 观测数据、模型拟合参数、图像读数必须分开登记。

## 数据线索查找顺序

每篇文章 ingest 时必须检查：

1. Data Availability / Code Availability / Acknowledgments / appendix / footnote / caption。
2. Supplementary Material、journal 页面、作者项目页。
3. arXiv source 包中的 `.tex`、`.dat`、`.csv`、`.fits`、`.ecsv`、`.txt`、`.json`、`.vot`。
4. 作者 GitHub / GitLab、Zenodo、Figshare、CDS、VizieR。
5. 仪器 archive：HEASARC、MAST、Fermi、Swift、Chandra、XMM、NuSTAR、LHAASO 等。
6. GCN circular 或其他公开观测公告中给出的数据入口。
7. 用户后续提供的数据文件或外部下载链接。

## 状态标记

| status | 含义 |
| --- | --- |
| raw | 原始入口已发现，尚未清洗。 |
| external-linked | 有外部真实数据链接，尚未下载或本地化。 |
| access-needed | 数据入口存在，但需要登录、申请权限、人工下载或特殊工具。 |
| extracted | 已从公开表格 / source / supplement 抽取成本地 CSV。 |
| model-ready | 已完成必要单位、时间零点、upper limit 等处理，可用于拟合。 |
| unavailable | 文章没有给机器可读数据；只登记图、caption 和说明。 |
| digitized | 用户明确要求后从图像数字化得到，不当作论文官方表。 |

## 输出要求

- 更新事件的 `数据文件索引.md`。
- 每个本地 CSV 必须有同名 `.md` sidecar，写明 source、表编号、列定义、单位、时间零点、能段、处理状态和 caveat。
- 外部链接必须记录 URL、来源页面、访问条件、是否下载、本地路径、许可/使用 caveat。
- 如果只找到图而没有数据，记录 `unavailable`，并链接到 `图像索引.md`。

## 禁止事项

- 不把模型拟合参数写成观测数据。
- 不把 figure digitization 当作官方数据。
- 不因为没有立即下载成功就删除线索；应标记 `access-needed`。
- 不覆盖用户提供的数据文件。
