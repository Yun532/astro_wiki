# 16 Electromagnetic Cascade Transport 接口

状态：v0.1 讲义级理论接口页。本页把 12 页中的 `RAD-GAP-CASCADE-INTERFACE-001` 展开为源类无关的 EM cascade 理论接口。它不是 solver 设计文档，也不新增 production code；目标是把 \(\gamma\gamma\) 吸收、pair injection、pair synchrotron / IC cooling、photon escape 与能量守恒写成同一套可审计的 transport 起点。

核心原则：EM cascade 不能从 \(F_{\rm esc}=F_{\rm int}e^{-\tau}\) 开始。那只是未重处理 photon 的吸收 envelope。真正的 cascade 起点是一组 coupled photon-pair distributions；吸收掉的 photon energy 会进入 \(e^\pm\)，再通过 synchrotron / IC 产生新的 photons，可能继续被吸收。

## 1. 物理图像

最小 EM cascade 链条是：

```text
primary high-energy photons
  -> gamma-gamma absorption
  -> e+ e- pair injection
  -> pair synchrotron / IC cooling
  -> secondary photons
  -> repeated gamma-gamma absorption or escape
```

Formula ID：`CASCADE-PICTURE-001`。

这条链条可以由 \(p\gamma\)、BH、pp、proton synchrotron、external IC 或 prompt photons 触发，但 cascade 本身不是某一个 hadronic channel。课程页必须把“谁注入 high-energy photons / pairs”和“这些 photons / pairs 如何输运”分开。

## 2. 状态变量与参考系

本页默认在源区 local comoving frame 写 transport。无撇号符号表示该局域系；接 observer frame 时再加入 Doppler / redshift / EATS / propagation。

| 符号 | 含义 |
| --- | --- |
| \(N_\gamma(E,t)\) | photon number spectrum per energy |
| \(N_e(\gamma,t)\) | electron plus positron spectrum per Lorentz factor |
| \(Q_\gamma(E,t)\) | primary photon injection |
| \(Q_e(\gamma,t)\) | primary pair injection |
| \(\alpha_{\gamma\gamma}(E)\) | gamma-gamma absorption coefficient |
| \(t_{\rm esc,\gamma}\), \(t_{\rm esc,e}\) | photon / pair escape time |
| \(\dot\gamma_{\rm syn}\), \(\dot\gamma_{\rm IC}\) | pair cooling rates |
| \(j_E^{\rm syn}\), \(j_E^{\rm IC}\) | secondary photon emissivity |
| \(B\), \(n_{\rm ph}(\epsilon,\Omega)\) | magnetic field and target photon field |

Formula ID：`CASCADE-STATE-VARIABLES-001`。

若代码用 total number distribution \(N\)，emissivity 是 total production rate；若用 density \(n\)，emissivity 是 volume emissivity。二者不能混用，否则 cascade 的能量守恒会假通过。

## 3. General expression：coupled transport

最小 photon equation 是

$$
{\partial N_\gamma\over\partial t}
=
Q_\gamma^{\rm pri}
-
{N_\gamma\over t_{\rm esc,\gamma}}
-
c\alpha_{\gamma\gamma}N_\gamma
+
Q_\gamma^{\rm sec}.
$$

pair equation 是

$$
{\partial N_e(\gamma,t)\over\partial t}
=
Q_e^{\rm pri}(\gamma,t)
+
Q_{e,\gamma\gamma}(\gamma,t)
-
{\partial\over\partial\gamma}
\left[\dot\gamma(\gamma,t)N_e(\gamma,t)\right]
-
{N_e(\gamma,t)\over t_{\rm esc,e}(\gamma)}
-
{N_e\over t_{\rm ann}}.
$$

Formula ID：`CASCADE-COUPLED-TRANSPORT-001`。

其中

$$
\dot\gamma
=
\dot\gamma_{\rm syn}
+\dot\gamma_{\rm IC}
+\dot\gamma_{\rm ad}
+\cdots .
$$

如果只保留 \(e^{-\tau}\)，等价于把 \(Q_{e,\gamma\gamma}\) 与 \(Q_\gamma^{\rm sec}\) 都设为零；这不是 cascade，只是 absorption。

## 4. Gamma-gamma pair injection

高能 photon \(E\) 与 target photon \(\epsilon\) 的 pair-production rate 来自 03 页的 Breit-Wheeler kernel。吸收系数为

$$
\alpha_{\gamma\gamma}(E)
=
\int d\epsilon\int d\Omega\,
n_{\rm ph}(\epsilon,\Omega)(1-\mu)
\sigma_{\gamma\gamma}(E,\epsilon,\mu).
$$

Formula ID：`CASCADE-GG-ABS-SOURCE-001`。

pair injection 不能只写成 \(c\alpha_{\gamma\gamma}N_\gamma\)，因为还要知道 pair energy 分布。formal expression 是

$$
Q_{e^\pm,\gamma\gamma}(\gamma)
=
c
\int dE\,N_\gamma(E)
\int d\epsilon\int d\Omega\,
n_{\rm ph}(\epsilon,\Omega)(1-\mu)
{d\sigma_{\gamma\gamma}\over d\gamma}
(E,\epsilon,\mu;\gamma).
$$

Formula ID：`CASCADE-GG-PAIR-INJECTION-001`。

teaching layer 可以用 equal-energy approximation：

$$
\gamma
\sim
{E\over2m_ec^2},
$$

但这只是注入能段定位，不是 pair injection spectrum。完整 pair injection 需要 differential Breit-Wheeler kernel 或成熟表格。

## 5. Pair cooling 与 secondary photon source

pair synchrotron cooling 由

$$
\dot\gamma_{\rm syn}
=
-
{4\sigma_T\over3m_ec}
U_B\gamma^2
$$

给出，前提是 isotropic pitch-angle / Thomson classical limit。IC cooling 更一般地应写成 kernel energy-loss integral：

$$
\dot\gamma_{\rm IC}
=
-
{1\over m_ec^2}
\int d\epsilon\,n_{\rm ph}(\epsilon)
\int d\epsilon_s\,(\epsilon_s-\epsilon)c
{d\sigma_{\rm IC}\over d\epsilon_s}.
$$

Formula ID：`CASCADE-PAIR-COOLING-001`。

secondary photon source 是 pair distribution 对 synchrotron 与 IC kernel 的卷积：

$$
Q_\gamma^{\rm sec}(E)
=
\int d\gamma\,N_e(\gamma)
\left[
{d\dot N_\gamma^{\rm syn}\over dE}
+
{d\dot N_\gamma^{\rm IC}\over dE}
\right].
$$

Formula ID：`CASCADE-SECONDARY-PHOTON-SOURCE-001`。

若 IC 进入 KN regime，\(\dot\gamma_{\rm IC}\) 与 emitted photon spectrum 都不再由单个 Thomson \(Y\) 描述。若 seed photons 各向异性，还需要 14 页的 anisotropic IC 接口。

## 6. 能量守恒检查

cascade solver 的最低 sanity check 是能量流守恒。定义 photon 与 pair 能量：

$$
U_\gamma
=
\int dE\,E\,N_\gamma(E),
\qquad
U_e
=
\int d\gamma\,\gamma m_ec^2N_e(\gamma).
$$

在没有 escape、adiabatic loss、annihilation 和 external injection 的封闭盒中，应满足

$$
{d\over dt}(U_\gamma+U_e)
\simeq
0
$$

到数值误差。含 escape 时，

$$
{d\over dt}(U_\gamma+U_e)
=
L_{\rm inj}
-
L_{\rm esc}
-
L_{\rm ad}
\quad
{\rm plus\ explicit\ sinks}.
$$

Formula ID：`CASCADE-ENERGY-CONSERVATION-001`。

这条检查比“谱形看起来平滑”更重要。若没有能量账本，cascade 数值结果可能通过肉眼但在物理上虚增能量。

## 7. Steady-state one-zone 极限

如果源区近似稳态、均匀、one-zone，并忽略空间输运，可令时间导数为零：

$$
0
=
Q_\gamma^{\rm pri}
-
{N_\gamma\over t_{\rm esc,\gamma}}
-
c\alpha_{\gamma\gamma}N_\gamma
+
Q_\gamma^{\rm sec},
$$

$$
0
=
Q_e^{\rm pri}
+
Q_{e,\gamma\gamma}
-
{\partial\over\partial\gamma}(\dot\gamma N_e)
-
{N_e\over t_{\rm esc,e}}.
$$

Formula ID：`CASCADE-STEADY-ONE-ZONE-001`。

这是未来最小 solver 的合理起点，但仍不是 \(e^{-\tau}\)。它至少要同时更新 \(N_\gamma\) 与 \(N_e\)，并检查 \(Q_{e,\gamma\gamma}\to Q_\gamma^{\rm sec}\) 的反馈。

## 8. Opacity-only 与 cascade 的差异

opacity-only 写法是

$$
F_{\rm abs}(E)
=
F_{\rm int}(E)e^{-\tau_{\gamma\gamma}(E)}.
$$

cascade 写法至少是

$$
F_{\rm esc}(E)
=
F_{\rm int}(E)e^{-\tau_{\gamma\gamma}(E)}
+
F_{\rm cas}(E),
$$

其中

$$
F_{\rm cas}
\leftarrow
Q_{e,\gamma\gamma}
\rightarrow
N_e
\rightarrow
Q_\gamma^{\rm sec}
\rightarrow
{\rm escape/absorb}.
$$

Formula ID：`CASCADE-OPACITY-VS-CASCADE-001`。

因此 \(\tau_{\gamma\gamma}\gg1\) 不能自动说明能量消失，只说明 primary photons 不以原能量直接逃逸。能量可能被重处理到 X-ray、MeV、GeV 或更低能段，具体取决于 \(B\)、seed photon field、escape time 和 geometry。

## 9. Internal cascade 与 propagation cascade

源内 cascade 和传播 cascade 需要分开：

| 类型 | target fields | 关键变量 | 不能混淆 |
| --- | --- | --- | --- |
| internal cascade | source photons, local \(B\), local size | \(n_{\rm ph}\), \(B\), \(R\), \(t_{\rm esc}\) | 不是 EBL attenuation |
| intergalactic cascade | EBL, CMB, IGMF | redshift, IGMF, source duration, angular spread | 不是源内 photon density |
| detector response | instrument effective area / exposure | sky direction, event class, time window | 不是 cascade physics |

Formula ID：`CASCADE-INTERNAL-PROPAGATION-SPLIT-001`。

GRB transient 尤其敏感：intergalactic cascade 的 time delay 和 angular broadening 可能让 reprocessed photons 不在 prompt / afterglow 时间窗内出现。

## 10. 接口契约

未来 EM cascade solver 至少需要：

| 类别 | 输入 / 输出 | 说明 |
| --- | --- | --- |
| energy grids | photon \(E\), pair \(\gamma\) | 必须覆盖吸收、注入和冷却后的能段 |
| target photon field | \(n_{\rm ph}(\epsilon,\Omega)\) 或 isotropic \(n_{\rm ph}(\epsilon)\) | 来源必须登记 |
| magnetic field | \(B\) and pitch convention | 决定 pair synchrotron |
| kernels | \(\sigma_{\gamma\gamma}\), \(d\sigma_{\gamma\gamma}/d\gamma\), IC / synch kernels | differential kernel 不能被 total opacity 替代 |
| escape model | \(t_{\rm esc,\gamma}\), \(t_{\rm esc,e}\) | 影响归一化和谱形 |
| injection | \(Q_\gamma^{\rm pri}\), \(Q_e^{\rm pri}\), hadronic source terms | 注入来源与 cascade 分开 |
| outputs | escaped photon spectrum, pair spectrum, energy ledger | 需标注 validation level |

Formula ID：`CASCADE-INTERFACE-CONTRACT-001`。

代码层建议拆成：

```text
gamma-gamma absorption kernel
  -> pair injection kernel
  -> pair cooling/emissivity kernels
  -> transport RHS
  -> steady/time-dependent solver
  -> benchmark adapter
```

## 11. 当前代码实现约定

当前本地代码已经有：

| 代码 | 层级 | 边界 |
| --- | --- | --- |
| `gamma_gamma.py::gamma_gamma_cross_section_cgs` | Breit-Wheeler kernel | no pair injection |
| `gamma_gamma.py::isotropic_tabulated_absorption_coefficient_cgs` | isotropic opacity integral | no reprocessing |
| `production.py::gamma_gamma_target_spectrum_opacity_curve` | opacity curve wrapper | no cascade |
| `cooling_angle.py::gamma_gamma_angle_averaged_cross_section_cgs` | angle average helper | mono/isotropic convention |
| `hadronic.py` pp / proton synch helpers | selected source terms | no cascade feedback |
| `fields.py::electron_cooling_curve` | cooling arrays | no particle transport |

Formula ID：`CASCADE-CODE-BOUNDARY-001`。

所以当前可声称：已有 \(\gamma\gamma\) absorption kernel、isotropic target opacity、EBL attenuation envelope、若干 hadronic / proton-synch source candidates。不能声称：已有 pair injection spectrum、pair transport、cascade-reprocessed spectrum、internal cascade solver、intergalactic cascade solver 或 event-level cascade fit。

## 12. Exact analytic status

| 对象 | 状态 | 说明 |
| --- | --- | --- |
| Breit-Wheeler total cross-section | closed | 03 页已推导 |
| gamma-gamma absorption coefficient | semi-analytic / numerical | target field 积分 |
| differential pair injection | kernel / table | 通常数值 |
| pair synchrotron source | numerical kernel integral | 可复用 synchrotron kernel |
| pair IC source | numerical BG/KN or anisotropic kernel | KN / angle dependence 重要 |
| steady one-zone cascade | coupled algebraic/ODE problem | 一般数值 |
| time-dependent cascade | PDE/ODE transport | 数值 |
| intergalactic cascade | propagation solver | 依赖 EBL/CMB/IGMF |

Formula ID：`CASCADE-EXACT-STATUS-001`。

## 13. Benchmark boundary

| Benchmark route | 可检查 | 不能证明 |
| --- | --- | --- |
| local \(\gamma\gamma\) opacity checks | absorption coefficient 和 threshold behavior | cascade reprocessing |
| energy-conservation toy cascade | energy ledger / solver bookkeeping | astrophysical realism |
| AM3 / specialized source cascade | same-input source-local cascade convention | 唯一理论标准 |
| ELMAG / CRPropa | intergalactic propagation cascade | source-local emission |
| EBL tables | \(\tau_{\rm EBL}\) comparison | internal opacity or cascade |

Formula ID：`CASCADE-BENCHMARK-BOUNDARY-001`。

外部 cascade code 的输出必须标成 `benchmark-output`。如果输入 photon field、magnetic field、escape time、source duration 或 EBL model 不同，ratio 差异不能简单解释为本地代码错误。

## 14. 不声称

- 不声称本页实现 EM cascade solver。
- 不声称 \(\tau_{\gamma\gamma}\) 决定 reprocessed flux。
- 不声称 \(F_{\rm int}e^{-\tau}\) 是 cascade。
- 不声称当前代码有 pair injection spectrum 或 pair transport。
- 不声称 EBL attenuation 等于源内 cascade。
- 不声称 AM3、ELMAG、CRPropa 或任一外部工具是唯一物理标准。
- 不声称 TeV photons 或 neutrino non-detections 可以单独证明 hadronic / cascade 起源。

## 15. 参考入口

- `03-gamma-gamma-opacity.md`
- `05-hadronic-order-of-magnitude.md`
- `12-missing-process-interface-roadmap.md`
- `15-photohadronic-and-bethe-heitler-interface.md`
- `../grb-afterglow/12-cascade-neutrino-and-propagation-boundaries.md`
- `reproduce/grb/core/radiation/gamma_gamma.py`
- `reproduce/grb/core/radiation/cooling_angle.py`
