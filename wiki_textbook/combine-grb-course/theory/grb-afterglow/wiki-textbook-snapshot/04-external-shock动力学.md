# 04 External shock 动力学

External shock 是 GRB afterglow 标准模型的动力学核心：central engine ejecta 在大半径处扫过 circumburst medium，把 bulk kinetic energy 转移给 shocked external medium；电子加速和磁场放大随后产生 synchrotron afterglow。本章只处理动力学标度，辐射谱中的 `ν_m`、`ν_c`、`F_{ν,max}` 留到下一章。

## 1. 从 coasting 到 deceleration

第三章已经用 swept-up mass 的量级条件定义 deceleration：

```tex
m_{\rm sw} \sim \frac{E}{\Gamma_0^2 c^2}.
```

这个条件的物理含义是：在 lab frame 中，外部介质的 rest mass 虽然比 ejecta kinetic energy 对应的质量小很多，但 ultra-relativistic shock 会把每个 swept-up baryon 加热到约 `Γ m_p c^2` 的能量量级；当 shocked external medium 中积累的能量达到 ejecta 能量的显著份额时，原本 coasting 的 shell 开始减速。

在 afterglow 建模中常把 deceleration 前后分成三段：

1. **coasting phase**：`Γ ≈ Γ_0`，外部介质只被少量扫过；
2. **onset / deceleration phase**：reverse shock 穿过 ejecta，forward shock 能量迅速增长；
3. **self-similar phase**：ejecta 的初始细节被逐渐“遗忘”，blast wave 接近 Blandford-McKee self-similar solution。

本章的主要标度从第三段开始。

## 2. 外部介质密度剖面

把 circumburst medium 写成统一形式：

```tex
\rho_{\rm ext}(R) = A R^{-k}.
```

常用两种极限：

- **uniform ISM**：`k=0`，`ρ_ext = n m_p`；
- **stellar wind**：`k=2`，`ρ_ext = A R^{-2}`。

对应 swept-up mass 量级为

```tex
m_{\rm sw}(R) \sim \int_0^R 4\pi r^2 \rho_{\rm ext}(r)\,dr
        \sim \frac{4\pi A}{3-k}R^{3-k}, \quad k<3.
```

因此外部介质的关键差别不是一个数值系数，而是 swept-up mass 随半径增长的速度：ISM 中 `m_sw ∝ R^3`，wind 中 `m_sw ∝ R`。

## 3. Relativistic shock jump 的量级关系

对进入 cold external medium 的 ultra-relativistic forward shock，shock 后的 comoving number density 和 internal energy density 量级为

```tex
n' \sim 4\Gamma n_{\rm ext},
```

```tex
e' \sim 4\Gamma^2 n_{\rm ext}m_p c^2.
```

这里 `Γ` 是 shocked fluid 相对 lab / burster frame 的 bulk Lorentz factor，`n_ext` 是 shock 前外部介质 number density。不同文献可能使用 shock-front Lorentz factor `Γ_sh`，它和 shocked fluid 的 `Γ` 相差一个 order-unity 因子；比较数值系数时必须先检查约定。

这两个关系给出 afterglow 辐射章节的入口：

- `e'` 决定 magnetic field 的常用参数化 `B'^2/(8π)=ε_B e'`；
- `Γ` 决定 shocked electrons 的典型能量和 Doppler boosting；
- `n'` 决定 emitting electron number 和 absorption optical depth。

## 4. Energy conservation 与 Blandford-McKee 标度

在 adiabatic relativistic blast wave 中，总能量近似守恒。忽略 order-unity 系数时，blast wave energy 可写成

```tex
E \sim \Gamma^2 m_{\rm sw} c^2.
```

代入 `m_sw ∝ R^{3-k}` 得到

```tex
E \sim \Gamma^2 R^{3-k},
```

因此

```tex
\Gamma(R) \propto R^{-(3-k)/2}.
```

更完整的 Blandford-McKee solution 会给出含 `17-4k` 等数值系数的能量表达式，例如可写成量级形式

```tex
E \sim \frac{16\pi}{17-4k} A c^2 \Gamma^2 R^{3-k},
```

但在教材主线中，最重要的是 `Γ` 对 `R` 的幂律标度和它对 observer time 的映射。

## 5. Observer time 映射

对 on-axis observer，relativistic arrival-time compression 给出

```tex
t_{\rm obs} \sim (1+z)\frac{R}{2c\Gamma^2}.
```

在严格 BM 解中，常见写法会包含和 `k` 有关的 order-unity 系数，例如 `R/[4(4-k)cΓ^2]`；本教材在推导标度时保留 `R/(2cΓ^2)` 的量级关系，在引用具体数值公式时再检查对应文献约定。

把 `Γ(R) ∝ R^{-(3-k)/2}` 代入 observer-time relation：

```tex
t_{\rm obs} \propto (1+z) R^{4-k}.
```

所以

```tex
R(t_{\rm obs}) \propto \left(\frac{t_{\rm obs}}{1+z}\right)^{1/(4-k)},
```

```tex
\Gamma(t_{\rm obs}) \propto \left(\frac{t_{\rm obs}}{1+z}\right)^{-(3-k)/[2(4-k)]}.
```

这就是 external-shock afterglow 所有标准光变标度的动力学底座。

## 6. Uniform ISM 标度

对 `k=0`，`ρ_ext = n m_p`，swept-up mass 为

```tex
m_{\rm sw} \sim \frac{4\pi}{3}R^3 n m_p.
```

Energy conservation 给出

```tex
\Gamma(R) \propto R^{-3/2}.
```

Observer time 映射给出

```tex
R \propto t_{\rm obs}^{1/4},
```

```tex
\Gamma \propto t_{\rm obs}^{-3/8}.
```

若保留常用归一化，adiabatic ISM afterglow 的 bulk Lorentz factor 常写成类似

```tex
\Gamma(t) \sim 6\left(\frac{E_{\rm iso,52}}{n_0}\right)^{1/8}
\left(\frac{t_{\rm obs}}{1\ {\rm day}}\right)^{-3/8}
(1+z)^{3/8},
```

其中数值系数依赖 `E` 是 isotropic-equivalent kinetic energy 还是 beaming-corrected true energy、`Γ` 的定义以及 BM 系数取法。这里的重点是弱依赖：`Γ` 对 `E/n` 只按 `1/8` 次方变化。

## 7. Wind-like medium 标度

对 massive-star progenitor 的 stellar wind，常写

```tex
\rho_{\rm ext}(R)=A R^{-2}.
```

此时 swept-up mass 为

```tex
m_{\rm sw} \sim 4\pi A R.
```

Energy conservation 给出

```tex
\Gamma(R) \propto R^{-1/2}.
```

Observer time 映射给出

```tex
R \propto t_{\rm obs}^{1/2},
```

```tex
\Gamma \propto t_{\rm obs}^{-1/4}.
```

和 ISM 相比，wind medium 中早期半径较小时密度更高，但 swept-up mass 随 `R` 增长较慢；因此 `Γ(t)` 的下降比 ISM 更缓。GRB 080319B 的 Racusin et al. 解释使用 wind-like environment，因此不能直接把 ISM closure relation 和 deceleration scaling 套用过去。

## 8. Radiative vs adiabatic evolution

上面的 BM 标度默认 blast wave 近似 adiabatic：shock 产生的大部分 internal energy 留在 shocked fluid 中，并通过 expansion 做功，而不是立即辐射掉。

若 radiative loss 很强，则能量不再守恒：

```tex
E = E(t)
```

会随时间下降，`Γ(t)` 比 adiabatic 情况衰减更快。实际 GRB afterglow 建模中，标准 closure relations 通常先采用 adiabatic forward shock，再通过 cooling regime、inverse Compton、energy injection 或 evolving microphysics 解释偏离。

因此使用本章标度时必须先说明：

- blast wave 是否 adiabatic；
- energy injection 是否重要；
- 外部介质是 ISM、wind，还是更复杂的 density profile；
- 使用的是 spherical-equivalent dynamics 还是已进入 jet-break regime。

## 9. Jet break 与 non-relativistic transition 的接口

当 bulk Lorentz factor 下降到 jet opening angle 的倒数附近：

```tex
\Gamma(t_j) \sim \theta_j^{-1},
```

observer 开始看到 jet edge，且 sideways expansion 或 angular structure 可能改变 light curve decay。这是后续 jet-break 章节的入口。

更晚时，当 `Γ → 1`，blast wave 进入 trans-relativistic / non-relativistic 阶段，BM solution 不再适用，需要转向 Sedov-Taylor-like dynamics。GRB 030329 的 radio calorimetry 正是利用 late-time radio afterglow 对 kinetic energy 作更接近几何无关的约束，但它已经不属于早期 ultra-relativistic BM 标度的简单适用范围。

## 10. 和事件页面的接口

- GRB 221009A：极高 `E_iso` 不自动意味着同样极高的 true kinetic energy；external shock modeling 需要同时约束 `E_k`、`n` 或 wind parameter、`Γ_0`、jet structure 和 radiative efficiency。
- GRB 080319B：naked-eye optical flash 和 afterglow modeling 涉及 narrow core / wide component 与 wind-like environment；介质选择会改变 `Γ(t)`、`R(t)` 和 closure relations。
- GRB 030329：early break、late radio behavior 和 two-component interpretation 需要区分 narrow component 的 early relativistic dynamics 与 wide component / late calorimetry 的动力学阶段。

## 11. 常见误区

- **把 deceleration radius 之后仍当作 coasting**：进入 BM 阶段后 `Γ` 随 `R` 和 `t_obs` 下降，不能继续使用 `Γ=Γ_0`。
- **把 ISM 和 wind 的 closure relation 混用**：介质密度剖面改变 `Γ(t)`，进而改变 `ν_m`、`ν_c` 和 light curve slope。
- **忽略 energy convention**：公式中的 `E` 可能是 isotropic-equivalent kinetic energy，也可能是 beaming-corrected true energy；两者不能混用。
- **过度相信数值系数**：BM solution、shock Lorentz factor、fluid Lorentz factor、arrival-time convention 不同会带来 order-unity 差异。
- **把 jet break 之前的 spherical scaling 外推到所有时间**：当 `Γθ_j ≲ 1` 或 observer off-axis 时，几何效应和 angular structure 必须进入模型。

## 12. 和后续章节的接口

- Synchrotron spectrum：利用 `e'`、`n'` 和 `Γ(t)` 推导 `B'`、`γ_m`、`γ_c`、`ν_m`、`ν_c`、`F_{ν,max}`。
- Closure relations：把动力学标度和 synchrotron spectral segments 组合成 `F_ν ∝ t^{-α}ν^{-β}`。
- Jet break：从 `Γ(t_j) ~ θ_j^{-1}` 得到 opening angle 和 beaming correction。
- Structured / two-component jet：把 spherical-equivalent `E` 和 `Γ` 推广到 angular-dependent `E(θ)`、`Γ_0(θ)`。

## 13. 公式 ID 与代码映射

| formula ID | 内容 | Python reference | C++ kernel | 验证 |
| --- | --- | --- | --- | --- |
| `FS-DYN-ISM-001` | uniform ISM number density | `core/dynamics/blastwave.py::ism_number_density` | none | `forward_shock_afterglow_program_check.md` |
| `FS-DYN-WIND-001` | wind `A = 5e11 A_* g cm^-1` | `core/dynamics/blastwave.py::wind_mass_parameter` | none | `forward_shock_afterglow_program_check.md` |
| `FS-DYN-WIND-002` | wind `n(R)=A/(m_p R^2)` | `core/dynamics/blastwave.py::wind_number_density` | none | `forward_shock_afterglow_program_check.md` |
| `FS-DYN-BM-ISM-001` | ISM BM `Γ(t)` reference scaling | `core/dynamics/blastwave.py::bm_lorentz_factor` | none | `forward_shock_afterglow_program_check.md` |
| `FS-DYN-BM-WIND-001` | wind BM `Γ(t)` reference scaling | `core/dynamics/blastwave.py::bm_lorentz_factor` | none | `forward_shock_afterglow_program_check.md` |
| `FS-DYN-R-001` | `R ≈ factor c t Γ^2/(1+z)` | `core/dynamics/blastwave.py::bm_radius` | none | `forward_shock_afterglow_program_check.md` |
| `FS-DYN-JUMP-001` | `e'≈4Γ^2 n m_p c^2` | `core/dynamics/blastwave.py::shocked_internal_energy_density` | none | `forward_shock_afterglow_program_check.md` |
| `EATS-DELAY-001` | spherical on-axis angular delay `Delta t=(1+z)R(1-cos theta)/c` | `core/dynamics/equal_arrival.py::angular_time_delay_s` | none | `forward_shock_afterglow_program_check.md` |
| `EATS-WEIGHT-001` | Doppler-weighted toy EATS average | `core/dynamics/equal_arrival.py::spherical_on_axis_eats_average` | future angular kernel | `forward_shock_afterglow_program_check.md` |

## 来源

- R. D. Blandford and C. F. McKee, “Fluid dynamics of relativistic blast waves,” Physics of Fluids 19, 1130-1138 (1976)。
- R. Sari, T. Piran and R. Narayan, “Spectra and Light Curves of Gamma-Ray Burst Afterglows,” ApJL 497, L17-L20 (1998), arXiv:astro-ph/9712005。
- R. A. Chevalier and Z.-Y. Li, “Wind Interaction Models for Gamma-Ray Burst Afterglows: The Case for Two Types of Progenitors,” ApJ 536, 195-212 (2000), arXiv:astro-ph/9908272。
- Tsvi Piran, “The Physics of Gamma-Ray Bursts,” Reviews of Modern Physics 76, 1143-1210 (2004), arXiv:astro-ph/0405503。
- Bing Zhang, “The Physics of Gamma-Ray Bursts & Relativistic Jets,” arXiv:1410.0679。
- E. Berger et al., “A common origin for cosmic explosions inferred from calorimetry of GRB030329,” Nature 426, 154-157 (2003), arXiv:astro-ph/0308187。
- J. L. Racusin et al., “Broadband observations of the naked-eye gamma-ray burst GRB 080319B,” Nature 455, 183-188 (2008), arXiv:0805.1557。
