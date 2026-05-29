# 06 Non-Relativistic Transition and Radio Calorimetry

状态：v0.1 课程讲义草案。本页把 early ultra-relativistic BM afterglow 推到 late-time trans-relativistic / Newtonian regime。核心问题不是再套一个早期 closure relation，而是明确：什么时候 BM 标度失效，为什么 Sedov-Taylor dynamics 成为 late radio 的自然底座，以及 radio calorimetry 如何用 source size、self-absorption turnover 和 synchrotron energy budget 估计 kinetic energy。

本页原则：late radio calorimetry 是 energy-budget diagnostic，不是 prompt gamma-ray energy，也不是自动证明 two-component jet。任何 calorimetry result 都依赖 geometry、microphysics、density profile、SSA/scintillation 和 event-level modeling convention。

## 1. 物理图像

BM solution 的入口条件是 ultra-relativistic：

$$
\Gamma\gg1.
$$

随着 blast wave sweep up external mass，bulk kinetic energy 被转成 shocked gas internal energy，\(\Gamma\) 下降到 order unity。此时两个早期近似同时失效：

- observer 只看 \(\Gamma^{-1}\) beaming cone 的几何近似变弱；
- BM self-similar ultra-relativistic shock jump 和 \(t_{\rm obs}\sim R/(c\Gamma^2)\) 标度不再适用。

Late radio afterglow 的价值正在这里：source 变大、beaming 较弱、radio spectrum 可能保留 self-absorption turnover，因而能对 true kinetic energy 和 emitting size 给出比早期单纯 slope fitting 更直接的约束。

## 2. 参考系与变量

| 符号 | 含义 | 单位 |
| --- | --- | --- |
| \(E\) | late blast-wave kinetic energy；需说明 true / spherical-equivalent convention | erg |
| \(R_{\rm NR}\) | non-relativistic transition radius scale | cm |
| \(t_{\rm NR}\) | observer-frame transition time scale | s |
| \(R_{\rm ST}\) | Sedov-Taylor radius scale | cm |
| \(v=dR/dt\) | Newtonian shock velocity | cm s\(^{-1}\) |
| \(\rho=A R^{-k}\) | external mass density profile | g cm\(^{-3}\) |
| \(R_s\) | synchrotron source radius used in calorimetry | cm |
| \(\nu_a\) | self-absorption turnover frequency | Hz |
| \(F_{\nu,p}\) | observed peak flux density near SSA/peak | mJy or cgs |

本页默认 \(t\) 在 Sedov-Taylor 推导中是 source-frame Newtonian dynamical time；observer time 只差一个 \((1+z)\) 和 geometry convention。写事件模型时必须显式转换。

## 3. General Expression

### 3.1 Transition condition

Non-relativistic transition 的量级条件可以写成：

$$
m_{\rm sw}(R_{\rm NR})c^2\sim E.
$$

Formula ID：`NR-TRANSITION-MSW-001`。

Formula ID：`AG-DYN-NR-ENTRY-001`。

这不是 sharp light-curve break，而是 BM solution 失效并进入 trans-relativistic dynamics 的能量尺度。

### 3.2 Sedov-Taylor energy conservation

Newtonian adiabatic blast wave 的 general expression 是：

$$
E
\sim
C_{\rm ST}\rho(R)R^3v^2,
\qquad
v={dR\over dt}.
$$

对 \(\rho=A R^{-k}\)：

$$
E\sim C_{\rm ST}A R^{3-k}\left({dR\over dt}\right)^2.
$$

Formula ID：`NR-ST-ENERGY-K-001`。

这里 \(C_{\rm ST}\) 是 order-unity self-similar constant，依赖 adiabatic index、\(k\) 和 shock convention。本页推导只保留 scaling。

### 3.3 Radio calorimetry schematic

Radio calorimetry 的一般结构是把 spectrum 和 size 反推 energy：

$$
\{F_{\nu,p},\nu_a,\nu_m,D_L,z\}
\quad\Rightarrow\quad
\{R_s,B,N_e,E_e,E_B\}.
$$

最低层的能量预算为

$$
E_{\rm radio}
\sim
E_e+E_B+E_{\rm baryon},
$$

其中 \(E_{\rm baryon}\) 需要 dynamics 或 composition assumption 才能闭合。若使用 equipartition/minimum-energy estimate，则先最小化

$$
E_{\rm eq}(R_s,B)
=
E_e(R_s,B)+E_B(R_s,B),
$$

而不是声称系统真的严格 \(\epsilon_e=\epsilon_B\)。Formula ID：`RC-EQPART-ENERGY-001`。

## 4. Detailed Derivation I：Transition Radius

### 4.1 ISM

Uniform ISM 中

$$
\rho=nm_p.
$$

swept-up mass：

$$
m_{\rm sw}
=
{4\pi\over3}R^3nm_p.
$$

令

$$
m_{\rm sw}c^2\sim E,
$$

得到

$$
{4\pi\over3}R_{\rm NR}^3nm_pc^2\sim E.
$$

因此

$$
\boxed{
R_{\rm NR,ISM}
\sim
\left({3E\over4\pi nm_pc^2}\right)^{1/3}
}
$$

Formula ID：`NR-RADIUS-ISM-001`。

对应 observer-frame time scale 常写作

$$
\boxed{
t_{\rm NR,ISM}
\sim
(1+z){R_{\rm NR,ISM}\over c}
}
$$

Formula ID：`NR-TIME-ISM-001`。

系数不是精确预测，因为真正的 trans-relativistic transition 是 gradual，并且受 jet geometry、lateral spreading 和 EATS 影响。

### 4.2 Wind

Wind medium 中

$$
\rho=A R^{-2}.
$$

swept-up mass：

$$
m_{\rm sw}
=
\int_0^R 4\pi r^2 A r^{-2}\,dr
=
4\pi A R.
$$

令 \(m_{\rm sw}c^2\sim E\)：

$$
4\pi A R_{\rm NR}c^2\sim E.
$$

所以

$$
\boxed{
R_{\rm NR,wind}
\sim
{E\over4\pi A c^2}
}
$$

and

$$
\boxed{
t_{\rm NR,wind}
\sim
(1+z){E\over4\pi A c^3}
}
$$

Formula IDs：`NR-RADIUS-WIND-001`、`NR-TIME-WIND-001`。

这说明不能把 ISM \(R_{\rm NR}\propto(E/n)^{1/3}\) 直接套到 wind event；wind case 的 energy / density dependence 完全不同。

## 5. Detailed Derivation II：Sedov-Taylor Scaling

### 5.1 Dimensional derivation for general \(k\)

从

$$
E\sim A R^{3-k}\left({dR\over dt}\right)^2
$$

出发。假设

$$
R(t)=C t^a.
$$

则

$$
{dR\over dt}=aCt^{a-1}.
$$

代入 energy conservation：

$$
E
\propto
A(Ct^a)^{3-k}(aCt^{a-1})^2.
$$

整理时间指数：

$$
E
\propto
AC^{5-k}a^2
t^{a(3-k)+2a-2}
=
AC^{5-k}a^2t^{a(5-k)-2}.
$$

绝热能量为常数，因此

$$
a(5-k)-2=0.
$$

于是

$$
\boxed{
R(t)\propto
\left({E\over A}\right)^{1/(5-k)}
t^{2/(5-k)}
}
$$

and

$$
\boxed{
v(t)\propto
\left({E\over A}\right)^{1/(5-k)}
t^{-(3-k)/(5-k)}
}
$$

Formula ID：`NR-ST-GENERAL-K-001`。

### 5.2 ISM and wind limits

ISM \(k=0\)：

$$
R\propto (E/\rho)^{1/5}t^{2/5},
\qquad
v\propto t^{-3/5}.
$$

Formula ID：`NR-ST-ISM-001`。

Wind \(k=2\)：

$$
R\propto (E/A)^{1/3}t^{2/3},
\qquad
v\propto t^{-1/3}.
$$

Formula ID：`NR-ST-WIND-001`。

这些指数和 BM phase 的 \(R\simeq ct\)、\(\Gamma(t)\) 幂律完全不同。Late radio 如果仍用 ultra-relativistic closure，会把 energy、density 和 geometry 系统性搅在一起。

## 6. Detailed Derivation III：Radio Synchrotron Source-Size Argument

### 6.1 SSA turnover as an optical-depth condition

Self-absorption turnover 的最低层条件是

$$
\tau_{\nu_a}
=
\alpha_{\nu_a}R_s
\sim1.
$$

Formula ID：`RC-SSA-TAUA-001`。

这里 \(\alpha_\nu\) 不是自由参数。第 01 个辐射机制模板和第 02 个 afterglow synchrotron 页已经给出：

$$
\alpha_\nu
\propto
K B'^{(p+2)/2}\nu^{-(p+4)/2}
$$

for a power-law electron population in the optically thin synchrotron framework. 因此 \(\nu_a\) 同时约束 electron normalization、magnetic field 和 source size。

### 6.2 Peak flux and emitting area

若 radio peak 是 SSA-controlled peak，Rayleigh-Jeans-like optically thick surface brightness 可写成 schematic form：

$$
F_{\nu_a}
\sim
{\pi R_s^2\over D_A^2}
S_{\nu_a},
$$

其中 source function

$$
S_\nu={j_\nu\over\alpha_\nu}.
$$

对 synchrotron power-law electron distribution，

$$
S_\nu\propto B'^{-1/2}\nu^{5/2}.
$$

Formula ID：`RC-SSA-SOURCE-SIZE-001`。

因此

$$
F_{\nu_a}
\propto
R_s^2B'^{-1/2}\nu_a^{5/2}D_A^{-2}.
$$

如果 \(F_{\nu_a}\)、\(\nu_a\) 和 \(D_A\) 已知，这个式子给 \(R_s\) 与 \(B'\) 的关系；再结合 \(\tau_{\nu_a}\sim1\) 或 equipartition/minimum-energy 条件，就能估计 \(R_s\)、\(B'\) 和 energy scale。

### 6.3 Equipartition is a closure assumption

Magnetic energy:

$$
E_B
\sim
{B'^2\over8\pi}{4\pi R_s^3\over3}f_V.
$$

Electron energy for power-law electrons:

$$
E_e
=
\int_{\gamma_m}^{\gamma_{\max}}
N(\gamma)\gamma m_ec^2\,d\gamma.
$$

Without an independent size or microphysical constraint, \(E_e\) and \(E_B\) are degenerate. Minimum-energy / equipartition calorimetry picks the \(R_s,B'\) pair that minimizes \(E_e+E_B\). That is a practical estimator, not a proof that the plasma is exactly equipartitioned.

Formula ID：`RC-EQPART-SOURCE-001`。

## 7. Geometry, Beaming, and True Energy

Early afterglow often reports \(E_{\rm iso}\) and then applies beaming correction:

$$
E_{\rm true}\simeq f_bE_{\rm iso},
\qquad
f_b\simeq{\theta_j^2\over2}.
$$

Late radio calorimetry is useful because the outflow may be less beamed and closer to quasi-spherical. But this does not remove all model dependence:

- if the jet has not sphericalized, \(E_{\rm radio}\) is still geometry-dependent;
- if there is a wide mildly relativistic component, late radio may measure that component more than the narrow prompt component;
- if energy injection continues, late kinetic energy differs from early afterglow energy;
- if density profile or microphysics is wrong, calorimetry shifts.

Thus radio calorimetry estimates late kinetic energy under stated assumptions; it is not automatically the prompt radiated energy and not automatically the total explosion energy.

## 8. Scintillation, SSA, and Source Size Diagnostics

Radio data have one complication that is also a gift: compact sources scintillate. Early strong modulation can be propagation-driven, not intrinsic. As the source expands, scintillation is quenched; this gives an angular-size diagnostic.

Key checks:

- Is the radio peak \(\nu_m\), \(\nu_a\), or a component transition?
- Is flux modulation consistent with interstellar scintillation?
- Does \(\nu_a(t)\) move consistently with an expanding source?
- Is there VLBI or scintillation-quenching evidence for angular size?
- Are optical/X-ray bands consistent with the same component?

Without these checks, a radio bump can be over-interpreted as a density jump, wide jet, refreshed shock, or reverse shock.

## 9. Event Interpretation Boundary

GRB 030329 is the classic radio calorimetry / two-component context: late radio behavior can point to a wider or mildly relativistic component, while early optical and gamma-ray behavior can be dominated by a narrow component. But the event-level conclusion depends on SN subtraction, radio spectral modeling, angular-size constraints, microphysics and geometry.

GRB 221009A radio/mm extra component should be treated the same way: it is not automatically simple calorimetry, simple density structure, or simple wide component. It may involve additional outflow, reverse shock, density variation, SSA/scintillation, or emission regions not present in a single forward-shock model.

## 10. Exact Analytic Status

| 对象 | 解析状态 | 说明 |
| --- | --- | --- |
| \(R_{\rm NR}\) from \(m_{\rm sw}c^2\sim E\) | closed scaling | transition is gradual |
| ISM / wind \(t_{\rm NR}\) | closed order-of-magnitude | coefficient and geometry dependent |
| Sedov-Taylor general-\(k\) scaling | closed scaling | exact constants require self-similar solution |
| SSA optical-depth condition | formal closed condition | \(\alpha_\nu\) depends on electron distribution |
| source-size / SSA peak relation | semi-analytic | requires homogeneous-source assumption |
| equipartition calorimetry | minimization estimate | not proof of exact equipartition |
| full radio calorimetry fit | numerical / event-model | needs multi-frequency data and geometry |

## 11. Approximation Hierarchy

| 层级 | 做法 | 保留 | 牺牲 |
| --- | --- | --- | --- |
| BM invalid boundary | \(m_{\rm sw}c^2\sim E\) | transition scale | trans-relativistic hydrodynamics |
| Sedov-Taylor scaling | \(E\sim\rho R^3v^2\) | late-time dynamics | relativistic corrections |
| homogeneous SSA source | \(F_{\nu_a}\sim\pi R_s^2S_{\nu_a}/D_A^2\) | size-B relation | geometry gradients |
| equipartition calorimetry | minimize \(E_e+E_B\) | practical energy estimate | exact microphysics |
| multi-frequency radio modeling | fit spectrum and dynamics | event-level constraints | model dependence |
| hydro / numerical afterglow solver | trans-relativistic dynamics + EATS | smooth transition | code convention dependence |

## 12. 从推导到代码的实现约定

| Formula ID | 内容 | 代码 | 层级 |
| --- | --- | --- | --- |
| `NR-TRANSITION-MSW-001` | \(m_{\rm sw}c^2\sim E\) | theory-only | course-derived |
| `NR-RADIUS-ISM-001` | ISM \(R_{\rm NR}\) | theory-only | course-derived |
| `NR-TIME-ISM-001` | ISM \(t_{\rm NR}\) | theory-only | scale estimate |
| `NR-RADIUS-WIND-001` | wind \(R_{\rm NR}\) | theory-only | course-derived |
| `NR-TIME-WIND-001` | wind \(t_{\rm NR}\) | theory-only | scale estimate |
| `NR-ST-ENERGY-K-001` | Sedov-Taylor energy scaling | theory-only | course-derived |
| `NR-ST-GENERAL-K-001` | general-\(k\) Newtonian ST scaling | theory-only | course-derived |
| `NR-ST-ISM-001` | ISM ST \(R,v\) exponents | theory-only | course-derived |
| `NR-ST-WIND-001` | wind ST \(R,v\) exponents | theory-only | course-derived |
| `RC-SSA-TAUA-001` | \(\tau_{\nu_a}\sim1\) source condition | theory-only | course-derived |
| `RC-SSA-SOURCE-SIZE-001` | SSA peak source-size relation | theory-only | semi-analytic |
| `RC-EQPART-ENERGY-001` | calorimetry energy budget | theory-only | teaching model |
| `RC-EQPART-SOURCE-001` | equipartition/minimum-energy closure | theory-only | teaching model |

Implementation differences:

- 当前本地 afterglow code 没有 trans-relativistic hydrodynamic solver，也没有 radio calorimetry fitter。
- Existing synchrotron helpers can describe sharp spectra, but they do not infer \(R_s\), \(B'\) or \(E_{\rm radio}\) from radio data.
- A future helper should keep `true_energy_erg` and `isotropic_equivalent_energy_erg` separate.
- A future radio calorimetry routine must state whether it assumes homogeneous source, equipartition, known angular size, measured \(\nu_a\), or external density.

## 13. Benchmark Boundary

External hydrodynamic tables, BOXFIT-like tools, afterglowpy trans-relativistic options, VLBI source-size constraints, and published GRB 030329 calorimetry are mature-method / event benchmark layers. They can calibrate convention and trend, but cannot replace the theory-page assumptions.

Current local state:

- BM and synchrotron early afterglow helpers exist.
- Late-time non-relativistic and radio calorimetry formulas are theory-only.
- No claim is made for full GRB 030329 or GRB 221009A radio calorimetry reproduction.

## 14. Interfaces to Later Pages

- two-component jet：late radio calorimetry can indicate a wide/mild component.
- event-model interpretation：must separate observed radio data, model-inferred source size, and physical interpretation.
- particle acceleration：late-time shock velocity changes injection/cooling assumptions.
- data workflow：radio measurements need frequency, flux, upper limits, scintillation caveat and time zero provenance.

## 15. 不声称

- 不把 \(t_{\rm NR}\) 写成 sharp observed break。
- 不把 \(E_{\rm iso}\) 直接等同于 late-time calorimetric energy。
- 不把 equipartition estimate 写成 plasma 必然处于 equipartition。
- 不把 radio bump 自动解释成 wide component、density jump 或 refreshed shock。
- 不忽略 SSA、source size 和 scintillation 就做 radio energy conclusion。

## 16. 参考来源

- Sedov 1959, *Similarity and Dimensional Methods in Mechanics*.
- Taylor 1950, *The Formation of a Blast Wave by a Very Intense Explosion*.
- Frail, Waxman & Kulkarni 2000, radio calorimetry of GRB afterglows.
- Berger, Kulkarni & Frail 2003, *A Common Origin for Cosmic Explosions Inferred from Calorimetry of GRB030329*.
- Piran 2004, *The Physics of Gamma-Ray Bursts*.
- Granot & Sari 2002, *The Shape of Spectral Breaks in Gamma-Ray Burst Afterglows*.
- Zhang 2014, *The Physics of Gamma-Ray Bursts & Relativistic Jets*.
