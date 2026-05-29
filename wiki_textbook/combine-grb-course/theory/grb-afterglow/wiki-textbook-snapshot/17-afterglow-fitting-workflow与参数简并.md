# 17 Afterglow fitting workflow 与参数简并

前面章节给出了 GRB afterglow 的主要理论模块：relativistic dynamics、synchrotron spectrum、closure relations、jet break、energy injection、structured jet、two-component jet、reverse shock、density variation、SSC、radio calorimetry 和几何诊断。本章把它们组织成一个实际使用流程：如何从多波段数据走到模型解释，并且不把模型假设写成观测事实。

Afterglow fitting 的核心困难不是公式不够，而是参数简并太多。`E_k`、`n/A_*`、`ε_e`、`ε_B`、`p`、`θ_j`、`θ_v`、energy injection、density structure 和 extra components 都可能产生相似 light curve。因此可靠写法必须保留 assumptions、alternatives 和 caveats。

## 1. 数据整理优先于模型选择

开始拟合前，先统一数据定义：

1. redshift `z`；
2. observer-frame time 与 source-frame time；
3. observing frequency / energy band；
4. Galactic extinction、host extinction、X-ray absorption；
5. flux density、energy flux、fluence 或 count rate 的转换；
6. upper limits 与 non-detections；
7. prompt、afterglow、SN/kilonova、host contamination 的分离。

时间转换最基本的是

```tex
t_{src}=\frac{t_{obs}}{1+z}.
```

能量 / 频率转换为

```tex
ν_{src}=(1+z)ν_{obs}.
```

若这些基础定义不一致，后面的 closure relation 或 energy estimate 都会失去意义。

## 2. 先做 SED，再解释 light curve

单波段 light curve slope 不能唯一确定模型。更稳妥的顺序是：先在相近时间构造 SED，判断 observing bands 相对 `ν_m`、`ν_c`、`ν_a` 的位置，再解释 temporal evolution。

如果采用

```tex
F_ν\propto t^{-α}ν^{-β_{spec}},
```

则 spectral index `β_spec` 可先用于估计 electron index `p`。例如 slow cooling 中：

```tex
β_{spec}=\frac{p-1}{2}\quad (ν_m<ν<ν_c),
```

```tex
β_{spec}=\frac{p}{2}\quad (ν>ν_c).
```

然后再检查对应 closure relation 是否预测 observed `α`。如果 spectral 和 temporal indices 不共享同一个 `p`，应优先怀疑 spectral regime、extinction、extra component 或模型假设，而不是立即引入复杂 jet structure。

## 3. First-pass closure diagnosis

一个最小 diagnosis 流程是：

1. 判断 fast / slow cooling；
2. 判断 observing band 在 `ν_m`、`ν_c`、`ν_a` 哪个 segment；
3. 用 `β_spec` 推断 `p`；
4. 对 ISM/wind closure relation 预测 `α`；
5. 比较 optical、X-ray、radio 是否一致；
6. 若不一致，检查 jet break、energy injection、density variation、reverse shock、SSC 或 extra component。

Closure relation 是 first-pass filter，不是 final model。它的价值在于排除明显不一致的解释。

## 4. Dynamics model selection

选择动力学模型时，应按最小复杂度逐层增加：

| 层级 | 模型 | 何时考虑 |
| --- | --- | --- |
| 1 | single forward shock, ISM/wind | broadband SED 与 closure relation 基本一致 |
| 2 | jet break / beaming correction | achromatic steepening、geometry evidence |
| 3 | energy injection / refreshed shock | plateau、shallow decay、late rebrightening |
| 4 | density variation | chromatic bump、radio/optical response、medium evidence |
| 5 | reverse shock | early optical flash、radio flare、shock-crossing timescale |
| 6 | SSC / high-energy component | GeV–TeV excess、IC cooling evidence |
| 7 | structured / two-component jet | viewing-angle effect、late component、radio calorimetry、geometry diagnostics |

这个顺序不是物理优先级，而是报告时的 complexity control：不要在简单模型尚未排除时直接采用高度参数化结构。

## 5. Microphysical parameter degeneracy

Forward shock fitting 常使用参数：

```tex
(E_k,n,\epsilon_e,\epsilon_B,p)
```

或 wind case 中把 `n` 替换为 `A_*`。这些参数高度简并。例如增加 `E_k`、改变 `n`、降低 `ε_B` 都可能移动 spectral breaks 或改变 flux normalization。

特别需要注意：

- `ε_e` 和 `ε_B` 是 phenomenological shock parameters，不一定随时间恒定；
- `p` 应尽量由 spectrum 支持，而不是只由 light curve slope 推出；
- `E_k` 是 kinetic energy，不能与 prompt `E_γ` 混用；
- `n` 或 `A_*` 的约束通常依赖 radio 和 `ν_c`；
- `Y` 和 SSC cooling 会反过来改变 `ν_c`。

## 6. Geometry degeneracy

几何参数也存在强简并：

```tex
(θ_j, θ_c, θ_v, \mathcal{E}(θ), Γ(θ)).
```

Top-hat jet 的 `θ_j`、Gaussian structured jet 的 `θ_c`、two-component jet 的 `θ_n/θ_w` 不是同一个物理量，不能直接横向比较。

若只有 light curve，一个 broad bump 可能来自：

- off-axis structured jet core 逐渐可见；
- wide component emergence；
- refreshed shock；
- density enhancement；
- reverse shock / radio flare；
- evolving microphysics。

因此 geometry interpretation 最好由 polarization、VLBI、source size、multi-band break achromaticity 或 radio calorimetry 支持。

## 7. 模型报告表格模板

实际写事件页或模型比较页时，建议至少报告以下字段：

| Category | Required fields |
| --- | --- |
| Data | bands、time range、redshift、extinction / absorption correction、upper limits |
| Dynamics | ISM / wind / general `k`、jet model、energy injection assumption |
| Radiation | synchrotron / SSC、spectral regime、`p`、`ε_e`、`ε_B`、`Y` |
| Geometry | top-hat `θ_j`、structured `θ_c`/`θ_v`、two-component `θ_n`/`θ_w` |
| Energetics | `E_iso`、`E_k`、true energy、band definition、beaming convention |
| Components | forward shock、reverse shock、extra radio/mm、prompt contamination、SN/kilonova |
| Caveats | degeneracies、excluded alternatives、source-specific assumptions |

这个表格的目的不是制造统一模板，而是防止把关键 assumptions 藏在文字里。

## 8. 未来事件页 ingest checklist

当新 GRB afterglow source 被 ingest 时，建议按以下顺序更新：

1. 事件页观测事实：redshift、trigger、fluence、multi-band detections、breaks、upper limits；
2. 观测子页：prompt、afterglow、radio、TeV、spectral evolution；
3. 模型解释页：明确 source 使用的 density、geometry、radiation assumptions；
4. 综合比较页：只放跨事件可比较量；
5. 教材页：只有当 source 引入新理论形式、重要 caveat 或典型应用时才更新；
6. open questions / contradictions：记录相互冲突的模型解释。

这与本项目规则一致：论文是证据，不是主结构；观测事实和模型解释必须分开。

## 9. 最小可复现检查

一个 afterglow model claim 至少应能回答：

- 使用哪些数据点和 upper limits？
- 时间和频段是否已转到 source frame？
- `E_iso` 的能段和 bolometric correction 是什么？
- `E_k` 是 isotropic-equivalent 还是 true energy？
- 介质是 ISM、wind 还是 fitted `k`？
- 采用 synchrotron-only 还是 SSC？
- `ν_m`、`ν_c`、`ν_a` 在哪些频段？
- 是否存在 reverse shock、host/SN、prompt contamination 或 scintillation？
- 是否尝试过替代模型？
- 哪些结论是 robust，哪些只在该模型假设下成立？

## 10. 常见误区

- **先选模型再解释数据**：应先整理 SED、closure 和基本观测事实。
- **把 best-fit parameter 当作直接观测量**：`θ_j`、`ε_B`、`n` 都是模型参数。
- **忽略 non-detections**：upper limits 对排除模型很关键。
- **混用 `E_iso`、`E_k`、`E_true`**：必须记录定义和 band。
- **把复杂模型写成唯一解释**：除非 source 明确排除 alternatives，否则应保留非唯一性。

## 来源

- Bing Zhang, “The Physics of Gamma-Ray Bursts & Relativistic Jets,” arXiv:1410.0679。
- J. Granot and R. Sari, “The Shape of Spectral Breaks in Gamma-Ray Burst Afterglows,” ApJ 568, 820-829 (2002), arXiv:astro-ph/0108027。
- R. Sari, T. Piran and R. Narayan, “Spectra and Light Curves of Gamma-Ray Burst Afterglows,” ApJL 497, L17-L20 (1998), arXiv:astro-ph/9712005。
- O. S. Salafia and G. Ghirlanda, “The Structure of Gamma Ray Burst Jets,” arXiv:2206.11088。
- Berger et al. 2003、Racusin et al. 2008、LHAASO Collaboration 2023、O'Connor et al. 2023、Laskar et al. 2023：作为事件拟合和模型报告 caveat 的应用接口。
