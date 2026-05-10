---
title: Afterglow dynamics
type: model
status: growing
last_updated: 2026-05-10
tags: [GRB, afterglow, jet-break, two-component-jet, structured-jet]
source_count: 3
confidence: medium
related:
  - two-component-jet.md
  - ../../40_综合比较/模型比较/two-component-grb-models.md
---

# Afterglow dynamics

## 本页用途

本页用于记录 GRB afterglow dynamics 模型、公式、假设和来源。当前已正式整理 two-component jet 与 structured jet review source，用于说明 narrow / wide component 的 deceleration time、jet-break time、afterglow light curve transition，以及 angular jet structure 对 off-axis afterglow 的影响。

## 当前已记录模型接口

- [双成分 GRB 喷流模型](two-component-jet.md)：narrow component 与 wide component 的 opening angle、Lorentz factor、energy ratio 和 R-band afterglow behavior。
- t_dec,w 与 t_jet,n 的相对时序可决定 wide component 是否掩盖 narrow component 的 jet break。
- GRB 030329 的 Berger et al. source 提供事件级例子：early optical/X-ray break t ≈ 0.55 d 与 radio jet break t_j,rad ≈ 9.8 d 被解释为 5° narrow component 和 17° wide component 的不同 dynamical timescale。
- Salafia & Ghirlanda review 将 structured jet afterglow 连接到 angular energy profile dE/dΩ(θ,t)、Γ(θ,t)、viewing angle θ_v 和 external shock evolution；对于 θ_obs > θ_c 的观测者，不同时刻可由不同角区主导 emission。
- GW170817 / GRB170817A 是 off-axis structured jet 的关键案例：pre-peak light curve 与 quasi-spherical outflow 存在简并，VLBI centroid motion 和 compact image size 对打破简并很重要。
- afterglow bump、flattening、shallow rise 或 jet-break 缺失都不是 two-component / structured jet 的唯一证据，必须结合多波段 light curve、SED、成像或 centroid motion 约束。

## 未来应记录

- standard forward shock dynamics。
- jet break 的几何解释和 alternative explanations。
- energy injection、refreshed shock、structured jet 与 two-component jet 的可区分观测量。
- structured jet angular profile 的完整推导应优先进入 `wiki_textbook/`。

## 相关页面

- [双成分 GRB 喷流模型](two-component-jet.md)
- [Two-component GRB model comparison](../../40_综合比较/模型比较/two-component-grb-models.md)
- [知识库总览](../../00_总览/index.md)

## 来源

- F. Peng, A. Königl and J. Granot, “Two-Component Jet Models of Gamma-Ray Burst Sources,” ApJ 626, 966-977 (2005), arXiv:astro-ph/0410384, DOI: 10.1086/430045。
- E. Berger et al., “A common origin for cosmic explosions inferred from calorimetry of GRB030329,” Nature 426, 154-157 (2003), arXiv:astro-ph/0308187, DOI: 10.1038/nature01998。
- O. S. Salafia and G. Ghirlanda, “The Structure of Gamma Ray Burst Jets,” arXiv:2206.11088。
