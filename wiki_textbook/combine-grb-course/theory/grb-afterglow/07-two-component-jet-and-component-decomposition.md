# 07 Two-Component Jet and Component Decomposition

状态：v0.1 课程讲义草案。本页把 structured jet 的连续角结构离散化为 narrow / wide 两个 angular components，并讨论它如何影响 afterglow onset、jet break、late radio calorimetry 和 event-level component assignment。

核心原则：two-component jet 不是“任意两个光变成分”的同义词。它必须有明确的 angular geometry、component energy convention、initial Lorentz factor、deceleration time 和 spectral contribution。单独的 bump、plateau 或 radio excess 不能唯一证明 two-component jet。

## 1. 物理图像

Structured jet 在第 04 讲中写成连续 profile：

$$
\mathcal E(\theta)={dE\over d\Omega}(\theta),
\qquad
\Gamma_0=\Gamma_0(\theta).
$$

Two-component jet 是一个低维离散近似：一个窄而快的 narrow component 和一个宽而慢的 wide component 共同组成 outflow。常见直觉是：

- narrow component：高 \(\Gamma_{0,n}\)、小 \(\theta_n\)、主导 prompt gamma-ray 和 early afterglow；
- wide component：较低 \(\Gamma_{0,w}\)、较大 \(\theta_w\)、可能主导 late optical / radio；
- late wide component 的 rise 可掩盖 narrow component 的 jet break。

因此 two-component jet 的诊断点不是“光变看起来有两个阶段”，而是两个 angular zones 是否有不同的 dynamical timescales 和 spectral/radio constraints。

## 2. 参考系与变量

| 符号 | 含义 | 单位 |
| --- | --- | --- |
| \(\theta_n,\theta_w\) | narrow / wide half-opening angle | rad |
| \(\Gamma_{0,n},\Gamma_{0,w}\) | two components 的 initial Lorentz factors | dimensionless |
| \(\mathcal E_n,\mathcal E_w\) | energy per solid angle | erg sr\(^{-1}\) |
| \(E_{n,\rm iso},E_{w,\rm iso}\) | isotropic-equivalent kinetic energy | erg |
| \(E_{n,\rm true},E_{w,\rm true}\) | beaming-corrected true kinetic energy | erg |
| \(t_{{\rm dec},n},t_{{\rm dec},w}\) | component deceleration times | s |
| \(t_{j,n},t_{j,w}\) | component jet-break times | s |
| \(\theta_v\) | viewing angle from jet axis | rad |

本页默认 on-axis 或 near-axis observer，除非特别说明。Off-axis two-component jet 需要完整 angular/EATS integral，本页只给 geometry logic。

## 3. General Expression

### 3.1 Piecewise angular profile

最简单 nested two-component jet 写成：

$$
\mathcal E(\theta)=
\begin{cases}
\mathcal E_n, & 0\le\theta<\theta_n,\\
\mathcal E_w, & \theta_n\le\theta<\theta_w,\\
0, & \theta\ge\theta_w,
\end{cases}
$$

and

$$
\Gamma_0(\theta)=
\begin{cases}
\Gamma_{0,n}, & 0\le\theta<\theta_n,\\
\Gamma_{0,w}, & \theta_n\le\theta<\theta_w,\\
1, & \theta\ge\theta_w.
\end{cases}
$$

Formula ID：`TCJ-PROFILE-001`。

有些文献把 wide component 当成包住 narrow 的 full cone，而不是 annulus。两种 convention 的 true-energy integral 不同，必须在引用参数时说明。

### 3.2 Total observed flux

在 semi-analytic component decomposition 中，总 flux 写成线性叠加：

$$
F_\nu(t)
=
F_{\nu,n}(t)+F_{\nu,w}(t).
$$

Formula ID：`TCJ-FLUX-SUM-001`。

这个表达式只是 optically thin、无 radiative coupling 的最低层近似。若两个 component 在同一 line of sight 上相互作用，或 wide component 是 cocoon / shocked sheath，完整问题不是简单相加。

## 4. Detailed Derivation I：True Energy of Two Components

### 4.1 Top-hat component

若一个 component 是 half-opening angle \(\theta_i\) 的 two-sided top-hat，且 isotropic-equivalent energy 为

$$
E_{i,\rm iso}=4\pi\mathcal E_i,
$$

则 true energy 为

$$
E_{i,\rm true}
=
2\times
\int_0^{2\pi}d\phi\int_0^{\theta_i}
\mathcal E_i\sin\theta\,d\theta.
$$

积分：

$$
E_{i,\rm true}
=
4\pi\mathcal E_i(1-\cos\theta_i)
=
E_{i,\rm iso}(1-\cos\theta_i).
$$

small-angle limit:

$$
1-\cos\theta_i\simeq{\theta_i^2\over2}.
$$

因此

$$
\boxed{
E_{i,\rm true}
\simeq
{\theta_i^2\over2}E_{i,\rm iso}
}
$$

Formula ID：`TCJ-TRUE-ENERGY-CONE-001`。

### 4.2 Annular wide component

若 wide component 被定义为 \(\theta_n<\theta<\theta_w\) 的环带，而不是 full cone，则 two-sided true energy 为

$$
E_{w,\rm true}^{\rm ann}
=
4\pi\mathcal E_w(\cos\theta_n-\cos\theta_w).
$$

small-angle:

$$
\cos\theta_n-\cos\theta_w
\simeq
{\theta_w^2-\theta_n^2\over2}.
$$

所以

$$
\boxed{
E_{w,\rm true}^{\rm ann}
\simeq
{\theta_w^2-\theta_n^2\over2}E_{w,\rm iso}
}
$$

Formula ID：`TCJ-TRUE-ENERGY-ANNULUS-001`。

这就是参数比较中最容易出错的地方：\(E_{w,\rm iso}<E_{n,\rm iso}\) 并不意味着 \(E_{w,\rm true}<E_{n,\rm true}\)，因为 \(\theta_w\) 可能大得多。

## 5. Detailed Derivation II：Component Deceleration Time

### 5.1 ISM

对 component \(i\)，deceleration condition 为

$$
m_{\rm sw}(R_{{\rm dec},i})c^2\Gamma_{0,i}^2\sim E_i.
$$

ISM 中

$$
m_{\rm sw}={4\pi\over3}R^3nm_p.
$$

代入：

$$
{4\pi\over3}R_{{\rm dec},i}^3nm_pc^2\Gamma_{0,i}^2
\sim
E_i.
$$

于是

$$
R_{{\rm dec},i}
\sim
\left({3E_i\over4\pi nm_pc^2\Gamma_{0,i}^2}\right)^{1/3}.
$$

observer time:

$$
t_{{\rm dec},i}
\sim
(1+z){R_{{\rm dec},i}\over C_t c\Gamma_{0,i}^2}.
$$

因此

$$
\boxed{
t_{{\rm dec},i}^{\rm ISM}
\propto
(1+z)E_i^{1/3}n^{-1/3}\Gamma_{0,i}^{-8/3}
}
$$

Formula ID：`TCJ-TDEC-ISM-001`。

因为 \(\Gamma_{0,w}\ll\Gamma_{0,n}\) 常成立，wide component 即使能量不小，也会显著晚于 narrow component decelerate。

### 5.2 Wind

wind 中

$$
m_{\rm sw}=4\pi AR.
$$

deceleration condition:

$$
4\pi A R_{{\rm dec},i}c^2\Gamma_{0,i}^2\sim E_i.
$$

所以

$$
R_{{\rm dec},i}^{\rm wind}
\sim
{E_i\over4\pi Ac^2\Gamma_{0,i}^2}.
$$

observer time:

$$
t_{{\rm dec},i}^{\rm wind}
\propto
(1+z)E_iA^{-1}\Gamma_{0,i}^{-4}.
$$

Formula ID：`TCJ-TDEC-WIND-001`。

ISM 的 \(\Gamma_0^{-8/3}\) 和 wind 的 \(\Gamma_0^{-4}\) 不可互换。

## 6. Detailed Derivation III：Narrow Jet Break and Wide-Component Masking

### 6.1 Narrow component jet break

对 on-axis top-hat-like narrow component，jet break entry condition 是

$$
\Gamma_n(t_{j,n})\theta_n\sim1.
$$

ISM 中 \(\Gamma\propto(E/n)^{1/8}t^{-3/8}\)，所以

$$
\theta_n^{-1}
\propto
\left({E_{n,\rm iso}\over n}\right)^{1/8}
\left({t_{j,n}\over1+z}\right)^{-3/8}.
$$

整理：

$$
\boxed{
t_{j,n}^{\rm ISM}
\propto
(1+z)E_{n,\rm iso}^{1/3}n^{-1/3}\theta_n^{8/3}
}
$$

Formula ID：`TCJ-TJET-NARROW-ISM-001`。

wind 中 \(\Gamma\propto(E/A)^{1/4}t^{-1/4}\)，因此

$$
\boxed{
t_{j,n}^{\rm wind}
\propto
(1+z)E_{n,\rm iso}A^{-1}\theta_n^4
}
$$

Formula ID：`TCJ-TJET-NARROW-WIND-001`。

### 6.2 Masking criterion

总 flux：

$$
F_\nu=F_{\nu,n}+F_{\nu,w}.
$$

如果

$$
t_{{\rm dec},w}\sim t_{j,n},
$$

并且

$$
F_{\nu,w}(t_{{\rm dec},w})
\gtrsim
F_{\nu,n}(t_{j,n}),
$$

那么 wide component 的 rise / peak 会填平 narrow component 的 steepening，使 total light curve 看起来像 plateau、smooth bump 或 delayed break。

Formula ID：`TCJ-MASKING-001`。

更细一点，可以定义 instantaneous observed slope：

$$
\alpha_{\rm obs}
=
-{d\ln(F_{\nu,n}+F_{\nu,w})\over d\ln t}.
$$

对两个局部 power laws \(F_{\nu,i}\propto t^{-\alpha_i}\)，有

$$
\alpha_{\rm obs}
=
{\alpha_nF_{\nu,n}+\alpha_wF_{\nu,w}\over F_{\nu,n}+F_{\nu,w}}.
$$

若 wide component 正在上升，则 \(\alpha_w<0\)，总 slope 可以显著小于 narrow component 的 post-break slope。Formula ID：`TCJ-SLOPE-MIX-001`。

## 7. Viewing-Angle Regimes

Two-component geometry 至少有三个 viewing regimes：

| Regime | 条件 | 直觉 |
| --- | --- | --- |
| on narrow core | \(\theta_v<\theta_n\) | prompt / early afterglow 常由 narrow component 主导 |
| inside wide only | \(\theta_n<\theta_v<\theta_w\) | prompt 可变弱，afterglow 可由 wide local material 主导 |
| outside both | \(\theta_v>\theta_w\) | prompt 可能弱或不可见，afterglow peak 延迟 |

Formula ID：`TCJ-VIEWING-REGIME-001`。

这些 regime 只是 geometry labels。实际 observed flux 仍需 Doppler factor、EATS、component dynamics 和 spectrum。

## 8. Distinguishing Two-Component Jet from Alternatives

| 现象 | two-component interpretation | 主要替代解释 |
| --- | --- | --- |
| late optical bump | wide component emerges | refreshed shock, density bump, SN/kilonova contamination |
| radio excess | wide/mild component dominates radio | reverse shock, SSA/scintillation, density structure |
| missing narrow jet break | wide component masks break | energy injection, structured jet smooth wing |
| chromatic behavior | different components in different bands | cooling break, absorption, central-engine component |
| late kinetic energy larger than early beaming-corrected energy | wide component stores energy | energy injection, wrong density/microphysics |

Two-component jet becomes persuasive only when data support distinct dynamical timescales, spectral evolution, radio calorimetry/source-size evidence, or geometry diagnostics.

## 9. Event Interpretation Boundary

GRB 030329 is a classic two-component / radio-calorimetry interpretation: a narrow component explains early gamma-ray / optical-X-ray behavior, while a wider mildly relativistic component explains late radio and optical resurgence. But angles and energies are model-inferred, not directly observed images.

GRB 080319B demonstrates a different use: very narrow core geometry can increase apparent prompt brightness, while a wider component contributes later afterglow. However, geometry alone does not explain prompt optical / gamma-ray spectral mismatch.

GRB 221009A should keep candidate language: radio/mm extra component, narrow energetic core, structured jet and SSC/TeV interpretations remain alternatives unless a joint model explicitly compares them under shared data and conventions.

## 10. Exact Analytic Status

| 对象 | 解析状态 | 说明 |
| --- | --- | --- |
| piecewise angular profile | closed parameterization | artificial boundary |
| true-energy angular integrals | closed for top-hat / annulus | one-sided/two-sided convention matters |
| component \(t_{\rm dec}\) | closed scaling | onset estimate, not full light curve |
| narrow component \(t_j\) | closed scaling | top-hat, on-axis |
| flux sum | algebraic | assumes independent components |
| slope mixing | closed for local power laws | local diagnostic only |
| full two-component afterglow | numerical | needs dynamics, EATS, spectrum, microphysics |

## 11. Approximation Hierarchy

| 层级 | 做法 | 保留 | 牺牲 |
| --- | --- | --- | --- |
| discrete angular profile | narrow + wide top hats | simple geometry | smooth wings/cocoon |
| component timescales | \(t_{\rm dec,i}\), \(t_{j,i}\) scalings | onset and masking intuition | full hydro |
| flux decomposition | \(F_n+F_w\) | component dominance | interaction/coupling |
| local slope mixing | weighted \(\alpha\) | break masking intuition | curved spectra |
| event model | fit multi-band components | data comparison | uniqueness |
| hydrodynamic structured model | angular dynamics + EATS | realistic light curves | model/code dependence |

## 12. 从推导到代码的实现约定

| Formula ID | 内容 | 代码 | 层级 |
| --- | --- | --- | --- |
| `TCJ-PROFILE-001` | piecewise narrow/wide angular profile | theory-only | course-derived |
| `TCJ-TRUE-ENERGY-CONE-001` | cone true energy | theory-only | course-derived |
| `TCJ-TRUE-ENERGY-ANNULUS-001` | annular wide true energy | theory-only | course-derived |
| `TCJ-FLUX-SUM-001` | \(F_\nu=F_n+F_w\) | theory-only | semi-analytic |
| `TCJ-TDEC-ISM-001` | component deceleration time in ISM | theory-only | course-derived |
| `TCJ-TDEC-WIND-001` | component deceleration time in wind | theory-only | course-derived |
| `TCJ-TJET-NARROW-ISM-001` | narrow jet-break time in ISM | theory-only | course-derived |
| `TCJ-TJET-NARROW-WIND-001` | narrow jet-break time in wind | theory-only | course-derived |
| `TCJ-MASKING-001` | wide component masking condition | theory-only | diagnostic |
| `TCJ-SLOPE-MIX-001` | local slope mixing | theory-only | diagnostic |
| `TCJ-VIEWING-REGIME-001` | viewing-angle regimes | theory-only | geometry labels |

Implementation differences:

- 当前本地 structured-jet code only implements angular profile / Doppler toy helpers, not a two-component hydrodynamic light-curve solver.
- A future helper should require explicit convention: wide component as full cone or annulus.
- A future event model must not reuse a single \(E_{\rm iso}\), \(\Gamma_0\), \(\epsilon_e\), \(\epsilon_B\) for both components unless that is a stated assumption.
- Component fitting must keep observed data, derived BPL parameters, and model-inferred geometry separate.

## 13. Benchmark Boundary

Two-component jet benchmarks are mostly event-model and mature-method comparisons: Peng, Koenigl & Granot style semi-analytic models, GRB 030329 radio calorimetry, GRB 080319B broadband modeling, and structured-jet numerical solvers. Agreement with one model family is not proof that two-component geometry is unique.

Current local status:

- This page is theory-only.
- No two-component production solver exists.
- Existing radio/SSA diagnostics for GRB 221009A keep wide component as a candidate, not a selected explanation.

## 14. Interfaces to Later Pages

- polarization / VLBI diagnostics：can distinguish angular structure and source size.
- afterglow fitting workflow：must compare top-hat, structured, two-component, refreshed shock and density alternatives.
- event pages：GRB 030329, GRB 080319B and GRB 221009A should separate observation from model-inferred component parameters.

## 15. 不声称

- 不把任意两个光变成分叫 two-component jet。
- 不把 \(E_{\rm iso}\) 与 true energy 混用。
- 不把 GRB 030329 的 5 degree / 17 degree 参数写成普适模板。
- 不把 GRB 080319B 的 prompt optical/gamma mismatch 只归因于几何。
- 不把 GRB 221009A radio/mm extra component 自动解释成 wide component。

## 16. 参考来源

- Peng, Koenigl & Granot 2005, *Two-Component Jet Models of Gamma-Ray Burst Sources*.
- Berger et al. 2003, *A Common Origin for Cosmic Explosions Inferred from Calorimetry of GRB030329*.
- Racusin et al. 2008, *Broadband Observations of the Naked-Eye Gamma-Ray Burst GRB 080319B*.
- Salafia & Ghirlanda 2022, *The Structure of Gamma Ray Burst Jets*.
- Zhang 2014, *The Physics of Gamma-Ray Bursts & Relativistic Jets*.
