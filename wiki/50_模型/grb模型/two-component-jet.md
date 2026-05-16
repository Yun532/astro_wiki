---
title: 双成分 GRB 喷流模型
type: model
status: growing
last_updated: 2026-05-10
tags: [GRB, jet, two-component-jet, structured-jet, afterglow, synchrotron]
source_count: 4
confidence: medium
related:
  - ../../40_综合比较/模型比较/two-component-grb-models.md
  - afterglow-dynamics.md
  - ../../20_天体源/grb/grb-030329/index.md
  - ../../20_天体源/grb/grb-080319b/index.md
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

## GRB 030329 事件级案例

详见事件页：[GRB 030329](../../20_天体源/grb/grb-030329/index.md)。Berger et al. 对 GRB 030329 做 radio calorimetry，并将该事件解释为 two-component explosion：

- 事件红移 z = 0.1685，使 radio calorimetry 成为可能。
- centimetre radio observations 约在 burst 后 13.8 h 开始；作者还结合 millimetre / sub-millimetre 数据。
- radio light curve 在 t ≳ 10 d 快速下降，且低于约 22.5 GHz 的 peak flux 下降，被作者解释为 collimated explosion 的证据。
- radio component 需要 t_j,rad ≈ 9.8 d，对应 θ_j,rad ≈ 0.3 rad ≈ 17°；beaming-corrected kinetic energy E_K ≈ 2.5×10^50 erg。
- optical / X-ray early break 在 t ≈ 0.55 d；在相同参数假设下，作者将 early component 建模为 θ_j ≈ 0.09 rad ≈ 5° 的 narrow jet。
- t ≲ 1.5 d 的 optical resurgence 被解释为较慢 second component 的 deceleration / emergence；narrow component 负责 gamma-ray burst 与 early optical / X-ray afterglow，wide component 负责 radio afterglow 与 late optical emission。
- narrow jet 的 beaming-corrected gamma-ray energy 约 E_gamma ≈ 5×10^49 erg；作者强调 total explosive yield 由 mildly relativistic wide component 主导，因此可接近其他 GRB 的总能量尺度。

这个案例是 two-component jet 的事件级支持 source，但其中 component assignment、角度和能量都是 Berger et al. 的模型解释；观测事实是 radio / optical / X-ray light curves、早期 break、late optical resurgence 和 SN 2003dh contamination / subtraction 问题。

## GRB 080319B naked-eye burst 案例

详见事件页：[GRB 080319B](../../20_天体源/grb/grb-080319b/index.md)。Racusin et al. 将 GRB 080319B 的 broadband observations 解释为 narrow core + wider jet 的两成分结构：

- GRB 080319B 的 prompt optical emission 达到约 visual magnitude 5.3，是 naked-eye burst；事件红移 z ≈ 0.937。
- prompt optical 与 gamma-ray light curves 在时间上相关，但 optical flux 远高于 gamma-ray spectrum 的低能外推，支持至少两个 spectral components 的解释。
- source interpretation 中，观测者接近 very narrow core 的轴向；narrow core opening angle 约 0.2°，用于解释极端 apparent brightness。
- wider component opening angle 约 4°，用于解释后续 afterglow 行为。
- 该 source 还将环境解释为 wind-like medium，符合 long GRB 的 massive-star origin 图像。

这个案例说明 two-component / narrow-core-wide-jet 模型不只用于 late afterglow bump，也可用于解释 prompt optical/gamma spectral mismatch、极端 on-axis brightness 与 chromatic afterglow behavior 的组合。但 opening angle、Lorentz factor 和环境参数都属于 Racusin et al. 的模型解释。

## 与 structured jet 的关系

Salafia & Ghirlanda 的 jet-structure review 将 GRB jet structure 概括为由 central engine、progenitor vestige / cocoon interaction、breakout 和 external-shock evolution 共同塑造的角向结构。若忽略径向结构并关注 kinetic energy，常用描述是 angular energy profile dE/dΩ(θ,t) 和 average Lorentz factor profile Γ(θ,t)。

在这个谱系中，two-component jet 可视为 structured outflow 的离散化极限：能量和 Lorentz factor 主要分成 narrow / wide 两个区域；continuous structured jet 则使用 top-hat、Gaussian、power-law 或 quasi-universal angular profile 等连续参数化。两者都可产生非单一 power-law afterglow，但 two-component jet 更强调 component transition、t_dec,w 与 t_jet,n 的相对时序，以及 wide component 是否掩盖 narrow jet break。

该 review 还强调，对于 off-core viewing angle，early afterglow 可先由 line-of-sight material 主导，随后 emission 逐渐转向由更靠近 jet axis 的区域主导；这使 light curve、SED、VLBI centroid motion 和 luminosity function 都可能携带 jet structure 信息。

## 使用 caveat

- 本页记录的是模型定义和预测，不是单一事件观测事实。
- flux ratio、break timing 和 brightening 是否可见依赖 θ_obs、E_w/E_n、θ_j,w/θ_j,n、η_n、η_w、p、外部介质密度和 synchrotron spectral regime。
- 将某个 GRB 的 bump、flattening 或 jet-break 缺失归因于 two-component jet 时，必须使用该事件的 source-backed light curve 和 SED 约束。

## 图像候选

- `raw/arxiv/astro-ph-0410384/astro-ph-0410384-source.tar.gz` 中的 `f1.eps`：R-band afterglow light curve from a two-component jet。
- `f2.eps`：几何和时序参数改变下的 light-curve behavior。
- `f3.eps`：GRB 030329 参数下的 R-band two-component model light curve。
- `raw/arxiv/astro-ph-0308187/astro-ph-0308187-source.tar.gz` 中的 `f1.ps`：GRB 030329 radio light curves and synchrotron model。
- `f2.ps`：GRB 030329 radio-to-X-ray light curves, early optical break, late optical resurgence, and SN component。
- `f3.ps`：GRB energy histograms comparing E_gamma, X-ray-inferred kinetic energy, and total relativistic energy。
- `raw/arxiv/0805.1557/0805.1557.pdf`：GRB 080319B prompt optical / gamma-ray comparison and broadband afterglow model figures；TeX source unavailable in this session, so figure filenames need later provenance check before embedding。
- `raw/arxiv/2206.11088/2206.11088-source.tar.gz` 中的 `figures/Eiso_struct_examples.pdf`、`figures/offaxis-sj-examples.pdf`、`figures/jet_cocoon_images.pdf`：structured jet viewing-angle 和 off-axis afterglow / image examples。

## 相关页面

- [Two-component GRB model comparison](../../40_综合比较/模型比较/two-component-grb-models.md)
- [Afterglow dynamics](afterglow-dynamics.md)
- [GRB 030329](../../20_天体源/grb/grb-030329/index.md)
- [GRB 080319B](../../20_天体源/grb/grb-080319b/index.md)

## 来源

- F. Peng, A. Königl and J. Granot, “Two-Component Jet Models of Gamma-Ray Burst Sources,” ApJ 626, 966-977 (2005), arXiv:astro-ph/0410384, DOI: 10.1086/430045。
- E. Berger et al., “A common origin for cosmic explosions inferred from calorimetry of GRB030329,” Nature 426, 154-157 (2003), arXiv:astro-ph/0308187, DOI: 10.1038/nature01998。
- J. L. Racusin et al., “Broadband observations of the naked-eye gamma-ray burst GRB 080319B,” Nature 455, 183-188 (2008), arXiv:0805.1557, DOI: 10.1038/nature07270。
- O. S. Salafia and G. Ghirlanda, “The Structure of Gamma Ray Burst Jets,” arXiv:2206.11088。
