---
title: INTEGRAL / IBIS-PICsIT
type: instrument
status: growing
last_updated: 2026-05-10
tags: [INTEGRAL, IBIS, PICsIT, gamma-ray, GRB, GRB 221009A]
source_count: 1
confidence: medium
related:
  - ../../20_天体源/grb/grb-221009a/瞬时辐射.md
  - ../../20_天体源/grb/grb-221009a/能谱演化.md
  - ../../20_天体源/grb/grb-221009a/光变曲线.md
  - ../../20_天体源/grb/grb-221009a/余辉.md
---

# INTEGRAL / IBIS-PICsIT

## 页面定位

本页记录 INTEGRAL 及其 IBIS-PICsIT soft gamma-ray detector 与高能暂现源相关的观测事实。当前正式 ingest 的 source 只覆盖 GRB 221009A 的 prompt / early afterglow spectral-timing 分析。

## GRB 221009A 代表性结果

Rodi & Ubertini 使用 INTEGRAL/IBIS-PICsIT spectral-timing data 分析 GRB 221009A 的 200–2600 keV 时间和能谱演化。

已整理事实：

- PICsIT 是 IBIS 的 soft gamma-ray detector；该 source 使用 200–2600 keV spectral-timing data。
- PICsIT spectral-timing data 在 8 个宽能带提供 7.8 ms 时间分辨率。
- GRB 221009A 发生时 INTEGRAL 正在观测 XTE J1701-462，GRB 方向约偏离 pointing direction 65.8°。
- prompt emission 持续超过 600 s，包括 precursor。
- PICsIT light curve 显示 afterglow emission 在约 T0 + 630 s 开始占主导，并以 1.6 ± 0.2 的斜率衰减。
- 论文报告 flux-tracking spectral behavior：亮度越高时 spectrum 越 soft；spectral-index / flux relation 在 burst 过程中发生变化。

## 使用 caveat

- 该 source 说明最亮 prompt pulses 的若干时间段存在 telemetry gaps，因此部分 peak behavior 未被 PICsIT 完整记录。
- 作者移除了 bad time intervals，并报告未发现接近 telemetry maximum 的 time bins，说明 PICsIT 未受 pile-up effects 影响。
- flux-tracking 是观测到的谱演化关系；进一步的 emission-process 解释需要归因给论文作者。

## 相关页面

- [GRB 221009A 瞬时辐射](../../20_天体源/grb/grb-221009a/瞬时辐射.md)
- [GRB 221009A 能谱演化](../../20_天体源/grb/grb-221009a/能谱演化.md)
- [GRB 221009A 光变曲线](../../20_天体源/grb/grb-221009a/光变曲线.md)
- [GRB 221009A 余辉](../../20_天体源/grb/grb-221009a/余辉.md)

## 来源

- J. Rodi and P. Ubertini, “Soft Gamma-Ray Spectral and Time Evolution of GRB 221009A: Prompt and Afterglow Emission with INTEGRAL/IBIS-PICsIT,” A&A 677, L3 (2023), arXiv:2303.16943, DOI: 10.1051/0004-6361/202346373。
