# 11 Event applications：GRB 030329、GRB 080319B、GRB 221009A

前十章建立了从相对论 beaming、fireball、external shock、synchrotron spectrum、closure relations、jet break、energy injection、structured jet 到 two-component jet 的理论链。本章不重新推导公式，而是说明如何把这些公式应用到具体事件，并强调观测事实与模型解释的边界。

## 1. 事件应用的阅读顺序

对每个 GRB，建议按三层阅读：

1. **观测事实**：redshift、fluence、light curve break、radio peak、TeV photon、multiwavelength coverage、spectral mismatch、SN contamination 等。
2. **模型解释**：jet opening angle、structured jet profile、two-component assignment、energy injection、density profile、microphysical parameters、radiative efficiency 等。
3. **非唯一性 / caveat**：同一 bump、break 或 plateau 是否也可由 refreshed shock、density variation、reverse shock、scintillation、SSC 或数据处理差异解释。

这三层不应混写。比如“radio light curve 在约 10 d 后衰减”是观测事实；“这是 17° wide component 的 jet break”是 Berger et al. 的模型解释。

## 2. 从公式到事件量的最小检查表

将前面章节用于事件时，至少检查：

| 问题 | 对应章节 | 为什么重要 |
| --- | --- | --- |
| 时间和能段是否已转到 source frame？ | 第 2 章 | `t_obs/(1+z)`、能段和 K-correction 会影响跨事件比较。 |
| `E_iso` 是否来自同一 bolometric band？ | 第 2 章 | fluence band 不同会造成 apparent energy discrepancy。 |
| 介质是 ISM 还是 wind？ | 第 4-6 章 | `Γ(t)`、`ν_c(t)`、closure relations 和 `t_dec` 标度不同。 |
| 光变 break 是 cooling、jet、injection end 还是 component transition？ | 第 6-10 章 | 不能把所有 steepening 都叫 jet break。 |
| `E` 是 isotropic-equivalent 还是 true energy？ | 第 7、9、10 章 | beaming correction 在 top-hat 与 structured jet 中含义不同。 |
| 是否需要多成分辐射？ | 第 5、8、10 章 | prompt optical/gamma mismatch 或 radio excess 不能强行塞进单一 forward shock。 |

## 3. GRB 030329：radio calorimetry 与 two-component explosion

### 3.1 观测事实入口

GRB 030329 是 nearby long GRB，redshift `z=0.1685`，并与 SN 2003dh 关联。它的价值在于 dense radio monitoring、early optical / X-ray break、late optical resurgence 和 radio calorimetry 共同约束 outflow geometry 与 energy budget。

关键观测约束包括：

- optical / X-ray light curve 在约 `t≈0.55 d` 有 early break；
- radio afterglow 在厘米波段非常明亮，并在 late time 提供 calorimetry；
- radio modeling 需要约 `t_{j,rad}≈9.8 d` 的 break；
- late optical resurgence 与 SN 2003dh contribution 叠加，photometry 和 SN subtraction 是 caveat。

### 3.2 Berger et al. 的模型解释

Berger et al. 将 GRB 030329 解释为 two-component explosion：

| 成分 | 代表 opening angle | 主要作用 | 观测约束 |
| --- | --- | --- | --- |
| narrow component | `θ_n≈0.09 rad≈5°` | gamma-ray emission 与 early optical / X-ray afterglow | `t≈0.55 d` early break |
| wide component | `θ_w≈0.3 rad≈17°` | radio afterglow 与 late optical component | `t_{j,rad}≈9.8 d` radio break |

在这个解释中，narrow component 的 beaming-corrected gamma-ray energy 约为

```tex
E_γ \approx 5\times 10^{49}\ \mathrm{erg},
```

而 wide mildly relativistic component 携带较多 kinetic energy，使 total explosive yield 可接近普通 GRB 的尺度。

### 3.3 连接前面章节

GRB 030329 对应多个章节的接口：

- 第 4 章：late radio calorimetry 已接近 trans-relativistic dynamics，不能只用 early ultra-relativistic BM scaling。
- 第 6 章：early optical break 和 late radio behavior 不应由单一 closure relation 完整解释。
- 第 7 章：不同 component 有不同 effective opening angle，单一 top-hat beaming correction 会误导。
- 第 10 章：`t_{jet,n}` 与 wide component emergence / radio break 是 two-component interpretation 的核心。

### 3.4 Caveat

GRB 030329 是 two-component jet 的经典案例，但不是直接成像证据。late optical resurgence 还受 SN 2003dh subtraction 影响；radio synchrotron modeling 的参数也依赖 microphysics、density profile 和 geometry。因此应写作“Berger et al. 解释为 two-component explosion”，而不是“观测到两个喷流”。

## 4. GRB 080319B：naked-eye burst 与 narrow-core viewing

### 4.1 观测事实入口

GRB 080319B 是著名的 naked-eye GRB，prompt optical emission 达到约 visual magnitude 5.3，redshift 约 `z≈0.937`。它的核心观测事实是 prompt optical 与 gamma-ray light curves 有时间相关性，但 optical flux 远高于 gamma-ray spectrum 的简单低能外推。

这意味着 prompt optical 和 gamma-ray emission 至少需要 distinct spectral components。该结论是观测与谱形驱动的，不依赖特定 jet geometry。

### 4.2 Racusin et al. 的模型解释

Racusin et al. 将 GRB 080319B 放入 narrow core + wider component 框架：

| 成分 | 代表 opening angle | 主要作用 |
| --- | --- | --- |
| very narrow core | `≈0.2°` | viewed nearly on-axis，解释极端 apparent brightness |
| wider component | `≈4°` | 贡献 later afterglow evolution |

该模型还 favor wind-like environment，因此 deceleration time、closure relation 和 jet-opening scaling 都应使用 wind medium 形式，而不是直接套用 ISM scaling。

### 4.3 连接前面章节

- 第 1、9 章：near-axis viewing of a very narrow core 通过 Doppler boosting 增强 apparent brightness。
- 第 2 章：prompt optical 与 gamma-ray 比较必须确保时间窗和谱定义一致。
- 第 4、6 章：wind-like medium 改变 `Γ(t)` 和 closure relation。
- 第 10 章：narrow core / wide component 是 two-component jet 的 on-axis extreme case。

### 4.4 Caveat

Geometry 可以解释极端 apparent brightness，但不能自动解释 prompt optical / gamma-ray spectral mismatch。后者需要多 spectral components 或多 emission zones。Racusin et al. 的 opening angle、Lorentz factor、density profile 和 microphysical parameters 都是模型拟合结果，不是直接观测量。

## 5. GRB 221009A：极端 `E_iso`、TeV afterglow 与 structured jet

### 5.1 观测事实入口

GRB 221009A 是 extremely bright nearby long GRB，也是当前 wiki 中 prompt energetics、TeV afterglow、radio-to-GeV afterglow 和 structured jet 解释的核心事件。需要特别注意：不同论文给出的 `E_iso`、fluence 或 luminosity 可能使用不同能段、时间积分区间和 bolometric correction。

已整理的关键观测约束包括：

- LHAASO 在最初 3000 s 内探测到超过 64,000 个 `>0.2 TeV` 光子；
- TeV flux 在 trigger 后数分钟开始、约 10 s 达峰、峰后衰减，并在约峰后 650 s 衰减变快；
- O'Connor et al. 使用前三个月 multiwavelength afterglow，记录 X-ray brightness 以约 `t^{-1.66}` 衰减；
- Laskar et al. 的 radio-to-GeV afterglow 数据跨越约 15 个数量级 photon energy，并显示 radio/mm 需要额外 component。

### 5.2 当前模型解释谱系

| Source / 模型 | 核心解释 | 需要保留的边界 |
| --- | --- | --- |
| LHAASO narrow jet | TeV afterglow 来自 narrow relativistic jet，半张角约 `0.8°`，可与 structured jet core 一致。 | narrow jet 是模型解释，不是直接成像；TeV break 是否等同 multi-band jet break 需比较。 |
| O'Connor et al. shallow structured jet | 前三个月 afterglow 指向 shallow structured jet / shallow energy profile。 | `t^{-1.66}` 是观测约束；shallow profile 是解释。 |
| Laskar et al. forward shock + extra radio component | highly collimated jet + low-density wind-like medium 可解释部分 radio-to-GeV afterglow；radio/mm 需额外 component。 | 额外 component 不服从若干简单模型，包括 simple two-component jet prescription。 |

### 5.3 连接前面章节

- 第 2 章：GRB 221009A 的 prompt fluence / `E_iso` 比较必须记录能段和 K-correction。
- 第 5 章：radio/mm excess 不能只用 optically thin single synchrotron segment 解释。
- 第 7 章：top-hat beaming correction 对 structured jet core 只能作为 effective approximation。
- 第 8 章：long-lived decay 或 extra component 可能与 energy injection 简并。
- 第 9 章：`θ_v`、`θ_c` 和 angular profile 决定 apparent `E_iso` 与 afterglow decay。
- 第 10 章：two-component jet 是候选语言，但 Laskar et al. 已指出其 radio/mm component 不符合 simple two-component prescription。

### 5.4 Caveat

GRB 221009A 的极端亮度容易诱导“单一解释”。当前更稳妥的写法是并列记录：narrow jet / structured jet core、shallow structured jet、forward shock + wind-like medium、extra radio component、SSC 或 density / injection alternatives。只有在同一 source 或后续综合拟合明确合并时，才把它们写成统一模型。

## 6. 跨事件对照

| 事件 | 最强观测约束 | 主要模型语言 | 关键 caveat |
| --- | --- | --- | --- |
| GRB 030329 | radio calorimetry、early optical/X-ray break、late optical resurgence | two-component explosion；5° narrow + 17° wide | SN 2003dh subtraction；component assignment 是模型解释 |
| GRB 080319B | naked-eye prompt optical；optical/gamma mismatch；afterglow modeling | narrow core + wider component；wind-like medium | geometry 不能单独解释 spectral mismatch |
| GRB 221009A | prompt energetics、TeV afterglow、radio-to-GeV afterglow、X-ray long decay | narrow / structured jet core；shallow structured jet；extra radio component | 多模型并列，不能提前合并成单一结构 |

## 7. 哪些量可以横向比较

比较事件时，优先比较“同类量”：

- source-frame break time：`t/(1+z)`；
- 同一能段或 bolometric-corrected `E_iso`；
- beaming-corrected energy，但必须说明 top-hat 还是 structured jet；
- component opening angle，但只在模型假设相近时比较；
- radio calorimetry energy，但注意是否已进入 trans-relativistic regime；
- spectral regime 下的 closure relation，而不是只比较 light-curve slope。

不建议直接比较：

- 不同能段的 fluence-derived `E_iso`；
- prompt gamma-ray energy 与 late kinetic energy；
- top-hat `θ_j` 与 structured jet `θ_c`；
- two-component model 的 `θ_n/θ_w` 与 continuous structured jet 的 Gaussian width；
- 单波段 bump 的出现时间。

## 8. 后续更新规则

后续 ingest 新事件或新模型论文时：

1. 先更新对应事件页的观测事实；
2. 再更新模型解释页，明确 source-specific assumptions；
3. 若引入新的理论形式，回到对应课程章补充公式或 caveat；
4. 若只是事件拟合参数，保留在事件页和模型比较页，不重复写进理论推导；
5. 若同一事件出现互相矛盾的解释，更新 open questions / contradictions。

## 来源

- E. Berger et al., “A common origin for cosmic explosions inferred from calorimetry of GRB030329,” Nature 426, 154-157 (2003), arXiv:astro-ph/0308187。
- J. L. Racusin et al., “Broadband observations of the naked-eye gamma-ray burst GRB 080319B,” Nature 455, 183-188 (2008), arXiv:0805.1557。
- LHAASO Collaboration, “A tera-electronvolt afterglow from a narrow jet in an extremely bright gamma-ray burst 221009A,” Science 380, 1390-1396 (2023), arXiv:2306.06372。
- B. O'Connor et al., “A structured jet explains the extreme GRB 221009A,” Science Advances 9, eadi1405 (2023), arXiv:2302.07906。
- T. Laskar et al., “The Radio to GeV Afterglow of GRB 221009A,” ApJL, arXiv:2302.04388。
- F. Peng, A. Königl and J. Granot, “Two-Component Jet Models of Gamma-Ray Burst Sources,” ApJ 626, 966-977 (2005), arXiv:astro-ph/0410384。
