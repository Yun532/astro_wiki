# 19 Nuclei Photodisintegration 与 Spallation 接口

状态：v0.1 讲义级理论接口页。本页把 12 页中的 P3 缺口 `nuclei / photodisintegration / spallation` 展开为 nuclear channel 的安全入口。它不是 nuclear cascade solver，也不新增 production code；目标是把 heavy-nucleus synchrotron scale、photon-induced disintegration、gas spallation、fragment yield、de-excitation gamma、nuclear network 和 benchmark boundary 分开。

核心原则：不能从 mass-scaled proton formula 开始定义核种辐射与碎裂。\(Z/A\) 缩放只适用于带电粒子 synchrotron 或 Larmor/Hillas 这类单粒子电磁量；photodisintegration 和 spallation 由 nuclear cross-section matrix 与 fragment yields 决定。

## 1. 物理图像

高能 nuclei 进入 radiation / gas / magnetic field 后，可能有三类不同结果：

```text
primary nucleus (A,Z)
  -> magnetic field: nuclei synchrotron / confinement
  -> photon field: photodisintegration, photopion, Bethe-Heitler
  -> gas target: spallation / hadronic fragmentation
  -> fragments, nucleons, de-excitation gamma, pions, neutrinos, pairs
  -> EM cascade and propagation
```

Formula ID：`NUC-PICTURE-001`。

这里的关键对象不是单一 proton spectrum，而是 isotope / mass-number resolved distribution \(N_{A,Z}(E,t)\)。只跟踪总 baryon energy 会丢掉 charge、mass、阈值、fragment branching 和 secondary composition。

## 2. 变量与核种状态

本页默认在局域 comoving frame 写相互作用率。若接观测量，再加 Doppler factor、redshift 和 escape / propagation。

| 符号 | 含义 |
| --- | --- |
| \(A,Z\) | nucleus mass number and charge |
| \(N_{A,Z}(E,t)\) | differential nucleus distribution |
| \(\gamma_A=E_A/(A m_pc^2)\) | nucleus Lorentz factor |
| \(\epsilon\) | target photon energy |
| \(\bar\epsilon\) | nucleus rest-frame photon energy |
| \(n_\gamma(\epsilon)\) | photon number density per energy |
| \(n_{\rm gas,j}\) | gas target species density |
| \(\sigma_{A\to f}\) | channel cross-section to fragment set \(f\) |
| \(Y_{A\to i}\) | fragment / secondary yield |
| \(Q_i(E,t)\) | source term for daughter species \(i\) |

Formula ID：`NUC-VARIABLES-001`。

核种网络应保留 \(A,Z\) 标签。若只用 \(A\) 或只用 \(Z\)，必须说明哪些过程被忽略：例如 beta decay 会改变 \(Z\)，spallation 会改变 \(A,Z\)，而 synchrotron 只看 \(Z/A\) 的电磁缩放。

## 3. Photon interaction 的 Lorentz 变量

photon-induced nuclear process 的共同入口是 nucleus rest-frame photon energy：

$$
\bar\epsilon
=
\gamma_A\epsilon(1-\beta_A\mu),
$$

其中 \(\mu\) 是 nucleus 速度方向与 photon 方向的夹角。

Formula ID：`NUC-REST-FRAME-PHOTON-001`。

这个量控制 photodisintegration、nuclear excitation、photopion 和 Bethe-Heitler 的阈值。对 head-on photons，\(\bar\epsilon\simeq2\gamma_A\epsilon\)；但完整 rate 不能只用 head-on threshold，需要对 photon spectrum 和 angle 分布积分。

## 4. Photodisintegration rate

各向同性 photon field 下，nucleus \((A,Z)\) 的 photodisintegration rate 可写成

$$
t_{A,\gamma}^{-1}(\gamma_A)
=
{c\over2\gamma_A^2}
\sum_c
\int_{\bar\epsilon_{{\rm thr},c}}^\infty
d\bar\epsilon\,
\sigma_{A,c}(\bar\epsilon)
\bar\epsilon
\int_{\bar\epsilon/(2\gamma_A)}^\infty
d\epsilon\,{n_\gamma(\epsilon)\over\epsilon^2}.
$$

Formula ID：`NUC-PHOTODIS-RATE-001`。

这里 \(c\) 是 channel，例如 single-neutron emission、single-proton emission、multi-nucleon emission、alpha emission 或 fission-like fragments。若只写总 cross-section \(\sigma_A\)，只能得到 survival probability，不能得到 daughter composition。

## 5. Giant Dipole Resonance 与阈值直觉

许多中重核的 photodisintegration 在 nucleus rest frame 的 giant dipole resonance 区域最重要，典型能量尺度是

$$
\bar\epsilon_{\rm GDR}
\sim
10\text{--}30\,{\rm MeV}.
$$

数量级阈值可由

$$
\gamma_A
\sim
{\bar\epsilon_{\rm GDR}\over2\epsilon}
$$

估计。对应 observer / source convention 下的 nucleus energy scale 为

$$
E_A
\sim
A m_pc^2
{\bar\epsilon_{\rm GDR}\over2\epsilon}.
$$

Formula ID：`NUC-GDR-THRESHOLD-001`。

这只是能区筛选，不是谱模型。GDR 的宽度、quasi-deuteron 区域、高能 baryonic resonance、多重碎裂和核种依赖 cross-section 都会改变 rate 与 fragment yields。

## 6. Fragment yield 与核种网络

完整核种输运应把母核损失和 daughter source 同时写出。schematic network 为

$$
{\partial N_i(E,t)\over\partial t}
=
Q_i(E,t)
-{N_i(E,t)\over t_{{\rm esc},i}}
-N_i(E,t)\sum_c t_{i,c}^{-1}(E)
+
\sum_{j,c}\int dE_j\,
N_j(E_j,t)
R_{j,c}(E_j)
Y_{j,c\to i}(E;E_j).
$$

Formula ID：`NUC-FRAGMENT-NETWORK-001`。

若 fragmentation 近似保持 Lorentz factor，即 daughter \(i\) 继承母核的 \(\gamma_A\)，则

$$
E_i
\simeq
{A_i\over A_j}E_j.
$$

Formula ID：`NUC-LORENTZ-INHERITANCE-001`。

这个近似常用于快速 network，但不能替代 differential yield。真实 fragments 可能有 recoil、excitation、neutron decay、beta decay 和 multi-fragment channels。

## 7. Gas spallation

gas target 中的 spallation 是 nucleus 与 ambient gas nuclei 的 hadronic fragmentation：

$$
(A,Z)+j
\to
(A_1,Z_1)+(A_2,Z_2)+\cdots+\pi+X.
$$

对 gas species \(j\)，loss rate 的 envelope 是

$$
t_{A,j}^{-1}(E_A)
=
n_j c\,\sigma_{A j}^{\rm sp}(E_A).
$$

daughter source 一般应写成

$$
Q_i^{\rm sp}(E_i)
=
\sum_{A,Z,j}
n_j c
\int dE_A\,N_{A,Z}(E_A)
{d\sigma_{A j\to i}\over dE_i}(E_A,E_i).
$$

Formula ID：`NUC-SPALLATION-SOURCE-001`。

用一个 nuclear enhancement factor 只能修正 pion gamma-ray normalization 的数量级，不能给出 isotope-resolved fragments，也不能替代 spallation network。

## 8. De-excitation gamma

photodisintegration 或 spallation 后的 excited daughter nucleus 可通过 de-excitation 发射 MeV gamma rays：

$$
(A,Z)^\ast
\to
(A,Z)+\gamma_{\rm deex}.
$$

若 nucleus rest frame line energy 为 \(E_{\rm line}^\ast\)，observer energy scale 为

$$
E_{\gamma,{\rm obs}}
\simeq
{\delta_D\over1+z}
\gamma_A E_{\rm line}^\ast(1+\beta_A\cos\theta^\ast).
$$

Formula ID：`NUC-DEEX-GAMMA-001`。

对各向同性 rest-frame emission，line 会被 Lorentz boost 展宽。没有 nuclear level table 和 branching ratio 时，只能写成 candidate channel，不能预测 line spectrum。

## 9. 与 heavy-nucleus synchrotron 的关系

05 页已有 heavy-nucleus synchrotron frequency scale：

$$
\nu_A'
\simeq
{3ZeB'\over4\pi A m_pc}\gamma_A^2,
\qquad
{\nu_A'\over\nu_p'}
\simeq
{Z\over A}.
$$

Formula ID：`HAD-NUCLEUS-SYN-NU-001`。

但 synchrotron kernel 只回答电磁辐射，不回答 nucleus 是否能在 photon/gas field 中存活。实际可观测 high-energy nucleus synchrotron 还要满足

$$
t_{\rm acc}
<
\min(t_{\rm dyn},t_{\rm esc},t_{\rm syn},t_{A\gamma},t_{\rm sp}).
$$

Formula ID：`NUC-SURVIVAL-COMPETITION-001`。

因此，不能只算 \(Z/A\) 的 synchrotron frequency，就声称 heavy nuclei channel 成立。

## 10. 与 cascade / neutrino 的关系

nuclear channel 会给 EM 和 neutrino 系统注入多个源项：

$$
Q_{\rm nuc}
\to
\{Q_{\rm fragments},Q_n,Q_p,Q_\gamma^{\rm deex},Q_{\pi},Q_{e^\pm},Q_\nu\}.
$$

Formula ID：`NUC-CASCADE-SOURCE-TERMS-001`。

fragments 和 nucleons 可继续参与 \(p\gamma\)、\(pp\)、BH、synchrotron 和 gamma-gamma / EM cascade。neutrons 还可能 escape 后 beta decay。完整结果必须接 transport / cascade；不能把 photodisintegration loss rate 直接写成 escaped gamma-ray spectrum。

## 11. 接口契约

未来 nuclei / photodisintegration / spallation helper 至少需要：

| 类别 | 输入 / 输出 | 说明 |
| --- | --- | --- |
| primary composition | \(N_{A,Z}(E)\) | 必须保留 \(A,Z\) 或明确近似 |
| photon target | \(n_\gamma(\epsilon,\Omega)\) | photodisintegration / photopion / BH 共用 target |
| gas target | \(n_j\), composition | spallation 和 pA/AA channels |
| cross-section tables | \(\sigma_{A,c}(\bar\epsilon)\), \(d\sigma/dE\) | 版本、能区和 channel coverage 必须记录 |
| yields | daughter nuclei、nucleons、gamma、pions、pairs、neutrinos | fragment-resolved |
| transport | escape, cooling, decay, repeated interactions | 决定 survival 与 cascade |
| outputs | rates, survival probability, fragment spectra, source terms | 不能只输出 single \(E_{\max}\) |

Formula ID：`NUC-INTERFACE-CONTRACT-001`。

建议代码层级：

```text
nuclear species registry
  -> photon / gas target field builder
  -> cross-section / yield table adapter
  -> rate and source-term kernels
  -> nuclear transport network
  -> cascade / propagation coupling
  -> benchmark adapter
```

## 12. 当前代码边界

当前本地代码只有：

| 代码 | 层级 | 边界 |
| --- | --- | --- |
| `hadronic.py::nucleus_synchrotron_frequency_hz` | electromagnetic scale helper | \(Z/A\) frequency scaling only |
| `acceleration.py` Hillas / confinement helpers | source-screening | no photodisintegration survival |
| `05-hadronic-order-of-magnitude.md` | reaction matrix and boundary | no nuclear network |
| `16-electromagnetic-cascade-transport-interface.md` | cascade interface | no nuclear source-term solver |

Formula ID：`NUC-CODE-BOUNDARY-001`。

因此当前可声称：已有 heavy-nucleus synchrotron frequency scale 和 general reaction-matrix boundary。不能声称：已有 photodisintegration rate table、spallation network、fragment yields、nuclear de-excitation gamma spectrum、UHECR propagation solver、nuclear cascade 或 composition-resolved event prediction。

## 13. Exact analytic status

| 对象 | 状态 | 说明 |
| --- | --- | --- |
| rest-frame photon energy \(\bar\epsilon\) | closed kinematics | common safe entry |
| GDR threshold scale | analytic estimate | not a rate |
| photodisintegration rate | semi-analytic integral after tables supplied | cross-section table dependent |
| fragment yields | table / model / Monte Carlo | channel dependent |
| gas spallation | cross-section table / parameterization | isotope and target dependent |
| de-excitation gamma | nuclear level table + Lorentz transform | no universal line spectrum |
| nuclear transport network | numerical | coupled composition evolution |

Formula ID：`NUC-EXACT-STATUS-001`。

## 14. Benchmark boundary

| Benchmark / mature route | 可检查 | 不能证明 |
| --- | --- | --- |
| CRPropa photodisintegration tables | rate / propagation convention | GRB source model |
| TALYS / nuclear data tables | channel cross-section / branching | cascade closure |
| NeuCosmA / AM3 nuclear channels | same-input nuclear source terms | unique physical standard |
| UHECR propagation literature | survival and fragment benchmarks | prompt GRB spectrum |
| local \(Z/A\) synchrotron helper | electromagnetic scale | photodisintegration survival |

Formula ID：`NUC-BENCHMARK-BOUNDARY-001`。

任何 benchmark 必须记录 isotope set、cross-section model、photon field convention、gas composition、energy grid、fragment bookkeeping、decay handling 和 output species。外部 propagation code 的 survival curve 不是本地 GRB source theory 的替代品。

## 15. 不声称

- 不声称本页实现 nuclear cascade solver。
- 不声称 \(Z/A\) synchrotron scaling 足以判断 heavy nuclei channel。
- 不声称 photodisintegration threshold 是 fragment spectrum。
- 不声称 nuclear enhancement factor 等于 spallation network。
- 不声称 de-excitation gamma line spectrum 已可预测。
- 不声称当前代码能做 UHECR composition propagation 或 GRB nuclear event inference。

## 16. 参考入口

- `05-hadronic-order-of-magnitude.md`
- `12-missing-process-interface-roadmap.md`
- `15-photohadronic-and-bethe-heitler-interface.md`
- `16-electromagnetic-cascade-transport-interface.md`
- `11-source-agnostic-foundation-and-acceleration.md`
- `../grb-afterglow/11-particle-acceleration-and-maximum-energy.md`
- `../grb-afterglow/12-cascade-neutrino-and-propagation-boundaries.md`
- `reproduce/grb/core/radiation/hadronic.py`
