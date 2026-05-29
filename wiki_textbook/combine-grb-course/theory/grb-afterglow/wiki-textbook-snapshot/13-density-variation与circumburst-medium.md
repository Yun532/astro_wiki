# 13 Density variation 与 circumburst medium

External shock afterglow 不只由 blast-wave energy 和 microphysics 决定，也强烈依赖 circumburst medium。前面章节已经分别给出 ISM 和 wind 的基本 scaling；本章把它们统一到 general density profile，并说明 density variation 如何与 energy injection、reverse shock、structured jet 和 two-component jet 简并。

介质诊断的困难在于：light curve slope 并不是 density profile 的直接观测量。它还依赖 spectral regime、cooling、jet geometry、energy evolution 和观测频段。因此本章的核心不是“看到某个斜率就判定 wind/ISM”，而是建立一个检查流程：先确定 spectral regime，再用 closure relation 和 broadband consistency 判断介质。

## 1. General density profile

常用的 circumburst medium parameterization 是

```tex
ρ_{ext}(R)=A R^{-k}.
```

其中：

- `k=0` 对应 uniform ISM；
- `k=2` 对应 steady stellar wind；
- `0<k<2` 或其他值可作为 phenomenological profile，但必须说明物理来源；
- `A` 的单位依赖 `k`，不能在不同 `k` 间直接比较。

若写成 number density，则

```tex
n_{ext}(R)=\frac{ρ_{ext}(R)}{m_p}.
```

对 wind medium，常写作

```tex
ρ_{ext}(R)=A R^{-2},
```

其中 `A=\dot{M}/(4πv_w)`，也常用 `A_*` 归一化。

## 2. Swept-up mass 与 BM scaling

对 `ρ_{ext}=A R^{-k}`，swept-up mass 的量级为

```tex
m_{sw}(R)\propto R^{3-k}.
```

Adiabatic relativistic blast wave 中，BM energy scaling 可写成

```tex
E\sim Γ^2 m_{sw}c^2.
```

因此

```tex
Γ^2 R^{3-k}\sim const.
```

再结合 observer time relation

```tex
t_{obs}\sim (1+z)\frac{R}{2cΓ^2},
```

可得到 general-`k` scaling：

```tex
Γ\propto t_{obs}^{-\frac{3-k}{2(4-k)}},
```

```tex
R\propto t_{obs}^{\frac{1}{4-k}}.
```

代入 `k=0` 得到 ISM 中 `Γ\propto t^{-3/8}`；代入 `k=2` 得到 wind 中 `Γ\propto t^{-1/4}`。

## 3. Density 对 spectral breaks 的影响

介质 profile 会改变 `ν_m`、`ν_c`、`F_{ν,max}` 的时间演化。直观上：

- `ν_m` 主要由 shock energy、electron injection 和 magnetic field 决定，在 ISM/wind 的 adiabatic forward shock 中常有相似时间标度；
- `ν_c` 对 density profile 更敏感，ISM 中通常随时间升高或降低的方向与 wind 不同；
- `F_{ν,max}` 直接依赖 emitting electron number 和 magnetic field，对 density evolution 敏感。

因此介质诊断不能只看单一 light curve，需要结合 SED 中 `ν_m`、`ν_c`、`ν_a` 的位置。

## 4. X-ray band 为什么有时不敏感

当 X-ray 位于 `ν>ν_c` 的 slow-cooling segment，forward-shock flux 对 density 的依赖会显著减弱。这意味着：

- X-ray decay slope 可以很好地约束 `p` 或 energy evolution；
- 但 X-ray alone 往往不能强约束 `n` 或 `A_*`；
- optical/radio 与 X-ray 的联合拟合才更有介质诊断能力。

这也是为什么 GRB 事件页中不能只用 X-ray slope 断言 ISM 或 wind。

## 5. Density jump / density drop

若 blast wave 遇到 density jump，forward-shock emission 可能出现 bump、flattening 或 spectral change。可以把外部介质写成 background profile 加局部扰动：

```tex
ρ_{ext}(R)=A R^{-k}\,g(R),
```

其中 `g(R)` 描述 density enhancement 或 cavity。若 `g(R)` 在某个半径显著增加，radio/optical band 可能更敏感；若观测频段在 `ν>ν_c`，响应可能较弱。

Density drop 或 cavity 也可导致 flux steepening，但这种 steepening 不应自动解释为 jet break。Jet break 是几何效应，density variation 是 external medium effect；二者的 chromaticity 和 multi-band response 不同。

## 6. Wind termination shock

Long GRB progenitor 常与 massive star wind 联系，因此 wind-like medium 是自然候选。但 stellar wind 可能在外层遇到 shocked ISM，形成 wind termination shock。Blast wave 可能从 `k=2` 的 wind 区域进入近似 constant-density region。

这种 transition 会使 closure relation 诊断变复杂：早期数据可能 favor wind，晚期数据可能更接近 ISM。若模型强行使用单一 `k`，会把介质 transition 的影响误归因给 energy injection 或 jet structure。

## 7. Closure relation 诊断流程

用 closure relation 判断介质时，建议按以下顺序：

1. 先由 SED 判断 `ν_m`、`ν_c` 与观测频段的相对位置；
2. 用 spectral index `β_spec` 推断 electron index `p`；
3. 在 ISM/wind/general-`k` closure relation 中预测 temporal index `α`；
4. 比较 optical、X-ray、radio 是否可由同一 `p` 和同一 spectral regime 解释；
5. 若不一致，再考虑 injection、jet break、density variation、reverse shock 或 extra component。

不能反过来只从 `α` 直接推出介质类型。

## 8. 和其他模型的简并

Density variation 常与以下机制简并：

- **energy injection**：都能让 light curve 变浅或产生 bump；但 energy injection 会改变 blast-wave energy，可能影响所有 bands。
- **refreshed shock**：slower ejecta catch-up 也可产生 rebrightening，并可能伴随 reverse-shock-like radio flare。
- **two-component jet**：wide component rise 可模拟 density-induced bump。
- **structured jet viewing effect**：off-axis bright core 进入视线也可产生 delayed rise。
- **microphysical evolution**：`ε_e`、`ε_B` 随时间变化可伪装成 density effect。

因此 density interpretation 应写作候选模型，并说明为什么其他机制不优先。

## 9. 事件接口

- **GRB 080319B**：afterglow modeling favor wind-like environment，因此涉及 `t_dec`、closure relation 和 jet-opening scaling 时不能直接套 ISM 形式。
- **GRB 221009A**：部分 afterglow 模型使用 low-density wind-like medium；但 radio/mm extra component 说明单一 forward shock + smooth density profile 可能不够。
- **GRB 030329**：late radio calorimetry 接近 trans-relativistic regime，介质和几何 assumptions 会影响 energy estimate。

## 10. 常见误区

- **把 wind/ISM 当成观测事实**：它通常是 closure relation 或 broadband fitting 的模型解释。
- **只用 X-ray slope 判定 density profile**：`ν>ν_c` 时 X-ray 对 density 不敏感。
- **把所有 bump 归因于 density jump**：energy injection、reverse shock、jet structure 都可能产生 bump。
- **忽略 `A` 的单位依赖 `k`**：general profile 中 normalization 不能随意比较。
- **把 source-specific density 写成普适结论**：每个 GRB 的 medium diagnosis 都依赖数据覆盖和模型假设。

## 来源

- R. A. Chevalier and Z.-Y. Li, “Wind Interaction Models for Gamma-Ray Burst Afterglows: The Case for Two Types of Progenitors,” ApJ 536, 195-212 (2000), arXiv:astro-ph/9908272。
- R. Sari, T. Piran and R. Narayan, “Spectra and Light Curves of Gamma-Ray Burst Afterglows,” ApJL 497, L17-L20 (1998), arXiv:astro-ph/9712005。
- J. Granot and R. Sari, “The Shape of Spectral Breaks in Gamma-Ray Burst Afterglows,” ApJ 568, 820-829 (2002), arXiv:astro-ph/0108027。
- E. Nakar and J. Granot, density variations and afterglow variability caveat literature。
- Bing Zhang, “The Physics of Gamma-Ray Bursts & Relativistic Jets,” arXiv:1410.0679。
