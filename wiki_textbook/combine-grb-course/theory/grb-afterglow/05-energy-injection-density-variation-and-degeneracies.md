# 05 Energy Injection, Density Variation, and Afterglow Degeneracies

状态：v0.1 课程讲义草案。本页接在 BM dynamics、synchrotron closure、reverse shock、jet/EATS 之后，讨论标准 constant-energy blast wave 被两类常见物理改写的方式：

1. blast wave energy 随 observer time 增长，来自 continuous central-engine injection 或 refreshed shock；
2. circumburst density 偏离单一 \(R^{-k}\) power law，来自 wind termination shock、density jump/drop 或 clumpy medium。

核心原则：plateau、bump、rebrightening 或 smooth break 不是单一机制的指纹。先写动力学和谱段响应，再讨论模型简并；不能用某个 fitting code 的参数化反向决定理论起点。

## 1. 物理图像

前四讲默认 blast wave 在绝热、球对称等效、外部密度 \(\rho=A R^{-k}\) 中演化，且 isotropic-equivalent kinetic energy \(E\) 为常数。这个模型给出标准 BM 标度：

$$
E \sim \xi_k A c^2 \Gamma^2 R^{3-k},
\qquad
t_{\rm obs}\sim (1+z){R\over C_t c\Gamma^2}.
$$

真实余晖常出现比标准 closure 更平的衰减、再增亮或多阶段 break。两类自然改写是：

- energy injection：blast wave 的有效能量 \(E(t)\) 增长，使 deceleration 变慢；
- density variation：外部介质不是单一 \(A R^{-k}\)，改变 swept-up mass、electron number 和 magnetic field。

这两类效应都能改变 light curve。更麻烦的是，它们还会和 jet break、structured jet、reverse shock、SSA/scintillation、evolving microphysics 和 two-component outflow 互相简并。

## 2. 参考系与变量

| 符号 | 含义 | 单位 |
| --- | --- | --- |
| \(E(t)\) | shock 中的 isotropic-equivalent kinetic energy | erg |
| \(L_{\rm inj}(t)\) | 注入到 blast wave 的 luminosity | erg s\(^{-1}\) |
| \(e\) | \(E(t_{\rm obs})\propto t_{\rm obs}^e\) 的 phenomenological index | dimensionless |
| \(q\) | \(L_{\rm inj}\propto t^{-q}\) 的 luminosity index | dimensionless |
| \(s\) | cumulative ejecta energy \(E(>\Gamma)\propto\Gamma^{-s}\) 的 stratification index | dimensionless |
| \(g(R)\) | density perturbation factor in \(\rho=A R^{-k}g(R)\) | dimensionless |
| \(R_t\) | wind termination-shock radius | cm |
| \(t_t\) | density transition 对应的 observer time | s |

本页默认 \(t\) 表示 observer time。若公式使用 source-frame 或 lab-frame time，会显式说明。

## 3. General Expression

### 3.1 Continuous energy injection

用 phenomenological luminosity 写：

$$
L_{\rm inj}(t)
=
L_0\left({t\over t_0}\right)^{-q}.
$$

Formula ID：`EI-LINJ-POWERLAW-001`。

注入后的能量为

$$
E(t)
=
E_0+\int_{t_0}^{t} L_{\rm inj}(t')\,dt'.
$$

若 \(q\ne1\)，积分给

$$
E(t)
=
E_0+
{L_0t_0\over1-q}
\left[
\left({t\over t_0}\right)^{1-q}-1
\right].
$$

其中方括号是 dimensionless growth factor，前面的 \(L_0t_0\) 提供能量单位。

本页后续只使用等效幂律：

$$
E(t)\propto t^e.
$$

当注入项主导且 \(q<1\) 时，

$$
e=1-q.
$$

Formula ID：`EI-ENERGY-E-T-001`。

若 \(q=1\)，则 \(E(t)=E_0+L_0t_0\ln(t/t_0)\)，不能严格写成单一 \(t^e\)，只能在有限时间段用 local slope 近似。

### 3.2 Refreshed shock

另一种写法不从 central engine luminosity 出发，而从 ejecta 的 Lorentz-factor stratification 出发：

$$
E(>\Gamma)
=
E_\ast\left({\Gamma\over\Gamma_\ast}\right)^{-s}.
$$

Formula ID：`EI-REFRESHED-E-GAMMA-001`。

当 blast wave decelerates 到较低 \(\Gamma\) 时，原来更慢的 shell 追上 shock，等效 \(E\) 增大。这是 refreshed shock。这里 \(s=0\) 对应没有额外 energy stratification。注意有些文献定义的是 \(M(>\Gamma)\propto\Gamma^{-s_M}\)，此时 cumulative energy 的指数会变成 \(s_M-1\)。比较论文时必须先对齐定义。

### 3.3 Density variation

基础外部介质仍写作

$$
\rho_0(R)=A R^{-k}.
$$

密度扰动写成

$$
\rho(R)
=
A R^{-k}g(R),
$$

其中 \(g(R)=1\) 回到标准 BM。Formula ID：`DENS-PERTURB-GR-001`。

swept-up mass 的一般表达式不再是简单的 \(R^{3-k}\)：

$$
m_{\rm sw}(R)
=
4\pi A\int_0^R r^{2-k}g(r)\,dr.
$$

如果 \(g(R)\) 缓慢变化，可以把它近似成局部或累积平均扰动；如果 \(g(R)\) 是 sharp jump/drop，hydrodynamic response 和 EATS smoothing 必须保留，不能把 flux 直接乘一个 density factor 当成完整 light curve。

## 4. Detailed Derivation I：Power-Law Energy Injection Dynamics

### 4.1 从 BM energy 到 \(R(t)\)

保留 BM energy scaling：

$$
E(t)
\propto
\Gamma^2 R^{3-k}.
$$

observer-time relation 给

$$
t\propto {R\over\Gamma^2}.
$$

因此

$$
\Gamma^2\propto {R\over t}.
$$

代入 energy scaling：

$$
E(t)
\propto
{R\over t}R^{3-k}
=
{R^{4-k}\over t}.
$$

若

$$
E(t)\propto t^e,
$$

则

$$
R^{4-k}\propto t^{1+e}.
$$

所以

$$
R(t)
\propto
t^{(1+e)/(4-k)}.
$$

### 4.2 \(\Gamma(t)\)

由 \(\Gamma^2\propto R/t\)，得到

$$
\Gamma^2
\propto
t^{(1+e)/(4-k)-1}
=
t^{(e+k-3)/(4-k)}.
$$

因此

$$
\Gamma(t)
\propto
t^{-(3-k-e)/[2(4-k)]}.
$$

合并写作

$$
\boxed{
R(t)\propto t^{(1+e)/(4-k)},
\qquad
\Gamma(t)\propto t^{-(3-k-e)/[2(4-k)]}
}
$$

Formula ID：`EI-DYN-GENERAL-K-001`。

检查：令 \(e=0\)，回到第 01 讲的 constant-energy BM 标度。

### 4.3 物理边界

要保持 deceleration 而不是 acceleration，需要 \(\Gamma\) 随时间下降：

$$
3-k-e>0.
$$

因此 \(e<3-k\)。对 ISM 是 \(e<3\)，对 wind 是 \(e<1\)。多数 afterglow plateau 的 phenomenological \(e\) 远小于这个上限。若拟合需要非常大的 \(e\)，通常说明模型、能段、额外 component 或时间零点可能有问题。

## 5. Detailed Derivation II：Refreshed Shock 和 \(e\) 的关系

以本页定义

$$
E(>\Gamma)\propto \Gamma^{-s}
$$

为起点。进入 self-similar deceleration 后，blast wave 可用当前 \(\Gamma\) 上方已经并入的 cumulative energy：

$$
E\propto\Gamma^{-s}.
$$

同时 BM 给

$$
E\propto \Gamma^2R^{3-k}.
$$

两式相等：

$$
\Gamma^{-s}\propto\Gamma^2R^{3-k}.
$$

整理：

$$
\Gamma^{-(s+2)}
\propto
R^{3-k},
$$

所以

$$
\Gamma
\propto
R^{-(3-k)/(s+2)}.
$$

observer time：

$$
t\propto {R\over\Gamma^2}
\propto
R^{1+2(3-k)/(s+2)}
=
R^{(s+8-2k)/(s+2)}.
$$

于是

$$
\Gamma(t)
\propto
t^{-(3-k)/(s+8-2k)}.
$$

能量增长为

$$
E(t)\propto\Gamma^{-s}
\propto
t^{s(3-k)/(s+8-2k)}.
$$

因此在本页 convention 下，

$$
\boxed{
e={s(3-k)\over s+8-2k}
}
$$

Formula ID：`EI-REFRESHED-E-INDEX-001`。

对 ISM：

$$
e={3s\over s+8}.
$$

对 wind：

$$
e={s\over s+4}.
$$

这说明 refreshed shock 的 \(e\) 不是任意自由指数；它由 ejecta stratification 和外部介质共同决定。

## 6. Detailed Derivation III：Break Evolution with Energy Injection

第 02 讲已经给出 synchrotron break 的构造：

$$
\nu_m\propto \Gamma B'\gamma_m^2,
\qquad
\nu_c\propto \Gamma B'\gamma_c^2,
\qquad
F_{\nu,\max}\propto N_e\Gamma B'.
$$

现在把 \(E(t)\propto t^e\) 放入 general-\(k\) dynamics。

### 6.1 基础时间指数

定义 \(D=4-k\)。从第 4 节：

$$
R\propto t^{(1+e)/D},
\qquad
\Gamma\propto t^{-(3-k-e)/(2D)}.
$$

外部密度：

$$
n\propto R^{-k}
\propto
t^{-k(1+e)/D}.
$$

shock magnetic field：

$$
B'\propto \Gamma n^{1/2}.
$$

因此

$$
B'
\propto
t^{[-3+e(1-k)]/[2(4-k)]}.
$$

electron injection Lorentz factor \(\gamma_m\propto\Gamma\)，所以

$$
\gamma_m
\propto
t^{-(3-k-e)/[2(4-k)]}.
$$

cooling Lorentz factor：

$$
\gamma_c\propto {1\over B'^2\Gamma t}.
$$

代入上面的 \(\Gamma\) 与 \(B'\)：

$$
\gamma_c
\propto
t^{[1+k+e(2k-3)]/[2(4-k)]}.
$$

### 6.2 三个 break quantity

先推 \(\nu_m\)：

$$
\nu_m\propto\Gamma B'\gamma_m^2
\propto
\Gamma^3B'.
$$

代入指数：

$$
\nu_m
\propto
t^{[-12+3k+4e-ek]/[2(4-k)]}.
$$

再推 \(\nu_c\)：

$$
\nu_c\propto \Gamma B'\gamma_c^2,
$$

所以

$$
\nu_c
\propto
t^{(3k-4)(1+e)/[2(4-k)]}.
$$

最后

$$
F_{\nu,\max}\propto N_e\Gamma B',
\qquad
N_e\propto R^{3-k}.
$$

因此

$$
F_{\nu,\max}
\propto
t^{[-k+e(8-3k)]/[2(4-k)]}.
$$

Formula ID：`EI-BREAK-EVOL-K-001`。

### 6.3 ISM limit

令 \(k=0\)，得到常用 ISM 注入标度：

$$
\boxed{
\nu_m\propto t^{e/2-3/2},
\qquad
\nu_c\propto t^{-e/2-1/2},
\qquad
F_{\nu,\max}\propto t^e
}
$$

Formula ID：`EI-BREAK-EVOL-ISM-001`。

检查：\(e=0\) 给 \(\nu_m\propto t^{-3/2}\)、\(\nu_c\propto t^{-1/2}\)、\(F_{\nu,\max}\propto t^0\)，即第 02 讲的 ISM constant-energy 结果。

## 7. Detailed Derivation IV：Closure Relation Modification

### 7.1 Slow cooling, \(\nu_m<\nu<\nu_c\), ISM

在 fixed observing frequency 下：

$$
F_\nu
=
F_{\nu,\max}
\left({\nu\over\nu_m}\right)^{-(p-1)/2}.
$$

因为 \(\nu\) 固定，

$$
F_\nu\propto F_{\nu,\max}\nu_m^{(p-1)/2}.
$$

使用 ISM 注入标度：

$$
F_{\nu,\max}\propto t^e,
\qquad
\nu_m\propto t^{e/2-3/2}.
$$

于是

$$
F_\nu
\propto
t^e
t^{(p-1)(e/2-3/2)/2}.
$$

指数相加：

$$
F_\nu
\propto
t^{e+(p-1)(e/4-3/4)}.
$$

定义 \(F_\nu\propto t^{-\alpha}\)，则

$$
\boxed{
\alpha
=
{3(p-1)\over4}
-
{e(p+3)\over4}
}
$$

Formula ID：`EI-CLOSURE-SLOW-MID-ISM-001`。

这就是 plateau 直觉的解析来源：\(e>0\) 会减小 \(\alpha\)，使 light curve 变平。

### 7.2 Slow cooling, \(\nu>\nu_c\), ISM

对于 high-frequency slow-cooling segment：

$$
F_\nu
\propto
F_{\nu,\max}\nu_m^{(p-1)/2}\nu_c^{1/2}.
$$

代入 ISM 注入标度：

$$
F_\nu
\propto
t^e
t^{(p-1)(e/4-3/4)}
t^{(-e/2-1/2)/2}.
$$

因此

$$
\boxed{
\alpha
=
{3p-2\over4}
-
{e(p+2)\over4}
}
$$

Formula ID：`EI-CLOSURE-SLOW-HIGH-ISM-001`。

这个 segment 对 density 的直接敏感性弱于 optical mid segment，但对 energy injection 仍敏感。

## 8. Magnetar-Like Injection as a Special Case

一个常用 central-engine toy model 是 spin-down-like luminosity：

$$
L_{\rm sd}(t)
=
{L_0\over(1+t/T_{\rm sd})^2}.
$$

Formula ID：`EI-MAGNETAR-SPINDOWN-001`。

积分能量为

$$
E(t)=E_0+\int_0^t {L_0\,dt'\over(1+t'/T_{\rm sd})^2}
=
E_0+
L_0T_{\rm sd}{t\over t+T_{\rm sd}}.
$$

当 \(t\ll T_{\rm sd}\) 且 \(E_0\) 不主导时：

$$
E(t)\simeq E_0+L_0t,
$$

局部近似 \(e\simeq1\)。当 \(t\gg T_{\rm sd}\)：

$$
E(t)\to E_0+L_0T_{\rm sd},
$$

回到 \(e\simeq0\) 的 constant-energy afterglow。这个 toy model 可以产生 plateau 和 plateau 结束后的 steepening，但同样不是唯一解释。

## 9. Density Variation

### 9.1 从 density profile 到 swept-up mass

若

$$
\rho(R)=A R^{-k}g(R),
$$

则 swept-up mass 是

$$
m_{\rm sw}(R)
=
4\pi A\int_0^R r^{2-k}g(r)\,dr.
$$

Formula ID：`DENS-MSW-GR-001`。

对缓慢变化的 \(g(R)\)，可以把局部动力学看成带有 effective \(A_{\rm eff}\) 或 effective \(k_{\rm eff}\) 的 BM。对 sharp density jump，shock 会产生 transmitted / reflected wave，\(\Gamma(R)\)、emissivity 和 EATS 都会被平滑，不能只把 \(n\) 替换进 closure formula。

### 9.2 Fixed-time spectral response

在 ISM slow cooling 的标准 asymptotic scalings 中，可把 flux 对 \(E\) 和 \(n\) 的依赖写成：

$$
F_\nu(\nu_m<\nu<\nu_c)
\propto
E^{(p+3)/4}n^{1/2}
t^{-3(p-1)/4},
$$

而

$$
F_\nu(\nu>\nu_c)
\propto
E^{(p+2)/4}
t^{-(3p-2)/4},
$$

在这个 high-frequency segment 中对 uniform density 的显式依赖近似抵消。Formula IDs：`DENS-FLUX-SLOW-MID-ISM-001`、`DENS-FLUX-SLOW-HIGH-ISM-001`。

这给出一个重要诊断：如果 optical bump 强但 X-ray 同步不明显，density variation 比纯 energy injection 更自然；如果多个 optically thin bands 近似 achromatic 变平，energy injection 或 geometric effect 更容易解释。不过实际判断还要检查 \(\nu_c\) 是否位于两 band 之间、是否有 dust/absorption、以及 radio 是否受 SSA/scintillation 影响。

### 9.3 Wind termination shock

Massive-star progenitor 的 circumburst medium 可能从自由 wind

$$
\rho_w=A R^{-2}
$$

过渡到 shocked wind 或 ISM-like 外层。一个 schematic profile 可写成

$$
\rho(R)=
\begin{cases}
A R^{-2}, & R<R_t,\\
\rho_{\rm out}, & R>R_t.
\end{cases}
$$

Formula ID：`DENS-WIND-TERMINATION-001`。

对应的 transition observer time 量级来自第 01 讲：

$$
t_t\sim (1+z){R_t\over C_t c\Gamma^2(R_t)}.
$$

若在 \(t_t\) 附近看到 break，不应立刻称为 jet break；也可能是 wind-to-ISM transition、energy-injection end 或 structured-jet viewing effect。

## 10. Degeneracy Map

| 观测现象 | 可能机制 | 优先检查 |
| --- | --- | --- |
| shallow decay / plateau | energy injection, structured jet, high-latitude tail contamination, evolving microphysics | achromaticity, spectral index stability, plateau end slope |
| optical rebrightening | refreshed shock, density bump, reverse shock, two-component jet | X-ray counterpart, color evolution, radio/SSA behavior |
| smooth steepening | jet break, energy-injection end, cooling break, density transition | spectral-index jump, multi-band timing |
| radio/mm excess | reverse shock, wide component, density enhancement, SSA, scintillation | source size, modulation, \(\nu_a\), late calorimetry |
| chromatic X-ray break | central-engine component, cooling/IC effect, absorption/systematics | optical counterpart, hardness evolution, instrument cross-calibration |

最稳妥的写法是：先列出同一数据特征能被哪些机制解释，再说明额外观测如何打破简并。单一 band 的 bump 或 break 不足以唯一确定机制。

## 11. Exact Analytic Status

| 对象 | 解析状态 | 说明 |
| --- | --- | --- |
| \(L_{\rm inj}\propto t^{-q}\) 积分 | closed for \(q\ne1\), logarithmic for \(q=1\) | \(e=1-q\) 只在注入主导时成立 |
| \(E(t)\propto t^e\) dynamics | closed power-law | assumes BM form remains valid |
| refreshed shock \(E(>\Gamma)\) relation | closed scaling | depends on cumulative energy convention |
| break evolution with \(e,k\) | closed power-law | optically thin synchrotron asymptotic |
| injected closure relations | closed in selected segments | here explicitly gives ISM slow cooling |
| smooth density perturbation | semi-analytic | can use effective local profile |
| sharp density jump/drop | generally numerical | hydrodynamic response plus EATS smoothing |
| full event degeneracy resolution | observational/model comparison | not a single formula |

## 12. Approximation Hierarchy

| 层级 | 做法 | 保留 | 牺牲 |
| --- | --- | --- | --- |
| constant-energy BM | \(e=0\), \(g=1\) | standard closure | plateau/bump |
| phenomenological injection | \(E\propto t^e\) | transparent slope changes | central-engine physics |
| luminosity model | \(L_{\rm inj}\propto t^{-q}\) or spin-down | injection timescale | shell collision details |
| refreshed shock | \(E(>\Gamma)\propto\Gamma^{-s}\) | ejecta stratification | detailed shell hydrodynamics |
| smooth density variation | \(\rho=A R^{-k}g(R)\) | medium trend | shock response |
| sharp transition | hydrodynamic plus EATS numerical model | jump/drop physics | closed-form closure |
| event fit | joint dynamics, spectrum, geometry, data systematics | multi-band inference | uniqueness without priors |

## 13. 从推导到代码的实现约定

| Formula ID | 内容 | 代码 | 层级 |
| --- | --- | --- | --- |
| `EI-LINJ-POWERLAW-001` | \(L_{\rm inj}=L_0(t/t_0)^{-q}\) | theory-only | course-derived |
| `EI-ENERGY-E-T-001` | \(E(t)\propto t^e\) | theory-only | course-derived |
| `EI-DYN-GENERAL-K-001` | injected BM \(R(t),\Gamma(t)\) | theory-only | course-derived |
| `EI-BREAK-EVOL-K-001` | general-\(k\) break evolution with injection | theory-only | course-derived |
| `EI-BREAK-EVOL-ISM-001` | ISM injected \(\nu_m,\nu_c,F_{\nu,\max}\) | theory-only | course-derived |
| `EI-CLOSURE-SLOW-MID-ISM-001` | ISM slow mid closure with \(e\) | theory-only | course-derived |
| `EI-CLOSURE-SLOW-HIGH-ISM-001` | ISM slow high closure with \(e\) | theory-only | course-derived |
| `EI-REFRESHED-E-GAMMA-001` | \(E(>\Gamma)\propto\Gamma^{-s}\) | theory-only | course-derived |
| `EI-REFRESHED-E-INDEX-001` | \(e=s(3-k)/(s+8-2k)\) | theory-only | course-derived |
| `EI-MAGNETAR-SPINDOWN-001` | \(L=L_0(1+t/T_{\rm sd})^{-2}\) | theory-only | teaching model |
| `DENS-PERTURB-GR-001` | \(\rho=A R^{-k}g(R)\) | theory-only | course-derived |
| `DENS-MSW-GR-001` | perturbed swept-up mass integral | theory-only | course-derived |
| `DENS-FLUX-SLOW-MID-ISM-001` | ISM slow mid density response | theory-only | course-derived |
| `DENS-FLUX-SLOW-HIGH-ISM-001` | ISM slow high weak density response | theory-only | course-derived |
| `DENS-WIND-TERMINATION-001` | wind-to-outer-medium transition | theory-only | schematic |

Implementation differences:

- 当前本地 forward-shock code 仍主要覆盖 constant-energy ISM/wind break scalings、sharp synchrotron spectrum 和 teaching light-curve helpers；没有 self-consistent energy-injection hydrodynamic solver。
- 若后续代码加入 `E(t)`，应把 `e` 或 \(L_{\rm inj}(t)\) 明确标为 phenomenological input，而不是把 plateau fit 写成 central-engine proof。
- Density variation 不能只改 `density_cm3` 常数。对 time-dependent density，必须说明采用的是 local scaling、piecewise profile、hydrodynamic table 还是 external mature solver。
- `afterglowpy`、`VegasAfterglow`、BOXFIT-like tables 或专用 structured-jet solvers 可作为 benchmark-output / mature-method comparison，不能作为本页推导的唯一物理来源。

## 14. Benchmark Boundary

当前本页是 theory-only extension。它可以给代码 Codex 的接口建议：

- `energy_injection_dynamics_exponents(k, e)`：返回 \(R,\Gamma,\nu_m,\nu_c,F_{\nu,\max}\) exponents；
- `closure_alpha_energy_injection(segment, p, e, medium)`：先实现 ISM slow-cooling segments；
- `refreshed_shock_e_index(s, k)`：明确 cumulative energy convention；
- `density_profile_piecewise_wind_ism(R, A, R_t, rho_out)`：只作为 profile helper，不声称 full hydrodynamics。

但在这些 helper 出现并验证前，本页新增 Formula ID 均保持 `theory-only`。若未来和外部 solver 对照，比较对象应是 matched convention 下的 slope、break time 和 limiting behavior，不是把外部 package 输出写成理论证明。

## 15. Interfaces to Later Pages

- non-relativistic transition / radio calorimetry：energy injection 会改变 late kinetic energy，density profile 会改变 Sedov-Taylor interpretation。
- two-component jet：离散 component 可以模仿 refreshed shock 或 structured jet。
- particle acceleration：若 \(\epsilon_e,\epsilon_B,p\) 随 shock condition 演化，会和 injection/density variation 简并。
- event workflow：必须区分 observed plateau、model-inferred \(e\)、central-engine interpretation 和 refreshed-shock interpretation。

## 16. 不声称

- 不把 X-ray plateau 自动解释成 magnetar。
- 不把 optical bump 自动解释成 density jump。
- 不把 smooth steepening 自动解释成 jet break。
- 不把 \(E(t)\propto t^e\) 的 phenomenological fit 写成直接观测到的 kinetic-energy growth。
- 不把 density jump 的 instantaneous flux rescaling 写成完整 hydrodynamic light curve。
- 不把 radio/mm excess 在未处理 SSA、source size 和 scintillation 前写成唯一 wide component 或 density structure。

## 17. 参考来源

- Rees & Meszaros 1998, *Refreshed Shocks and Afterglow Longevity in Gamma-Ray Bursts*.
- Sari & Meszaros 2000, *Impulsive and Varying Injection in Gamma-Ray Burst Afterglows*.
- Zhang & Meszaros 2001, *Gamma-Ray Burst Afterglow with Continuous Energy Injection*.
- Nousek et al. 2006, *Evidence for a Canonical Gamma-Ray Burst Afterglow Light Curve in the Swift XRT Data*.
- Zhang et al. 2006, *Physical Processes Shaping GRB X-Ray Afterglow Light Curves*.
- Chevalier & Li 2000, *Wind Interaction Models for Gamma-Ray Burst Afterglows*.
- Nakar & Granot 2007, *The Effect of Density Variations on Gamma-Ray Burst Afterglow Light Curves*.
- Granot & Sari 2002, *The Shape of Spectral Breaks in Gamma-Ray Burst Afterglows*.
- Piran 2004, *The Physics of Gamma-Ray Bursts*.
- Zhang 2014, *The Physics of Gamma-Ray Bursts & Relativistic Jets*.
