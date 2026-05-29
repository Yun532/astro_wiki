# 13 事件解释链

状态：v0.1 课程讲义草稿。本页不是事件拟合报告，也不是 afterglow package 使用手册。它把 01-12 页的动力学、辐射机制、几何诊断、高能过程和 cascade boundary 收束成一条可审计的解释链：从观测量出发，逐层进入模型假设，再说明哪些结论可以声称，哪些只能作为候选。

核心原则：不要把一个最优拟合参数表、一个 benchmark package output、一个 closure relation 或一个 TeV photon 单独写成物理结论。GRB afterglow interpretation 应该是一组条件判断和残差解释，而不是单公式判案。

## 1. 物理图像

一个 afterglow event interpretation 至少经过四层：

```text
observed data
  -> derived local diagnostics
  -> model assumptions and forward prediction
  -> interpretation claims with boundaries
```

其中 observed data 包括 fluxes、upper limits、spectra、polarization、VLBI size/centroid、TeV photons、redshift 和 host constraints。Derived local diagnostics 包括 local temporal slope \(\alpha\)、spectral slope \(\beta\)、closure residual、break time、source-frame frequency / time、SED curvature 和 high-energy attenuation hints。Model assumptions 包括 external density profile、jet geometry、microphysics、energy injection、SSC / KN cooling、hadronic / cascade boundary 和 propagation model。Interpretation claims 则必须区分：

| Claim type | 可以说什么 | 不能说什么 |
| --- | --- | --- |
| consistency | 某模型在 stated assumptions 下不矛盾 | 唯一起源 |
| tension | 某 closure / SED / geometry diagnostic 有残差 | 该机制被完全排除 |
| preference | 在同一数据和同一复杂度惩罚下更优 | 物理真实性已证明 |
| benchmark parity | 与某外部包同 convention 一致 | 外部包就是理论证明 |
| missing boundary | 当前代码没有求解 | 该物理过程不存在 |

Formula ID：`AG-INTERP-CLAIM-CLASS-001`。

## 2. 参考系、数据向量与模型向量

令观测数据向量为

$$
\mathcal{D}
=
\{t_i,\nu_i,F_{\nu,i},\sigma_i,\mathcal{U}_j,
P_k,\theta_{{\rm VLBI},l},E_{{\rm HE},m},z,\ldots\},
$$

其中 \(\mathcal{U}_j\) 表示 upper limits，\(P_k\) 表示 polarization / Stokes-derived quantities，\(\theta_{\rm VLBI}\) 表示角尺寸或质心位移，\(E_{\rm HE}\) 表示 GeV-TeV events 或 high-energy flux points。

Formula ID：`AG-INTERP-DATA-VECTOR-001`。

模型不是一个参数表，而是参数和假设的组合：

$$
\mathcal{M}
=
\{\Theta_{\rm dyn},\Theta_{\rm rad},\Theta_{\rm geom},
\Theta_{\rm ext},\Theta_{\rm HE},\mathcal{A}\}.
$$

Here

| Block | Examples |
| --- | --- |
| \(\Theta_{\rm dyn}\) | \(E_{\rm iso},n/A_\ast,k,\Gamma_0,t_{\rm dec}\) |
| \(\Theta_{\rm rad}\) | \(p,\epsilon_e,\epsilon_B,\xi_e,Y,\nu_a,\nu_m,\nu_c,F_{\nu,\max}\) |
| \(\Theta_{\rm geom}\) | \(\theta_j,\theta_c,\theta_v,\mathcal{E}(\theta)\), EATS prescription |
| \(\Theta_{\rm ext}\) | energy injection, density perturbation, two-component decomposition |
| \(\Theta_{\rm HE}\) | SSC / KN / \(\gamma\gamma\) / hadronic / cascade / EBL assumptions |
| \(\mathcal{A}\) | approximation layer: analytic, semi-analytic, toy code, production code, benchmark-output |

Formula ID：`AG-INTERP-MODEL-VECTOR-001`。

## 3. 一般表达式：forward model 与 evidence chain

A forward model predicts data-space quantities:

$$
\hat{\mathcal{D}}
=
\mathcal{F}(\mathcal{M}).
$$

For flux data with Gaussian errors, a local likelihood contribution is

$$
\ln \mathcal{L}_{\rm det}
=
-{1\over2}
\sum_i
\left[
{F_{\nu,i}-F_\nu(t_i,\nu_i|\mathcal{M})\over\sigma_i}
\right]^2
+{\rm const}.
$$

For upper limits \(F_{\nu,j}<F_{{\rm lim},j}\), the likelihood is one-sided:

$$
\mathcal{L}_{\rm ul}
=
\prod_j
\Phi\left(
{F_{{\rm lim},j}-F_\nu(t_j,\nu_j|\mathcal{M})\over\sigma_j}
\right),
$$

where \(\Phi\) is the standard normal CDF if the limit is Gaussian. A hard cut \(F_\nu<F_{\rm lim}\) is a different convention and must be labeled.

Formula ID：`AG-INTERP-FORWARD-LIKELIHOOD-001`。

This expression is not asking every course page to implement an inference engine. It states the direction of reasoning:

```text
assumptions -> predicted observables -> residuals -> bounded claims
```

not

```text
desired mechanism -> selected formula -> conclusion
```

## 4. 详细推导 I：local diagnostic slopes

In a small time-frequency patch, write the observed flux as

$$
F_\nu(t,\nu)
=
F_0
\left({t\over t_0}\right)^{-\alpha}
\left({\nu\over\nu_0}\right)^{-\beta}.
$$

Taking logarithms gives

$$
\ln F_\nu
=
\ln F_0
-\alpha\ln{t\over t_0}
-\beta\ln{\nu\over\nu_0}.
$$

Thus a local temporal slope at fixed band is

$$
\alpha_{\rm loc}
=
-
{\partial\ln F_\nu\over\partial\ln t},
$$

and a local spectral slope at fixed epoch is

$$
\beta_{\rm loc}
=
-
{\partial\ln F_\nu\over\partial\ln \nu}.
$$

Formula ID：`AG-INTERP-LOCAL-SLOPE-001`。

These are diagnostics, not model parameters by themselves. If a spectral break crosses the band, if host extinction or absorption is important, or if two components overlap, a single \(\alpha,\beta\) pair can be misleading.

## 5. 详细推导 II：closure gate

A closure relation predicts

$$
\alpha_{\rm th}
=
\alpha_{\rm th}(\beta;k,{\rm segment},{\rm dynamics}).
$$

Define the closure residual

$$
\boxed{
\Delta_{\rm cl}
=
\alpha_{\rm obs}-\alpha_{\rm th}.
}
$$

Formula ID：`AG-INTERP-CLOSURE-GATE-001`。

For example, in the ISM, adiabatic, pre-jet, slow-cooling segment \(\nu_m<\nu<\nu_c\),

$$
\alpha_{\rm th}
=
{3(p-1)\over4},
\qquad
\beta
=
{p-1\over2}.
$$

Eliminate \(p\):

$$
p=2\beta+1,
$$

so

$$
\alpha_{\rm th}
=
{3\beta\over2}.
$$

The closure residual is therefore

$$
\Delta_{\rm cl}
=
\alpha_{\rm obs}-{3\beta_{\rm obs}\over2}.
$$

If \(\Delta_{\rm cl}\neq0\), the next step is not automatically "standard afterglow fails". It may indicate wrong spectral segment, wind medium, energy injection, jet break, two components, SSC cooling, evolving microphysics, density structure, extinction/systematics, or a high-energy process contaminating the band.

## 6. 详细推导 III：break-ordering gate

Synchrotron interpretation requires the observed band ordering to be stated:

$$
\nu_a(t),\nu_m(t),\nu_c(t)
\quad{\rm versus}\quad
\nu_{\rm radio},\nu_{\rm opt},\nu_{\rm X},\nu_{\rm GeV}.
$$

A model should predict a segment label

$$
s_i
=
{\rm segment}[\nu_i;\nu_a(t_i),\nu_m(t_i),\nu_c(t_i)].
$$

Formula ID：`AG-INTERP-BREAK-ORDER-GATE-001`。

If the assumed segment changes, both \(\alpha_{\rm th}\) and \(\beta_{\rm th}\) change. Therefore a fit that quotes \(p\) from \(\beta\) must also quote the segment:

$$
p=
\begin{cases}
2\beta+1, & \nu_m<\nu<\nu_c,\\
2\beta, & \nu>\nu_c,
\end{cases}
$$

for slow cooling. Without the segment label, \(p\) is not an interpretable physical inference.

## 7. 详细推导 IV：multi-band residual decomposition

Suppose a baseline forward-shock model predicts \(F_{\nu,{\rm FS}}\). Define residuals in log flux:

$$
r_i
=
\ln F_{\nu,i}
-\ln F_{\nu,{\rm FS}}(t_i,\nu_i).
$$

Formula ID：`AG-INTERP-MULTIBAND-RESIDUAL-001`。

The residual pattern matters more than a single bad point:

| Residual pattern | Candidate interpretation | Boundary |
| --- | --- | --- |
| radio/mm excess only | SSA/source-size issue, reverse shock, wide component, density structure | not automatically two-component jet |
| optical bump | reverse shock, refreshed shock, density variation, SN/host contribution | needs color and timing |
| X-ray excess over optical closure | IC cooling, separate component, absorption/systematics | not automatically SSC |
| GeV-TeV excess | SSC, external IC, extreme synchrotron, hadronic/cascade | requires KN and opacity checks |
| achromatic steepening | jet break candidate | must test spectral regime and geometry |
| chromatic break | spectral-break crossing or multi-component behavior | not a clean jet break |

A two-component residual model is

$$
F_\nu
=
F_{\nu,1}+F_{\nu,2}.
$$

The observed local slope is a flux-weighted mixture:

$$
\alpha_{\rm obs}
=
{\alpha_1F_{\nu,1}+\alpha_2F_{\nu,2}\over F_{\nu,1}+F_{\nu,2}}.
$$

This means an apparently shallow or steep slope can be produced by component mixing without changing the microphysics of either component.

## 8. Geometry Gate: Jet, Viewing Angle, Polarization, VLBI

Geometry claims should combine independent observables. A top-hat jet-break entry is only

$$
\Gamma(t_j)\theta_j\sim1.
$$

Formula ID：`AG-INTERP-GEOMETRY-GATE-001`。

For structured or off-axis jets, the relevant parameters are not just \(\theta_j\), but

$$
\Theta_{\rm geom}
=
\{\theta_c,\theta_w,\theta_v,\mathcal{E}(\theta),\Gamma_0(\theta),{\rm EATS}\}.
$$

Polarization and VLBI add orthogonal diagnostics:

$$
\Pi_L={\sqrt{Q^2+U^2}\over I},
\qquad
\beta_{\rm app}
=
{\beta\sin\theta\over1-\beta\cos\theta}.
$$

But each diagnostic has a boundary:

- polarization depends on magnetic-field geometry and image symmetry;
- VLBI centroid motion depends on brightness distribution, not only shock radius;
- jet-break time depends on density profile, lateral spreading convention and viewing geometry;
- two-component decomposition is a model basis, not a unique physical structure.

Therefore a geometry claim should be written as a matrix of constraints, not as one inferred angle.

## 9. High-Energy Gate: SSC, KN, Opacity, Hadronic Boundary

For a high-energy component, the interpretation chain should ask:

1. Can electron synchrotron reach the observed photon energy under the burnoff bound?
2. If SSC is invoked, is the scattering in Thomson or KN regime?
3. Does SSC cooling alter \(\gamma_c\), \(\nu_c\) and closure interpretation?
4. Is the source internally transparent to \(\gamma\gamma\)?
5. Is EBL attenuation modeled externally and stated?
6. If hadronic/cascade is invoked, are acceleration feasibility, target field, secondary cooling and cascade transport specified?

Formula ID：`AG-INTERP-HE-GATE-001`。

The minimum TeV interpretation expression is not a spectrum; it is a checklist:

$$
\mathcal{C}_{\rm HE}
=
\{
E_{\gamma,\rm obs},
\gamma_{\max},
Y(\gamma),
b_{\rm KN},
\tau_{\gamma\gamma}^{\rm int},
\tau_{\rm EBL},
{\rm cascade\ treatment}
\}.
$$

Formula ID：`AG-INTERP-TEV-CHECKLIST-001`。

If any of these entries is missing, the event report can still say "candidate" or "sanity check", but should not say "origin proven".

## 10. Complexity ladder 与 claim discipline

A useful model ladder is:

| Level | Model class | Allowed claim |
| --- | --- | --- |
| 0 | local slopes and SED diagnostics | descriptive trend |
| 1 | standard FS synchrotron closure | consistency / tension |
| 2 | FS with wind/ISM and break ordering | environment-dependent consistency |
| 3 | energy injection or density variation | extended-dynamics candidate |
| 4 | jet / structured jet / EATS | geometry candidate |
| 5 | reverse shock / two components | component-decomposition candidate |
| 6 | SSC / KN / \(\gamma\gamma\) | high-energy leptonic candidate |
| 7 | hadronic / cascade / neutrino | high-energy non-leptonic boundary or candidate |
| 8 | full numerical hydrodynamics / transport / inference | model-comparison result under stated priors |

Formula ID：`AG-INTERP-COMPLEXITY-LADDER-001`。

The ladder is not a ranking of physical truth. It is a reporting discipline: do not jump to Level 7 claims when the calculation only reached Level 2 diagnostics.

## 11. 精确解析状态

| Object | Analytic status | Comment |
| --- | --- | --- |
| source-frame conversion | closed | requires trigger and redshift convention |
| local \(\alpha,\beta\) | diagnostic estimate | affected by breaks and systematics |
| simple closure relations | closed asymptotic limits | require segment and dynamics assumptions |
| break ordering | semi-analytic in simple FS | full spectra require smooth transfer |
| multi-band residuals | diagnostic | not a unique decomposition |
| jet-break angle | closed scaling in top-hat limits | structured/off-axis needs model |
| polarization/VLBI constraints | formal definitions | image synthesis needed for full inference |
| SSC / TeV interpretation | mixed analytic/numerical | KN and opacity often numerical |
| hadronic/cascade interpretation | generally numerical | current local code lacks full solver |
| event-level inference | statistical / numerical | prior and likelihood choices matter |

## 12. 近似层级

| Layer | Starting point | What it can support | What it cannot support |
| --- | --- | --- | --- |
| diagnostic | \(\alpha,\beta\), SED, residuals | segment and tension hints | unique model |
| analytic closure | asymptotic FS formulas | quick consistency checks | broadband fit |
| semi-analytic light curve | break evolution and components | trend comparison | full hydro/EATS proof |
| numerical forward model | package or local solver | convention-stated prediction | truth without priors |
| benchmark-output | external package parity | implementation check | physical proof |
| full inference | likelihood + priors + model comparison | quantified preference | assumption-free conclusion |

Formula ID：`AG-INTERP-APPROX-HIERARCHY-001`。

## 13. 从推导到代码的实现约定

Relevant existing local code and reports:

```text
reproduce/grb/models/forward_shock/
reproduce/grb/models/reverse_shock/
reproduce/grb/models/structured_jet/
reproduce/grb/core/dynamics/
reproduce/grb/core/radiation/
reproduce/grb/events/grb_221009a/scripts/
reproduce/grb/validation_lab/
```

当前实现状态：

| Layer | Local status | Boundary |
| --- | --- | --- |
| closure / break helpers | partial code-backed | asymptotic, not full inference |
| reverse shock | toy scales | not hydrodynamic light curve |
| structured jet / EATS | geometry and weighted toy helpers | not full structured-jet solver |
| fitting workflow | reports and diagnostics | not MCMC pipeline |
| SSC / TeV | toy feedback, tabulated SSC, opacity sanity | not full EATS-integrated TeV transfer |
| acceleration | source-agnostic screening helpers plus theory boundary | no full afterglow maximum-energy solver |
| cascade / neutrino | theory-only boundary | no full cascade or event-rate predictor |

Formula ID：`AG-INTERP-CODE-LAYER-MAP-001`。

If code and course diverge, the report must say which object changed:

$$
\text{course expression}
\rightarrow
\text{implemented approximation}
\rightarrow
\text{validated fixed point / benchmark}.
$$

Common divergence sources are arrival-time convention, Doppler factor, density profile, break smoothing, pitch-angle average, seed photon convention, KN treatment, \(\gamma\gamma\) target field, EBL model, component decomposition, and statistical treatment of upper limits.

## 14. 报告 checklist

An event interpretation report should include:

| Section | Required content |
| --- | --- |
| Data provenance | instruments, bands, units, trigger time, redshift |
| Quantity class | observed / derived / model-inferred / benchmark-output |
| Local diagnostics | \(\alpha,\beta\), SED, residuals, upper limits |
| Baseline model | FS assumptions, density profile, microphysics, segment labels |
| Closure test | \(\Delta_{\rm cl}\) and caveats |
| Extension tests | injection, density, reverse shock, components, geometry |
| High-energy tests | SSC/KN, burnoff, \(\gamma\gamma\), EBL, hadronic/cascade boundary |
| Code layer | analytic / toy / production / benchmark-output |
| Claims | consistency, tension, preference, exclusion, or missing boundary |

Formula ID：`AG-INTERP-REPORT-CHECKLIST-001`。

This checklist is intentionally conservative. It is better to write "consistent with SSC under stated assumptions" than to write "TeV emission is SSC" when KN feedback, opacity, EBL and alternatives have not been modeled.

## 15. Benchmark boundary

External tools may enter at specific layers:

- `afterglowpy`, `VegasAfterglow`, BOXFIT-like grids: mature afterglow light-curve comparison.
- `agnpy`, `naima`: radiation SED convention parity.
- `ebltable` or EBL model tables: propagation attenuation.
- SOPHIA / AM3 / NeuCosmA / CRPropa / ELMAG: hadronic, cascade or propagation benchmark candidates.
- Bayesian samplers / inference frameworks: statistical machinery, not physical assumptions.

The course should never let benchmark-output decide the theory starting point. Benchmark-output can verify implementation, expose convention differences, or support a model comparison under stated assumptions.

## 16. 不声称

- 不声称 closure relation alone proves an afterglow model.
- 不声称 best-fit parameter table proves a unique physical origin.
- 不声称 polarization, VLBI, jet break, TeV photon or neutrino non-detection alone selects one geometry or emission mechanism.
- 不声称 external package output is an observation.
- 不声称 current local code has full afterglow inference, full structured-jet hydrodynamics, full SSC transfer, full hadronic cascade or neutrino event-rate prediction.
- 不把 GRB 221009A 或任何事件的 candidate mechanism 写成唯一解释。

## 17. 参考文献

- Sari, Piran & Narayan 1998; Granot & Sari 2002, standard afterglow spectral and closure context.
- Piran 2004; Zhang 2014, GRB afterglow review and interpretation caveats.
- Sari & Esin 2001, afterglow SSC and \(Y\) feedback.
- Salafia & Ghirlanda 2022, structured-jet and viewing-angle review.
- Rybicki & Lightman, radiation diagnostics and synchrotron polarization basis.
- MAGIC GRB 190114C and LHAASO GRB 221009A papers as high-energy observational contexts.
- `afterglowpy`, `VegasAfterglow`, `naima`, `agnpy`, `ebltable` documentation as benchmark / convention references only.
