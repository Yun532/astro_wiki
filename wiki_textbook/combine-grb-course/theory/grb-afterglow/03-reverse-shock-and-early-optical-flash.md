# 03 Reverse Shock and Early Optical Flash

状态：v0.1 课程讲义草案。本页把 forward-shock afterglow onset 扩展到 reverse shock：从四区结构、ejecta shell 宽度、deceleration condition 和 crossing time 出发，推导 thin/thick shell 判据，并解释 crossing 附近常用的 reverse / forward synchrotron scale relations。它是早期 optical flash / radio flare 的理论入口，不是完整 reverse-shock hydrodynamic solver。

## 1. 物理图像

Relativistic ejecta 撞入 circumburst medium 后会形成双激波结构：

```text
region 1: unshocked external medium
region 2: forward-shocked external medium
contact discontinuity
region 3: reverse-shocked ejecta
region 4: unshocked ejecta
```

Forward shock 向外扫过 external medium，长期 afterglow 主体通常来自 region 2。Reverse shock 向内穿过 ejecta，直接探测 ejecta 的 Lorentz factor、shell thickness、magnetization 和 baryon loading。它常在 shock crossing time 附近最亮，随后因为没有新的 ejecta 被 shock 加热而快速衰减。

重要边界：early optical peak 不自动等于 reverse shock。Forward-shock onset、prompt optical、density variation、energy injection、structured jet 和 extra component 都可产生 early bump。

## 2. 参考系与变量表

默认使用 observer time \(t_{\rm obs}\)，并显式保留 redshift factor。若使用 source-frame duration，必须先除以 \(1+z\)。

| 符号 | 含义 | 约定 |
| --- | --- | --- |
| \(E\) | isotropic-equivalent kinetic energy | erg |
| \(\Gamma_0\) | initial ejecta Lorentz factor | coasting shell |
| \(\Gamma_\times\) | bulk Lorentz factor at shock crossing | often \(\sim\Gamma_0/2\) in thin shell |
| \(T\) | prompt / engine duration | must specify observer/source frame |
| \(\Delta_0\) | lab-frame shell width | \(\sim cT/(1+z)\) if \(T\) is observed |
| \(t_{\rm dec}\) | observer-frame deceleration time | onset scale |
| \(t_\times\) | reverse-shock crossing time | \(\sim\max(T,t_{\rm dec})\) |
| \(A\) | wind mass parameter | \(A=5\times10^{11}A_\ast{\rm g\,cm^{-1}}\) |
| \(\sigma\) | ejecta magnetization | model-dependent |

## 3. General Expression

### 3.1 Deceleration condition

Deceleration begins when swept-up external matter carries a lab-frame energy comparable to the ejecta kinetic energy:

$$
\Gamma_0^2m_{\rm sw}(R_{\rm dec})c^2
\sim
E.
$$

For a power-law external medium,

$$
m_{\rm sw}(R)
=
\int_0^R4\pi r^2\rho_{\rm ext}(r)dr.
$$

This condition is the same onset scale used by the forward-shock dynamics page; reverse shock uses it to decide when the ejecta shell is substantially processed.

### 3.2 Shell crossing

The reverse shock crossing time is the time when the reverse shock finishes crossing region 4. A first asymptotic estimate is

$$
t_\times
\sim
\max(T,t_{\rm dec}),
$$

where \(T\) and \(t_{\rm dec}\) must use the same observer/source-frame convention.

Formula ID：`RS-CROSS-001`。

### 3.3 Reverse-shock emission as a distribution integral

The reverse-shock synchrotron spectrum is not fundamentally a new radiation mechanism. In region 3,

$$
j'_{\nu',r}
=
{1\over4\pi}
\int_{\gamma_{m,r}}^\infty
N'_r(\gamma_e)P'_{\nu'}(\gamma_e,B'_r)d\gamma_e.
$$

The differences from forward shock enter through \(N'_r\), \(\gamma_{m,r}\), \(B'_r\), shell geometry, crossing history, and magnetization. Therefore the common \(\nu_{m,r}\sim\Gamma_0^{-2}\nu_{m,f}\) and \(F_{\nu,\max,r}\sim\Gamma_0F_{\nu,\max,f}\) relations must be understood as crossing-time scale estimates, not exact spectra.

## 4. Detailed Derivation I：ISM Deceleration Time

### 4.1 目标公式

For uniform ISM, the code and many textbook estimates use

$$
t_{\rm dec,ISM}
\sim
(1+z)
\left(
{3E\over32\pi n m_pc^5\Gamma_0^8}
\right)^{1/3}.
$$

Formula ID：`RS-TDEC-ISM-001`。

### 4.2 Swept-up mass

For ISM,

$$
\rho_{\rm ext}=nm_p,
\qquad
m_{\rm sw}(R)
=
{4\pi\over3}R^3nm_p.
$$

Insert this into the deceleration condition:

$$
\Gamma_0^2
\left({4\pi\over3}R_{\rm dec}^3nm_p\right)c^2
\sim
E.
$$

Solve for \(R_{\rm dec}\):

$$
R_{\rm dec}^3
\sim
{3E\over4\pi n m_pc^2\Gamma_0^2},
$$

so

$$
R_{\rm dec}
\sim
\left(
{3E\over4\pi n m_pc^2\Gamma_0^2}
\right)^{1/3}.
$$

### 4.3 Arrival-time mapping

Use the onset convention

$$
t_{\rm dec}
\sim
(1+z){R_{\rm dec}\over C_t c\Gamma_0^2}.
$$

If \(C_t=2\), then

$$
t_{\rm dec}
\sim
{1+z\over2c\Gamma_0^2}
\left(
{3E\over4\pi n m_pc^2\Gamma_0^2}
\right)^{1/3}.
$$

Collect powers:

$$
t_{\rm dec}
\sim
(1+z)
\left(
{3E\over32\pi n m_pc^5\Gamma_0^8}
\right)^{1/3}.
$$

The numerical coefficient changes if the arrival-time factor is 4 or a BM self-similar coefficient. The local `deceleration_time_s(..., medium="ism")` adopts the \(32\pi\) convention above as a literature-scale fixed point.

## 5. Detailed Derivation II：Wind Deceleration Time

### 5.1 目标公式

For wind medium,

$$
\rho_{\rm ext}=AR^{-2},
\qquad
A=5\times10^{11}A_\ast{\rm\,g\,cm^{-1}},
$$

the common observer-frame estimate is

$$
t_{\rm dec,wind}
\sim
(1+z){E\over8\pi Ac^3\Gamma_0^4}.
$$

Formula ID：`RS-TDEC-WIND-001`。

### 5.2 Swept-up mass

For wind,

$$
m_{\rm sw}(R)
=
\int_0^R4\pi r^2Ar^{-2}dr
=
4\pi AR.
$$

Insert into deceleration condition:

$$
\Gamma_0^2(4\pi AR_{\rm dec})c^2
\sim
E.
$$

Thus

$$
R_{\rm dec}
\sim
{E\over4\pi Ac^2\Gamma_0^2}.
$$

Using

$$
t_{\rm dec}
\sim
(1+z){R_{\rm dec}\over2c\Gamma_0^2}
$$

gives

$$
t_{\rm dec,wind}
\sim
(1+z){E\over8\pi Ac^3\Gamma_0^4}.
$$

Wind deceleration depends more weakly on \(\Gamma_0\) than ISM in radius, but \(t_{\rm dec}\) still has a steep \(\Gamma_0^{-4}\) dependence.

## 6. Detailed Derivation III：Thin and Thick Shells

### 6.1 Shell width

If the central engine is active for source-frame duration \(T_{\rm src}\), the lab-frame shell width is approximately

$$
\Delta_0\sim cT_{\rm src}.
$$

If the observed duration is \(T_{\rm obs}\), then

$$
T_{\rm src}={T_{\rm obs}\over1+z},
\qquad
\Delta_0\sim {cT_{\rm obs}\over1+z}.
$$

### 6.2 Crossing-time estimate

The reverse shock must cross the shell. Two limiting timescales compete:

- the blast wave deceleration time \(t_{\rm dec}\);
- the shell duration \(T\), i.e. the time for the engine to deliver the whole shell.

Thus

$$
t_\times
\sim
\max(T,t_{\rm dec}).
$$

### 6.3 Regimes

Define the qualitative shell classifier:

$$
\begin{cases}
T<t_{\rm dec}: & \hbox{thin shell},\\
T\ge t_{\rm dec}: & \hbox{thick shell}.
\end{cases}
$$

Formula ID：`RS-SHELL-001`。

In thin shell, the reverse shock crosses near deceleration and is often Newtonian or mildly relativistic in the shell frame. In thick shell, crossing happens while the prompt-duration shell is still dynamically important, and the reverse shock can be relativistic.

This is a regime classifier, not a hydrodynamic solution. A real shell may have Lorentz-factor stratification, spreading, magnetization, and refreshed material.

## 7. Detailed Derivation IV：Reverse / Forward Synchrotron Scale Relations

### 7.1 Pressure balance at contact discontinuity

Regions 2 and 3 share a contact discontinuity. In a simple baryonic, weakly magnetized crossing-time estimate, their pressures are comparable:

$$
e'_r\sim e'_f.
$$

If the microphysical parameters are also comparable,

$$
\epsilon_{B,r}\sim\epsilon_{B,f},
$$

then

$$
B'_r\sim B'_f.
$$

If ejecta magnetization is important, this relation can fail.

### 7.2 Electron Lorentz factor ratio

Forward-shock electrons are heated by a relative Lorentz factor of order \(\Gamma_\times\) against cold external medium:

$$
\gamma_{m,f}
\sim
{p-2\over p-1}\epsilon_{e,f}{m_p\over m_e}\Gamma_\times.
$$

Reverse-shock electrons are heated by the relative Lorentz factor between unshocked ejecta and shocked ejecta, denoted \(\Gamma_{34}\):

$$
\gamma_{m,r}
\sim
{p-2\over p-1}\epsilon_{e,r}{m_p\over m_e}(\Gamma_{34}-1).
$$

For the standard thin-shell crossing estimate,

$$
\Gamma_\times\sim{\Gamma_0\over2},
\qquad
\Gamma_{34}-1
\sim
O(1).
$$

Therefore

$$
{\gamma_{m,r}\over\gamma_{m,f}}
\sim
{\epsilon_{e,r}\over\epsilon_{e,f}}
{1\over\Gamma_0}
$$

up to order-unity factors.

### 7.3 Injection-frequency ratio

Since

$$
\nu_m\propto \Gamma B'\gamma_m^2,
$$

and both shocked regions share the same bulk \(\Gamma_\times\), we get

$$
{\nu_{m,r}\over\nu_{m,f}}
\sim
{B'_r\over B'_f}
\left({\gamma_{m,r}\over\gamma_{m,f}}\right)^2.
$$

For similar microphysics and \(B'_r\sim B'_f\),

$$
\nu_{m,r}
\sim
\Gamma_0^{-2}\nu_{m,f}.
$$

Formula ID：`RS-NU-M-001`。

This is why reverse shock is naturally bright at lower frequencies than forward shock.

### 7.4 Peak-flux ratio

At deceleration, swept-up external mass is

$$
m_{\rm sw}\sim {E\over\Gamma_0^2c^2}.
$$

The number of forward-shocked external electrons is

$$
N_{e,f}\sim {m_{\rm sw}\over m_p}
\sim
{E\over\Gamma_0^2m_pc^2}.
$$

The ejecta baryonic mass associated with kinetic energy \(E\) is approximately

$$
M_{\rm ej}\sim {E\over\Gamma_0c^2}.
$$

Thus the number of reverse-shocked ejecta electrons is

$$
N_{e,r}\sim {M_{\rm ej}\over m_p}
\sim
{E\over\Gamma_0m_pc^2}.
$$

Therefore

$$
{N_{e,r}\over N_{e,f}}
\sim
\Gamma_0.
$$

Because

$$
F_{\nu,\max}\propto N_e\Gamma B',
$$

and \(\Gamma\), \(B'\) are comparable at contact under simple assumptions,

$$
F_{\nu,\max,r}
\sim
\Gamma_0F_{\nu,\max,f}.
$$

Formula ID：`RS-FMAX-001`。

This relation is a crossing-time scale, not a full light curve. It changes if ejecta magnetization, pair loading, \(\epsilon_{B,r}/\epsilon_{B,f}\), \(\epsilon_{e,r}/\epsilon_{e,f}\), or shell stratification differs.

## 8. Early Optical Flash and Radio Flare

### 8.1 Optical flash

The optical flash is expected when \(\nu_{m,r}\) and \(F_{\nu,\max,r}\) place the reverse-shock spectrum near optical at \(t_\times\). A practical diagnostic requires:

- peak time close to \(t_\times\);
- post-peak decay steeper than forward-shock closure expectation;
- spectral component distinct from prompt optical if prompt overlap exists;
- forward-shock component able to explain later afterglow;
- no simpler explanation from density bump, energy injection, or structured jet.

### 8.2 Radio flare

Because \(\nu_{m,r}\) is lower and decreases after crossing, reverse shock can appear later as a radio flare. Radio interpretation must check:

- self-absorption \(\nu_a\);
- scintillation;
- source size;
- overlap with forward-shock radio rise;
- possible wide-component or refreshed-shock contribution.

Current local code maps reverse-shock crossing scales into the shared synchrotron spectrum API. That is a toy spectral interface, not a radio transfer solution.

## 9. Magnetization Boundary

Ejecta magnetization is often represented by a dimensionless parameter

$$
\sigma
\equiv
{L_{\rm Poynting}\over L_{\rm matter}}.
$$

Low \(\sigma\) baryonic ejecta generally allow a stronger reverse shock. High \(\sigma\) can weaken or suppress reverse shock, while moderate ordered magnetic field may increase polarization or modify brightness. The absence of optical flash is therefore not proof of no ejecta; it may reflect magnetization, extinction, cadence, or unfavorable spectral placement.

The present course page does not solve relativistic MHD shock jump conditions. It only records where magnetization breaks the baryonic toy scalings.

## 10. Exact Analytic Status

| 对象 | 解析状态 | 说明 |
| --- | --- | --- |
| \(R_{\rm dec}\), \(t_{\rm dec}\) in ISM/wind | closed scale | coefficient depends on arrival-time convention |
| shell regime \(T\lessgtr t_{\rm dec}\) | classifier | not hydrodynamic crossing solution |
| \(t_\times\sim\max(T,t_{\rm dec})\) | asymptotic estimate | ignores shell structure and spreading |
| \(\nu_{m,r}/\nu_{m,f}\sim\Gamma_0^{-2}\) | crossing-time scale | assumes similar microphysics and weak magnetization |
| \(F_{\nu,\max,r}/F_{\nu,\max,f}\sim\Gamma_0\) | crossing-time scale | assumes baryonic ejecta and comparable \(B'\) |
| reverse-shock light curve after crossing | generally not closed | depends on hydrodynamics, curvature, cooling, SSA |
| magnetized reverse shock | requires MHD treatment | not implemented here |

## 11. Approximation Hierarchy

| 层级 | 做法 | 保留 | 牺牲 |
| --- | --- | --- | --- |
| deceleration scale | \(m_{\rm sw}\sim E/(\Gamma_0^2c^2)\) | onset time | shock structure |
| shell classifier | \(T<t_{\rm dec}\) vs \(T\ge t_{\rm dec}\) | thin/thick intuition | exact crossing dynamics |
| crossing-time scale | \(t_\times=\max(T,t_{\rm dec})\) | optical-flash timing | detailed hydrodynamic profile |
| reverse/forward ratios | \(\nu_{m,r}\sim\Gamma_0^{-2}\nu_{m,f}\), \(F_{\max,r}\sim\Gamma_0F_{\max,f}\) | quick spectral placement | microphysics and magnetization |
| shared synchrotron toy spectrum | map scales to `SpectralBreaks` | sanity flux | full reverse-shock spectrum |
| numerical RS/MHD model | solve shell and shock evolution | realistic light curves | code/model dependence |

## 12. 从推导到代码的实现约定

| Formula ID | 内容 | 代码 | 层级 |
| --- | --- | --- | --- |
| `RS-TDEC-ISM-001` | ISM deceleration time | `models/reverse_shock/analytic.py::deceleration_time_s` | fixed-point / toy |
| `RS-TDEC-WIND-001` | wind deceleration time | `models/reverse_shock/analytic.py::deceleration_time_s` | fixed-point / toy |
| `RS-SHELL-001` | thin/thick shell classifier | `models/reverse_shock/analytic.py::shell_regime` | teaching-code |
| `RS-CROSS-001` | \(t_\times\simeq\max(T,t_{\rm dec})\) | `models/reverse_shock/analytic.py::crossing_time_s` | teaching-code |
| `RS-NU-M-001` | reverse injection frequency scale | `models/reverse_shock/analytic.py::reverse_scales_from_forward` | toy-model |
| `RS-FMAX-001` | reverse peak flux scale | `models/reverse_shock/analytic.py::reverse_scales_from_forward` | toy-model |
| `RS-SPEC-TOY-001` | reverse scales mapped to shared spectrum API | `spectral_breaks_from_reverse`, `reverse_flux_density` | toy-model |

Implementation differences:

- `deceleration_time_s()` uses the \(C_t=2\) / \(32\pi\) ISM convention.
- `shell_regime()` compares supplied `duration_s` and `deceleration_time`; it does not infer source-frame vs observer-frame duration.
- `reverse_scales_from_forward()` assumes \(\Gamma_\times=0.5\Gamma_0\), \(\nu_{c,r}=\nu_{c,f}\), \(\nu_{m,r}=\Gamma_0^{-2}\nu_{m,f}\), and \(F_{\max,r}=\Gamma_0F_{\max,f}\).
- `reverse_flux_density()` uses the shared sharp/smooth synchrotron toy API. It does not calculate reverse-shock hydrodynamic decay, self-absorption, or magnetized ejecta.

## 13. Benchmark Boundary

Mature reverse-shock modeling may use hydrodynamic shell evolution, radiative transfer, magnetized shock jump conditions, or full forward+reverse decomposition. Those can be benchmark / mature-method comparisons, but not a replacement for the course assumptions.

Current local code can claim:

- deceleration time and shell classification fixed-point sanity;
- crossing-time reverse/forward scale mapping;
- toy optical/radio flux through shared synchrotron API.

It cannot claim:

- detection or exclusion of reverse shock in any event;
- full reverse-shock light curve;
- full radio self-absorption treatment;
- magnetized reverse-shock solution;
- prompt optical interpretation.

## 14. Interfaces to Later Pages

- Jet / structured jet：early bumps can be angular-structure effects rather than reverse shock.
- EATS：post-crossing decay and curvature require equal-arrival-time treatment.
- Particle acceleration：reverse shock probes ejecta composition and magnetic fields.
- Event workflow：early optical/radio diagnostics must be compared with forward shock, prompt emission, SSC, and extra components.

## 15. 不声称

- 不把 early optical peak 自动命名为 reverse shock。
- 不把 lack of optical flash 当成 lack of ejecta。
- 不把 \(t_\times=\max(T,t_{\rm dec})\) 写成 exact crossing solution。
- 不把 \(\nu_{m,r}\) 和 \(F_{\max,r}\) 的 crossing-time ratios 写成 full light-curve model。
- 不把 GRB 990123、GRB 080319B 或 GRB 221009A 的某个解释写成唯一答案。

## 16. 参考来源

- Sari & Piran, early afterglow / reverse shock optical flash papers.
- Kobayashi 2000, *Light Curves of Gamma-Ray Burst Optical Flashes*.
- Zhang, Kobayashi & Mészáros, reverse shock and magnetized ejecta work.
- Piran 2004, *The Physics of Gamma-Ray Bursts*.
- Zhang 2014, *The Physics of Gamma-Ray Bursts & Relativistic Jets*.
- Racusin et al. 2008, GRB 080319B broadband observations.
