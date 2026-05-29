# 08 Energy injection 与 refreshed shock

前面章节默认 external shock 在 deceleration 后进入 adiabatic、constant-energy Blandford-McKee evolution。许多 GRB afterglow 却显示 shallow decay、plateau、rebrightening 或 bump，说明 blast wave energy 可能不是常数，或者不同 ejecta components 在不同时间主导 emission。本章讨论 energy injection 和 refreshed shock 的基本图像，并说明它们与 density variation、jet structure、two-component jet 的区别。

## 1. 为什么需要 energy injection

标准 forward shock 在给定 medium、cooling regime 和 spectral segment 后，会给出 closure relation：

```tex
F_\nu \propto t^{-\alpha}\nu^{-\beta_{\rm spec}}.
```

如果观测到的 decay 明显比标准 closure relation 更浅，或出现 plateau / bump，一个自然解释是 blast wave energy 随 observer time 增加：

```tex
E = E(t).
```

能量增加会减缓 `Γ(t)` 的下降，使 `ν_m`、`ν_c`、`F_{ν,max}` 的演化改变，从而让 light curve 变平或重新变亮。

Energy injection 的物理来源常分为两类：

- **long-lived central engine**：central engine 持续输出 Poynting flux 或 matter-dominated wind；
- **refreshed shock**：初始 ejecta 具有 Lorentz-factor stratification，较慢但能量可观的 shell 后来追上 decelerated blast wave。

## 2. Continuous injection 参数化

常用 phenomenological form 是把注入 luminosity 写成

```tex
L_{\rm inj}(t) = L_0\left(\frac{t}{t_0}\right)^{-q}.
```

若 `q<1`，累积注入能量随时间增长：

```tex
E_{\rm inj}(t) \sim \int^t L_{\rm inj}(t')dt' \propto t^{1-q}.
```

若初始 blast wave energy 可忽略或注入能量主导，可写成

```tex
E(t) \propto t^e,
```

其中

```tex
e = 1-q.
```

当 `q>1` 时，late-time 注入能量快速收敛，动力学接近 constant-energy case；当 `q≈0` 时，近似 constant luminosity injection，可产生明显 plateau。

## 3. Energy injection 下的动力学标度

第四章 constant-energy BM 标度来自

```tex
E \sim \Gamma^2 R^{3-k}.
```

若

```tex
E(t) \propto t^e,
```

并使用 observer-time mapping

```tex
t \propto R/\Gamma^2,
```

则可推得

```tex
R(t) \propto t^{(1+e)/(4-k)},
```

```tex
\Gamma(t) \propto t^{-(3-k-e)/[2(4-k)]}.
```

当 `e=0` 时回到第四章的 standard BM result：

```tex
\Gamma \propto t^{-(3-k)/[2(4-k)]}.
```

只要 `e>0`，`Γ(t)` 下降更慢；若 `e` 足够大，某些 spectral segment 的 light curve 可以从 normal decay 变成 plateau，甚至出现 rise。

## 4. 对 synchrotron break evolution 的影响

以 uniform ISM、adiabatic、slow cooling 为例，constant-energy 情况下第五章给出

```tex
\nu_m \propto t^{-3/2},\quad \nu_c \propto t^{-1/2},\quad F_{\nu,\max}\propto t^0.
```

若 `E(t)∝t^e`，常用 scaling 可写成

```tex
\nu_m \propto E^{1/2}t^{-3/2} \propto t^{e/2-3/2},
```

```tex
\nu_c \propto E^{-1/2}t^{-1/2} \propto t^{-e/2-1/2},
```

```tex
F_{\nu,\max} \propto E \propto t^e.
```

因此在 slow cooling `ν_m<ν<ν_c` 中：

```tex
F_\nu \propto F_{\nu,\max}\nu_m^{(p-1)/2},
```

得到

```tex
F_\nu \propto t^{e-(3-e)(p-1)/4}.
```

若仍写作 `F_ν∝t^{-α}`，则

```tex
\alpha = \frac{3(p-1)}{4}-\frac{e(p+3)}{4}.
```

这展示了 energy injection flattening 的本质：`e>0` 会把标准 decay index 减小。

## 5. Refreshed shock 图像

Refreshed shock 不要求 central engine 在 observer time 的 plateau 阶段仍持续活动。它可以来自初始 explosion ejecta 的 Lorentz-factor stratification：fast material 先产生 forward shock，slower material 后来追上已减速的 blast wave。

若 ejecta energy above Lorentz factor `Γ` 写成

```tex
E(>\Gamma) \propto \Gamma^{-s},
```

随着 blast wave decelerates 到更低 `Γ`，更多 slower ejecta 加入 shock，等效 `E(t)` 增长。`s` 越大，低 Lorentz-factor material 携带的能量越多，injection 越强。

这个机制的观测特征可能包括：

- smooth shallow decay / plateau；
- discrete bumps 或 step-like rebrightening；
- reverse-shock related radio flare；
- energy injection 结束后恢复 standard decay。

## 6. Injection break 与 plateau end

若 energy injection 在时间 `t_b` 附近结束，light curve 会从 shallow decay 转入 normal decay。这个 transition 有时称为 injection break：

```tex
t_b \sim t_{\rm end,inj}.
```

它和 jet break 都可表现为 light curve steepening，但物理意义不同：

- injection break：energy supply stops，dynamics 回到 constant-energy BM；
- jet break：beaming cone reaches jet edge，geometry changes。

区分二者需要检查：

- steepening 是否 achromatic；
- post-break slope 是否符合 jet-break expectation；
- `E_k` 是否需要在 break 前增长；
- 是否有 spectral evolution；
- radio / optical / X-ray 是否共享同一 component。

## 7. Magnetar-like injection 的常用形式

若 central engine 是 rapidly spinning magnetar，常用 spin-down luminosity 近似为

```tex
L(t) = L_0\left(1+\frac{t}{T_{\rm sd}}\right)^{-2}.
```

在 `t \ll T_sd` 时，`L≈L_0`，接近 constant luminosity injection；在 `t \gg T_sd` 时，`L∝t^{-2}`，late energy input quickly converges。

这类模型常用于解释 X-ray plateau，但应注意：plateau luminosity、duration、beaming、radiative efficiency 和 magnetar maximum rotational energy 共同限制模型可行性。不能仅凭 plateau 形状就确认 magnetar engine。

## 8. Density variation 与 energy injection 的区别

外部 density enhancement 也能改变 light curve，但它和 energy injection 的物理作用不同：

- density jump 增加 emitting electron number 和 magnetic field；
- energy injection 增加 blast wave total energy，并改变 dynamics；
- density drop 可以造成 decay steepening，但不等同于 jet break；
- density variation 对不同 spectral segment 的影响不同，特别是 `ν>ν_c` 时 density sensitivity 较弱。

因此若 X-ray band 位于 `ν>ν_c`，一个强 X-ray plateau 通常不容易只靠 density variation 解释；但 radio / optical bump 可能对 density structure 更敏感。

## 9. 与 structured / two-component jet 的简并

Energy injection、structured jet、two-component jet 都能产生 shallow decay 或 bump：

- energy injection：同一 blast wave 的 total energy 随时间增加；
- structured jet：observer 随时间看到不同 angular zones；
- two-component jet：narrow / wide component 有不同 `E`、`Γ_0`、`θ_j` 和 deceleration time；
- refreshed shock：不同 Lorentz-factor ejecta shells 追上 forward shock。

这些机制在光变曲线上可能高度简并。打破简并通常需要：

- broadband SED consistency；
- radio peak / self-absorption / scintillation 信息；
- polarization；
- VLBI source size 或 centroid motion；
- 与 prompt energetics 和 engine duration 的一致性。

## 10. 和事件页面的接口

- GRB 030329：late optical resurgence 和 radio behavior 可由 two-component jet 解释，但 refreshed shock 或 continuous angular structure 是需要并列比较的 alternatives。
- GRB 080319B：naked-eye optical prompt 与 afterglow component separation 很关键；不能把所有 early optical structure 都归因于 forward-shock energy injection。
- GRB 221009A：radio-to-GeV afterglow 中额外 component、long-lived decay 或 bump 需要和 structured jet、density profile、SSC contribution 共同比较，energy injection 只是候选机制之一。

## 11. 常见误区

- **把 plateau 自动等同于 magnetar**：plateau 只是 phenomenology，central-engine 类型需要 energetics 和 timing 约束。
- **把 injection break 当作 jet break**：两者都能 steepen，但一个是 energy supply 结束，一个是 geometry effect。
- **只用单波段 bump 判定 refreshed shock**：density variation、reverse shock、two-component jet 或 scintillation 也可能造成 bump。
- **忽略能量预算**：强 injection 需要额外 kinetic / magnetic energy，不能超过合理 engine budget 而不说明。
- **继续使用 constant-energy closure relation**：一旦 `E(t)` 增长，第四到六章的标准标度需要重推。

## 12. 和后续章节的接口

- Structured jet：把 apparent energy growth 与 angular structure / viewing-angle effect 区分。
- Two-component jet：比较 refreshed shock 与 wide component emergence 的 light-curve signatures。
- Event applications：在 GRB 030329、GRB 080319B、GRB 221009A 中分别列出 energy injection 是否必要、是否唯一。

## 来源

- M. J. Rees and P. Mészáros, “Refreshed Shocks and Afterglow Longevity in Gamma-Ray Bursts,” ApJL 496, L1-L4 (1998), arXiv:astro-ph/9712252。
- R. Sari and P. Mészáros, “Impulsive and Varying Injection in Gamma-Ray Burst Afterglows,” ApJL 535, L33-L37 (2000), arXiv:astro-ph/0003406。
- B. Zhang and P. Mészáros, “Gamma-Ray Burst Afterglow with Continuous Energy Injection: Signature of a Highly Magnetized Millisecond Pulsar,” ApJL 552, L35-L38 (2001), arXiv:astro-ph/0011133。
- J. A. Nousek et al., “Evidence for a Canonical Gamma-Ray Burst Afterglow Light Curve in the Swift XRT Data,” ApJ 642, 389-400 (2006), arXiv:astro-ph/0508332。
- B. Zhang et al., “Physical Processes Shaping Gamma-Ray Burst X-Ray Afterglow Light Curves: Theoretical Implications from the Swift XRT Observations,” ApJ 642, 354-370 (2006), arXiv:astro-ph/0508321。
- Bing Zhang, “The Physics of Gamma-Ray Bursts & Relativistic Jets,” arXiv:1410.0679。
