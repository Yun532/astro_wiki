# 08 Polarization, VLBI, and Geometric Diagnostics

状态：v0.1 课程讲义草案。本页补上 light curve / SED 之外的几何诊断：linear polarization、position angle、radio source size、centroid motion 和 apparent expansion。它们不替代 afterglow dynamics，而是为 top-hat、structured jet、two-component jet、cocoon-like outflow 和 quasi-spherical alternatives 提供额外约束。

本页原则：polarization detection 不是 jet detection；VLBI centroid motion 不是直接成像出完整喷流结构；source size 也不是自动 calorimetry。所有几何诊断都必须和 foreground correction、magnetic-field model、scintillation、EATS 和 event-level data quality 一起解释。

## 1. 物理图像

Afterglow light curve 和 SED 主要约束：

$$
E,\ n/A_\ast,\ \epsilon_e,\ \epsilon_B,\ p,\ \nu_m,\ \nu_c,\ F_{\nu,\max}.
$$

但它们通常不能唯一确定几何。一个 smooth break 可来自 jet edge、energy-injection end、density transition 或 component transition；一个 radio bump 可来自 wide component、reverse shock、SSA/scintillation 或 density structure。

Polarization / VLBI 提供不同类型的信息：

- polarization degree：emission-region asymmetry 和 magnetic-field ordering；
- position angle：sky-plane projected symmetry axis 或 ordered-field direction；
- angular size：source expansion and emitting area；
- centroid motion：off-axis bright core entering the beaming cone；
- apparent velocity：relativistic light-travel-time geometry。

## 2. 参考系与变量

| 符号 | 含义 | 单位 |
| --- | --- | --- |
| \(I,Q,U,V\) | Stokes parameters | flux-density units |
| \(\Pi_L\) | linear polarization degree | dimensionless |
| \(\chi\) | polarization position angle | rad or degree |
| \(p\) | electron power-law index | dimensionless |
| \(D_A\) | angular-diameter distance | cm |
| \(\theta_s\) | observed angular source size | rad |
| \(R_\perp\) | projected source radius / size | cm |
| \(\beta_{\rm app}\) | apparent transverse speed in units of \(c\) | dimensionless |
| \(\theta_{\rm los}\) | motion direction relative to line of sight | rad |
| \(\Delta\theta_c\) | centroid angular displacement on sky | rad |

## 3. General Expression

### 3.1 Stokes description

Observed linear polarization is computed from Stokes parameters:

$$
\Pi_L
=
{\sqrt{Q^2+U^2}\over I},
\qquad
\chi
=
{1\over2}\arctan2(U,Q).
$$

Formula ID：`POL-STOKES-001`。

For an unresolved afterglow, \(I,Q,U\) are integrals over the equal-arrival-time image:

$$
I_\nu=\int d\Omega\,I_\nu(\Omega),
$$

$$
Q_\nu=\int d\Omega\,\Pi_{\rm loc}I_\nu(\Omega)\cos2\chi(\Omega),
\qquad
U_\nu=\int d\Omega\,\Pi_{\rm loc}I_\nu(\Omega)\sin2\chi(\Omega).
$$

Formula ID：`POL-EATS-STOKES-001`。

Thus a high local synchrotron polarization can integrate to a low net polarization if opposite regions cancel.

### 3.2 VLBI observables

Projected source size:

$$
R_\perp
=
D_A\theta_s.
$$

Formula ID：`VLBI-SIZE-001`。

Centroid displacement:

$$
\Delta R_\perp
=
D_A\Delta\theta_c.
$$

Formula ID：`VLBI-CENTROID-001`。

The interpretation of \(R_\perp\) and \(\Delta R_\perp\) depends on the brightness distribution, not merely the outer shock radius.

## 4. Detailed Derivation I：Maximum Synchrotron Polarization

For optically thin synchrotron emission from a uniform magnetic field and electron distribution

$$
N(\gamma)=K\gamma^{-p},
$$

the emissivity can be decomposed into two linear polarization modes:

$$
j_\perp(\nu),\qquad j_\parallel(\nu),
$$

where the labels are relative to the projected magnetic-field direction. The polarization degree is

$$
\Pi_{\max}
=
{j_\perp-j_\parallel\over j_\perp+j_\parallel}.
$$

The same synchrotron kernel integral that gives

$$
j_\nu\propto K B_\perp^{(p+1)/2}\nu^{-(p-1)/2}
$$

also gives a fixed ratio of the two mode emissivities after integrating over electron pitch angle and energy. For a power-law electron distribution, the result is

$$
\boxed{
\Pi_{\max}
=
{p+1\over p+7/3}
}
$$

Formula ID：`POL-SYN-MAX-001`。

For \(p=2.2\),

$$
\Pi_{\max}\simeq {3.2\over4.533}\simeq0.71.
$$

This is an upper bound for a single uniform-field patch. Real afterglows often show much lower net polarization because magnetic fields are partly random and unresolved images contain many polarization angles.

## 5. Detailed Derivation II：Cancellation by Symmetry

For an unresolved image, write local polarized flux as

$$
dQ=\Pi_{\rm loc}dI\cos2\chi,
\qquad
dU=\Pi_{\rm loc}dI\sin2\chi.
$$

If the image is axisymmetric around the line of sight and the magnetic-field statistics are also symmetric, then for every patch at azimuth \(\phi\) there is a counterpart whose polarization vector cancels it. Mathematically:

$$
Q\propto\int_0^{2\pi}\cos2\chi(\phi)\,d\phi=0,
$$

$$
U\propto\int_0^{2\pi}\sin2\chi(\phi)\,d\phi=0.
$$

Formula ID：`POL-SYMMETRY-CANCEL-001`。

This is why an on-axis spherical afterglow can have bright synchrotron emission but nearly zero net polarization.

Jet geometry breaks this cancellation. When the beaming cone expands to the jet edge,

$$
\Gamma^{-1}\sim\theta_j,
$$

one side of the otherwise symmetric image is missing or dimmer, and net \(Q,U\) need not vanish. Formula ID：`POL-JET-EDGE-001`。

The sign and time evolution of \(Q,U\), including possible position-angle rotation, depends on magnetic-field geometry and viewing offset.

## 6. Detailed Derivation III：Apparent Superluminal Motion

Consider a feature moving with speed \(\beta c\) at angle \(\theta_{\rm los}\) to the line of sight. During lab-frame time interval \(\Delta t_{\rm lab}\), it moves transverse distance

$$
\Delta R_\perp
=
\beta c\Delta t_{\rm lab}\sin\theta_{\rm los}.
$$

The second photon has a shorter path by

$$
\Delta l
=
\beta c\Delta t_{\rm lab}\cos\theta_{\rm los}.
$$

Therefore the observer receives the two photons separated by

$$
\Delta t_{\rm obs}
=
(1+z)\left[
\Delta t_{\rm lab}
-
{\Delta l\over c}
\right]
=
(1+z)\Delta t_{\rm lab}(1-\beta\cos\theta_{\rm los}).
$$

The apparent transverse speed in the source frame is

$$
v_{\rm app}
=
{\Delta R_\perp\over \Delta t_{\rm obs}/(1+z)}
=
{\beta c\sin\theta_{\rm los}\over1-\beta\cos\theta_{\rm los}}.
$$

Thus

$$
\boxed{
\beta_{\rm app}
=
{\beta\sin\theta_{\rm los}\over1-\beta\cos\theta_{\rm los}}
}
$$

Formula ID：`VLBI-BETA-APP-001`。

For relativistic \(\beta\approx1\) and small nonzero \(\theta_{\rm los}\), the denominator can be very small, so \(\beta_{\rm app}>1\). This is a light-travel-time effect, not superluminal material motion.

## 7. Structured Jet and Centroid Motion

For an off-axis structured jet, early emission may be dominated by material near the line of sight. As \(\Gamma\) decreases, the bright core enters the beaming cone. The sky brightness distribution \(I_\nu(\boldsymbol\theta,t)\) changes, and the centroid

$$
\boldsymbol\theta_c(t)
=
{\int \boldsymbol\theta\,I_\nu(\boldsymbol\theta,t)\,d^2\theta
\over
\int I_\nu(\boldsymbol\theta,t)\,d^2\theta}
$$

can move on the sky. Formula ID：`VLBI-CENTROID-WEIGHT-001`。

Centroid motion is powerful because it constrains geometry differently from total flux. A quasi-spherical mildly relativistic outflow and a successful off-axis structured jet can have similar light curves, but very different centroid motion.

## 8. Source Size and Radio Calorimetry

VLBI angular size or scintillation quenching gives \(R_\perp\). Radio calorimetry then uses:

$$
R_\perp=D_A\theta_s,
$$

with SSA/source-function constraints from the previous page. This helps constrain:

- emitting volume;
- brightness temperature;
- expansion speed;
- energy budget;
- whether a wide/mild component is needed.

But \(R_\perp\) is projected size, not automatically spherical radius. For a jet, cocoon or asymmetric image, the conversion from size to energy is model-dependent.

## 9. Diagnostic Matrix

| Diagnostic | Direct observable | Main physics constrained | Caveats |
| --- | --- | --- | --- |
| polarization degree | \(\Pi_L\) | asymmetry, field ordering | foreground / host polarization |
| position angle | \(\chi(t)\) | projected symmetry axis, field geometry | 180 degree ambiguity |
| angular size | \(\theta_s\) | expansion, source area | resolution, scintillation |
| centroid motion | \(\Delta\theta_c(t)\) | off-axis geometry | requires nearby/bright source |
| apparent velocity | \(\beta_{\rm app}\) | relativistic projection | not material superluminal motion |

Formula ID：`GEOM-DIAGNOSTIC-MATRIX-001`。

## 10. Event Interpretation Boundary

GRB 030329: radio source-size constraints and calorimetry are important for late energy and geometry, but the two-component interpretation remains a model assignment.

GRB 170817A / GW170817: VLBI superluminal centroid motion is a canonical example where geometry data strongly support an off-axis successful structured jet over quasi-spherical alternatives.

GRB 221009A: bright afterglow makes polarization and geometry diagnostics valuable, but TeV, X-ray, optical and radio/mm interpretations must remain separated unless a joint model explicitly connects them.

## 11. Exact Analytic Status

| 对象 | 解析状态 | 说明 |
| --- | --- | --- |
| \(\Pi_{\max}\) for power-law synchrotron | closed | uniform field, optically thin |
| Stokes addition | exact definition | requires local \(I,Q,U\) model |
| symmetry cancellation | analytic ideal limit | broken by jet edge / viewing offset / ordered field |
| \(\beta_{\rm app}\) | closed kinematic formula | moving feature idealization |
| centroid definition | exact weighted mean | needs resolved or model image |
| full polarization light curve | numerical | EATS + magnetic-field model |
| full VLBI image evolution | numerical | hydrodynamics + radiation + image synthesis |

## 12. Approximation Hierarchy

| 层级 | 做法 | 保留 | 牺牲 |
| --- | --- | --- | --- |
| maximum patch polarization | \((p+1)/(p+7/3)\) | synchrotron upper bound | field disorder |
| Stokes cancellation | azimuthal symmetry | why net polarization can vanish | realistic image |
| jet-edge polarization intuition | broken image symmetry | relation to jet break | field model |
| apparent-speed formula | moving feature kinematics | VLBI motion intuition | brightness distribution |
| centroid model | flux-weighted image center | off-axis diagnostic | full image morphology |
| full image/polarization synthesis | hydro + EATS + polarized transfer | event comparison | model dependence |

## 13. 从推导到代码的实现约定

| Formula ID | 内容 | 代码 | 层级 |
| --- | --- | --- | --- |
| `POL-STOKES-001` | polarization degree and position angle from Stokes | theory-only | definition |
| `POL-EATS-STOKES-001` | unresolved Stokes image integral | theory-only | formal |
| `POL-SYN-MAX-001` | maximum synchrotron polarization | theory-only | course-derived |
| `POL-SYMMETRY-CANCEL-001` | axisymmetric cancellation | theory-only | course-derived |
| `POL-JET-EDGE-001` | jet-edge polarization intuition | theory-only | diagnostic |
| `VLBI-SIZE-001` | angular size to projected size | theory-only | definition |
| `VLBI-CENTROID-001` | centroid displacement to projected displacement | theory-only | definition |
| `VLBI-BETA-APP-001` | apparent transverse velocity | theory-only | course-derived |
| `VLBI-CENTROID-WEIGHT-001` | flux-weighted centroid | theory-only | formal |
| `GEOM-DIAGNOSTIC-MATRIX-001` | diagnostic matrix | theory-only | interpretation guide |

Implementation differences:

- Current local code has no polarized radiative-transfer solver.
- Current EATS helper computes toy intensity weights, not Stokes \(Q,U\).
- Current structured-jet helper has Doppler-weighted angular toy averages, not VLBI image synthesis.
- A future implementation should separate observables \(I,Q,U,\theta_s,\Delta\theta_c\) from model-inferred \(\theta_v,\theta_c,\theta_j\).

## 14. Benchmark Boundary

Polarization and VLBI benchmarks require event data and instrument-specific reductions. Published GRB 030329 radio-size studies and GRB 170817A centroid-motion analyses are mature-method references, not local validation outputs. They may calibrate interpretation language, but they do not make local theory pages into a VLBI solver.

## 15. Interfaces to Later Pages

- afterglow fitting workflow：geometry claims should ask whether polarization/VLBI/source-size evidence exists.
- event pages：must separate observed polarization/centroid/size from model-inferred jet geometry.
- high-energy afterglow：TeV brightness alone cannot determine geometry without multi-band and geometry diagnostics.

## 16. 不声称

- 不把 polarization detection 自动写成 jet detection。
- 不把 \(\Pi_{\max}\) 当成 observed polarization。
- 不把 apparent superluminal motion 写成真实超光速。
- 不把 VLBI centroid motion 写成完整喷流成像。
- 不用 light curve alone 断言 top-hat、structured jet 或 two-component jet。

## 17. 参考来源

- Rybicki & Lightman 1979, *Radiative Processes in Astrophysics*.
- Sari 1999, GRB afterglow polarization work.
- Granot & Koenigl 2003, GRB afterglow polarization and magnetic-field geometry.
- Taylor et al. 2004 / related GRB 030329 VLBI source-size studies.
- Mooley et al. 2018 / Ghirlanda et al. 2019, GW170817 / GRB 170817A VLBI centroid motion.
- Salafia & Ghirlanda 2022, *The Structure of Gamma Ray Burst Jets*.
