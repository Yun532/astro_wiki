# 12 Cascade、Neutrino 与传播边界

状态：v0.1 课程讲义草稿。本页接在 particle acceleration / maximum energy 之后，回答一个更完整的问题：如果 afterglow shock 真的把 protons / nuclei 加速到足够高能，secondary gamma rays、pairs、neutrinos 和传播吸收应该怎样进入理论链条。

核心原则：不能从 \(E_\nu\simeq0.05E_p\)、\(\tau_{\gamma\gamma}=n\sigma l\) 或某个 cascade package 输出开始。安全起点是 primary distribution、target fields、interaction kernel、secondary yield 和 coupled transport equations。阈值、能量分配、delta approximation 只能作为后置 sanity layer。

## 1. 物理图像

高能 afterglow 的 hadronic / cascade picture 不是一个单通道辐射机制，而是一组相互耦合的粒子输运问题：

```text
accelerated protons / nuclei
  -> pp / p gamma / Bethe-Heitler / photodisintegration
  -> pi0 gamma rays, pi+/- muons, neutrinos, secondary e+-
  -> gamma-gamma absorption
  -> pair synchrotron and IC emission
  -> repeated EM cascade
  -> internal escape, EBL/IGM propagation, detector response
```

这条链条和第 11 页的 timescale competition 相接：如果 \(t'_{p\gamma}\)、\(t'_{pp}\)、\(t'_{\rm syn}\)、\(t'_{\rm esc}\) 或 \(t'_{\rm dyn}\) 限制了 primary particles，就会同时限制 secondary spectra。反过来，观测到 TeV photons 也不能自动证明 primary protons 存在，因为 leptonic SSC、external IC、extreme synchrotron、internal attenuation 和 EBL attenuation 都可能参与解释。

Formula ID：`AG-CASCADE-PICTURE-001`。

## 2. 参考系与变量

本页默认在 shocked-fluid comoving frame 写局域产生率，带 prime。传播到观测者时再乘 Doppler / bulk Lorentz factor 和 redshift 约定。除非特别说明，\(N_i'(E')\) 表示区域内的总粒子数谱，\(Q_i'(E')\) 表示每单位能量每单位时间的注入率。

| 符号 | 含义 |
| --- | --- |
| \(N_p'(E_p')\) | primary proton spectrum |
| \(N_A'(E_A')\) | primary nucleus spectrum |
| \(n_\gamma'(\epsilon')\) | target photon number density per energy |
| \(n_{\rm gas}'\) | gas target density |
| \(Q_s'(E_s')\) | secondary species \(s\) injection rate |
| \(Y_s(E_s';E_a',\chi)\) | secondary yield kernel |
| \(t'_{\rm esc}\), \(t'_{\rm cool}\), \(t'_{\rm dec}\) | escape, cooling, decay times |
| \(\tau_{\gamma\gamma}^{\rm int}\) | internal pair-production optical depth |
| \(\tau_{\rm EBL}\) | extragalactic background light optical depth |
| \(\Phi_\nu(E_\nu)\) | observed neutrino fluence / flux |
| \(A_{\rm eff}(E_\nu)\) | detector effective area |

comoving energy 与 observer energy 的关系可示意写成

$$
E_{\rm obs}
\simeq
{\delta_D\over1+z}E',
$$

其中 \(\delta_D\) 是 emitting patch 的 Doppler factor。对 spherical on-axis scale estimate，\(\delta_D\sim\Gamma\) 到 \(2\Gamma\) 都会在文献中出现，取决于 convention。这个 factor-of-two 差异不能在 hadronic energy budget 中被悄悄隐藏。

## 3. 一般表达式：secondary emissivity

对 primary species \(a\) 产生 secondary species \(s\) 的过程，最一般的局域结构是

$$
Q_s'(E_s')
=
\int dE_a'\,N_a'(E_a')
\int d\chi\,
n_{\rm target}'(\chi)\,
c\,\mathcal{R}_a(E_a',\chi)
Y_s(E_s';E_a',\chi).
$$

这里 \(\chi\) 可以表示 target photon energy and angle、gas species、nuclear target，或多维 phase-space variable。\(\mathcal{R}_a\) 包含 relative velocity、cross-section 与 inelasticity convention。yield \(Y_s\) 可以来自闭合运动学极限、解析参数化、lookup table 或 Monte Carlo。

Formula ID：`AG-CASCADE-SECONDARY-EMISSIVITY-001`。

这个表达式刻意放在任何 delta approximation 之前。例如替换

$$
Y_s(E_s';E_p')
\rightarrow
N_s\,\delta(E_s'-k_sE_p')
$$

是对 yield 的近似，不是 hadronic emission 的定义。

## 4. 详细推导 I：\(pp\) 与 \(p\gamma\) formal integrals

对 gas target，\(pp\) secondary source term 可写成

$$
Q_s^{\prime pp}(E_s')
=
c\,n_{\rm gas}'
\int dE_p'\,
N_p'(E_p')
{d\sigma_{pp\to s}\over dE_s'}(E_p',E_s').
$$

这是 neutral-pion gamma rays、charged-pion neutrinos 与 secondary electrons 的自然母式。thin-target efficiency \(f_{pp}\simeq n_{\rm gas}\sigma_{pp}\kappa l\) 只是压掉 differential yield 后得到的 energy-loss envelope。

For a photon target, the proton rest-frame photon energy is

$$
\bar\epsilon'
=
\gamma_p'\epsilon'(1-\beta_p\mu).
$$

这里 \(\mu=\cos\theta\in[-1,1]\)，\(\theta\) 是 proton direction 与 target photon direction 的夹角。各向同性 photon field 的 energy-loss rate 可先写成角积分：

$$
t_{p\gamma}^{\prime -1}(\gamma_p')
=
{c\over2}
\int d\epsilon'\,n_\gamma'(\epsilon')
\int_{-1}^{1}d\mu\,
(1-\beta_p\mu)\,
\sigma_{p\gamma}(\bar\epsilon')
K_{p\gamma}(\bar\epsilon').
$$

换元到 proton rest-frame photon energy 时，

$$
d\mu
=
-
{d\bar\epsilon'\over \gamma_p'\beta_p\epsilon'},
\qquad
1-\beta_p\mu
=
{\bar\epsilon'\over\gamma_p'\epsilon'}.
$$

角度端点对应

$$
\bar\epsilon'_{\min}
=
\gamma_p'\epsilon'(1-\beta_p),
\qquad
\bar\epsilon'_{\max}
=
\gamma_p'\epsilon'(1+\beta_p)
\simeq
2\gamma_p'\epsilon'
$$

其中最后一步使用 ultra-relativistic proton。相互作用还要求 \(\bar\epsilon'\ge \bar\epsilon_{\rm thr}\)。把积分次序交换后，给定 \(\bar\epsilon'\) 的 target photon energy 必须满足 \(\epsilon'\gtrsim\bar\epsilon'/(2\gamma_p')\)，于是得到常用的 isotropic photon field 形式：

$$
t_{p\gamma}^{\prime -1}(\gamma_p')
=
{c\over2\gamma_p'^2}
\int_{\bar\epsilon_{\rm thr}}^\infty d\bar\epsilon\,
\sigma_{p\gamma}(\bar\epsilon)K_{p\gamma}(\bar\epsilon)\bar\epsilon
\int_{\bar\epsilon/(2\gamma_p')}^\infty
d\epsilon'\,{n_\gamma'(\epsilon')\over\epsilon'^2}.
$$

这个式子已经压缩了角分布与 inelasticity convention。若要写 secondary injection，则不能只保留 \(K_{p\gamma}\) 的能量损失包络，而要保留 channel yield 与阈值条件：

$$
Q_s^{\prime p\gamma}(E_s')
=
\int dE_p'\,N_p'(E_p')
\int d\epsilon'\,n_\gamma'(\epsilon')
\int_{-1}^{1} d\mu\,{1-\beta_p\mu\over2}\,c\,
{d\sigma_{p\gamma\to s}\over dE_s'}
\,\Theta\!\left[\gamma_p'\epsilon'(1-\beta_p\mu)-\bar\epsilon_{\rm thr}\right].
$$

Formula ID：`AG-CASCADE-PP-PGAMMA-INTEGRAL-001`。

熟悉的 Delta-resonance threshold 只有在 full kernel 被压缩到 \(\bar\epsilon_\Delta\) 附近之后才会出现。higher resonances、direct pion、multi-pion 和 kaon channels 正是过度使用 single delta peak 时丢掉的部分。

## 5. 详细推导 II：pion chain 与 neutrino energy scale

neutral pion decay 为

$$
\pi^0\to\gamma+\gamma .
$$

若 proton energy 的 fraction \(f_\pi\) 进入一个 pion，characteristic photon energy 为

$$
E_{\gamma,\pi^0}'
\sim
{E_\pi'\over2}
\sim
{f_\pi\over2}E_p'.
$$

charged pion decay 为

$$
\pi^+\to\mu^+ + \nu_\mu,
\qquad
\mu^+\to e^+ + \nu_e+\bar\nu_\mu ,
$$

\(\pi^-\) 有对应的 charge-conjugate channels。粗略 equal-partition argument 给出

$$
E_\nu'
\sim
{E_\pi'\over4}
\sim
{f_\pi\over4}E_p'.
$$

For \(f_\pi\sim0.2\),

$$
\boxed{
E_\nu'\sim0.05E_p'.
}
$$

Formula ID：`AG-NU-PION-CHAIN-001` and `AG-NU-ENERGY-SCALE-001`。

这个尺度有助于定位能段，但它不是 neutrino spectrum，因为它省略了 parent proton spectrum、multi-pion yield、muon polarization、decay 前 cooling、flavor mixing 与 detector response。

## 6. 详细推导 III：pion 与 muon 在 decay 前的 cooling

rest-frame lifetime 为 \(\tau_0\) 的 charged secondary 的 decay time 为

$$
t_{\rm dec}'=\gamma\tau_0 .
$$

其 synchrotron cooling time 继承 charged-particle cooling 推导：

$$
t_{\rm syn}'
=
{6\pi m^3c\over
\sigma_Tm_e^2Z^4B'^2\gamma}.
$$

pion 或 muon 的 cooling-break Lorentz factor 由 \(t_{\rm syn}'=t_{\rm dec}'\) 给出：

$$
{6\pi m^3c\over
\sigma_Tm_e^2Z^4B'^2\gamma}
=
\gamma\tau_0 .
$$

Therefore

$$
\boxed{
\gamma_{\rm cool/dec}
=
\left(
{6\pi m^3c\over
\sigma_Tm_e^2Z^4B'^2\tau_0}
\right)^{1/2}.
}
$$

Formula ID：`AG-CASCADE-SECONDARY-COOL-DECAY-001`。

当 \(\gamma>\gamma_{\rm cool/dec}\) 时，secondary 倾向于在 decay 前先辐射。这会压低或重塑 neutrino spectrum，并注入额外 electromagnetic power。因此一旦 \(B'\) 足够大，就不能只凭 proton spectrum 预测 neutrino signal。

## 7. 详细推导 IV：coupled EM cascade transport

\(\pi^0\) decay、proton synchrotron 或 IC 产生的 high-energy photons 可被 \(\gamma\gamma\to e^\pm\) 吸收。photon transport equation 的示意形式为

$$
{\partial N_\gamma'(E_\gamma',t')\over\partial t'}
=
Q_\gamma'(E_\gamma')
-
{N_\gamma'\over t_{\rm esc,\gamma}'}
-
c\,\alpha_{\gamma\gamma}'(E_\gamma')N_\gamma'
+
Q_{\gamma,{\rm sec}}'(E_\gamma').
$$

gamma-gamma absorption 产生 pair injection 的 formal 写法为

$$
Q_{e^\pm,\gamma\gamma}'(E_e')
=
\int dE_\gamma' N_\gamma'(E_\gamma')
\int d\epsilon'\int d\Omega\,
n_\gamma'(\epsilon',\Omega)(1-\mu)c\,
{d\sigma_{\gamma\gamma}\over dE_e'}.
$$

Formula ID：`AG-CASCADE-GG-PAIR-INJECTION-001`。

pair distribution 随后满足

$$
{\partial N_e'(\gamma,t')\over\partial t'}
=
Q_e'(\gamma)
-
{\partial\over\partial\gamma}
\left[\dot\gamma_{\rm syn+IC}'N_e'\right]
-
{N_e'\over t_{\rm esc,e}'}
-
{N_e'\over t_{\rm ann}'}
$$

其中 synchrotron 与 IC emission 会回灌 \(Q_{\gamma,{\rm sec}}'\)。反复出现的循环

```text
gamma absorption -> pair injection -> pair cooling -> new photons -> absorption
```

就是 EM cascade。

Formula ID：`AG-CASCADE-TRANSPORT-SKELETON-001` and `AG-CASCADE-PAIR-COOLING-001`。

optical-depth reprocessing envelope 可写成

$$
F_{\rm esc}(E)
=
F_{\rm int}(E)e^{-\tau_{\gamma\gamma}(E)}
 + F_{\rm cas}(E),
$$

其中 \(F_{\rm cas}\) 不能只由 \(\tau_{\gamma\gamma}\) 决定；它依赖 injected pairs、magnetic field、IC kernel、escape 和 geometry。

Formula ID：`AG-CASCADE-TAU-REPROCESS-001`。

## 8. Neutrino flavor mixing 与 event-rate boundary

若 charged-pion chain 没有 strong cooling，source flavor ratio 常近似为

$$
(\nu_e:\nu_\mu:\nu_\tau)_{\rm src}
\simeq
(1:2:0).
$$

cosmological baseline 上的 vacuum oscillations 给出

$$
\phi_\alpha^\oplus
=
\sum_\beta P_{\alpha\beta}\phi_\beta^{\rm src},
\qquad
P_{\alpha\beta}
=
\sum_i |U_{\alpha i}|^2|U_{\beta i}|^2 .
$$

用当前 mixing angles，常把它概括为

$$
\boxed{
(1:2:0)_{\rm src}
\rightarrow
(1:1:1)_\oplus
}
$$

但 exact mixing values、source flavor composition 与 cooling regimes 都会带来 order-unity 偏差。

Formula ID：`AG-NU-FLAVOR-MIXING-001`。

detector event expectation 还需要额外 convolution：

$$
N_{\rm ev}
=
\int dE_\nu\,\Phi_\nu(E_\nu)
A_{\rm eff}(E_\nu,\Omega)
T_{\rm obs}.
$$

Formula ID：`AG-NU-EVENT-RATE-BOUNDARY-001`。

这个方程是 boundary marker，不是 local afterglow radiation formula。\(A_{\rm eff}\) 依赖 instrument、direction、event class 与 analysis choice。

## 9. 传播边界：EBL 与 IGM

逃出源区的 gamma rays 仍要穿过 extragalactic radiation fields：

$$
F_{\rm obs}(E_0)
=
F_{\rm src}(E_0)
\exp[-\tau_{\rm EBL}(E_0,z_s)]
 + F_{\rm IGM\ cascade}(E_0).
$$

EBL optical depth 继承自 gamma-gamma 页：

$$
\tau_{\rm EBL}(E_0,z_s)
=
\int_0^{z_s} dz\,{dl\over dz}
\int d\epsilon\,n_{\rm EBL}(\epsilon,z)
\int_{-1}^{1}{d\mu\over2}(1-\mu)
\sigma_{\gamma\gamma}[E_0(1+z),\epsilon,\mu].
$$

可能的 intergalactic cascade term 依赖 EBL model、CMB、intergalactic magnetic field、source duration、angular extension 与 time delay。对 transient GRBs，这不是无害的 normalization correction。

Formula ID：`AG-CASCADE-PROPAGATION-BOUNDARY-001`。

## 10. 精确解析状态

| Object | Analytic status | Comment |
| --- | --- | --- |
| secondary emissivity formal integral | formal, not closed | needs cross-section and yield kernel |
| \(pp\) gamma/neutrino spectrum | generally numerical / parameterized | Kafexhiu/Kelner-like choices are conventions |
| \(p\gamma\) spectrum | generally numerical / Monte Carlo | Delta threshold is not full spectrum |
| pion/neutrino characteristic energy | closed scale estimate | not a spectral prediction |
| pion/muon cooling-vs-decay boundary | closed regime condition | spectrum still requires transport |
| EM cascade | coupled numerical transport | no short closed-form solution in general |
| flavor mixing | closed linear mixing after source spectrum is known | source ratio can differ from \(1:2:0\) |
| neutrino event rate | detector convolution | not part of local emission theory |
| EBL / IGM propagation | external model / numerical | depends on EBL, IGMF and cosmology |

## 11. 近似层级

| 层级 | 做法 | 保留 | 牺牲 |
| --- | --- | --- | --- |
| full transport | solve coupled \(p,A,\gamma,e^\pm,\pi,\mu,\nu\) equations | feedback and cooling | expensive, model dependent |
| mature parameterization | use Kelner/Kafexhiu/SOPHIA/AM3-like yields | broad spectral shapes | package/model convention |
| thin-target efficiency | \(f_{pp},f_{p\gamma}\) energy-loss envelope | interaction probability scale | differential spectra |
| energy partition | \(E_\gamma\sim0.1E_p\), \(E_\nu\sim0.05E_p\) | band-location intuition | yield width and cooling |
| delta approximation | \(Y_s\to N_s\delta(E_s-kE_p)\) | teaching slope checks | curvature and thresholds |
| opacity-only | \(F_{\rm esc}=F_{\rm int}e^{-\tau}\) | absorption envelope | reprocessed cascade emission |
| detector event-rate | fold fluence with \(A_{\rm eff}\) | observational count expectation | source physics if used alone |

Formula ID：`AG-CASCADE-APPROX-HIERARCHY-001`。

## 12. 从推导到代码的实现约定

相关现有本地代码：

```text
reproduce/grb/core/radiation/hadronic.py
reproduce/grb/core/radiation/gamma_gamma.py
reproduce/grb/core/radiation/cooling_angle.py
reproduce/grb/core/radiation/production.py
reproduce/grb/events/grb_221009a/scripts/05_tev_ssc_sanity.py
```

当前代码边界：

| Code layer | Existing capability | Boundary |
| --- | --- | --- |
| hadronic teaching helpers | pp threshold, \(p\gamma\) threshold, BH threshold, energy partition | not spectra |
| pp mature route | Kafexhiu-like LUT / `naima.PionDecay` parity | pp gamma only, not neutrinos/cascade |
| proton synchrotron | local / `agnpy`-compatible SED parity | no acceleration feasibility |
| secondary cooling helpers | pion/muon decay time and cooling-vs-decay regime | no secondary spectrum |
| gamma-gamma kernel | Breit-Wheeler and tabulated target opacity | no pair cascade |
| TeV event sanity | SSC / opacity / candidate diagnostics | not an event fit |

本页与当前代码的差异：

- Course formalism starts from \(Q_s\) and coupled transport; current code has threshold, envelope and selected SED helpers.
- Course keeps \(p\gamma\), Bethe-Heitler, secondary pairs and neutrinos as formal integrals; current code does not implement their spectra.
- Course separates internal cascade from EBL/IGM propagation; current code only accepts supplied optical depths or target photon fields.
- Course writes detector event rate as a final convolution; current code does not predict IceCube / KM3NeT / CTA / LHAASO event counts.

未来 helper 候选：

| Suggested helper | Formula ID | Layer |
| --- | --- | --- |
| `secondary_emissivity_integral(...)` | `AG-CASCADE-SECONDARY-EMISSIVITY-001` | future mature-method interface |
| `pion_muon_cooling_break_gamma(...)` | `AG-CASCADE-SECONDARY-COOL-DECAY-001` | teaching/reference |
| `cascade_transport_rhs(...)` | `AG-CASCADE-TRANSPORT-SKELETON-001` | future production candidate |
| `neutrino_flavor_mix(...)` | `AG-NU-FLAVOR-MIXING-001` | teaching/reference |
| `neutrino_event_count(...)` | `AG-NU-EVENT-RATE-BOUNDARY-001` | detector-specific boundary |

在这些 helper 存在并通过验证之前，本页新的 cascade / neutrino Formula IDs 都应读作 theory-only 或 future-helper candidates。

## 13. Benchmark boundary

可用的外部或成熟方法参考：

| Benchmark / reference | Target | Required inputs | Cannot claim |
| --- | --- | --- | --- |
| `naima.PionDecay` | pp gamma-ray benchmark under package convention | proton spectrum, gas density, distance / normalization | full hadronic cascade or neutrino event rate |
| SOPHIA / NeuCosmA / AM3 | photohadronic yield and neutrino-cascade calculation | proton spectrum, photon target field, geometry / escape convention | local default truth or code-backed afterglow solver |
| CRPropa / ELMAG | propagation / electromagnetic cascade benchmark | source spectrum, redshift, EBL, CMB, IGMF, duration | source-local emission mechanism proof |
| IceCube / KM3NeT effective-area products | detector event-count convolution | fluence, sky direction, time window, event class, \(A_{\rm eff}\) | source neutrino flux without detector assumptions |
| Dominguez / Franceschini / Finke / Gilmore EBL tables | \(\tau_{\rm EBL}(E,z)\) model comparison | model name, cosmology convention, redshift and energy grid | unique propagation truth or internal opacity |

Benchmarks 可以测试 convention-matched calculations。若没有完整 model comparison，它们不能把 observed TeV photon 或 neutrino non-detection 变成唯一 source mechanism 结论。

## 14. 不声称

- 不声称当前本地代码已经有 full hadronic / EM cascade solver。
- 不声称当前本地代码已经有 \(p\gamma\) secondary spectra、Bethe-Heitler pair injection spectra、photodisintegration spectra 或 neutrino event-rate predictor。
- 不把 \(E_\nu\simeq0.05E_p\) 写成 neutrino spectrum。
- 不把 \(\tau_{\gamma\gamma}\) 写成 cascade reprocessed flux。
- 不把 `naima`、`agnpy`、SOPHIA、AM3、CRPropa、ELMAG 或任何 EBL table 写成唯一物理标准。
- 不把 GRB 221009A 或其他 TeV GRB 的高能辐射写成唯一 SSC、proton synchrotron、hadronic cascade 或 external IC 起源。

## 15. 参考文献

- Kelner, Aharonian & Bugayov 2006, pp secondary gamma/electron/neutrino parameterization.
- Kafexhiu et al. 2014, pp gamma-ray production near threshold.
- Kelner & Aharonian 2008, photohadronic secondary particle production.
- Muecke et al. / SOPHIA, photohadronic Monte Carlo modeling.
- NeuCosmA and AM3 literature for photohadronic / neutrino-cascade calculations.
- Rybicki & Lightman, charged-particle synchrotron and radiative transfer.
- Gould & Schreder 1967, gamma-gamma absorption.
- CRPropa / ELMAG documentation for propagation and electromagnetic cascade benchmarks.
- IceCube and KM3NeT public effective-area / GRB-neutrino analysis literature for detector-response boundaries.
