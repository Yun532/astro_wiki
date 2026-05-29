# 05 Hadronic Processes, Secondary Particles, and Cascade Boundaries

状态：v2.3 课程讲义草案。本页按 `physical picture -> reaction matrix -> general expression -> detailed derivation blocks -> exact analytic status -> approximation hierarchy -> code convention` 组织。强子过程不能从 threshold helper 或 delta approximation 开始；threshold 只是最小运动学条件，完整辐射谱需要相互作用率、二次粒子 yield、衰变、冷却和 cascade 共同决定。

## 1. 物理图像

高能 protons 或 nuclei 可以通过 gas、photon field 和 magnetic field 产生 gamma rays、neutrinos、pairs 或 secondary electrons：

```text
primary protons / nuclei
  -> pp / pA / AA hadronic collisions
  -> p gamma pion production
  -> Bethe-Heitler pair production
  -> proton / nuclei synchrotron
  -> pion / muon cooling before decay
  -> gamma-gamma absorption and EM cascade
  -> neutrino propagation and flavor mixing
```

本页的核心边界是：本地代码已经有若干可追踪 helper 和 package-compatible pp/proton-synch route，但没有完整 hadronic / EM cascade solver，也没有 \(p\gamma\) Monte Carlo、Bethe-Heitler pair injection table 或 neutrino event-rate predictor。

## 2. 参考系与变量表

本页默认在源区 comoving frame 中写相互作用率；无撇号时可表示局域 comoving quantity，接观测者时需要 Doppler factor、bulk Lorentz factor 和 redshift。已有 helper 的输入单位在代码约定中单独说明。

| 符号 | 含义 | 单位或量纲 |
| --- | --- | --- |
| \(E_p\) | proton energy | GeV / erg |
| \(E_A\) | nucleus energy | GeV / erg |
| \(E_\gamma\) | emitted photon energy | GeV / eV |
| \(\epsilon\) | target photon energy | eV / erg |
| \(n_{\rm gas}\) | gas target density | cm\(^{-3}\) |
| \(n_\gamma(\epsilon)\) | photon number density per energy | cm\(^{-3}\) erg\(^{-1}\) |
| \(N_p(E_p)\) | total proton distribution | particles GeV\(^{-1}\) |
| \(\sigma\) | interaction cross-section | cm\(^2\) |
| \(\kappa\) or \(K\) | inelasticity | dimensionless |
| \(Y_s(E_s;E_a)\) | secondary yield spectrum | per energy |
| \(B'\) | comoving magnetic field | G |
| \(\Gamma\) | bulk Lorentz factor | dimensionless |
| \(z\) | redshift | dimensionless |

## 3. Reaction Matrix

强子页必须先承认通道图谱，再讨论本地实现。下表是课程覆盖矩阵，不等于代码全部实现。

| 通道 | 典型反应 | 主要产物 | 解析/近似层 | 成熟数值方法 | 当前本地层级 |
| --- | --- | --- | --- | --- | --- |
| `pp` | \(p+p\to p+p+\pi^0/\pi^\pm+X\) | gamma、neutrino、secondary e± | threshold、thin-target efficiency、delta pion | Kelner/Aharonian、Kafexhiu、GAMERA、`naima.PionDecay` | production parity for Kafexhiu LUT；teaching delta |
| `pA / AA` | proton 或 nucleus 撞 gas nuclei | enhanced pion secondaries、fragments | nuclear enhancement factor | Mori、Kafexhiu extensions、GAMERA | missing / mature-method candidate |
| `pγ` Delta | \(p+\gamma\to\Delta^+\to p\pi^0,n\pi^+\) | gamma、neutrino、nucleons | Delta threshold、energy partition | SOPHIA、NeuCosmA、AM3、Kelner & Aharonian | teaching threshold only |
| `pγ` higher resonances | \(N^\ast,\Delta^\ast\) resonances | pion channels | resonance sum | SOPHIA/AM3 | missing |
| `pγ` direct pion | \(p+\gamma\to N+\pi\) | pion secondaries | channel-level cross-section | SOPHIA/NeuCosmA | missing |
| `pγ` multi-pion | \(p+\gamma\to N+n\pi\) | broad gamma/neutrino spectra | high-energy parameterization | SOPHIA/AM3 | missing |
| kaon channels | \(p\gamma,pp\to K^\pm/K^0+X\) | high-energy neutrinos | branching/inelasticity approximation | SOPHIA/NeuCosmA/AM3 | missing |
| Bethe-Heitler | \(p+\gamma\to p+e^+e^-\) | pair injection、proton cooling | threshold、loss-rate integral | CRPropa loss tables、specialized BH kernels | teaching threshold only |
| proton synchrotron | \(p+B\to p+\gamma\) | gamma / X-ray depending on \(B,\gamma_p\) | mass-scaled synchrotron kernel | agnpy, GAMERA, JetSeT-like one-zone tools | production parity with agnpy；teaching SED |
| pion/muon synchrotron | \(\pi^\pm,\mu^\pm+B\to\gamma\) before decay | modified neutrino and EM spectrum | compare \(t_{\rm syn}\) vs \(t_{\rm dec}\) | hadronic cascade solvers | teaching helper only |
| nuclei synchrotron | \(A_Z+B\to A_Z+\gamma\) | heavy-nucleus synch emission | \(\nu_A\propto (Z/A)B\gamma^2\) | specialized UHECR tools | teaching helper only |
| photodisintegration | \(A+\gamma\to(A-n)+n\) | fragments、neutrons | giant-dipole-resonance threshold | CRPropa、NeuCosmA | theory-only / missing |
| nuclear de-excitation | excited nucleus \(\to\gamma\) | MeV gamma lines | line energy scale | nuclear tables | theory-only / missing |
| spallation | \(A+p/A\to fragments\) | fragments、secondary nucleons | cross-section tables | CRPropa / cosmic-ray tools | missing |
| EM cascade | \(\gamma\gamma\to e^\pm\), repeated synch/IC | reprocessed gamma spectrum | transport equation | ELMAG、CRPropa、AM3 | not implemented |
| neutrino propagation | oscillation/flavor mixing | detector flavor ratios | PMNS mixing | event-rate tools | not implemented |

Formula ID：`HAD-REACTION-MATRIX-001`，状态：course-derived / audit。

## 4. General Expression：Secondary Emissivity

对任意 primary hadron \(a\) 和 secondary species \(s\)，统一结构是：

$$
Q_s(E_s)
=
\int dE_a\,N_a(E_a)
\int d\chi\,n_{\rm target}(\chi)\,
c\,\mathcal{K}(E_a,\chi)
\frac{dN_s}{dE_s}(E_s;E_a,\chi).
$$

这里：

- \(N_a(E_a)\) 是 primary proton / nucleus spectrum。
- \(\chi\) 可以表示 gas species、target photon energy、collision angle 或 nuclear target。
- \(\mathcal{K}\) 包含 cross-section、relative velocity、inelasticity 或 angular kernel。
- \(dN_s/dE_s\) 是 secondary yield，可能来自 delta approximation、解析参数化、lookup table 或 Monte Carlo。

对于 gas target 的 `pp`：

$$
Q_\gamma^{pp}(E_\gamma)
=
cn_{\rm gas}
\int dE_p\,N_p(E_p)
\frac{d\sigma_{pp\to\gamma}}{dE_\gamma}(E_p,E_\gamma).
$$

对于 photon target 的 \(p\gamma\)，需要 angle / photon energy integration：

$$
R_{p\gamma}(E_p)
=
c\int d\epsilon\,n_\gamma(\epsilon)
\int d\Omega\,(1-\beta_p\mu)
\sigma_{p\gamma}(\bar\epsilon)K_{p\gamma}(\bar\epsilon).
$$

当前本地代码不是完整强子 transport，只实现部分 threshold、efficiency、teaching SED、Kafexhiu LUT pp gamma SED、proton synchrotron SED 和 package-compatible parity。

Formula ID：`HAD-SECONDARY-EMISSIVITY-FORMAL-001`，状态：course-derived / theory-only for full channel set。

## 5. Detailed Derivation I：`pp -> pp pi0` Threshold and Thin-Target Efficiency

### 5.1 目标公式

目标是从 Lorentz invariant 推出 \(pp\to pp\pi^0\) 的 lab-frame kinetic threshold，并写出 thin-target efficiency：

$$
P_{\rm int}
=
1-e^{-n\sigma_{pp}l},
\qquad
f_{pp,\rm loss}
\simeq
\kappa_{pp}(1-e^{-\tau_{pp}}).
$$

### 5.2 阈值推导

设 projectile proton 的 total energy 为 \(E_p\)，target proton 在 lab frame 中静止。四动量不变量：

$$
s
=
(p_1+p_2)^2
=
m_p^2c^4+m_p^2c^4+2m_pc^2E_p.
$$

阈值处末态 \(p+p+\pi^0\) 在 center-of-mass frame 中没有相对动能，因此：

$$
s_{\rm thr}
=
(2m_pc^2+m_\pi c^2)^2.
$$

令两者相等：

$$
2m_p^2c^4+2m_pc^2E_{p,\rm thr}
=
(2m_p+m_\pi)^2c^4.
$$

解出 projectile total energy：

$$
E_{p,\rm thr}
=
\frac{(2m_p+m_\pi)^2-2m_p^2}{2m_p}c^2.
$$

若要 kinetic threshold：

$$
T_{p,\rm thr}
=
E_{p,\rm thr}-m_pc^2.
$$

代码返回 kinetic threshold：

```text
pp_pion_threshold_kinetic_energy_gev()
```

Formula ID：`HAD-PP-THRESHOLD-001`。

### 5.3 Thin/thick target efficiency

mean free path：

$$
\lambda_{pp}
=
\frac{1}{n\sigma_{pp}}.
$$

路径 \(l\) 上的 optical depth：

$$
\tau_{pp}
=
\frac{l}{\lambda_{pp}}
=
n\sigma_{pp}l.
$$

相互作用概率：

$$
P_{\rm int}
=
1-e^{-\tau_{pp}}.
$$

若只关心 energy loss fraction：

$$
f_{pp,\rm loss}
\simeq
\kappa_{pp}P_{\rm int}.
$$

本地 teaching helper 使用 capped approximation：

$$
f_{pp,\rm toy}
=
\min(n\sigma_{pp}l,1).
$$

这保留 thin-target 标度，但不是完整 interaction probability，也不含 energy-dependent \(\sigma_{pp}(E_p)\) 和 \(\kappa(E_p)\)。

代码：`pp_interaction_efficiency()`、`production.py::pp_energy_loss_time()`  
Formula IDs：`HAD-PP-EFF-001`、`COOL-PP-LOSS-TIME-001`。

## 6. `pp` Gamma-Ray Spectrum: Delta Approximation to Kafexhiu LUT

### 6.1 Delta approximation

delta approximation 假设每个 high-energy proton 把固定比例能量给 neutral pion，并最终给两个 photons：

$$
E_\gamma
=
k_\gamma E_p,
\qquad
k_\gamma\sim0.1.
$$

photon production rate 写成：

$$
\frac{dN_\gamma}{dt\,dE_\gamma}
=
\int dE_p\,N_p(E_p)\,
cn_{\rm gas}\sigma_{pp}
N_\gamma^{\rm mult}
\delta(E_\gamma-k_\gamma E_p).
$$

用 delta function 积掉 \(E_p\)。反解：

$$
E_p^\ast
=
\frac{E_\gamma}{k_\gamma}.
$$

Jacobian：

$$
\delta(E_\gamma-k_\gamma E_p)
=
\frac{1}{k_\gamma}
\delta\left(E_p-\frac{E_\gamma}{k_\gamma}\right).
$$

因此：

$$
\frac{dN_\gamma}{dt\,dE_\gamma}
=
N_p(E_p^\ast)
cn_{\rm gas}\sigma_{pp}
\frac{N_\gamma^{\rm mult}}{k_\gamma}.
$$

SED：

$$
E_\gamma^2F_{E_\gamma}
=
\frac{E_\gamma^2}{4\pi d^2}
\frac{dN_\gamma}{dt\,dE_\gamma}.
$$

代码：`CutoffPowerLawProtons`、`pp_delta_pion_decay_sed_erg_cm2_s()`  
Formula IDs：`HAD-PROTON-CUTOFF-PL-001`、`HAD-PP-DELTA-SED-001`。

### 6.2 Mature parameterization / LUT

成熟 \(pp\) gamma-ray spectrum 不把所有 photons 放在 \(0.1E_p\)，而是使用：

$$
q_\gamma(E_\gamma)
=
cn_H
\int dE_p\,J_p(E_p)
\frac{d\sigma(E_p,E_\gamma)}{dE_\gamma}.
$$

本地 production parity 的 Kafexhiu14 LUT route 实现这个结构：

```text
pp_kafexhiu_lut_pion_decay_sed_erg_cm2_s()
production.py::pp_pion_decay_sed_naima_parity()
```

validation adapter 显式传入 `naima` 安装包中的 Kafexhiu14 LUT 文件；core 不 import `naima`。这能对齐 `naima.PionDecay` 的 package-compatible convention，但仍不包含 \(p\gamma\)、Bethe-Heitler、charged-pion neutrino spectrum、secondary pairs 或 cascade。

Formula ID：`HAD-PP-KAFEXHIU-LUT-SED-001`。

## 7. Detailed Derivation II：\(p\gamma\) Threshold and Interaction-Rate Integral

### 7.1 Delta-resonance threshold

核心通道：

$$
p+\gamma\to\Delta^+\to
\begin{cases}
p+\pi^0,\\
n+\pi^+.
\end{cases}
$$

在 proton rest frame 中，target photon 达到 Delta resonance：

$$
\bar{\epsilon}_{\gamma,\Delta}
\sim
0.3\,{\rm GeV}.
$$

对 head-on photon：

$$
\bar{\epsilon}_\gamma
=
\gamma_p'\epsilon_\gamma'(1-\beta_p\cos\theta')
\simeq
2\gamma_p'\epsilon_\gamma'.
$$

数量级上：

$$
E_p'\epsilon_\gamma'
\sim
0.3\,{\rm GeV^2}.
$$

observer 与 comoving frame 近似关系：

$$
E_p
\simeq
\frac{\Gamma E_p'}{1+z},
\qquad
\epsilon_\gamma
\simeq
\frac{\Gamma \epsilon_\gamma'}{1+z}.
$$

相乘：

$$
E_p\epsilon_\gamma
\sim
\frac{\Gamma^2}{(1+z)^2}
0.3\,{\rm GeV^2}.
$$

所以：

$$
E_{p,\rm thr}
\sim
\frac{0.3\,{\rm GeV^2}\Gamma^2}
{(1+z)^2\epsilon_\gamma}.
$$

代码：`pgamma_threshold_proton_energy_gev()`  
Formula ID：`HAD-PGAMMA-THRESHOLD-001`。

### 7.2 Isotropic photon field rate

在 comoving frame 中，若 photon field 近似各向同性，proton Lorentz factor 为 \(\gamma_p\)，常用 interaction-rate integral 是：

$$
t_{p\gamma}^{-1}(\gamma_p)
=
\frac{c}{2\gamma_p^2}
\int_{\bar{\epsilon}_{\rm thr}}^\infty
d\bar{\epsilon}\,
\sigma_{p\gamma}(\bar{\epsilon})
K_{p\gamma}(\bar{\epsilon})
\bar{\epsilon}
\int_{\bar{\epsilon}/(2\gamma_p)}^\infty
d\epsilon\,
\frac{n_\gamma(\epsilon)}{\epsilon^2}.
$$

这个式子的内层积分下限来自：

$$
\bar{\epsilon}
=
\gamma_p\epsilon(1-\beta_p\mu)
\le
2\gamma_p\epsilon.
$$

所以给定 proton-rest-frame photon energy \(\bar\epsilon\)，lab/comoving photon 必须满足：

$$
\epsilon
\ge
\frac{\bar\epsilon}{2\gamma_p}.
$$

Delta approximation 把：

$$
\sigma_{p\gamma}K_{p\gamma}
\rightarrow
\sigma_\Delta K_\Delta\Delta\bar{\epsilon}\,
\delta(\bar{\epsilon}-\bar{\epsilon}_\Delta).
$$

这才退化为 threshold/envelope 直觉。higher resonances、direct pion、multi-pion 和 kaon channels 都是把这个 kernel 从一个 delta peak 扩展为多通道 yield。

当前代码只有 threshold/envelope，没有 \(p\gamma\) spectrum、cooling table 或 cascade。

Formula ID：`HAD-PGAMMA-RATE-INTEGRAL-001`，状态：course-derived / theory-only。

## 8. Pion Energy Partition and Neutrino Scale

若一次 hadronic interaction 中 fraction \(f_\pi\) 的 proton energy 进入 pion：

$$
E_\pi
\simeq
f_\pi E_p.
$$

neutral pion：

$$
\pi^0\to\gamma+\gamma,
\qquad
E_{\gamma,\pi^0}
\simeq
\frac{E_\pi}{2}
\simeq
0.5f_\pi E_p.
$$

默认 \(f_\pi=0.2\) 时：

$$
E_{\gamma,\pi^0}
\simeq
0.1E_p.
$$

charged pion chain：

$$
\pi^+\to\mu^++\nu_\mu,
\qquad
\mu^+\to e^++\nu_e+\bar\nu_\mu.
$$

几个 leptons 共享 pion energy，常用数量级：

$$
E_\nu
\simeq
\frac{E_\pi}{4}
\simeq
0.25f_\pi E_p
\simeq
0.05E_p.
$$

代码：`pion_decay_gamma_energy_gev()`、`neutrino_energy_from_proton_gev()`  
Formula IDs：`HAD-PI0-GAMMA-SCALE-001`、`HAD-NU-SCALE-001`。

这些 helper 不产生 gamma/neutrino spectrum，不预测 detector event rate，也不处理 flavor mixing。

## 9. Bethe-Heitler Pair Production

Bethe-Heitler 通道：

$$
p+\gamma\to p+e^++e^-.
$$

阈值在 proton rest frame 中约为：

$$
\bar{\epsilon}_\gamma
\ge
2m_ec^2.
$$

沿用 observer/comoving 约定，可得到 threshold helper：

$$
E_{p,\rm BH}^{\rm thr}
\epsilon_\gamma
\sim
2m_em_pc^4
\frac{\Gamma^2}{(1+z)^2}.
$$

由于 \(2m_ec^2\ll0.3\,{\rm GeV}\)，同一 photon field 下：

$$
E_{p,\rm BH}^{\rm thr}
\ll
E_{p,\pi}^{\rm thr}.
$$

但 BH 的 inelasticity 很小，完整 cooling 和 pair injection 来自大量小能损事件。formal pair injection 是：

$$
Q_{e^\pm}(E_e)
=
\int dE_p\,N_p(E_p)
\int d\epsilon\,n_\gamma(\epsilon)
\int d\mu\,(1-\beta\mu)c
\frac{d\sigma_{\rm BH}}{dE_e}.
$$

当前本地只实现 threshold helper，不实现 pair injection spectrum、BH cooling table 或 secondary pair cascade。

代码：`bethe_heitler_threshold_proton_energy_gev()`  
Formula IDs：`HAD-BH-THRESHOLD-001`、`HAD-BH-PAIR-INJECTION-FORMAL-001`。

## 10. Proton and Heavy-Particle Synchrotron

任意带电粒子的 synchrotron characteristic frequency：

$$
\nu_{\rm syn}'
\simeq
\frac{3qB'}{4\pi mc}\gamma^2.
$$

observer frame：

$$
\nu_{\rm obs}
\simeq
\frac{\Gamma}{1+z}\nu_{\rm syn}'.
$$

对 proton：

$$
\nu_{p,\rm syn}
\simeq
\frac{\Gamma}{1+z}
\frac{3eB'}{4\pi m_pc}\gamma_p^2.
$$

与 electron synchrotron 相比，在相同 \(\gamma\) 和 \(B\) 下：

$$
\frac{\nu_{p,\rm syn}}{\nu_{e,\rm syn}}
=
\frac{m_e}{m_p}.
$$

proton synchrotron 进入 high-energy band 通常要求极高 \(\gamma_p\) 或很强 \(B'\)。本地有两层：

- teaching/reference：`proton_synchrotron_sed_erg_cm2_s()` 对总质子谱和单粒子 synchrotron kernel 积分。
- package-compatible：`production.py::proton_synchrotron_sed_agnpy_one_zone_parity()` 对齐 `agnpy.ProtonSynchrotron` one-zone convention。

这些都不自动求最大加速能量，不处理 secondary pairs，不实现 cascade。

Formula IDs：`HAD-PROTON-SYN-001`、`HAD-PROTON-SYN-PNU-001`、`HAD-PROTON-SYN-SED-001`、`HAD-AGNPY-COMPAT-PROTON-SYN-001`。

对 charge \(Ze\)、mass \(A m_p\) 的 nucleus：

$$
\nu_A
\simeq
\frac{\Gamma}{1+z}
\frac{3ZeB'}{4\pi A m_pc}\gamma_A^2,
\qquad
\frac{\nu_A}{\nu_p}
\simeq
\frac{Z}{A}.
$$

代码：`nucleus_synchrotron_frequency_hz()`  
Formula ID：`HAD-NUCLEUS-SYN-NU-001`。

heavy nuclei 还会发生 photodisintegration、spallation 和 de-excitation gamma，这些不是 synchrotron kernel 能单独回答的问题。

## 11. Charged Pion / Muon Cooling Before Decay

charged pion 与 muon 不一定总是“立刻衰变”。在强磁场中，它们可能先 synchrotron cooling：

$$
t_{\rm dec}
=
\gamma\tau_0.
$$

带电粒子 synchrotron cooling time 可写作：

$$
t_{\rm syn}
=
\frac{\gamma mc^2}{P_{\rm syn}}
\propto
\frac{m^3}{q^4B^2\gamma}.
$$

比较：

$$
\mathcal{R}_{\rm cool/dec}
=
\frac{t_{\rm syn}}{t_{\rm dec}}.
$$

若 \(\mathcal{R}<1\)，secondary synchrotron cooling 会在 decay 之前发生，neutrino spectrum 和 EM cascade 都会改变。当前 helper 只输出 regime，不输出完整 secondary spectrum。

代码：

```text
charged_pion_decay_time_s()
muon_decay_time_s()
charged_particle_synchrotron_cooling_time_s()
synchrotron_cooling_to_decay_ratio()
secondary_synchrotron_decay_regime()
```

Formula IDs：`HAD-DECAY-TIME-001`、`HAD-PION-DECAY-TIME-001`、`HAD-MUON-DECAY-TIME-001`、`HAD-CHARGED-PARTICLE-SYN-COOL-TIME-001`、`HAD-SYN-DECAY-RATIO-001`、`COOL-HAD-SECONDARY-DECAY-REGIME-001`。

## 12. Hadronic / EM Cascade Boundary

完整 hadronic / EM cascade 至少包含：

```text
primary proton/nuclei injection
  -> pp / p gamma / Bethe-Heitler interactions
  -> pion / muon decay
  -> gamma rays / neutrinos / e±
  -> gamma-gamma absorption
  -> pair synchrotron / IC
  -> repeated EM cascade
  -> propagation attenuation
```

这个系统通常没有短闭式解析解，需要 Monte Carlo、transport solver、tabulated kernels 或 hybrid cascade code。当前本地不实现 hadronic / EM cascade，也不预测 neutrino event rate。

## 13. Exact Analytic Status

| 对象 | 解析状态 | 本地状态 |
| --- | --- | --- |
| pp threshold | 闭式 kinematics | teaching/reference helper |
| pp thin-target efficiency | 闭式 envelope | teaching/order-of-magnitude |
| pp gamma spectrum | 一般无短闭式；需 yield parameterization | delta helper + Kafexhiu LUT parity |
| \(p\gamma\) threshold | 闭式数量级 | teaching threshold |
| \(p\gamma\) interaction rate | formal integral；通常数值 | theory-only |
| Bethe-Heitler threshold | 闭式数量级 | teaching threshold |
| Bethe-Heitler pair injection | formal integral；通常数值 | theory-only |
| proton synchrotron kernel | 可数值积分 | teaching + agnpy parity |
| pion/muon cooling-vs-decay | closed regime ratio | teaching-only |
| photodisintegration / spallation | cross-section tables / transport | missing |
| hadronic / EM cascade | transport problem | missing |

## 14. Approximation Hierarchy

| 层级 | 做法 | 可声称 | 不能声称 |
| --- | --- | --- | --- |
| threshold scale | 只算最小能量条件 | 判断能区是否可能 | spectrum / rate |
| energy partition | \(E_\gamma\sim0.1E_p\), \(E_\nu\sim0.05E_p\) | characteristic scale | yield distribution |
| delta approximation | \(\delta(E_\gamma-kE_p)\) | teaching SED slope / sanity check | calibrated pion-decay spectrum |
| mature parameterization | Kelner/Kafexhiu/Baring-like formula or LUT | one-zone spectrum under stated convention | full cascade |
| package-compatible parity | 复刻 `naima` / `agnpy` convention | same-parameter numerical parity | unique physics standard |
| transport / cascade | coupled secondaries and absorption | full process within model assumptions | automatic event proof |

## 15. 从推导到代码的实现约定

当前代码层分为：

| 层级 | 内容 | 代码/输出 | 边界 |
| --- | --- | --- | --- |
| teaching threshold/envelope | pp threshold、pγ/BH threshold、energy partition、pp efficiency | `hadronic.py`, `teaching.py` | order-of-magnitude |
| teaching spectra | pp delta SED、proton synchrotron reference SED | `pp_delta_pion_decay_sed_erg_cm2_s()`, `proton_synchrotron_sed_erg_cm2_s()` | no cascade / no acceleration limit |
| mature numerical method | Kafexhiu14 LUT pp gamma-ray SED | `pp_kafexhiu_lut_pion_decay_sed_erg_cm2_s()` | pp gamma only |
| package-compatible | `naima.PionDecay`, `agnpy.ProtonSynchrotron` parity | `production.py` wrappers | benchmark-output / convention-specific |
| missing | pγ spectrum, BH injection, photodisintegration, EM cascade, neutrino event rate | none | must not claim |

如果后续使用成熟参数化，课程页必须记录替换关系：

$$
\text{characteristic energy scale}
\rightarrow
\frac{dN_s}{dE_s}(E_s;E_p)
\text{ parameterization}.
$$

如果后续使用 cascade solver，课程页必须记录：

$$
Q_s(E_s)
\rightarrow
\text{coupled transport equations for }p,\gamma,e^\pm,\nu,A.
$$

曲线差异常来自 cross-section、inelasticity、low-energy threshold treatment、nuclear enhancement factor、target photon field、secondary cooling、cascade treatment、EBL attenuation、particle distribution normalization 和 package-specific density convention。

## 16. Benchmark Boundary

当前可对照：

- `naima.PionDecay`：pp neutral-pion gamma-ray benchmark / Kafexhiu LUT convention。
- `agnpy.ProtonSynchrotron`：one-zone proton synchrotron benchmark。
- GAMERA、SOPHIA、NeuCosmA、AM3、CRPropa、ELMAG：future external benchmark candidates for hadronic/cascade subproblems。

这些 benchmark 不能替代 GRB jet hydrodynamics、\(p\gamma\) cascade、neutrino event-rate prediction、flavor mixing 或 EBL reprocessing。

Formula ID：`HAD-NAIMA-PIONDECAY-BENCHMARK-001`，状态：benchmark-output。

## 17. 代码与验证

代码：

```text
reproduce/grb/core/radiation/hadronic.py
reproduce/grb/core/radiation/agnpy_compat.py
reproduce/grb/core/radiation/production.py
reproduce/grb/core/radiation/teaching.py
```

验证：

```text
python -m reproduce.grb.validation.check_radiation_mechanisms_v1
python -m reproduce.grb.validation_lab.check_hadronic_course_v4
python -m reproduce.grb.validation_lab.check_radiation_cooling_angle_v1
python -m reproduce.grb.validation_lab.check_radiation_package_parity_v3
python -m reproduce.grb.validation_lab.check_radiation_production_suite_v1
```

验证重点：

- \(p\gamma\) threshold 随 target photon energy 增大而下降。
- Bethe-Heitler threshold 低于 pion-production threshold。
- pp efficiency capped at 1。
- pion gamma/neutrino energy partition 是数量级。
- proton synchrotron frequency 随 \(\gamma_p^2\) 增长。
- Kafexhiu LUT pp route 与 `naima.PionDecay` 在同 convention 下对齐。
- agnpy proton synchrotron route 与 `agnpy.ProtonSynchrotron` 在同 convention 下对齐。

## 18. 不声称

- 不声称完成 hadronic / EM cascade。
- 不声称 TeV origin 是 hadronic。
- 不预测 neutrino event rate。
- 不声称 \(p\gamma\) spectrum 或 Bethe-Heitler pair injection 已实现。
- 不内置 SOPHIA/AM3/GAMERA/CRPropa/ELMAG 为本地 API。
- 不把 benchmark-output 写成事件物理结论。

## 19. 参考来源

- Kelner, Aharonian & Bugayov 2006, pp secondary gamma/electron/neutrino parameterization。
- Kafexhiu et al. 2014, pp gamma-ray production near threshold。
- Kelner & Aharonian 2008, pγ secondary particle production。
- SOPHIA / NeuCosmA / AM3 photohadronic modeling literature。
- Rybicki & Lightman, synchrotron mass scaling。
- `naima.PionDecay`、`agnpy.ProtonSynchrotron`、GAMERA、CRPropa / ELMAG documentation as benchmark references。
