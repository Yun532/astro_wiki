# 15 Non-relativistic transition 与 radio calorimetry

前面章节主要讨论 ultra-relativistic Blandford-McKee phase。但 GRB afterglow 不会永远保持 `Γ\gg1`。随着 blast wave sweep up 越来越多 external mass，它会进入 trans-relativistic，再进入 Newtonian Sedov-Taylor phase。Late-time radio afterglow 在这个阶段尤其重要，因为 beaming correction 减弱，能量估计更接近 true kinetic energy。

Radio calorimetry 的核心价值是：它不只拟合早期 light curve slope，而是利用 late-time synchrotron spectrum、self-absorption、source size 和 dynamics 估计 ejecta kinetic energy。GRB 030329 的 two-component / calorimetry 解释正是这个方向的经典案例。

## 1. BM phase 的适用边界

Blandford-McKee solution 适用于 adiabatic ultra-relativistic blast wave。其基本条件是：

```tex
Γ\gg1.
```

当 swept-up rest-mass energy 接近 blast-wave energy 时，flow 逐渐变为 non-relativistic。Uniform ISM 中可用 Sedov-Taylor radius 估计 transition scale：

```tex
R_{ST}\sim \left(\frac{3E}{4π n m_p c^2}\right)^{1/3}.
```

这里 `E` 应是 kinetic energy；使用 isotropic-equivalent 还是 beaming-corrected true energy 必须说明。

## 2. Non-relativistic transition time

最粗略的 observer-frame transition time 可写成

```tex
t_{NR}\sim (1+z)\frac{R_{ST}}{c}.
```

更实际的 estimate 会考虑 jet geometry、lateral spreading、trans-relativistic dynamics 和 equal-arrival-time effect。因此 `t_NR` 通常是量级概念，不应被写成精确观测转折。

在 wind medium 中，swept-up mass scaling 不同，transition time 的 energy/density dependence 也不同。不能把 ISM 的 `R_ST` 公式直接套到 wind case。

## 3. Sedov-Taylor scaling

Newtonian adiabatic blast wave 在 uniform medium 中满足 Sedov-Taylor scaling：

```tex
R\propto \left(\frac{E t^2}{ρ}\right)^{1/5},
```

因此

```tex
R\propto t^{2/5},
```

```tex
v\propto t^{-3/5}.
```

这与 BM phase 的 `R\sim ct`、`Γ(t)` scaling 完全不同。Late radio modeling 若仍使用 ultra-relativistic formula，会系统性误估能量与 density。

## 4. 为什么 radio calorimetry 有用

Late radio band 的优势包括：

- emission 区域较大，beaming effect 较弱；
- self-absorption break `ν_a` 和 peak flux 可约束 source size 与 magnetic field；
- radio light curve 可追踪 trans-relativistic dynamics；
- late time optical/X-ray 常太暗或受 host/SN contamination 影响。

当 spectrum 中 self-absorption turnover 可测时，可以用 equipartition 或 synchrotron source-size argument 估计 energy。更完整的 calorimetry 会拟合 multi-frequency radio light curve 和 spectrum。

## 5. Beaming correction 与 true energy

早期 afterglow 常用 top-hat jet break 估计 opening angle，然后计算

```tex
E_{true}\simeq f_b E_{iso},
```

```tex
f_b\simeq \frac{θ_j^2}{2}.
```

Late-time calorimetry 的优势是，在 outflow 变宽、变慢后，观测对初始 beaming 的敏感性降低。若 late radio energy 与 early beaming-corrected energy 不一致，可能提示：

- jet structure 不是单一 top-hat；
- 存在 wide / mildly relativistic component；
- energy injection 改变了 kinetic energy；
- microphysical parameters 或 density assumptions 有误。

## 6. Jet spreading 与 sphericalization

理论上，jet 在 `Γθ_j\lesssim1` 后可能发生 lateral spreading，最终趋向 quasi-spherical Newtonian expansion。但实际 hydrodynamic simulations 显示 lateral spreading 的速度、程度和 light-curve imprint 都依赖 jet structure 与 external medium。

因此 late-time radio calorimetry 中常把 geometry 作为模型假设，而不是直接观测事实。若使用 spherical Sedov-Taylor approximation，应说明它适用于 sufficiently late time 或作为量级估计。

## 7. Self-absorption、scintillation 与 source size

Radio calorimetry 必须处理三个 caveat：

1. **Synchrotron self-absorption**：`ν_a` 附近谱形对 source size、magnetic field 和 electron distribution 敏感。
2. **Interstellar scintillation**：早期 compact radio source 可出现显著 flux modulation。
3. **Source size / expansion**：若 VLBI 或 scintillation quenching 能约束 angular size，可直接限制 expansion velocity。

这些效应既是 complication，也是 diagnostic。忽略它们会把 propagation effect 错当成 intrinsic variability。

## 8. GRB 030329 接口

GRB 030329 是 radio calorimetry 与 two-component interpretation 的经典事件。Berger et al. 将 early optical/X-ray break 与 late radio behavior 放入 two-component explosion 图像：narrow component 解释 gamma-ray 和 early afterglow，wide mildly relativistic component 解释 radio afterglow 和 late optical contribution。

在本教材中应保持边界：

- radio calorimetry 是 late-time energy budget 的重要约束；
- 5°/17° 是 Berger et al. 的模型解释；
- SN 2003dh subtraction、radio synchrotron modeling、microphysics 和 geometry 都影响参数；
- 不能把事件级 two-component fit 写成所有 GRB 的普适结构。

## 9. 和 GRB 221009A radio/mm extra component 的关系

GRB 221009A 中 radio/mm extra component 提醒我们：late radio excess 不一定等同于 simple wide component 或 simple calorimetry result。它可能涉及 additional outflow、reverse shock、density structure、scintillation、self-absorption 或模型中未包含的 emission region。

因此 late radio chapter 的作用是提供 energy and geometry diagnosis 的工具，而不是给所有 radio excess 一个统一解释。

## 10. 常见误区

- **把 `E_iso` 直接放进 Sedov radius**：late-time dynamics 更关心 true kinetic energy 或 spherical-equivalent approximation，必须说明约定。
- **把 `t_NR` 当成 sharp break**：transition 是 gradual 的，观测 light curve 不一定有清晰转折。
- **忽略 self-absorption**：radio peak 常不是 injection break，而可能是 absorption turnover。
- **把 scintillation 当成 intrinsic bump**：compact early radio source 尤其需要检查 propagation effect。
- **把 late radio energy 当作 prompt gamma-ray energy**：prompt radiated energy 与 afterglow kinetic energy 是不同物理量。

## 来源

- D. A. Frail et al., radio calorimetry and beaming-correction GRB afterglow work。
- E. Berger et al., “A common origin for cosmic explosions inferred from calorimetry of GRB030329,” Nature 426, 154-157 (2003), arXiv:astro-ph/0308187。
- T. Piran, “The Physics of Gamma-Ray Bursts,” Reviews of Modern Physics 76, 1143-1210 (2004), arXiv:astro-ph/0405503。
- J. Granot and R. Sari, “The Shape of Spectral Breaks in Gamma-Ray Burst Afterglows,” ApJ 568, 820-829 (2002), arXiv:astro-ph/0108027。
- Bing Zhang, “The Physics of Gamma-Ray Bursts & Relativistic Jets,” arXiv:1410.0679。
