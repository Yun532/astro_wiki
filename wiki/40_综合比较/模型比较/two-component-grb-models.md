---
title: Two-component GRB model comparison
type: comparison
status: growing
last_updated: 2026-05-10
tags: [GRB, model-comparison, two-component-jet, structured-jet, afterglow]
source_count: 4
confidence: medium
related:
  - ../../50_模型/grb模型/two-component-jet.md
  - ../../50_模型/grb模型/afterglow-dynamics.md
  - grb-221009a-model-comparison.md
  - ../../20_天体源/grb/grb-030329/index.md
  - ../../20_天体源/grb/grb-080319b/index.md
---

# Two-component GRB model comparison

## 当前已 ingest 模型

### Peng, Königl & Granot two-component jet

Peng, Königl & Granot 建立的 two-component jet model 将 GRB outflow 分为 narrow / wide 两个成分。narrow component 具有 θ_j,n 和 η_n ≳ 10^2，被用作 prompt gamma-ray emission 与 early afterglow 的来源；wide component 具有 θ_j,w ≲ 3 θ_j,n 和 η_w ~ 10，可在 t_dec,w 后影响 late afterglow。

### Berger et al. GRB 030329 calorimetry case

事件页：[GRB 030329](../../20_天体源/grb/grb-030329/index.md)。Berger et al. 使用 GRB 030329 的 radio calorimetry 和 optical / X-ray light curve 约束，提出事件级 two-component explosion 解释：narrow 5° ultra-relativistic component 负责 gamma-ray burst 与 early optical / X-ray afterglow，wide 17° mildly relativistic component 负责 radio afterglow 与 late optical emission。该 source 的关键比较价值在于：early optical/X-ray break、late optical resurgence、radio jet break 和 total relativistic energy 可以共同约束 component assignment，而不是只凭一个 bump 判定模型。

### Racusin et al. GRB 080319B naked-eye burst case

事件页：[GRB 080319B](../../20_天体源/grb/grb-080319b/index.md)。Racusin et al. 把 GRB 080319B 的极亮 naked-eye optical prompt emission、optical/gamma-ray spectral mismatch 和 afterglow behavior 放入 narrow core + wider jet 框架中解释。该 source 的比较价值在于：two-component / structured outflow 不只用于解释 late-time bump，也可用于解释 on-axis narrow core 造成的极端 apparent brightness 和 prompt 多成分辐射。

### Salafia & Ghirlanda GRB jet-structure review

Salafia & Ghirlanda 将 top-hat、continuous structured jet、quasi-universal structured jet 和 two-component / core-wing 图像放入统一谱系：jet structure 可由 dE/dΩ(θ,t) 与 Γ(θ,t) 等 angular profiles 表征，但这些 profiles 由 launch、propagation、cocoon / breakout 和 external-shock evolution 共同塑造，因此不同论文的参数化不应强行等同。该 review 的比较价值在于给出判断框架：prompt Eiso / Epeak / Liso、luminosity function、off-axis afterglow rise、post-peak core-dominated decay、VLBI centroid motion 都可能约束 jet angular structure。

## 可区分观测量

| 观测量 | two-component jet 预期 | 使用 caveat |
| --- | --- | --- |
| early optical afterglow | narrow component 可主导 early afterglow。 | 需要知道 viewing angle 和 spectral regime。 |
| late optical / radio brightening | 如果 E_w/E_n > 1，wide component 可在 t_dec,w 后接管或产生 bump / flattening。 | 不能只凭单一 bump 判定，需要 SED 和多波段同步性。 |
| jet break | t_dec,w 与 t_jet,n 接近时，wide component emergence 可 mask narrow jet break。 | jet break 缺失也可能由其他 structured jet 或 energy injection 解释。 |
| energy correction | 若用 wide angle 代替 narrow angle 做 beaming correction，可能高估 prompt gamma-ray energy 和 emission efficiency。 | 必须区分 true energy E 与 isotropic-equivalent energy E_iso。 |
| X-ray flash | 可解释为 θ_obs > θ_j,n 的 off-axis GRB jet。 | 需要和 XRF-specific population source 对照。 |
| GRB 030329-like calorimetry | radio t_j,rad ≈ 9.8 d / θ_j ≈ 17° 与 optical/X-ray t_j,opt ≈ 0.55 d / θ_j ≈ 5° 可支持 two-component interpretation。 | 角度、能量和 component assignment 是 Berger et al. 的模型解释；需要注意 SN 2003dh subtraction 和部分 early optical 数据的初步性质。 |
| GRB 080319B-like naked-eye prompt emission | on-axis narrow core 可解释极端 apparent brightness；prompt optical/gamma spectral mismatch 需要多 spectral components。 | narrow core θ ≈ 0.2°、wide component θ ≈ 4° 和 wind-like medium 都是 Racusin et al. 的模型解释。 |
| structured jet population / off-axis afterglow | angular dE/dΩ 和 Γ profile 可影响 Eiso、Epeak、luminosity function、afterglow rise 和 VLBI centroid motion。 | Review-level framework；具体事件仍需 source-specific light curve、SED、imaging 或 population analysis。 |

## 与 GRB 221009A 模型比较的接口

GRB 221009A 页面中已经记录 LHAASO narrow jet、O'Connor et al. shallow structured jet 与 Laskar et al. radio/mm extra component。Peng et al. source 为后续比较提供通用判据：如果某个 late component 在 t_dec,w 后出现并掩盖 narrow jet break，则 two-component jet 是候选解释之一；但 GRB 221009A 的具体归因必须依赖事件级 source，而不能由本模型页直接推出。

## 待扩展 source

- 后续需要 structured jet / top-hat jet 的原始模型论文和标准 afterglow review，用于把 review-level 谱系拆成可推导公式链。

## 相关页面

- [双成分 GRB 喷流模型](../../50_模型/grb模型/two-component-jet.md)
- [Afterglow dynamics](../../50_模型/grb模型/afterglow-dynamics.md)
- [GRB 030329](../../20_天体源/grb/grb-030329/index.md)
- [GRB 080319B](../../20_天体源/grb/grb-080319b/index.md)
- [GRB 221009A model comparison](grb-221009a-model-comparison.md)

## 来源

- F. Peng, A. Königl and J. Granot, “Two-Component Jet Models of Gamma-Ray Burst Sources,” ApJ 626, 966-977 (2005), arXiv:astro-ph/0410384, DOI: 10.1086/430045。
- E. Berger et al., “A common origin for cosmic explosions inferred from calorimetry of GRB030329,” Nature 426, 154-157 (2003), arXiv:astro-ph/0308187, DOI: 10.1038/nature01998。
- J. L. Racusin et al., “Broadband observations of the naked-eye gamma-ray burst GRB 080319B,” Nature 455, 183-188 (2008), arXiv:0805.1557, DOI: 10.1038/nature07270。
- O. S. Salafia and G. Ghirlanda, “The Structure of Gamma Ray Burst Jets,” arXiv:2206.11088。
