# 辐射机制课程与数值核索引

状态：v2.3 Docs-first / numerical-kernel 体系。默认中文写作；公式、变量、函数名、论文题名、package 名保留英文。

本目录的目标不是堆公式结果，而是建立一条可追踪链：

```text
radiative-transfer 公理层
  -> 机制级 j_nu / alpha_nu / cooling / opacity / injection
  -> numerical/reference kernels
  -> Python helper
  -> fixed-point validation
  -> GRB 221009A event-trend diagnostic
```

因此每个机制页都要回答四件事：公式从哪里来、代码调用哪一个近似、成熟数值方法和课程推导有什么差异、事件诊断不能声称什么。

统一页面结构为：

```text
物理图像
  -> general expression
  -> detailed derivation block
  -> exact analytic status
  -> analytic / semi-analytic limits
  -> mature numerical methods
  -> code implementation convention
  -> benchmark boundary
```

## 分章入口

- [00 Radiative Transfer Foundations](00-radiative-transfer-foundations.md)
- [01 Synchrotron and Synchrotron Self-Absorption](01-synchrotron-and-ssa.md)
- [02 Inverse Compton and Synchrotron Self-Compton](02-inverse-compton-and-ssc.md)
- [03 Gamma-Gamma Opacity](03-gamma-gamma-opacity.md)
- [04 Thermal Components and Thermal Bremsstrahlung](04-thermal-and-bremsstrahlung.md)
- [05 Hadronic Order-of-Magnitude Interfaces](05-hadronic-order-of-magnitude.md)
- [06 Leptonic Reference Spectra and Open Benchmarks](06-leptonic-reference-spectra-and-naima.md)
- [07 Open-Source Benchmark Matrix](07-open-source-benchmark-matrix.md)
- [08 v3 Package-Compatible Parity Report](08-v3-package-parity-report.md)
- [09 Course Completeness Audit](09-course-completeness-audit.md)
- [10 Production Code Validation Report](10-production-code-validation-report.md)
- [11 Source-Agnostic Foundation and Accelerator Screening](11-source-agnostic-foundation-and-acceleration.md)
- [12 缺口过程接口路线图](12-missing-process-interface-roadmap.md)
- [13 Self-Consistent SSC Transfer](13-self-consistent-ssc-transfer.md)
- [14 各向异性 Inverse Compton 接口](14-anisotropic-inverse-compton-interface.md)
- [15 Photohadronic 与 Bethe-Heitler 接口](15-photohadronic-and-bethe-heitler-interface.md)
- [16 Electromagnetic Cascade Transport 接口](16-electromagnetic-cascade-transport-interface.md)
- [17 Neutrino Fluence 与 Event-Rate 接口](17-neutrino-fluence-and-event-rate-interface.md)
- [18 Relativistic Photosphere Transfer 接口](18-relativistic-photosphere-transfer-interface.md)
- [公式索引](formula-index.md)

## 机制覆盖速查

这张表只回答“已经写到什么层级”，不把课程推导、production code、benchmark parity 和事件解释混成一件事。

| 过程 | 当前覆盖层级 | 代码 / 验证状态 | 不能声称 |
| --- | --- | --- | --- |
| radiative transfer | 公理层与不变量 | theory / trace | 不是具体机制 solver |
| synchrotron | 讲义级推导 + numerical kernel | naima / agnpy parity，cooling fixed point | full polarized transfer |
| synchrotron self-absorption | 讲义级推导 + slab / source-function toy | radio SSA diagnostic | 非均匀 transfer 或完整成像 |
| inverse Compton | 讲义级推导 + BG/KN kernel；各向异性 IC 接口已展开 | naima CMB IC parity，fixed point；各向异性仍 theory-only | full anisotropic IC solver |
| SSC | formal hierarchy + self-consistent transfer 接口页 | agnpy one-zone parity / toy feedback | self-consistent SSC solver |
| gamma-gamma opacity | Breit-Wheeler + isotropic target integral | mono / tabulated target production smoke | 内置 EBL 或 cascade |
| blackbody / thermal component | Planck / effective photosphere scale；relativistic photosphere transfer 接口已展开 | local fixed point；moving photosphere 仍 theory-only | full relativistic photosphere solver |
| thermal free-free | emissivity / absorption / cooling | local fixed point | relativistic Gaunt-table solver |
| nonthermal bremsstrahlung | formal boundary + package-compatible route | naima Baring99 parity | full cooling parity |
| pp pion decay | pp gamma SED mature route | naima / Kafexhiu parity | neutrino / secondary \(e^\pm\) spectrum complete |
| \(p\gamma\) | threshold + rate integral boundary；photohadronic yield 接口已展开 | theory / teaching envelope | production spectrum 或 full cooling table |
| Bethe-Heitler | threshold + pair injection formal boundary；BH loss / pair-injection 接口已展开 | theory / teaching envelope | pair injection / cooling spectrum |
| proton synchrotron | mass-scaled synchrotron SED | agnpy parity | acceleration feasibility proof |
| pion / muon synchrotron | cooling-vs-decay regime | teaching / local fixed point | secondary spectra |
| nuclei / photodisintegration / spallation | reaction matrix boundary | limited helper | full nuclear cascade |
| EM cascade / neutrino propagation | EM cascade transport 与 neutrino event-rate 接口已展开 | theory-only | full cascade 或 event-rate predictor |
| source-agnostic fields / cooling / acceleration | 局域场量、cooling arrays、Hillas/Bohm screening | foundation / acceleration checks | source geometry、transport、UHECR proof |

## v2 数值核地图

| 层级 | 机制 | v2 Formula ID | 代码入口 | 验证/事件输出 | 边界 |
| --- | --- | --- | --- | --- | --- |
| 公理层 | radiative transfer | `RT-TRANSFER-001`, `RT-INVARIANT-I-001` | theory page | trace only | 不替代具体发射机制 |
| synchrotron kernel | single-electron `F(x)` | `SYN-KERNEL-NUMERICAL-001` | `radiation/kernels.py::synchrotron_kernel_f` | `radiation_numerical_kernel_checks.csv` | reference/teaching kernel |
| synchrotron/SSA | source function / slab | `SYN-SOURCE-FUNCTION-001`, `SYN-SLAB-TRANSFER-001` | `synchrotron.py` | `radio_ssa_diagnostic.csv` | 不把 BPL peak 当直接 SSA 观测 |
| IC/SSC | BG/KN IC kernel + SSC hierarchy | `IC-BG-DSIGMA-001`, `LEP-IC-BG-TABULATED-SED-001`, `SSC-FORMAL-001` | `inverse_compton.py`, `leptonic_spectra.py`, `ssc.py` | fixed-point + benchmark CSVs | SSC 尚未完整自洽 solver |
| gamma-gamma | Breit-Wheeler + opacity formal integral | `GG-INVARIANT-S-001`, `GG-BREIT-WHEELER-SIGMA-001`, `GG-ABS-COEFF-FORMAL-001`, `GG-ABS-COEFF-TABULATED-001` | `gamma_gamma.py`, `kernels.py`, `production.py` | fixed-point / numerical-kernel checks | source-local isotropic target spectrum 已有 production wrapper；EBL/cascade 仍外置 |
| thermal/free-free | Planck / photosphere / Maxwellian free-free emissivity / Kirchhoff absorption | `TH-BPLANCK-NU-001`, `FF-EMISSIVITY-SPECTRAL-001`, `FF-ABSORPTION-KIRCHHOFF-001`, `FF-COOL-TIME-001` | `thermal.py`, `bremsstrahlung.py` | local fixed-point checks | scalar Gaunt factor；非完整 photospheric transfer |
| nonthermal bremsstrahlung | formal cross-section integral + simplified trend helper + Baring99 parity boundary | `LEP-BREM-NONTHERMAL-SED-001`, `LEP-NAIMA-COMPAT-BREM-001` | `leptonic_spectra.py`, `naima_compat.py`, `production.py` | benchmark CSVs | legacy helper 是 order-of-magnitude；package-compatible 只对齐对应 convention |
| hadronic | reaction matrix / secondary emissivity / pp LUT / pγ-BH boundaries / proton synchrotron | `HAD-REACTION-MATRIX-001`, `HAD-SECONDARY-EMISSIVITY-FORMAL-001`, `HAD-PP-KAFEXHIU-LUT-SED-001`, `HAD-PGAMMA-RATE-INTEGRAL-001` | `hadronic.py`, `production.py`, benchmark adapters | fixed-point + package parity checks | pp gamma and proton synch have parity routes；pγ/BH/cascade remain missing |
| cooling / angle v1 | cooling time, `gamma_c`, pitch-angle, IC anisotropy envelope, gamma-gamma angle average | `COOL-GAMMA-C-001`, `ANG-SYN-PITCH-MEAN-SIN2-001`, `ANG-IC-ANISO-GEOM-001`, `ANG-GG-AVG-SIGMA-001` | `cooling_angle.py`, `production.py`, `teaching.py` | `radiation_cooling_angle_v1_checks.csv` | mostly local-fixed-point / teaching-only |
| source-agnostic foundation | local field containers, cooling arrays, time-series bridge, accelerator screening | `RAD-FIELD-*`, `RAD-ZONE-*`, `RAD-COOL-*`, `ACC-*` | `fields.py`, `acceleration.py`, `production.py` | `radiation_foundation_v1_checks.csv`, `radiation_acceleration_v1_checks.csv`, PNG figures | draft-derived / implementation-feedback; no source geometry or transport solver |
| external benchmark | afterglow/radiation packages | benchmark-output | `validation_lab/benchmark_adapters` | `benchmark_manifest.csv` | 不作为本地 API 依赖 |

## TeV/Radio 诊断闭环

GRB 221009A 本轮只做诊断闭环，不做 MCMC 或论文级拟合。

TeV 链条：

```text
LHAASO TeV observed context
  -> synchrotron seed field from model-inferred forward shock breaks
  -> SSC Y and Thomson IC frequency
  -> KN suppression and IC cap
  -> internal gamma-gamma Breit-Wheeler / toy opacity
  -> external EBL tau boundary
  -> hadronic threshold / pion partition candidate
  -> event-trend diagnostic CSV
```

Radio/mm 链条：

```text
Laskar radio/mm observed excerpt + BPL derived table
  -> forward-shock nu_a toy expectation
  -> transfer equation: I_nu = S_nu(1-exp[-tau_nu])
  -> SSA source-function scaling
  -> reverse shock / wide component / density structure / scintillation alternatives
  -> event-trend diagnostic CSV
```

事件输出中的 `validation_level`、`quantity_class`、`mechanism_status`、`comparison_scope`、`must_not_claim` 必须保留。它们不是装饰字段，而是防止把 toy/candidate/benchmark 写成科学结论的边界。

## 开源 benchmark 的位置

外部开源代码只属于 `benchmark-output`。当前矩阵见 [07 Open-Source Benchmark Matrix](07-open-source-benchmark-matrix.md)。原则是：

- 可用于趋势、单位、接口、数量级对照。
- 不作为本地 `core/` API 依赖。
- 不证明 GRB 221009A 的 TeV 或 radio 物理解释。
- 强子与 cascade 类过程只能先做 benchmark envelope，不能因为外部库能跑就写成完整解释。

## 成熟数值方法披露规则

代码可以采用成熟参数化、表格核、角平均、random-field approximation、semi-analytic approximation 或 package-compatible convention，但课程页必须明确：

- 课程推导公式是什么。
- 代码实际实现的是哪一层近似。
- 差异来自哪里，例如 kernel、角平均、seed photon convention、Gaunt factor、cross-section parameterization、网格或单位。
- 差异影响归一化、谱形、能段边界还是运行速度。
- 输出应标为 `course/reference`、`mature numerical method`、`package-compatible`、`benchmark-output` 或 `order-of-magnitude`。

## 不声称

- 不声称唯一解释。
- 不声称复现 LHAASO 或完整 radio/mm 数据。
- 不声称完成 paper-level fit、MCMC constraint 或参数反演。
- 不内置 EBL model 为默认事实。
- 不实现完整 hadronic cascade、完整 photospheric transfer 或完整 anisotropic IC solver。
