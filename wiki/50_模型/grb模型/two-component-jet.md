---
title: 双成分 GRB 喷流模型
type: model
status: growing
last_updated: 2026-05-10
tags: [GRB, jet, two-component-jet, afterglow, synchrotron]
source_count: 1
confidence: medium
related:
  - ../../40_综合比较/模型比较/two-component-grb-models.md
  - afterglow-dynamics.md
---

# 双成分 GRB 喷流模型

## 模型定义

Peng, Königl & Granot 的 two-component jet model 假设 GRB outflow 包含两个物理上可区分的成分：

| 成分 | 几何 / 速度 | 主要作用 |
| --- | --- | --- |
| narrow component | opening half-angle θ_j,n；initial Lorentz factor η_n ≳ 10^2 | prompt gamma-ray emission 的来源，并主导 early afterglow。 |
| wide component | θ_j,w ≲ 3 θ_j,n；η_w ~ 10 | 围绕 narrow component 的较宽、较慢 outflow，可在 t_dec,w 后主导 late afterglow。 |

该模型使用 simple synchrotron emission model 计算 R-band afterglow light curve，并推导在主要 transition times 处 narrow / wide component 的 flux ratio。

## 典型光变行为

- 对 θ_obs < θ_j,n 的 viewing angle，如果 wide component 的 kinetic energy E_w 显著小于 narrow component 的 E_n，则 wide component 对 optical afterglow 的贡献可忽略；作者将其对应到 collapsar jet-breakout picture 中 jet core + cocoon outflow 的情形。
- 如果 E_w/E_n > 1，但 isotropic-equivalent energy ratio E_iso,w/E_iso,n 仍 <1，则 narrow component 只主导 early afterglow，wide component 可在其 deceleration time t_dec,w 后接管 afterglow。
- 典型参数下，t_dec,w ~ 0.1-1 d，且可与 narrow component 的 jet-break time t_jet,n 接近。
- 如果 t_dec,w 与 t_jet,n 接近，wide component 的出现可能 mask narrow component 的 jet break。
- jet break 被 mask 后，如果误用较宽角度估算 prompt gamma-ray beaming correction，可能高估 source 的 gamma-ray energy 和 required gamma-ray emission efficiency。

## 适用场景和案例解释

该 source 将模型用于以下解释框架：

- X-ray flash sources 可被解释为 viewing angle θ_obs > θ_j,n 的 GRB jets。
- neutron-rich hydromagnetic outflow 可能自然产生 afterglow light curve 中的 repeated brightening episodes。
- GRB 021004 和 GRB 030329 的 brightening episodes 被作者作为模型解释案例讨论；这些是模型归因，不是本页独立建立的观测事实。

## 与 structured jet 的关系

Two-component jet 是 structured outflow 的离散化极限：能量和 Lorentz factor 主要分成 narrow / wide 两个区域。它和连续 angular energy profile 的 structured jet 模型都可产生非单一 power-law afterglow，但 two-component jet 更强调 component transition、t_dec,w 与 t_jet,n 的相对时序，以及 wide component 是否掩盖 narrow jet break。

## 使用 caveat

- 本页记录的是模型定义和预测，不是单一事件观测事实。
- flux ratio、break timing 和 brightening 是否可见依赖 θ_obs、E_w/E_n、θ_j,w/θ_j,n、η_n、η_w、p、外部介质密度和 synchrotron spectral regime。
- 将某个 GRB 的 bump、flattening 或 jet-break 缺失归因于 two-component jet 时，必须使用该事件的 source-backed light curve 和 SED 约束。

## 图像候选

- `raw/arxiv/astro-ph-0410384/astro-ph-0410384-source.tar.gz` 中的 `f1.eps`：R-band afterglow light curve from a two-component jet。
- `f2.eps`：几何和时序参数改变下的 light-curve behavior。
- `f3.eps`：GRB 030329 参数下的 R-band two-component model light curve。

## 相关页面

- [Two-component GRB model comparison](../../40_综合比较/模型比较/two-component-grb-models.md)
- [Afterglow dynamics](afterglow-dynamics.md)

## 来源

- F. Peng, A. Königl and J. Granot, “Two-Component Jet Models of Gamma-Ray Burst Sources,” ApJ 626, 966-977 (2005), arXiv:astro-ph/0410384, DOI: 10.1086/430045。
