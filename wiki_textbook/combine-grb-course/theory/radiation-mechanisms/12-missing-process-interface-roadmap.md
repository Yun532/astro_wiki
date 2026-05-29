# 12 缺口过程接口路线图

状态：v0.1 旧内容补充页。本页不是新的辐射机制推导，也不是 production solver 设计文档，而是把 09 页列出的核心缺口整理成可执行的接口路线图：下一步若要补 self-consistent SSC、anisotropic IC、\(p\gamma\)、Bethe-Heitler、EM cascade、neutrino event-rate 或 relativistic photosphere，应从什么 general expression 开始，需要哪些输入，输出是什么，哪些 benchmark 可以用，不能声称什么。

核心原则：缺口不是空白许可证。不能因为某个过程还没有本地 solver，就从最方便的 delta approximation 或 package 输出开始；也不能因为外部软件能跑，就把外部 convention 当成本课程理论起点。本页只建立下一阶段的安全入口。

## 1. 物理图像

当前辐射机制章已经有 synchrotron、SSA、IC、SSC hierarchy、gamma-gamma、thermal/free-free、pp gamma、proton synchrotron、source-agnostic cooling 与 accelerator screening。真正还没进入完整 solver 的，是互相耦合、依赖角分布、依赖外部核函数或需要输运方程的过程：

```text
synchrotron photons
  -> SSC transfer with SSA / escape / KN feedback
  -> anisotropic IC if seed field is directional

accelerated hadrons
  -> p gamma / Bethe-Heitler / photodisintegration
  -> pions / muons / pairs / neutrinos
  -> gamma-gamma absorption
  -> EM cascade
  -> propagation and detector response
```

Formula ID：`RAD-GAP-PROCESS-MAP-001`。

## 2. 缺口优先级与安全起点

| Priority | 缺口 | 安全理论起点 | 不能从哪里开始 |
| --- | --- | --- | --- |
| P1 | self-consistent SSC transfer | synchrotron emissivity / transfer 得到 \(n_{\rm syn}\)，再进 IC kernel 和 cooling equation | broken-power-law SSC peak 或 \(Y\) toy iteration |
| P1 | anisotropic IC | angle-dependent photon distribution \(n(\epsilon,\Omega)\) 与 differential Compton kernel | head-on/tail-on teaching factor |
| P1 | \(p\gamma\) spectra | \(\bar\epsilon=\gamma_p\epsilon(1-\beta\mu)\) 的 rate integral 与 secondary yield | \(E_\nu=0.05E_p\) |
| P1 | Bethe-Heitler pair injection | \(p+\gamma\to p+e^+e^-\) differential yield / loss kernel | threshold-only helper |
| P1 | EM cascade | coupled photon-pair transport equations | \(F_{\rm esc}=F_{\rm int}e^{-\tau}\) |
| P2 | neutrino event-rate | source fluence + flavor mixing + detector \(A_{\rm eff}\) convolution | neutrino non-detection narrative |
| P2 | relativistic photosphere | radiative transfer in moving outflow + optical depth surface | blackbody radius scale |
| P3 | nuclei / photodisintegration / spallation | nuclear cross-section matrix and fragment yields | mass-scaled proton formulas |

Formula ID：`RAD-GAP-PRIORITY-MATRIX-001`。

## 3. Interface Contract I：Self-Consistent SSC

完整 SSC 不应从 \(\nu_{\rm IC}\sim\gamma^2\nu_{\rm syn}\) 开始，而应从 synchrotron photon field 开始。最小接口应分四层：

| 层 | 输入 | 输出 | 说明 |
| --- | --- | --- | --- |
| synchrotron source | \(n_e(\gamma)\), \(B\), geometry, pitch convention | \(j_\epsilon^{\rm syn}\), \(\alpha_\epsilon^{\rm syn}\) | SSA 不能事后随便补 |
| photon transport | \(j_\epsilon,\alpha_\epsilon,R\), escape model | \(n_{\rm syn}(\epsilon)\) | one-zone escape 是近似，不是定义 |
| IC emission | \(n_e(\gamma)\), \(n_{\rm syn}(\epsilon)\), IC/KN kernel | \(j_{\epsilon_s}^{\rm SSC}\) | delta approximation 只作 sanity check |
| cooling feedback | synch + IC cooling integral | updated \(n_e(\gamma,t)\) 或 \(\gamma_c\) | \(Y\) 一般随 \(\gamma\) 变 |

对应 formal structure 是

$$
j_{\epsilon_s}^{\rm SSC}
\propto
\epsilon_s
\int d\gamma\,n_e(\gamma)
\int d\epsilon\,n_{\rm syn}(\epsilon)
c\,{d\sigma_{\rm IC}\over d\epsilon_s}.
$$

Formula ID：`RAD-GAP-SSC-INTERFACE-001`。

代码边界：已有 `ssc_one_zone_tabulated_sed_erg_cm2_s` 可以作为 supplied seed-field numerical kernel，不是 self-consistent SSC transfer。下一步如果实现，应把 seed-field builder、IC kernel、cooling feedback 拆成显式层，而不是在一个函数里隐藏全部 convention。

## 4. Interface Contract II：Anisotropic IC

各向异性 IC 的理论对象不是一个 scalar \(U_{\rm ph}\)，而是 photon phase-space distribution：

$$
n_{\rm ph}(\epsilon,\Omega).
$$

emissivity 的结构应保留角积分：

$$
j_{\epsilon_s}(\Omega_s)
=
\epsilon_s c
\int d\gamma\,n_e(\gamma)
\int d\epsilon
\int d\Omega\,
n_{\rm ph}(\epsilon,\Omega)
{d\sigma_{\rm IC}\over d\epsilon_s d\Omega_s}.
$$

Formula ID：`RAD-GAP-ANISO-IC-INTERFACE-001`。

最小实现接口应至少要求：

| 输入 | 必需性 | 备注 |
| --- | --- | --- |
| electron distribution | 必需 | 可先各向同性 |
| photon energy grid | 必需 | per energy number density |
| photon angle grid / moments | 必需 | 不能只给 \(U_{\rm ph}\) |
| observer / scattering direction | 必需 | 决定 beaming 和 spectrum |
| kernel convention | 必需 | Jones / Aharonian-Atoyan / package convention 必须写清 |

当前 `anisotropic_ic_geometry_factor` 只能保留 teaching factor，不能升级成 anisotropic IC solver。

## 5. Interface Contract III：\(p\gamma\) 与 Bethe-Heitler

\(p\gamma\) 的安全起点是 proton rest-frame photon energy：

$$
\bar\epsilon
=
\gamma_p\epsilon(1-\beta_p\mu).
$$

各向同性 photon field 下的 energy-loss rate 可压缩成

$$
t_{p\gamma}^{-1}(\gamma_p)
=
{c\over2\gamma_p^2}
\int_{\bar\epsilon_{\rm thr}}^\infty d\bar\epsilon\,
\sigma_{p\gamma}(\bar\epsilon)K(\bar\epsilon)\bar\epsilon
\int_{\bar\epsilon/(2\gamma_p)}^\infty
d\epsilon\,{n_\gamma(\epsilon)\over\epsilon^2}.
$$

但 secondary spectra 不能只靠 \(K\)。它需要 yield：

$$
Q_s(E_s)
=
\int dE_p\,N_p(E_p)
\int d\epsilon\,d\mu\,
n_\gamma(\epsilon)
{1-\beta_p\mu\over2}c\,
{d\sigma_{p\gamma\to s}\over dE_s}.
$$

Formula ID：`RAD-GAP-PGAMMA-BH-INTERFACE-001`。

Bethe-Heitler 也应使用 pair injection / loss kernel，而不是 threshold-only helper。SOPHIA、NeuCosmA、AM3、Kelner-Aharonian-style parameterizations 可以作为 mature-method candidates，但每一个都必须记录 channel coverage、energy range、inelasticity convention 和 output species。

## 6. Interface Contract IV：EM Cascade

EM cascade 的最小状态变量不是一个 photon attenuation factor，而是一组 coupled distributions：

$$
\mathbf{N}
=
\{N_\gamma(E,t),\,N_{e^-}(\gamma,t),\,N_{e^+}(\gamma,t)\}.
$$

schematic transport 为

$$
{\partial N_\gamma\over\partial t}
=
Q_\gamma
-{N_\gamma\over t_{\rm esc,\gamma}}
-c\alpha_{\gamma\gamma}N_\gamma
+Q_{\gamma,{\rm IC/syn}},
$$

$$
{\partial N_e\over\partial t}
=
Q_e
-{\partial\over\partial\gamma}(\dot\gamma N_e)
-{N_e\over t_{\rm esc,e}}
+Q_{e,\gamma\gamma}.
$$

Formula ID：`RAD-GAP-CASCADE-INTERFACE-001`。

最小实现可以从 steady-state one-zone 开始，但必须显式记录：

| 选择 | 影响 |
| --- | --- |
| time-dependent vs steady-state | transient GRB 中差异很大 |
| synchrotron-dominated vs IC-dominated pair cooling | 决定 cascade bump 位置 |
| internal vs intergalactic cascade | 目标场、磁场、时间延迟完全不同 |
| escape model | 影响 normalization 和 spectral shape |
| energy conservation check | 防止数值 cascade 虚增能量 |

## 7. Interface Contract V：Neutrino Event Rate

neutrino emission 与 detector event rate 要分开。source-side fluence \(\Phi_\nu\) 经过 flavor mixing 后，event count 才是

$$
N_{\rm ev}
=
\int dE_\nu\,d\Omega\,dt\,
\Phi_\nu(E_\nu,\Omega,t)
A_{\rm eff}(E_\nu,\Omega,{\rm class})
P_{\rm sel}(E_\nu,\Omega,t).
$$

Formula ID：`RAD-GAP-NU-EVENT-INTERFACE-001`。

因此 event-rate helper 不能只输入一个 total neutrino energy。至少要有 energy grid、sky direction、time window、flavor convention、effective area、event class 和 selection assumption。IceCube / KM3NeT public effective-area products 是 detector boundary，不是 source theory。

## 8. Interface Contract VI：Relativistic Photosphere

blackbody / photosphere scale helper 只给 effective radius 或 temperature。完整 relativistic photosphere 至少需要 optical-depth surface：

$$
\tau(r,\theta)
=
\int_r^\infty \kappa \rho' \Gamma(1-\beta\cos\theta)\,ds
\sim 1,
$$

以及 moving surface 上的 Doppler-boosted transfer：

$$
I_\nu
=
\delta_D^3 I'_{\nu'},
\qquad
\nu=\delta_D\nu'/(1+z).
$$

Formula ID：`RAD-GAP-PHOTOSPHERE-INTERFACE-001`。

下一步若补 photosphere，应先声明 outflow model、opacity source、dissipation / heating convention、equal-arrival integration 和 spectral broadening mechanism。不能把 single-temperature blackbody 拟合半径写成物理 photospheric radius。

## 9. Benchmark 路线

| 缺口 | 可选 mature route | 使用方式 | 不能替代 |
| --- | --- | --- | --- |
| anisotropic IC | literature kernels / specialized packages | same-input kernel parity | 课程推导 |
| \(p\gamma\) | SOPHIA, NeuCosmA, AM3 | yield / spectrum benchmark | 本地默认标准 |
| Bethe-Heitler | Kelner-Aharonian-like loss / pair yield | loss / injection benchmark | full cascade |
| EM cascade | ELMAG, CRPropa, AM3 | propagation / cascade comparison | source-local transfer |
| neutrino detector | IceCube / KM3NeT effective areas | event-count convolution | source flux prediction |
| photosphere | radiative-transfer papers / specialized GRB codes | convention comparison | blackbody toy correction |

Formula ID：`RAD-GAP-BENCHMARK-ROUTE-001`。

## 10. 从路线图到代码的约定

任何新增 solver 前，必须先新增或更新：

```text
theory/radiation-mechanisms/formula-index.md
theory/radiation-mechanisms/09-course-completeness-audit.md
agents/memory/*
agents/task-ledger.md
PROJECT_MEMORY.md
```

新增代码应把接口层拆开：

| 层 | 命名建议 | 含义 |
| --- | --- | --- |
| kernel | `*_kernel`, `*_differential_cross_section` | 单次相互作用 |
| field builder | `*_seed_field`, `*_target_field` | 目标场 convention |
| transport rhs | `*_transport_rhs` | 方程右端 |
| solver | `solve_*`, `evolve_*` | 数值求解器 |
| benchmark adapter | `*_compatible`, `*_adapter` | 外部 convention 对齐 |

Formula ID：`RAD-GAP-CODE-CONTRACT-001`。

## 11. 不声称

- 不声称本页实现了任何缺口 solver。
- 不声称 P1 比 P2 更“真实”；优先级只表示当前工程和课程风险。
- 不声称 external package 的输出是观测事实。
- 不声称 threshold、delta approximation、effective opacity 或 event non-detection 足以替代 spectrum / transport / likelihood。
- 不声称 GRB、AGN、PWN、SNR 等源类可以共用同一个 geometry adapter。

## 12. 参考入口

- `02-inverse-compton-and-ssc.md`
- `03-gamma-gamma-opacity.md`
- `04-thermal-and-bremsstrahlung.md`
- `05-hadronic-order-of-magnitude.md`
- `09-course-completeness-audit.md`
- `11-source-agnostic-foundation-and-acceleration.md`
- `../grb-afterglow/10-ssc-and-tev-afterglow.md`
- `../grb-afterglow/12-cascade-neutrino-and-propagation-boundaries.md`
