# 04 Jet Break, Structured Jet, and Equal-Arrival-Time Geometry

状态：v0.1 课程讲义草案。本页把 spherical-equivalent afterglow 推广到 jet geometry：先从 top-hat jet 的 beaming cone 和 jet edge 推到 jet-break condition、opening-angle scaling 和 beaming correction；再推广到 structured jet 的 angular energy profile、viewing angle 和 Doppler-weighted angular integral；最后说明 equal-arrival-time surface (EATS) 为什么是 light-curve 计算的几何核心。

本页的原则：top-hat formula 只是一个 asymptotic geometry limit；structured-jet toy integral 和 EATS helper 只是当前本地代码的 sanity layer。它们不能替代 full hydrodynamic / radiative-transfer light-curve solver。

## 1. 物理图像

前三课默认 on-axis spherical-equivalent blast wave。这个近似在早期有效，因为 relativistic beaming 只让观测者看到角尺度

$$
\theta_{\rm beam}\sim\Gamma^{-1}
$$

内的 emission。若真实 ejecta 是 half-opening angle \(\theta_j\) 的 top-hat jet，早期

$$
\Gamma^{-1}\ll\theta_j
$$

时 observer 看不到 jet edge，光变近似球对称。随着 \(\Gamma\) 下降，可见角变宽。当

$$
\Gamma(t_j)\theta_j\sim1
$$

时，jet edge 或 angular structure 开始影响 light curve，这就是 jet-break geometry 的核心入口。

## 2. 参考系与角变量

Structured jet 中必须区分三个角：

| 符号 | 含义 |
| --- | --- |
| \(\theta\) | emitting patch 相对 jet axis 的 polar angle |
| \(\phi\) | patch azimuth |
| \(\theta_v\) | observer line of sight 相对 jet axis 的 viewing angle |
| \(\psi\) | patch velocity direction 与 observer line of sight 的夹角 |
| \(\theta_j\) | top-hat half-opening angle |
| \(\theta_c\) | structured-jet core angle |

对轴对称 jet，

$$
\cos\psi
=
\cos\theta\cos\theta_v
+\sin\theta\sin\theta_v\cos\phi.
$$

Formula ID：`SJ-GEOM-001`。

## 3. General Expression

### 3.1 Angular energy profile

Top-hat jet 写作

$$
{dE\over d\Omega}(\theta)
=
\begin{cases}
\mathcal E_0, & \theta<\theta_j,\\
0, & \theta>\theta_j.
\end{cases}
$$

Structured jet 则保留

$$
\mathcal E(\theta)\equiv {dE\over d\Omega}(\theta),
\qquad
\Gamma_0=\Gamma_0(\theta).
$$

Common profiles include:

$$
\mathcal E_{\rm G}(\theta)
=
\mathcal E_c\exp\left(-{\theta^2\over2\theta_c^2}\right),
$$

and

$$
\mathcal E_{\rm PL}(\theta)
=
\mathcal E_c
\left[1+\left({\theta\over\theta_c}\right)^2\right]^{-a/2}.
$$

Formula IDs：`SJ-PROFILE-TOPHAT-001`、`SJ-PROFILE-GAUSS-001`、`SJ-PROFILE-PL-001`。

### 3.2 Doppler factor

For a patch with Lorentz factor \(\Gamma\),

$$
\delta(\theta,\phi,\theta_v)
=
{1\over\Gamma[1-\beta\cos\psi]},
\qquad
\beta=\sqrt{1-\Gamma^{-2}}.
$$

Formula ID：`SJ-DOPPLER-001`。

### 3.3 Angular flux integral

A schematic observed flux from angular patches is

$$
F_\nu(t_{\rm obs})
=
\int d\Omega\,
W_{\rm geom}(\theta,\phi,t_{\rm obs})
F_{\nu,{\rm patch}}
[
\mathcal E(\theta),\Gamma(\theta,t),n,\epsilon_e,\epsilon_B,p
].
$$

In a full calculation, \(W_{\rm geom}\) includes Doppler boosting, arrival-time constraints, surface area, spectral frequency transform, and hydrodynamic evolution. Current local code uses only a Doppler-weighted angular toy integral:

$$
\langle Q\rangle_\delta
=
{\int Q(\theta)\delta^3 d\Omega\over\int\delta^3 d\Omega}.
$$

Formula ID：`SJ-INTEGRAL-001`。

### 3.4 Equal-arrival-time relation

For emission from radius \(R\) and angle \(\psi\) relative to the observer,

$$
\Delta t_{\rm obs}
=
(1+z){R(1-\cos\psi)\over c}.
$$

Formula ID：`EATS-DELAY-001`。

A full EATS light curve uses a constraint such as

$$
t_{\rm obs}
=
(1+z)\left[t_{\rm lab}-{R\cos\psi\over c}\right]
$$

inside the volume/surface integral. The local helper currently computes a spherical on-axis Doppler-weighted toy average, not the full constrained integral.

## 4. Detailed Derivation I：Jet-Break Condition

### 4.1 Beaming cone

The Doppler factor for a patch at angle \(\psi\) is

$$
\delta={1\over\Gamma(1-\beta\cos\psi)}.
$$

For \(\Gamma\gg1\), use

$$
\beta\simeq1-{1\over2\Gamma^2},
\qquad
\cos\psi\simeq1-{\psi^2\over2}.
$$

Then

$$
1-\beta\cos\psi
\simeq
1-\left(1-{1\over2\Gamma^2}\right)
\left(1-{\psi^2\over2}\right).
$$

Keeping lowest-order terms:

$$
1-\beta\cos\psi
\simeq
{1\over2\Gamma^2}+{\psi^2\over2}.
$$

Therefore

$$
\delta
\simeq
{2\Gamma\over1+\Gamma^2\psi^2}.
$$

Emission is strongly suppressed once \(\psi\gtrsim\Gamma^{-1}\), so the visible angular cone has scale

$$
\theta_{\rm beam}\sim\Gamma^{-1}.
$$

### 4.2 Edge condition

For an on-axis top-hat observer, jet edge becomes visible when

$$
\Gamma^{-1}\sim\theta_j,
$$

or

$$
\Gamma(t_j)\theta_j\sim1.
$$

Formula ID：`AG-DYN-JET-BREAK-ENTRY-001`。

This is the robust geometry condition. The post-break slope depends on edge effect, lateral spreading, angular structure, medium, and spectral regime.

## 5. Detailed Derivation II：Opening-Angle Scaling

### 5.1 ISM

For ISM BM dynamics,

$$
\Gamma(t)
\propto
\left({E_{\rm iso}\over n}\right)^{1/8}
\left({t_{\rm obs}\over1+z}\right)^{-3/8}.
$$

At \(t_j\),

$$
\theta_j\sim\Gamma(t_j)^{-1}.
$$

Invert:

$$
\theta_j
\propto
\left({t_j\over1+z}\right)^{3/8}
\left({n\over E_{\rm iso}}\right)^{1/8}.
$$

Formula ID：`AG-JET-THETA-ISM-001`。

Common normalized forms differ by order-unity factors because \(E_{\rm iso}\) may be prompt gamma energy, kinetic energy, or efficiency-corrected energy; \(\Gamma\) may refer to shock-front or shocked-fluid Lorentz factor.

### 5.2 Wind

For wind BM dynamics,

$$
\Gamma(t)
\propto
\left({E_{\rm iso}\over A}\right)^{1/4}
\left({t_{\rm obs}\over1+z}\right)^{-1/4}.
$$

Using \(\Gamma(t_j)\theta_j\sim1\),

$$
\theta_j
\propto
\left({t_j\over1+z}\right)^{1/4}
\left({A\over E_{\rm iso}}\right)^{1/4}.
$$

Formula ID：`AG-JET-THETA-WIND-001`。

Using the wrong medium changes both exponent and inferred true energy.

## 6. Detailed Derivation III：Beaming Correction

### 6.1 Solid angle

A one-sided top-hat cone has solid angle

$$
\Omega_j
=
\int_0^{2\pi}d\phi\int_0^{\theta_j}\sin\theta\,d\theta
=
2\pi(1-\cos\theta_j).
$$

The one-sided fraction of a full sphere is

$$
f_{b,1}
=
{\Omega_j\over4\pi}
=
{1-\cos\theta_j\over2}.
$$

Many GRB papers use the practical two-sided conversion

$$
f_b
\simeq
1-\cos\theta_j.
$$

For small angle,

$$
\cos\theta_j\simeq1-{\theta_j^2\over2},
$$

so

$$
f_b\simeq{\theta_j^2\over2}.
$$

Formula ID：`AG-JET-BEAMING-FB-001`。

### 6.2 True energy

For a top-hat on-axis convention,

$$
E_{\rm true}
\simeq
f_bE_{\rm iso}.
$$

For structured jet, there is no unique sharp \(\theta_j\). The total energy is

$$
E_{\rm tot}
=
\int {dE\over d\Omega}d\Omega
=
2\pi\int_0^{\theta_{\max}}
\mathcal E(\theta)\sin\theta\,d\theta.
$$

Formula ID：`SJ-TRUE-ENERGY-001`。

If \(\mathcal E(\theta)\) has a shallow wing, \(E_{\rm tot}\) can depend strongly on \(\theta_{\max}\). Thus structured-jet true energy is profile- and cutoff-dependent.

## 7. Detailed Derivation IV：Structured-Jet Viewing Angle

### 7.1 Angular separation

For a patch direction \(\hat n(\theta,\phi)\) and observer direction \(\hat n_v\),

$$
\cos\psi
=
\hat n\cdot\hat n_v
=
\cos\theta\cos\theta_v
+\sin\theta\sin\theta_v\cos\phi.
$$

This is the geometry implemented by `angular_separation()`.

### 7.2 Doppler-weighted prompt or toy afterglow quantity

If a local quantity \(Q(\theta)\) is emitted by each patch and boosted with approximate \(\delta^3\) weight, a toy observer-dependent average is

$$
\langle Q\rangle(\theta_v)
=
{\int_0^{\theta_{\max}}\int_0^{2\pi}
Q(\theta)\delta^3(\theta,\phi,\theta_v)\sin\theta\,d\phi d\theta
\over
\int_0^{\theta_{\max}}\int_0^{2\pi}
\delta^3(\theta,\phi,\theta_v)\sin\theta\,d\phi d\theta}.
$$

This reproduces the trend that on-axis observers see bright core material more strongly than off-axis observers. It does not include hydrodynamic time evolution or EATS constraints.

### 7.3 Off-axis peak intuition

For a bright core of angular size \(\theta_c\) viewed from \(\theta_v>\theta_c\), the core becomes visible when

$$
\Gamma(t_{\rm pk})(\theta_v-\theta_c)\sim1.
$$

For ISM \(\Gamma\propto t^{-3/8}\), this gives the scale

$$
t_{\rm pk}\propto(\theta_v-\theta_c)^{8/3}
$$

at fixed energy and density.

Formula ID：`SJ-OFFAXIS-PEAK-001`。

This is only a geometric intuition. Wing emission, line-of-sight material, lateral spreading, and the profile slope can change the actual peak.

## 8. Detailed Derivation V：EATS Toy Weight

### 8.1 Delay

For a spherical shell at radius \(R\), a photon emitted at angle \(\theta\) relative to an on-axis observer travels an extra distance

$$
\Delta l
=
R(1-\cos\theta).
$$

Therefore

$$
\Delta t_{\rm obs}
=
(1+z){R(1-\cos\theta)\over c}.
$$

For small \(\theta\),

$$
\Delta t_{\rm obs}
\simeq
(1+z){R\theta^2\over2c}.
$$

### 8.2 Doppler-weighted toy average

For an azimuth-symmetric spherical shell, \(d\Omega=2\pi\sin\theta\,d\theta\). The local helper computes

$$
\langle j\rangle_{\rm toy}
=
{\int j(\theta)\delta^3(\theta)d\Omega
\over
\int \delta^3(\theta)d\Omega}.
$$

Formula ID：`EATS-WEIGHT-001`。

This is useful for geometry sanity checks: constant emissivity returns the same constant; delays are positive and increase with angle. But it is not a full EATS light curve because it does not integrate over radius, lab time, evolving emissivity, or spectral frequency transformation.

## 9. Achromatic Break and Caveats

A standard top-hat jet break is a geometry effect, so it should be approximately achromatic: several bands steepen near the same time without a spectral-index jump. Single-band steepening can instead be:

- cooling break crossing;
- end of energy injection;
- density transition;
- reverse-shock or central-engine component fading;
- structured-jet peak / component transition;
- dust or absorption correction issue.

Post-break decay \(F_\nu\propto t^{-p}\) is a useful sideways-expanding top-hat limit, not a universal law.

## 10. Exact Analytic Status

| 对象 | 解析状态 | 说明 |
| --- | --- | --- |
| beaming cone \(\theta\sim\Gamma^{-1}\) | asymptotic closed | from Doppler factor expansion |
| jet-break condition | closed geometry criterion | \(\Gamma\theta_j\sim1\) |
| ISM / wind \(\theta_j(t_j)\) scaling | closed power-law | coefficient convention-dependent |
| top-hat beaming fraction | closed | one-sided/two-sided convention must be stated |
| structured-jet total energy | angular integral | depends on profile and cutoff |
| Doppler-weighted angular average | numerical quadrature | toy; no EATS constraint |
| full structured-jet light curve | generally numerical | requires dynamics + EATS + spectrum |

## 11. Approximation Hierarchy

| 层级 | 做法 | 保留 | 牺牲 |
| --- | --- | --- | --- |
| top-hat edge criterion | \(\Gamma\theta_j\sim1\) | jet-break intuition | smooth profile/viewing angle |
| opening-angle scaling | BM \(\Gamma(t)\) inversion | quick \(\theta_j\) estimate | coefficient and medium complexity |
| beaming correction | \(E_{\rm true}=f_bE_{\rm iso}\) | energy scale | structured profile |
| angular profile | \(\mathcal E(\theta)\), \(\Gamma(\theta)\) | viewing-angle physics | radial structure |
| Doppler-weighted toy integral | \(\delta^3d\Omega\) quadrature | trend checks | hydrodynamic EATS |
| full structured-jet solver | dynamics + EATS + spectrum | light curve fitting | model dependence |

## 12. 从推导到代码的实现约定

| Formula ID | 内容 | 代码 | 层级 |
| --- | --- | --- | --- |
| `AG-DYN-JET-BREAK-ENTRY-001` | \(\Gamma\theta_j\sim1\) | theory / future jet helper | course-derived |
| `AG-JET-THETA-ISM-001` | ISM opening-angle scaling | theory-only | course-derived |
| `AG-JET-THETA-WIND-001` | wind opening-angle scaling | theory-only | course-derived |
| `AG-JET-BEAMING-FB-001` | beaming fraction | theory-only | course-derived |
| `SJ-GEOM-001` | patch-observer angle | `models/structured_jet/angular.py::angular_separation` | fixed-point |
| `SJ-DOPPLER-001` | Doppler factor | `models/structured_jet/angular.py::doppler_factor` | fixed-point |
| `SJ-PROFILE-*` | top-hat / Gaussian / power-law profiles | `models/structured_jet/angular.py` | toy / fixed-point |
| `SJ-INTEGRAL-001` | Doppler-weighted angular toy integral | `integrate_weighted_energy` | toy |
| `SJ-FLUX-TOY-001` | patch-level weighted synchrotron flux | `integrate_weighted_flux` | toy / event-trend |
| `EATS-DELAY-001` | angular delay | `core/dynamics/equal_arrival.py::angular_time_delay_s` | toy |
| `EATS-DOPPLER-001` | on-axis patch Doppler factor | `core/dynamics/equal_arrival.py::on_axis_doppler_factor` | toy |
| `EATS-WEIGHT-001` | spherical on-axis toy average | `spherical_on_axis_eats_average` | toy |

Implementation differences:

- `integrate_weighted_energy()` normalizes a \(\delta^3\)-weighted angular average; it does not return observed \(E_{\rm iso}\).
- `integrate_weighted_flux()` reuses the local synchrotron toy spectrum for each angular patch; it does not evolve each patch hydrodynamically.
- `spherical_on_axis_eats_average()` is an EATS geometry sanity helper, not a light-curve integral.
- C++ structured-jet kernels are source-level / parity candidates where toolchain permits; they are not independent physics standards.

## 13. Benchmark Boundary

`afterglowpy`, `VegasAfterglow`, BOXFIT-like hydrodynamic tables, and structured-jet numerical solvers are benchmark / mature-method layers. Agreement with them can support trend consistency under matched conventions, but cannot prove a unique viewing angle or jet structure for an event.

Current local code can claim:

- angular separation and Doppler fixed-point checks;
- Gaussian / power-law profile sanity;
- Doppler-weighted toy energy and flux trends;
- spherical on-axis EATS delay/weight sanity.

It cannot claim:

- full structured-jet afterglow fit;
- full EATS light-curve integral;
- lateral spreading hydrodynamics;
- unique beaming-corrected energy for structured jets;
- GRB 221009A viewing-angle constraint.

## 14. Interfaces to Later Pages

- Two-component jet：discrete version of angular structure.
- Density variation / energy injection：can mimic smooth breaks or plateaus.
- Polarization / VLBI：geometric diagnostics that can break viewing-angle degeneracy.
- Event workflow：must separate observation, inferred model parameter, and interpretation.

## 15. 不声称

- 不把任何 steepening 自动称为 jet break。
- 不把 top-hat \(\theta_j\) 当成 structured jet 的唯一真实角度。
- 不把 \(E_{\rm true}=f_bE_{\rm iso}\) 套到 structured jet 而不说明 profile。
- 不把 Doppler-weighted toy integral 写成 EATS solver。
- 不把 smooth peak 自动解释为 off-axis structured jet。

## 16. 参考来源

- Rhoads 1999, *The Dynamics and Light Curves of Beamed Gamma-Ray Burst Afterglows*.
- Sari, Piran & Halpern 1999, *Jets in Gamma-Ray Bursts*.
- Frail et al. 2001, *Beaming in Gamma-Ray Bursts*.
- Piran 2004, *The Physics of Gamma-Ray Bursts*.
- Zhang 2014, *The Physics of Gamma-Ray Bursts & Relativistic Jets*.
- Peng, Koenigl & Granot 2005, *Two-Component Jet Models of Gamma-Ray Burst Sources*.
- Salafia & Ghirlanda 2022, *The Structure of Gamma Ray Burst Jets*.
