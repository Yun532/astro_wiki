# 11 粒子加速与最大能量

状态：v0.1 课程讲义草稿。本页接在 SSC / TeV afterglow 之后，回答一个更底层的问题：shock 中的粒子为什么能有 power-law 分布，以及最高能量由什么限制。它不是 GRB 221009A 的事件拟合页，也不是 UHECR 结论页；它提供 acceleration time、cooling time、escape time、Hillas condition 和 synchrotron burnoff 的课程级推导入口。

核心原则：不能用“观测到 TeV photon”倒推出唯一机制。先写加速、冷却和逃逸的时间尺度竞争，再把 synchrotron、SSC、hadronic/cascade 作为候选层级接上去。

## 1. 物理图像

GRB afterglow 的 external shock 是 collisionless shock。标准 afterglow 模型通常不从 plasma first principles 直接推导 \(\epsilon_e,\epsilon_B,p,\xi_e\)，而是把它们作为 microphysical parameters：

```text
bulk kinetic energy
  -> shocked internal energy
  -> magnetic turbulence / field amplification
  -> particle scattering across shock or turbulent cells
  -> nonthermal particle distribution
  -> radiation and escape
```

本页要区分三层：

| 层级 | 内容 | 是否已由标准 afterglow 公式自动给出 |
| --- | --- | --- |
| injection | 哪些粒子进入非热 tail | 否，通常参数化为 \(\xi_e,\epsilon_e\) |
| spectral slope | \(N(\gamma)\propto\gamma^{-p}\) 的 \(p\) | 否，观测和 PIC / theory 共同约束 |
| maximum energy | \(\gamma_{\max}\) 或 \(E_{\max}\) | 否，必须比较 acceleration / cooling / escape |

Formula ID：`AG-ACC-PICTURE-001`。

## 2. 参考系与变量

默认在 shocked-fluid comoving frame 中写局域时间尺度，带 prime。粒子质量 \(m\)、电荷 \(Ze\)，Lorentz factor \(\gamma\)。对电子 \(m=m_e,Z=1\)；对质子 \(m=m_p,Z=1\)；对原子核可写 \(m\simeq A m_p\)。

| 符号 | 含义 |
| --- | --- |
| \(B'\) | comoving magnetic field |
| \(R'\) | comoving size / residence scale |
| \(r_L'\) | Larmor radius |
| \(t'_{\rm acc}\) | acceleration time |
| \(t'_{\rm dyn}\) | dynamical / advection time |
| \(t'_{\rm esc}\) | escape time |
| \(t'_{\rm syn}\) | synchrotron cooling time |
| \(t'_{\rm IC}\) | inverse-Compton cooling time |
| \(t'_{p\gamma},t'_{pp}\) | hadronic interaction times |
| \(\eta_{\rm acc}\) | acceleration inefficiency factor, \(\eta_{\rm acc}\ge1\) |
| \(\gamma_{\max}\) | maximum Lorentz factor |
| \(E'_{\max}\) | maximum comoving particle energy |

The Larmor radius of a relativistic particle is

$$
r_L'
=
{p'c\over ZeB'}
\simeq
{\gamma m c^2\over ZeB'} .
$$

Formula ID：`AG-ACC-LARMOR-001`。

## 3. 一般表达式：timescale competition

The maximum energy is not a single formula. It is the minimum allowed by all loss and escape channels:

$$
t'_{\rm acc}(\gamma_{\max})
=
\min\left[
t'_{\rm dyn},
t'_{\rm esc},
t'_{\rm syn},
t'_{\rm IC},
t'_{p\gamma},
t'_{pp},
\cdots
\right].
$$

Equivalently,

$$
\gamma_{\max}
=
\min_i \gamma_i,
$$

where each \(\gamma_i\) is obtained by solving

$$
t'_{\rm acc}(\gamma_i)=t'_i(\gamma_i).
$$

Formula ID：`AG-ACC-COMPETITION-001`。

This expression is the safe starting point. A code helper that returns only a synchrotron-limited \(\gamma_{\max}\) or a Hillas energy is not a complete maximum-energy solver unless it also states which channels were omitted.

## 4. 详细推导 I：加速时间

For diffusive shock acceleration or Bohm-like stochastic scattering, one writes

$$
t'_{\rm acc}
=
\eta_{\rm acc}{r_L'\over c}.
$$

Substituting \(r_L'\) gives

$$
t'_{\rm acc}
=
\eta_{\rm acc}
{\gamma m c\over ZeB'}.
$$

Formula ID：`AG-ACC-TACC-001`。

The factor \(\eta_{\rm acc}\) hides the scattering mean free path, shock obliquity, turbulence level and acceleration mechanism. Bohm-like acceleration corresponds to \(\eta_{\rm acc}\sim1\), but this is an optimistic lower bound, not a default truth.

For a diffusion coefficient \(\kappa'=\lambda'c/3\), with \(\lambda'=\eta_{\rm mfp}r_L'\), a non-relativistic strong-shock DSA estimate has

$$
t'_{\rm acc}
\sim
{20\over3}{\eta_{\rm mfp}r_L'\over u_{\rm sh}'^2/c},
$$

so the \(\eta_{\rm acc}r_L'/c\) form is a compact parameterization of more detailed transport. Relativistic shocks and reconnection require their own numerical or kinetic treatment.

## 5. 详细推导 II：动力学限制与 Hillas 限制

A particle cannot be accelerated for longer than it remains in the emitting region. A common residence-time scale is

$$
t'_{\rm dyn}\sim {R'\over c}.
$$

Set \(t'_{\rm acc}=t'_{\rm dyn}\):

$$
\eta_{\rm acc}{\gamma m c\over ZeB'}
=
{R'\over c}.
$$

Solving for \(\gamma\):

$$
\gamma_{\rm dyn}
=
{ZeB'R'\over\eta_{\rm acc}mc^2}.
$$

Therefore the comoving maximum energy from finite size is

$$
\boxed{
E'_{\max,{\rm dyn}}
=
\gamma_{\rm dyn}mc^2
=
{ZeB'R'\over\eta_{\rm acc}} .
}
$$

Formula ID：`AG-ACC-DYN-LIMIT-001`。

If one only requires the Larmor radius to fit inside the source,

$$
r_L'<R',
$$

then

$$
\boxed{
E'_{\max,{\rm Hillas}}
\lesssim
ZeB'R' .
}
$$

Formula ID：`AG-ACC-HILLAS-001`。

The Hillas condition is necessary, not sufficient. It does not include radiative cooling, adiabatic losses, shock age, turbulence power, anisotropic escape, or photohadronic losses. In observer/source-frame discussions one may multiply the comoving energy scale by a bulk Lorentz factor, but the convention must be stated:

$$
E_{\max,{\rm src}}
\sim
\Gamma E'_{\max}.
$$

This boost estimate is appropriate for an outflow-frame particle energy scale; it is not a detector-frame cosmic-ray propagation calculation.

## 6. 详细推导 III：synchrotron cooling 限制

For a particle of charge \(Ze\) and mass \(m\), synchrotron power can be written by mass-scaling the Thomson expression:

$$
P'_{\rm syn}
=
{4\over3}\sigma_T c U'_B \gamma^2
Z^4\left({m_e\over m}\right)^2,
$$

where

$$
U'_B={B'^2\over8\pi}.
$$

The synchrotron cooling time is

$$
t'_{\rm syn}
=
{\gamma mc^2\over P'_{\rm syn}}
=
{6\pi m^3c\over
\sigma_T m_e^2 Z^4 B'^2\gamma}.
$$

Formula ID：`AG-ACC-SYN-COOL-001`。

Set \(t'_{\rm acc}=t'_{\rm syn}\):

$$
\eta_{\rm acc}{\gamma m c\over ZeB'}
=
{6\pi m^3c\over
\sigma_T m_e^2 Z^4 B'^2\gamma}.
$$

Cancel \(c\) and solve:

$$
\eta_{\rm acc}\gamma m
=
{6\pi ZeB'm^3\over
\sigma_T m_e^2 Z^4 B'^2\gamma},
$$

so

$$
\gamma^2
=
{6\pi e m^2\over
\eta_{\rm acc}\sigma_T m_e^2 Z^3B'}.
$$

Thus

$$
\boxed{
\gamma_{\rm syn}
=
\left(
{6\pi e m^2\over
\eta_{\rm acc}\sigma_T m_e^2 Z^3B'}
\right)^{1/2}.
}
$$

Formula ID：`AG-ACC-SYN-LIMIT-GAMMA-001`。

For electrons, this reduces to

$$
\gamma_{e,\rm syn}
=
\left(
{6\pi e\over\eta_{\rm acc}\sigma_TB'}
\right)^{1/2}.
$$

This is the electron synchrotron cooling limit used when judging whether a GeV photon can be synchrotron.

## 7. 详细推导 IV：最大 synchrotron photon energy

The characteristic synchrotron frequency for charge \(Ze\), mass \(m\), in the comoving frame is

$$
\nu'_{\rm syn}
\simeq
{3ZeB'\over4\pi mc}\gamma^2 .
$$

Insert \(\gamma_{\rm syn}^2\):

$$
\nu'_{\rm syn,max}
\simeq
{3ZeB'\over4\pi mc}
{6\pi e m^2\over
\eta_{\rm acc}\sigma_T m_e^2 Z^3B'} .
$$

The magnetic field cancels:

$$
\nu'_{\rm syn,max}
\simeq
{9 e^2 m\over
2\eta_{\rm acc}\sigma_T c m_e^2 Z^2}.
$$

Using \(\sigma_T=(8\pi/3)e^4/(m_e^2c^4)\), this can be written as

$$
h\nu'_{\rm syn,max}
\simeq
{27\over8}
{1\over\alpha_f}
{mc^2\over \eta_{\rm acc}Z^2},
$$

where \(\alpha_f=e^2/(\hbar c)\) is the fine-structure constant. Order-unity factors change with pitch-angle and exact peak-frequency convention; the important result is that \(B'\) cancels in the synchrotron-loss-limited photon energy.

For electrons, the often-quoted burnoff scale is therefore

$$
\boxed{
h\nu_{\rm syn,max}^{\rm obs}
\sim
{50\text{--}200\,{\rm MeV}\over\eta_{\rm acc}}
{\Gamma\over1+z}.
}
$$

Formula ID：`AG-ACC-SYN-BURNOFF-001`。

A photon well above this scale is not automatically impossible for synchrotron, because the coefficient depends on acceleration efficiency, pitch-angle distribution, electric-field acceleration, decaying magnetic fields and geometry. But it is a strong warning that SSC, external IC, hadronic or cascade alternatives must be checked.

## 8. Spectral Slope and Injection Caveat

Afterglow modeling often assumes

$$
N(\gamma)d\gamma
=
K\gamma^{-p}d\gamma,
\qquad
\gamma_m<\gamma<\gamma_{\max}.
$$

Formula ID：`AG-ACC-POWERLAW-001`。

For a non-relativistic test-particle shock, compression ratio \(r\) gives

$$
p_{\rm NR}
=
{r+2\over r-1}.
$$

For a strong gas shock with \(r=4\):

$$
p_{\rm NR}=2.
$$

Formula ID：`AG-ACC-SLOPE-NR-001`。

Relativistic collisionless shocks are not this simple. PIC simulations and afterglow observations often give \(p\sim2.1\text{--}2.5\), but \(p\) depends on magnetization, obliquity, turbulence and injection physics. Therefore the course should not pretend that standard afterglow theory predicts a unique \(p\) from first principles.

The minimum Lorentz factor \(\gamma_m\) in the synchrotron page is an energy-partition closure:

$$
\gamma_m
\simeq
{p-2\over p-1}
{\epsilon_e\over\xi_e}
{m_p\over m_e}
\Gamma .
$$

It tells us how a chosen fraction of energy is assigned to accelerated electrons; it does not solve the injection problem.

## 9. Hadronic and Cascade Interfaces

For protons and nuclei, the same size and synchrotron limits apply after replacing \(m,Z\). But additional loss channels enter:

$$
t'_{p\gamma}{}^{-1}
\sim
c\int d\epsilon'\,n'_\gamma(\epsilon')
\langle\sigma_{p\gamma}\kappa\rangle,
$$

and

$$
t'_{pp}{}^{-1}
\sim
n'_p\sigma_{pp}\kappa_{pp}c .
$$

These schematic expressions connect to the hadronic radiation page. They are not complete spectra.

Formula ID：`AG-ACC-HADRONIC-LOSS-ENTRY-001`。

The acceleration condition for hadronic models is therefore

$$
t'_{\rm acc}
<
\min(t'_{\rm dyn},t'_{\rm esc},t'_{\rm syn},t'_{p\gamma},t'_{pp},\cdots).
$$

Formula ID：`AG-ACC-HADRONIC-COMPETITION-001`。

If a hadronic or cascade model is proposed for TeV afterglow, the report must state:

| Quantity | Must be specified |
| --- | --- |
| \(E'_{p,\max}\) | which limiting time sets it |
| photon target field | synchrotron, prompt tail, external field, or assumed table |
| baryon loading | model-inferred, not observed |
| cascade treatment | none / envelope / numerical cascade |
| neutrino output | whether computed, bounded, or absent |

## 10. 精确解析状态

| Object | Analytic status | Comment |
| --- | --- | --- |
| Larmor radius | closed | relativistic \(p\simeq E/c\) assumed |
| Bohm-like acceleration time | parameterized | \(\eta_{\rm acc}\) hides transport physics |
| Hillas / dynamical limit | closed scaling | necessary, not sufficient |
| synchrotron cooling time | closed | assumes uniform \(B'\), pitch-angle convention hidden |
| synchrotron-limited \(\gamma_{\max}\) | closed | valid only if synch cooling dominates |
| synchrotron burnoff photon energy | closed up to order-unity factors | \(B'\) cancels |
| \(p\) from shock theory | not unique | relativistic collisionless shocks require kinetic physics |
| hadronic/cascade maximum energy | generally numerical | needs photon fields, cross sections, escape and cascade |

## 11. 近似层级

| 层级 | 做法 | 用途 | 不能声称 |
| --- | --- | --- | --- |
| timescale competition | list all \(t_i\), solve minimum | honest maximum-energy boundary | complete without target fields |
| Hillas check | \(E_{\max}\lesssim ZeBR\) | necessary size condition | sufficient acceleration |
| synchrotron-loss limit | \(t_{\rm acc}=t_{\rm syn}\) | electron burnoff / proton synch caveat | includes IC or hadronic losses |
| event sanity | compare observed photon energy with burnoff scale | mechanism triage | unique origin |
| kinetic simulation | PIC / transport / Monte Carlo | microphysical \(p,\eta_{\rm acc}\) | universal afterglow parameter |
| cascade modeling | solve secondary pairs and photons | hadronic TeV interpretation | present in current local code |

## 12. 从推导到代码的实现约定

当前本地代码已经有一组 source-agnostic acceleration screening helpers，但还没有 afterglow-specific 的 full maximum-energy solver。也就是说，Larmor radius、Bohm-like acceleration time、Hillas ceiling 与 electron synchrotron loss limit 已经可做 local-fixed-point 检查；photohadronic losses、escape model、shock residence time、target photon field 与 cascade feedback 仍没有被统一求解。

相关现有代码：

```text
reproduce/grb/core/radiation/acceleration.py
reproduce/grb/core/radiation/hadronic.py
reproduce/grb/core/radiation/cooling_angle.py
reproduce/grb/core/radiation/production.py
reproduce/grb/validation_lab/check_radiation_acceleration_v1.py
reproduce/grb/events/grb_221009a/scripts/05_tev_ssc_sanity.py
```

当前边界：

- `acceleration.py` contains source-agnostic screening helpers: `larmor_radius_cm`、`bohm_acceleration_time_s`、`hillas_max_energy_ev`、`confinement_max_lorentz_factor`、`light_crossing_escape_time_s`、`bohm_diffusion_escape_time_s`、`electron_synchrotron_loss_limited_gamma_max` 和 `accelerator_limit_summary`。
- 这些 helper 的原始 Formula IDs 是 `ACC-*`；本页的 `AG-ACC-*` 是 afterglow course alias / mapping，用来说明它们在 afterglow 章节中的物理位置。
- `hadronic.py` contains proton synchrotron and hadronic scale helpers, but its docstrings explicitly say they do not include acceleration limits or cascade.
- `cooling_angle.py` contains cooling-time and envelope helpers, but not a unified maximum-energy solver.
- `05_tev_ssc_sanity.py` contains candidate diagnostics for TeV interpretation, not a particle-acceleration model.
- External package parity for proton synchrotron is benchmark-output; it does not prove a proton population can be accelerated to the required energy.

已存在 helper 与课程 Formula ID 的映射：

| Helper | Course Formula ID | Source Formula ID / layer |
| --- | --- | --- |
| `larmor_radius_cm(...)` | `AG-ACC-LARMOR-001` | `ACC-LARMOR-RADIUS-001`, local-fixed-point |
| `bohm_acceleration_time_s(...)` | `AG-ACC-TACC-001` | `ACC-BOHM-TIME-001`, local-fixed-point |
| `hillas_max_energy_ev(...)` | `AG-ACC-HILLAS-001` | `ACC-HILLAS-ENERGY-001`, source-screening |
| `confinement_max_lorentz_factor(...)` | `AG-ACC-DYN-LIMIT-001` / `AG-ACC-HILLAS-001` | `ACC-HILLAS-GAMMA-001`, confinement ceiling |
| `electron_synchrotron_loss_limited_gamma_max(...)` | `AG-ACC-SYN-LIMIT-GAMMA-001` | `ACC-ELECTRON-SYN-LIMIT-GAMMA-001`, local-fixed-point |
| `accelerator_limit_summary(...)` | `AG-ACC-COMPETITION-001` | source-screening summary, not full solver |
| `forward_shock_cooling_acceleration_timeseries(...)` | `AG-FS-COOL-ACC-SCREEN-001` | GRB source-adapter smoke, BM slope propagation |

因此，本页不能再把所有 `AG-ACC-*` 都标成 `future-helper`；更准确的说法是：`AG-ACC-LARMOR-001`、`AG-ACC-TACC-001`、`AG-ACC-HILLAS-001` 与 `AG-ACC-SYN-LIMIT-GAMMA-001` 已有 source-agnostic partial-code 支撑，`AG-ACC-COMPETITION-001` 只有 screening summary，还不是包含所有 loss / escape / target-field channels 的 afterglow maximum-energy solver。

`AG-FS-COOL-ACC-SCREEN-001` 只是把这些 local helpers 沿 BM forward-shock time series 逐点调用。它能检查 \(t_{\rm acc}\)、\(t_{\rm esc}\)、\(t_{\rm syn}\)、Hillas energy 等随时间的标度，但没有求解完整 maximum-energy equation，也没有加入 \(p\gamma\)、BH、pp、adiabatic、turbulence residence time 或 cascade feedback。

## 13. Benchmark boundary

可用的 benchmark 或文献锚点：

- PIC simulations of relativistic shocks: useful for \(p\), injection and magnetization dependence, not a universal closed formula.
- CRPropa / ELMAG / cascade tools: useful for propagation and cascade benchmark, not a local afterglow proof.
- `agnpy` / `naima` proton synchrotron: SED benchmark, not acceleration feasibility.
- LHAASO / MAGIC TeV observations: observed context, not a mechanism selector.
- UHECR Hillas plots: necessary size-field comparison, not sufficient acceleration proof.

## 14. 不声称

- 不声称标准 afterglow theory 从 first principles 预测唯一 \(p\)。
- 不声称 Hillas condition 足以证明 UHECR acceleration。
- 不声称 proton synchrotron SED parity 证明 protons 可被加速到所需能量。
- 不声称 electron synchrotron burnoff 是绝对硬墙；它是效率和 convention 相关的强约束。
- 不声称当前本地代码已有 maximum-energy solver、escape model、PIC model、photohadronic cascade 或 neutrino event-rate prediction。
- 不把 TeV photon 自动写成 SSC、synchrotron、proton synchrotron 或 cascade 的唯一证据。

## 15. 参考文献

- Blandford & Eichler 1987, *Particle Acceleration at Astrophysical Shocks*.
- Drury 1983, diffusive shock acceleration review.
- Achterberg et al. 2001, relativistic shock acceleration.
- Sironi, Spitkovsky and collaborators, relativistic collisionless shock PIC literature.
- Rybicki & Lightman, synchrotron cooling and charged-particle radiation.
- Hillas 1984, maximum energy and source-size argument.
- Piran 2004 and Zhang 2014, GRB afterglow review context.
- Sari, Piran & Narayan 1998, standard afterglow electron parameterization.
- Aharonian / Kelner / Kafexhiu hadronic-process references used by the radiation mechanism pages.
