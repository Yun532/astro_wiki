# 09 Afterglow Fitting Workflow and Parameter Degeneracy

状态：v0.1 课程讲义草案。本页把前面 afterglow dynamics、synchrotron spectrum、closure relations、jet geometry、energy injection、density variation、radio calorimetry、two-component jet 和 polarization/VLBI diagnostics 组织成一条实际建模工作流。

核心原则：拟合流程不是“先选一个喜欢的模型再解释数据”。可靠写法必须先区分 observed、derived、model-inferred 和 benchmark-output，再逐层增加模型复杂度，并把未排除的 alternatives 保留下来。

## 1. 物理图像

Afterglow fitting 的困难不在于公式太少，而在于不同参数和机制能产生相似的 light curve：

$$
E_k,\ n/A_\ast,\ \epsilon_e,\ \epsilon_B,\ p,\ \theta_j,\ \theta_v,\ E(t),\ \rho(R),\ {\rm extra\ components}.
$$

因此事件解释必须分成三层：

| 层级 | 例子 | 写法 |
| --- | --- | --- |
| observed | flux density, magnitude, count rate, upper limit, observing time | 数据事实 |
| derived | spectral index, BPL peak, extinction-corrected flux, equipartition estimate | 处理/拟合产物 |
| model-inferred | \(E_k,\epsilon_B,A_\ast,\theta_j,\theta_v\) | 模型条件下的参数 |

Formula ID：`FIT-QUANTITY-CLASS-001`。

## 2. 参考系与变量

| 符号 | 含义 |
| --- | --- |
| \(t_{\rm obs}\) | observer-frame time since chosen trigger |
| \(t_{\rm src}\) | source-frame time |
| \(\nu_{\rm obs}\) | observed frequency |
| \(\nu_{\rm src}\) | source-frame frequency |
| \(F_\nu\) | spectral flux density |
| \(\alpha\) | temporal decay index in \(F_\nu\propto t^{-\alpha}\) |
| \(\beta\) | spectral index in \(F_\nu\propto\nu^{-\beta}\) |
| \(\Delta_{\rm cl}\) | closure residual |
| \(\Theta\) | model parameter vector |

## 3. General Expression

### 3.1 Data-to-source-frame conversion

The minimal time and frequency conversions are

$$
t_{\rm src}={t_{\rm obs}\over1+z},
$$

Formula ID：`FIT-TIME-SOURCE-001`。

and

$$
\nu_{\rm src}=(1+z)\nu_{\rm obs}.
$$

Formula ID：`FIT-FREQ-SOURCE-001`。

Flux conversion depends on whether the source reports \(F_\nu\), \(\nu F_\nu\), energy flux, photon flux, count rate, or fluence. Do not convert between them without a spectrum and response convention.

### 3.2 First-pass spectral-temporal model

For a local power-law segment,

$$
F_\nu(t,\nu)
=
F_0
\left({t\over t_0}\right)^{-\alpha}
\left({\nu\over\nu_0}\right)^{-\beta}.
$$

Formula ID：`FIT-FNU-PL-001`。

This is not a full afterglow model. It is a diagnostic layer used to estimate \(\alpha,\beta\), compare bands, and decide which physical modules are needed.

### 3.3 Model likelihood

A simple Gaussian data likelihood corresponds to

$$
\chi^2(\Theta)
=
\sum_i
\left[
{F_i-F_{\rm model}(t_i,\nu_i;\Theta)\over\sigma_i}
\right]^2.
$$

Formula ID：`FIT-CHI2-001`。

This expression is only valid after data units, covariance, calibration systematics, and upper-limit handling are specified.

## 4. Detailed Derivation I：From Spectrum to \(p\)

A first-pass workflow should use the SED before over-interpreting a light curve. In slow cooling:

### 4.1 \(\nu_m<\nu<\nu_c\)

From synchrotron theory:

$$
F_\nu\propto\nu^{-(p-1)/2}.
$$

Comparing with \(F_\nu\propto\nu^{-\beta}\):

$$
\beta={p-1\over2}.
$$

Therefore

$$
\boxed{
p=2\beta+1
}
$$

Formula ID：`FIT-P-FROM-BETA-SLOW-MID-001`。

### 4.2 \(\nu>\nu_c\)

For the high-frequency slow-cooling segment:

$$
F_\nu\propto\nu^{-p/2}.
$$

Thus

$$
\beta={p\over2},
$$

and

$$
\boxed{
p=2\beta
}
$$

Formula ID：`FIT-P-FROM-BETA-SLOW-HIGH-001`。

If optical and X-ray imply inconsistent \(p\), do not immediately introduce complex geometry. First check extinction, absorption, cooling-break placement, host/SN contamination, spectral curvature and calibration.

## 5. Detailed Derivation II：Closure Residual

Given a candidate medium, cooling regime and spectral segment, the theory predicts

$$
\alpha_{\rm th}=\alpha_{\rm th}(p,\mathrm{medium},\mathrm{segment}).
$$

Define closure residual:

$$
\boxed{
\Delta_{\rm cl}
=
\alpha_{\rm obs}-\alpha_{\rm th}.
}
$$

Formula ID：`FIT-CLOSURE-RESID-001`。

For example, ISM slow cooling with \(\nu_m<\nu<\nu_c\):

$$
\alpha_{\rm th}={3(p-1)\over4}.
$$

If \(p=2\beta+1\), then

$$
\alpha_{\rm th}={3\beta\over2}.
$$

Thus

$$
\Delta_{\rm cl}
=
\alpha_{\rm obs}-{3\beta\over2}.
$$

A nonzero \(\Delta_{\rm cl}\) is not automatically a discovery of jet structure. It is a pointer to missing physics: wrong spectral segment, wind medium, energy injection, density variation, reverse shock, SSC cooling, extinction, or extra component.

## 6. Detailed Derivation III：Upper Limits and Non-Detections

An upper limit is not a failed detection to ignore. If a \(k\sigma\) upper limit reports

$$
F<F_{\rm lim},
$$

then a simple hard-filter rule is:

$$
F_{\rm model}(t_i,\nu_i;\Theta)\le F_{\rm lim}.
$$

Formula ID：`FIT-UPPER-LIMIT-HARD-001`。

For likelihood work, one can use a one-sided Gaussian term. If measurement noise is Gaussian with standard deviation \(\sigma\), and limit corresponds to \(F_{\rm lim}=k\sigma\), then the probability of a non-detection is

$$
P_{\rm non-det}
=
\Phi\left({F_{\rm lim}-F_{\rm model}\over\sigma}\right),
$$

where \(\Phi\) is the normal cumulative distribution. The contribution to log-likelihood is

$$
\ln\mathcal L_{\rm lim}
=
\ln P_{\rm non-det}.
$$

Formula ID：`FIT-UPPER-LIMIT-LIKE-001`。

This is already more honest than treating the upper limit as a flux point at \(F_{\rm lim}\).

## 7. Parameter Degeneracy Map

### 7.1 Forward-shock parameter vector

The standard forward-shock parameter vector is

$$
\Theta_{\rm FS}
=
(E_k,\ n\ {\rm or}\ A_\ast,\ \epsilon_e,\ \epsilon_B,\ p,\ z,\ D_L).
$$

Formula ID：`FIT-PARAM-FS-001`。

Geometry and extensions add:

$$
\Theta_{\rm geom}
=
(\theta_j,\theta_c,\theta_v,\theta_n,\theta_w,\mathcal E(\theta),\Gamma_0(\theta)),
$$

Formula ID：`FIT-PARAM-GEOM-001`。

Energy/density extensions add:

$$
\Theta_{\rm ext}
=
(e,\ q,\ s,\ g(R),R_t).
$$

Formula ID：`FIT-PARAM-EXT-001`。

### 7.2 Degeneracy table

| Parameter / mechanism | Similar observable effect | How to break degeneracy |
| --- | --- | --- |
| \(E_k\) larger | brighter flux, later breaks | broadband SED, calorimetry |
| \(n/A_\ast\) change | shifts \(\nu_c,\nu_a,F_{\nu,\max}\) | radio, cooling break |
| lower \(\epsilon_B\) | changes \(\nu_c\), SSC importance | X-ray/TeV, IC cooling |
| energy injection | plateau / shallow decay | achromaticity, end slope |
| density bump | chromatic bump possible | optical/X-ray contrast, radio |
| jet break | achromatic steepening | polarization/VLBI, post-break slope |
| structured jet | smooth peak/break | viewing diagnostics, centroid |
| reverse shock | early flash/radio flare | onset time, color, polarization |
| scintillation | radio variability | frequency dependence, source size |

Formula ID：`FIT-DEGENERACY-MATRIX-001`。

## 8. Complexity Ladder

Use a ladder, not a leap:

| Level | Model | Add only when |
| --- | --- | --- |
| 1 | single forward shock, ISM/wind | SED and closure are roughly consistent |
| 2 | jet break / beaming correction | achromatic steepening or geometry clue |
| 3 | energy injection / refreshed shock | plateau or shallow decay |
| 4 | density variation | chromatic bump or medium evidence |
| 5 | reverse shock | early optical/radio flash |
| 6 | SSC / high-energy component | GeV-TeV excess or cooling evidence |
| 7 | structured / two-component jet | viewing-angle, late component, radio calorimetry |
| 8 | polarization/VLBI constrained geometry | direct geometry diagnostic exists |

Formula ID：`FIT-COMPLEXITY-LADDER-001`。

This ladder is a reporting discipline, not a claim that nature is simple. It prevents highly parameterized models from becoming unfalsifiable explanations.

## 9. Report Template

| Category | Must record |
| --- | --- |
| Data | bands, time zero, redshift, corrections, upper limits |
| Quantity class | observed / derived / model-inferred / benchmark-output |
| Dynamics | ISM/wind/general-\(k\), BM/ST/jet/energy injection |
| Radiation | synchrotron, SSC, \(\nu_m,\nu_c,\nu_a,p,Y\) |
| Geometry | \(\theta_j,\theta_c,\theta_v,\theta_n,\theta_w\), convention |
| Energetics | prompt \(E_{\gamma,\rm iso}\), kinetic \(E_k\), true energy |
| Components | FS, RS, prompt tail, SN/kilonova, host, radio extra |
| Alternatives | models tested, not tested, and excluded |

Formula ID：`FIT-REPORT-TEMPLATE-001`。

## 10. Code / Course Interface

Current local code can support first-pass checks:

- standard closure relations;
- synchrotron break sanity;
- event-level quantity-class checks;
- radio SSA / extra-component candidate diagnostics;
- trace manifest for outputs.

It does not yet provide:

- full MCMC afterglow fitter;
- self-consistent EATS structured-jet light curve;
- trans-relativistic radio calorimetry fitter;
- polarized transfer or VLBI image synthesis.

Therefore any event workflow should state whether it is `toy-model`, `event-trend`, `literature-scale candidate`, `benchmark-output`, or `production-ready`.

Formula ID：`FIT-CODE-LAYER-001`。

## 11. Exact Analytic Status

| 对象 | 解析状态 | 说明 |
| --- | --- | --- |
| source-frame time/frequency conversion | closed | depends on chosen trigger/time zero |
| \(p\) from \(\beta\) | closed by spectral segment | segment must be correct |
| closure residual | algebraic diagnostic | not model proof |
| \(\chi^2\) | closed likelihood form | assumes Gaussian independent errors |
| upper-limit likelihood | semi-analytic | depends on reported limit convention |
| parameter degeneracy map | conceptual | not a covariance matrix |
| full afterglow fit | numerical / statistical | depends on priors and model family |

## 12. Approximation Hierarchy

| 层级 | 做法 | 保留 | 牺牲 |
| --- | --- | --- | --- |
| data audit | classify observed/derived/model-inferred | provenance | no physics fit |
| SED/closure | estimate \(p,\alpha,\beta\) | quick consistency | normalization detail |
| semi-analytic FS | BM + breaks + closure | physical scalings | smooth spectra/EATS |
| component diagnostics | RS, radio extra, injection, density | alternatives | uniqueness |
| numerical light curve | mature solver / custom integration | full model comparison | convention dependence |
| statistical inference | likelihood + priors | uncertainty propagation | prior/model sensitivity |

## 13. Benchmark Boundary

External packages such as afterglowpy, VegasAfterglow, BOXFIT-like tables, or event-specific fitting codes are benchmark-output / mature-method comparisons. They can test whether a convention-matched model behaves similarly, but they do not make model-inferred parameters into observations.

## 14. Interfaces to Later Pages

- SSC / TeV afterglow：high-energy component enters workflow after synchrotron baseline.
- event pages：use this page as the template for separating observed, derived and model-inferred quantities.
- code Codex：can implement helpers for closure residuals, upper-limit likelihoods and report templates.

## 15. 不声称

- 不把 best-fit parameter 写成直接观测量。
- 不把 upper limit 当作 detection。
- 不混用 \(E_{\gamma,\rm iso}\)、\(E_k\) 和 \(E_{\rm true}\)。
- 不把 benchmark package output 写成理论证明。
- 不把复杂模型写成唯一解释，除非 alternatives 被明确检验并排除。

## 16. 参考来源

- Sari, Piran & Narayan 1998, *Spectra and Light Curves of Gamma-Ray Burst Afterglows*.
- Granot & Sari 2002, *The Shape of Spectral Breaks in Gamma-Ray Burst Afterglows*.
- Piran 2004, *The Physics of Gamma-Ray Bursts*.
- Zhang 2014, *The Physics of Gamma-Ray Bursts & Relativistic Jets*.
- Salafia & Ghirlanda 2022, *The Structure of Gamma Ray Burst Jets*.
- GRB 030329 / GRB 080319B / GRB 221009A literature as event-level caveat examples.
