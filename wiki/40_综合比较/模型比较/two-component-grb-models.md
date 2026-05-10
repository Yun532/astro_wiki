---
title: Two-component GRB model comparison
type: comparison
status: growing
last_updated: 2026-05-10
tags: [GRB, model-comparison, two-component-jet, structured-jet, afterglow]
source_count: 1
confidence: medium
related:
  - ../../50_模型/grb模型/two-component-jet.md
  - ../../50_模型/grb模型/afterglow-dynamics.md
  - grb-221009a-model-comparison.md
---

# Two-component GRB model comparison

## 当前已 ingest 模型

### Peng, Königl & Granot two-component jet

Peng, Königl & Granot 建立的 two-component jet model 将 GRB outflow 分为 narrow / wide 两个成分。narrow component 具有 θ_j,n 和 η_n ≳ 10^2，被用作 prompt gamma-ray emission 与 early afterglow 的来源；wide component 具有 θ_j,w ≲ 3 θ_j,n 和 η_w ~ 10，可在 t_dec,w 后影响 late afterglow。

## 可区分观测量

| 观测量 | two-component jet 预期 | 使用 caveat |
| --- | --- | --- |
| early optical afterglow | narrow component 可主导 early afterglow。 | 需要知道 viewing angle 和 spectral regime。 |
| late optical / radio brightening | 如果 E_w/E_n > 1，wide component 可在 t_dec,w 后接管或产生 bump / flattening。 | 不能只凭单一 bump 判定，需要 SED 和多波段同步性。 |
| jet break | t_dec,w 与 t_jet,n 接近时，wide component emergence 可 mask narrow jet break。 | jet break 缺失也可能由其他 structured jet 或 energy injection 解释。 |
| energy correction | 若用 wide angle 代替 narrow angle 做 beaming correction，可能高估 prompt gamma-ray energy 和 emission efficiency。 | 必须区分 true energy E 与 isotropic-equivalent energy E_iso。 |
| X-ray flash | 可解释为 θ_obs > θ_j,n 的 off-axis GRB jet。 | 需要和 XRF-specific population source 对照。 |

## 与 GRB 221009A 模型比较的接口

GRB 221009A 页面中已经记录 LHAASO narrow jet、O'Connor et al. shallow structured jet 与 Laskar et al. radio/mm extra component。Peng et al. source 为后续比较提供通用判据：如果某个 late component 在 t_dec,w 后出现并掩盖 narrow jet break，则 two-component jet 是候选解释之一；但 GRB 221009A 的具体归因必须依赖事件级 source，而不能由本模型页直接推出。

## 待扩展 source

- GRB 030329 event-specific calorimetry / two-component source。
- GRB 080319B naked-eye burst broadband source。
- GRB jet-structure review source，用于比较 top-hat、structured jet、two-component jet 的谱系。

## 相关页面

- [双成分 GRB 喷流模型](../../50_模型/grb模型/two-component-jet.md)
- [Afterglow dynamics](../../50_模型/grb模型/afterglow-dynamics.md)
- [GRB 221009A model comparison](grb-221009a-model-comparison.md)

## 来源

- F. Peng, A. Königl and J. Granot, “Two-Component Jet Models of Gamma-Ray Burst Sources,” ApJ 626, 966-977 (2005), arXiv:astro-ph/0410384, DOI: 10.1086/430045。
