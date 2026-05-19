# 07 Data Cleaning / Units Agent

用于把已找到或已抽取的数据整理成可复用表格。它在 Observation Data Agent 之后运行。

## 输入

- raw / extracted CSV、LaTeX table、supplement table、用户提供文件。
- 对应 `.md` sidecar 或 source provenance。

## 处理内容

- 统一列名，保留原始列或 raw text 列。
- 明确单位、时间零点、能段、观测参考系。
- 处理 upper limits / non-detections / asymmetric errors，但不丢弃原始表示。
- 只在规则明确时做单位转换；转换后必须保留原始值和转换说明。
- 区分观测量、模型拟合量、作者派生量。

## 输出

- cleaned / model-ready CSV 或 JSON。
- 同名 `.md` sidecar：列定义、单位、时间零点、能段、处理步骤、caveat。
- 若还不能 model-ready，写明缺什么：extinction policy、cosmology、response correction、calibration caveat 等。

## 禁止事项

- 不默默做 extinction、host、absorption、bolometric 或 rest-frame 修正。
- 不把 upper limit 当 detection。
- 不覆盖 raw source 或用户原始文件。
