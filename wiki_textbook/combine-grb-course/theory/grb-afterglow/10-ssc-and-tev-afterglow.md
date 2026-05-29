# 10 SSC 与 TeV 余辉

状态：v0.1 课程讲义草稿。本页把 radiation-mechanisms 里的 IC/SSC 和 gamma-gamma kernel 接到 afterglow 主线：同一群 forward-shock electrons 先产生 synchrotron seed photons，再通过 inverse-Compton scattering 产生 SSC component；SSC 又反过来改变 electron cooling、\(\nu_c\) 和 closure interpretation。TeV afterglow 的写法必须同时保留 SSC、Klein-Nishina suppression、internal \(\gamma\gamma\) opacity、EBL attenuation、extreme synchrotron、external IC、hadronic/cascade alternatives。

本页不把 delta approximation 当作理论起点；它只作为最后的 sanity layer。完整 SSC 的起点是 synchrotron photon field 与 IC kernel 的嵌套积分。

## 1. 物理图像

标准 synchrotron forward shock 可以解释许多 radio 到 X-ray afterglow，但 GeV-TeV 能段经常要求额外检查高能过程。最直接的 leptonic extension 是 synchrotron self-Compton, SSC：

```text
shock-accelerated electrons
  -> synchrotron seed photons
  -> same electrons scatter those photons
  -> SSC high-energy component
  -> stronger electron cooling
```

因此 SSC 不是简单地“多加一个 TeV 谱成分”。它至少影响三件事：

1. 直接贡献 high-energy flux。
2. 通过 \(Y=P_{\rm IC}/P_{\rm syn}\) 增强 electron cooling。
3. 把 synchrotron cooling frequency 推低为 \(\nu_c\propto(1+Y)^{-2}\)，进而影响 optical/X-ray closure relation。

TeV photon 的出现也不能自动等同于 SSC。TeV interpretation 至少要回答：

| 问题 | 物理含义 |
| --- | --- |
| 能否 synchrotron 解释？ | 需要检查 acceleration time、cooling time 和 maximum synchrotron photon energy |
| SSC 是否在 Thomson regime？ | 若进入 Klein-Nishina regime，\(Y\) 和 spectrum 都会能量依赖 |
| 源内是否透明？ | TeV photons 会与 synchrotron / prompt / afterglow photons pair produce |
| 传播是否透明？ | EBL attenuation 依赖 redshift、energy 和 EBL model |
| 是否有非轻子候选？ | hadronic / cascade / external IC 只能作为候选并列说明 |

Formula ID：`AG-TEV-INTERPRETATION-MATRIX-001`。

## 2. 参考系与变量

本页默认在 shocked fluid comoving frame 中写局域辐射与冷却量，用 prime 表示 comoving-frame 量。观测量再通过 bulk Lorentz factor 和 redshift 转换。

| 符号 | 含义 |
| --- | --- |
| \(n'_e(\gamma)\) | comoving electron number-density spectrum, per volume per \(\gamma\) |
| \(N'_e(\gamma)\) | total electron number distribution, \(N'_e=\int dV'\,n'_e\) |
| \(B'\) | shocked magnetic field |
| \(U'_B=B'^2/8\pi\) | magnetic energy density |
| \(n'_{\rm syn}(\epsilon')\) | synchrotron seed photon number density per energy |
| \(U'_{\rm syn}\) | synchrotron photon energy density |
| \(\epsilon_s'\) | scattered photon energy |
| \(\gamma_m,\gamma_c\) | injection and cooling Lorentz factors |
| \(\nu_m,\nu_c,F_{\nu,\max}\) | synchrotron characteristic quantities |
| \(\nu_m^{\rm IC},\nu_c^{\rm IC}\) | SSC characteristic frequencies |
| \(Y\) | Compton parameter, \(P_{\rm IC}/P_{\rm syn}\) |
| \(\eta\) | fraction of electron energy that is radiated |
| \(\tau_e\) | Thomson optical depth of emitting electrons |
| \(\tau_{\gamma\gamma}^{\rm int}\) | internal pair-production optical depth |
| \(\tau_{\rm EBL}\) | extragalactic background light optical depth |

comoving electron 对应的 observer-frame synchrotron frequency 可示意写成

$$
\nu_{\rm syn}(\gamma)
\simeq
{\Gamma\over1+z}
{3eB'\over4\pi m_ec}
\gamma^2 .
$$

不同文献会把 pitch-angle average 和谱峰数值因子吸收到不同位置。这会改变 order-unity 系数，不改变 SSC feedback 的推理结构。

## 3. 一般表达式

### 3.1 Synchrotron seed field

synchrotron seed field 先从 synchrotron emissivity 来。若要写局域 emissivity，电子分布必须是体密度谱 \(n'_e(\gamma)\)，单位是每体积每 \(\gamma\)。因此

$$
j_{\epsilon'}^{\rm syn}
=
{1\over4\pi}
\int d\gamma\,
n'_e(\gamma)
P_{\epsilon'}^{\rm syn}(\gamma).
$$

若使用总数谱 \(N'_e(\gamma)\)，同样的积分给出的不再是 emissivity，而是体积积分后的总 luminosity / total production rate；这时必须再除以有效体积或直接转到总光度写法。后文凡写 \(j_{\epsilon'}\)、\(n'_{\rm syn}\) 和 volume production rate，默认使用 \(n'_e\)。

在 comoving size 为 \(R'\) 的 homogeneous one-zone source 中，透明逃逸时间估计给出

$$
n'_{\rm syn}(\epsilon')
\sim
{4\pi R'\over c}
{j_{\epsilon'}^{\rm syn}\over\epsilon'} .
$$

这一步已经是模型选择：shell geometry、EATS integration、SSA transfer、anisotropic photon field 或 time-dependent escape model 都会替换简单的 \(R'/c\) 估计。

### 3.2 SSC emissivity as a nested kernel integral

first-order SSC 的局域 photon volume production rate 是

$$
{d\dot n_{\gamma}^{\rm SSC}\over d\epsilon_s'}
=
c\int d\gamma\,n'_e(\gamma)
\int d\epsilon'\,
n'_{\rm syn}(\epsilon')
{d\sigma_{\rm IC}\over d\epsilon_s'} .
$$

对应的 energy emissivity 可写成

$$
j_{\epsilon_s'}^{\rm SSC}
\sim
{\epsilon_s'\over4\pi}
c\int d\gamma\,n'_e(\gamma)
\int d\epsilon'\,
n'_{\rm syn}(\epsilon')
{d\sigma_{\rm IC}\over d\epsilon_s'} .
$$

若代码或文献用 \(N'_e\) 直接进入同一 kernel，那么结果应解释为总 photon production rate \(d\dot N_\gamma/d\epsilon_s'\)，或者是已经隐含了有效体积归一化的 one-zone convention；不能在同一行里同时叫它 volume emissivity。

Formula ID：`AG-SSC-FORMAL-INTEGRAL-001`。

IC differential cross-section 使用 Blumenthal-Gould / Klein-Nishina kernel：

$$
{d\sigma_{\rm IC}\over d\epsilon_s'}
=
{3\sigma_T\over4\gamma^2\epsilon'}
G(q,\Gamma_e),
$$

with

$$
\Gamma_e={4\gamma\epsilon'\over m_ec^2},
\qquad
q=
{\epsilon_s'
\over
\Gamma_e(\gamma m_ec^2-\epsilon_s')}.
$$

运动学范围为 \(1/(4\gamma^2)\le q\le1\)。Thomson limit 中 \(G\) 退化到通常的 kernel \(f(q)\)，不是直接退化成 delta function。delta approximation 只能在这一层写清之后作为后置近似。

## 4. 详细推导 I：由能量密度得到 \(Y\)

Thomson regime 中，ultra-relativistic electron 的 synchrotron cooling power 为

$$
P_{\rm syn}
=
{4\over3}\sigma_Tc\gamma^2U'_B ,
$$

在 isotropic seed photon bath 中，IC cooling power 为

$$
P_{\rm IC}
=
{4\over3}\sigma_Tc\gamma^2U'_{\rm ph}.
$$

二者相除会消掉共同的 \(\gamma^2\) 因子：

$$
Y\equiv {P_{\rm IC}\over P_{\rm syn}}
=
{U'_{\rm ph}\over U'_B}.
$$

对 SSC 来说，相关 seed field 就是 synchrotron photon field，所以在 Thomson one-zone limit 下

$$
\boxed{
Y\simeq {U'_{\rm syn}\over U'_B}.
}
$$

Formula ID：`AG-SSC-Y-THOMSON-001`。

这不是普适常数。高 \(\gamma\) 电子看到的 seed photons 进入 Klein-Nishina regime 后，\(Y\) 会变成 electron-energy dependent 的 \(Y(\gamma)\)。

## 5. 详细推导 II：二次方程形式的 \(Y\) 估计

令 post-shock internal energy density 为 \(e'\)。微物理参数化给出

$$
U'_B=\epsilon_B e',
\qquad
U'_e=\epsilon_e e'.
$$

只有 fraction \(\eta\) 的 electron energy 会在 dynamical time 内辐射。因此 escape time 内可用的总辐射能量密度量级为

$$
U'_{\rm rad,tot}\sim \eta\epsilon_e e'.
$$

在 first-order SSC 中，电子辐射损失分到 synchrotron 与 IC：

$$
P_{\rm rad}=P_{\rm syn}+P_{\rm IC}=P_{\rm syn}(1+Y).
$$

因此 synchrotron photon part 约为总 electron radiative output 的 \(1/(1+Y)\)：

$$
U'_{\rm syn}
\sim
{\eta\epsilon_e e'\over1+Y}.
$$

代入 \(Y=U'_{\rm syn}/U'_B\)：

$$
Y
=
{1\over\epsilon_Be'}
{\eta\epsilon_e e'\over1+Y}
=
{\eta\epsilon_e\over\epsilon_B(1+Y)}.
$$

Therefore

$$
Y(1+Y)={\eta\epsilon_e\over\epsilon_B},
$$

or

$$
Y^2+Y-{\eta\epsilon_e\over\epsilon_B}=0 .
$$

取正根得到

$$
\boxed{
Y\simeq
{-1+\sqrt{1+4\eta\epsilon_e/\epsilon_B}\over2}.
}
$$

Formula ID：`AG-SSC-Y-QUADRATIC-001`。

fast cooling 中 \(\eta\simeq1\)。slow cooling 中常用估计为

$$
\eta\simeq
\left({\gamma_m\over\gamma_c}\right)^{p-2},
\qquad p>2,
$$

但这个表达式本身会随 \(Y\) 改变 \(\gamma_c\) 而改变。这就是 toy code 常把 \(Y\) 与 \(\nu_c\) 一起迭代的原因。

## 6. 详细推导 III：IC 修正的 cooling break

Thomson one-zone limit 中，synchrotron plus SSC cooling 满足

$$
{d\gamma\over dt'}
=
-
\left({\sigma_TB'^2\over6\pi m_ec}\right)
(1+Y)\gamma^2 .
$$

cooling Lorentz factor 由 cooling time 等于 comoving dynamical time \(t'\) 定义：

$$
t'_{\rm cool}(\gamma_c)
=
{\gamma_c\over |d\gamma/dt'|_{\gamma_c}}
=
t'.
$$

Thus

$$
\gamma_c
=
{6\pi m_ec\over\sigma_TB'^2t'(1+Y)}.
$$

对 afterglow observer time，常用 \(t'\simeq\Gamma t_{\rm obs}/(1+z)\)，于是

$$
\boxed{
\gamma_c
=
{6\pi m_ec(1+z)
\over
\sigma_TB'^2\Gamma t_{\rm obs}(1+Y)} .
}
$$

Formula ID：`AG-SSC-COOL-GAMMA-C-001`。

由于 synchrotron frequency 满足 \(\nu\propto\gamma^2B'\Gamma/(1+z)\)，cooling break 变为

$$
\nu_c(Y)
=
{\nu_{c,{\rm syn}}\over(1+Y)^2}.
$$

Formula ID：`AG-SSC-NU-C-SUPPRESS-001`。

这是 SSC 即使没有直接探测到 TeV photons 也会影响 afterglow interpretation 的主要途径：大的 \(Y\) 会改变 cooling regime，从而改变由 optical 和 X-ray 数据推断的 closure relation。

## 7. 详细推导 IV：SSC breaks 与 peak flux

Thomson scattering 中，comoving frequency 为 \(\nu'\) 的 photon 被 Lorentz factor 为 \(\gamma\) 的 electron 散射后，会得到约 \(\gamma^2\) 的 boost。带角平均时常写成

$$
\nu_{\rm IC}
\simeq
{4\over3}\gamma^2\nu_{\rm seed}.
$$

许多 afterglow formula table 使用 \(2\gamma^2\nu_{\rm seed}\) 作为 characteristic peak convention。差异来自 kernel 与 spectral-peak definition 的 order-unity convention，不是新的物理模型。

把它用于定义 \(\nu_m\) 的电子，得到

$$
\boxed{
\nu_m^{\rm IC}
\sim
2\gamma_m^2\nu_m .
}
$$

Formula ID：`AG-SSC-NU-M-001`。

同理，

$$
\boxed{
\nu_c^{\rm IC}
\sim
2\gamma_c^2\nu_c .
}
$$

Formula ID：`AG-SSC-NU-C-001`。

对 SSC peak flux，最清楚的 scaling argument 从 scattering probability 开始。一个 synchrotron photon 穿过 shocked region 时被散射一次的概率约为

$$
\tau_e\sim \sigma_T n'_e R'
$$

因此 SSC peak flux density 的量级是

$$
\boxed{
F_{\nu,\max}^{\rm IC}
\sim
\tau_e F_{\nu,\max}.
}
$$

Formula ID：`AG-SSC-FMAX-001`。

这只是 scaling。精确归一化与 spectral curvature 依赖 seed spectrum、electron distribution、shell geometry、SSA、EATS，以及 IC kernel 位于 Thomson 还是 KN regime。

## 8. Klein-Nishina feedback

Thomson treatment 要求 electron rest frame 中的 seed photon energy 足够小：

$$
\epsilon''\ll m_ec^2 .
$$

对 relativistic electron 与近似 head-on 的 comoving seed photon，

$$
\epsilon''\sim 2\gamma\epsilon',
$$

常用 dimensionless KN parameter 为

$$
\boxed{
b_{\rm KN}
\equiv
{4\gamma\epsilon'\over m_ec^2}
\gtrsim1 .
}
$$

Formula ID：`AG-SSC-KN-CONDITION-001`。

当 \(b_{\rm KN}\gtrsim1\) 时：

- the IC cross-section falls below \(\sigma_T\);
- the scattered photon energy no longer grows as \(\gamma^2\) without limit;
- \(Y\) becomes \(Y(\gamma)\), not one global number;
- \(\gamma_c\) can no longer be corrected by a single \((1+Y)\) factor;
- TeV spectrum and cutoff shape depend strongly on \(\epsilon_B\), \(\epsilon_e\), \(p\), seed photon spectrum, and geometry.

更一致的 formal cooling expression 应写成单电子能量损失率，而不是直接把总 SSC photon production rate 塞进 \(\dot\gamma\)。对各向同性 seed field，可写为

$$
\left.{d\gamma\over dt'}\right|_{\rm IC}
=
-
{1\over m_ec^2}
\int d\epsilon'\,n'_{\rm ph}(\epsilon')
\int_{\epsilon_{s,\min}'}^{\epsilon_{s,\max}'}
d\epsilon_s'\,
(\epsilon_s'-\epsilon')\,
c\,{d\sigma_{\rm IC}\over d\epsilon_s'}(\gamma,\epsilon',\epsilon_s') .
$$

其中 \(d\sigma_{\rm IC}/d\epsilon_s'\) 必须使用 full KN kernel 和对应 kinematic limits。总冷却再加上 synchrotron 项：

$$
{d\gamma\over dt'}
=
-
{4\sigma_T\over3m_ec}
\gamma^2U'_B
+
\left.{d\gamma\over dt'}\right|_{\rm IC}.
$$

这里的 \(n'_{\rm ph}\) 可以是 synchrotron seed photons，也可以是外部 photon field；若用的是总 photon production rate 或总 electron spectrum，必须先除以对应 electron number / volume convention，才能得到单电子 cooling rate。常见的 `KN cap` 或 `KN suppression ratio` helper 是 envelope 与 fixed-point check，不是 full cooling integral。

## 9. Internal \(\gamma\gamma\) Opacity and EBL Attenuation

TeV photons can be absorbed before escaping the source or during propagation to Earth.

The general source-local absorption coefficient is inherited from the gamma-gamma page:

$$
\alpha_{\gamma\gamma}(E)
=
\int d\epsilon\int d\Omega\,
n(\epsilon,\Omega)(1-\mu)
\sigma_{\gamma\gamma}(E,\epsilon,\mu).
$$

The optical depth is

$$
\tau_{\gamma\gamma}^{\rm int}(E)
=
\int \alpha_{\gamma\gamma}(E,s)\,ds .
$$

For propagation, the observed flux is attenuated by both internal and EBL opacity:

$$
\boxed{
F_{\rm obs}(E,z)
=
F_{\rm int}(E,z)
\exp[-\tau_{\gamma\gamma}^{\rm int}(E)-\tau_{\rm EBL}(E,z)] .
}
$$

Formula ID：`AG-TEV-ATTENUATION-001`。

The EBL optical depth is not a local afterglow formula. It requires an external EBL model or table:

$$
\tau_{\rm EBL}(E_0,z_s)
=
\int_0^{z_s} dz\,{dl\over dz}
\int d\epsilon\,n_{\rm EBL}(\epsilon,z)
\int_{-1}^{1}{d\mu\over2}(1-\mu)
\sigma_{\gamma\gamma}[E_0(1+z),\epsilon,\mu].
$$

No course page should silently choose Dominguez, Franceschini, Finke, Gilmore, or any other EBL model as a default fact. They are external-model / benchmark-output choices.

## 10. 精确解析状态

| Object | Analytic status | Comment |
| --- | --- | --- |
| \(Y=U'_{\rm syn}/U'_B\) in Thomson one-zone | closed scaling | seed photon density convention required |
| quadratic \(Y\) estimate | closed algebraic estimate | assumes first-order Thomson SSC and simple escape |
| IC-corrected \(\gamma_c\) with constant \(Y\) | closed | invalid if \(Y=Y(\gamma)\) |
| SSC break positions | scaling / semi-analytic | order-unity coefficient convention |
| SSC full spectrum | generally numerical | nested synchrotron + IC kernel |
| KN-corrected cooling | generally numerical | needs seed spectrum integral |
| internal \(\gamma\gamma\) opacity | numerical kernel / model dependent | target photon field and geometry required |
| EBL attenuation | external model / table | cosmology and EBL evolution required |
| TeV event interpretation | model comparison | not determined by one formula |

## 11. 近似层级

| 层级 | 做法 | 保留 | 牺牲 |
| --- | --- | --- | --- |
| full formal | synchrotron transfer gives \(n'_{\rm syn}\), full IC/KN kernel, time and geometry integration | kernel physics and feedback | usually numerical |
| semi-analytic one-zone | approximate \(n'_{\rm syn}\) by luminosity / escape time, retain IC kernel | kernel shape | geometry and EATS |
| broken-power-law SSC | use \(\nu_m,\nu_c,F_{\nu,\max}\), derive SSC breaks and slopes | afterglow scaling intuition | spectral curvature and KN details |
| \(Y\)-feedback iteration | solve \(Y,\gamma_c,\nu_c\) with simple \(\eta\) | cooling feedback | full seed-field transfer |
| delta approximation | \(\nu_{\rm IC}\sim\gamma^2\nu\) | quick sanity | kernel normalization and curvature |
| effective opacity | \(\tau\sim n\sigma l\) | compactness intuition | threshold, angle, spectrum, geometry |

The hierarchy is important because code often implements the lower layers first. That does not license the course to start from those lower layers.

## 12. 从推导到代码的实现约定

Current local code relevant to this page lives mainly in:

```text
reproduce/grb/core/radiation/ssc.py
reproduce/grb/core/radiation/inverse_compton.py
reproduce/grb/core/radiation/gamma_gamma.py
reproduce/grb/core/radiation/cooling_angle.py
reproduce/grb/models/forward_shock/local_zone.py
reproduce/grb/events/grb_221009a/scripts/05_tev_ssc_sanity.py
```

The implementation layers are:

表中的 `SSC-*`、`IC-*`、`GG-*` 是 radiation-mechanisms 模块的 cross-module Formula IDs；本 afterglow 页使用 `AG-SSC-*` / `AG-TEV-*` 作为课程主线别名。跨模块追踪时应同时查 afterglow formula-index 与 `radiation-mechanisms/formula-index.md`。

| Code layer | Formula IDs / helpers | What it means |
| --- | --- | --- |
| SSC cooling toy | `SSC-Y-ITER-001`, `SSC-NU-C-COOL-001`, `SSC-ETA-001` | iterates \(Y\) and cooling frequency using simple one-zone assumptions |
| SSC break helper | `SSC-NU-M-IC-001`, `SSC-NU-C-IC-001` | characteristic-frequency scaling, not full SSC spectrum |
| one-zone tabulated SSC | `SSC-SEED-FIELD-TABULATED-001`, `SSC-ONE-ZONE-TABULATED-SED-001` | supplied synchrotron seed luminosity passed into BG/KN IC solver |
| KN envelope | `IC-KN-SUPPRESS-NUM-001`, `IC-KN-CAP-001`, `COOL-IC-KN-ENVELOPE-001` | suppression/cap fixed points, not full cooling integral |
| gamma-gamma kernel | `GG-BREIT-WHEELER-SIGMA-001`, `GG-ABS-COEFF-TABULATED-001` | numerical opacity kernel when target spectrum is supplied |
| local gamma-gamma opacity workbench | `RAD-ZONE-GG-TABULATED-OPACITY-SCREEN-001` | source-agnostic wrapper for caller-supplied target spectrum and path length |
| forward-shock local-zone bridge | `AG-FS-LOCAL-ZONE-001`, `RAD-ZONE-SCREENING-001` | maps BM \(B'\), \(R/\Gamma\), and caller-supplied \(U'_{\rm ph}\) into screening rows |
| forward-shock cooling / acceleration screening | `AG-FS-COOL-ACC-SCREEN-001` | tracks fixed-probe cooling, escape and Bohm-like acceleration times; not SSC transfer |
| forward-shock gamma-gamma opacity screening | `AG-FS-GG-OPACITY-SCREEN-001`, `GG-ABS-COEFF-MONO-001`, `RT-TAU-001` | maps BM local size and caller-supplied mono target envelope to \(\alpha_{\gamma\gamma}\), \(\tau_{\gamma\gamma}\), and \(\exp(-\tau)\); not full source opacity transfer |
| forward-shock tabulated target opacity screening | `AG-FS-GG-TARGET-SPECTRUM-SCREEN-001`, `RAD-ZONE-GG-TABULATED-OPACITY-SCREEN-001` | normalizes caller-supplied target spectral shape to \(U'_{\rm ph}=f_{\rm ph}e'\) and screens opacity; not SSC photon transfer |
| event sanity | `grb221009a_tev_ssc_sanity` | event-trend diagnostic, no LHAASO fit |

The difference between this page and current code is deliberate:

- Course formalism starts from \(n'_{\rm syn}(\epsilon')\) and IC kernel; some code helpers start from characteristic breaks or supplied seed grids.
- Course \(\gamma_c\) formula shows the clean Thomson constant-\(Y\) limit; code iteration is a toy feedback closure, not a self-consistent radiative transfer calculation.
- Course \(\gamma\gamma\) opacity is an angle and spectrum integral; `internal_gamma_gamma_opacity()` is an effective compactness helper.
- EBL helper computes \(\exp(-\tau_{\rm EBL})\) only after \(\tau_{\rm EBL}\) is supplied externally.
- `forward_shock_radiation_screening_summary()` can provide a first SSC / TeV screening input bridge, but `photon_energy_density_fraction` and `characteristic_seed_photon_energy_ev` are caller-provided envelope quantities. They are not a self-consistent synchrotron seed photon transfer solution and do not define a TeV light curve.
- `forward_shock_cooling_acceleration_timeseries()` extends that bridge to time-dependent cooling / acceleration diagnostics. It still uses \(U'_{\rm ph}=f_{\rm ph}e'\) as an envelope and does not solve \(n'_{\rm syn}(\epsilon,t)\), electron continuity, SSC photon balance, or KN feedback self-consistently.
- `forward_shock_gamma_gamma_opacity_screening()` uses \(n'_{\rm target}=U'_{\rm ph}/\epsilon'_{\rm seed}\), `GG-ABS-COEFF-MONO-001`, and \(l'=f_RR/\Gamma\). This is a monoenergetic target-envelope screen; it does not infer \(U'_{\rm ph}\) from observed flux, build a synchrotron target spectrum, integrate over EATS, include EBL, or solve pair cascades.
- `forward_shock_gamma_gamma_target_spectrum_screening()` accepts a target spectral shape and normalizes it to \(U'_{\rm ph}=f_{\rm ph}e'\) at each BM time. This lets source adapters test tabulated opacity kernels, but the shape provenance is still caller-owned and is not a self-consistent synchrotron/SSC photon field.
- GRB 221009A TeV outputs are event-trend / sanity summaries; they are not paper-level TeV fits and do not select a unique SSC origin.

## 13. Benchmark boundary

External packages or literature tools can be used for comparison:

| Benchmark | Target | Required inputs | Cannot claim |
| --- | --- | --- | --- |
| `agnpy` one-zone SSC | package-compatible SSC SED parity | electron distribution, \(B'\), size, seed / geometry convention | afterglow hydrodynamics or EATS self-consistency |
| `naima` IC | external IC kernel / SED benchmark | particle spectrum, seed photon field, distance / normalization | self-consistent forward-shock SSC feedback |
| `ebltable` | model-dependent EBL \(\tau(E,z)\) table | EBL model name, redshift, energy grid | source-local opacity or intrinsic TeV spectrum |
| `afterglowpy`, `VegasAfterglow`, BOXFIT-like grids | mature afterglow light-curve comparison | jet geometry, density profile, microphysics, viewing angle | unique radiation mechanism selection |
| MAGIC GRB 190114C papers | observational SSC/TeV context | event time, redshift, bandpass, paper convention | that all TeV afterglows are SSC |
| LHAASO GRB 221009A papers | observed TeV context and event-model benchmark | event cuts, exposure, attenuation convention, source model | that local sanity scripts reproduce LHAASO fit |

These benchmarks can check convention-matched numerical behavior. They do not turn benchmark-output into an observation, and they do not replace the course derivation.

## 14. 不声称

- 不声称完成 full self-consistent afterglow SSC transfer。
- 不声称完成 anisotropic IC solver or EATS-integrated SSC light curve。
- 不声称一个 constant \(Y\) 能描述 KN-dominated TeV cooling。
- 不声称 `internal_gamma_gamma_opacity()` 是完整 source opacity。
- 不声称本地代码内置 EBL model。
- 不声称 GRB 221009A TeV emission 已被拟合、唯一来自 SSC、或复现 LHAASO 数据。
- 不把 hadronic/cascade alternatives 写成已经排除，除非有明确的数据和模型比较。

## 15. 参考文献

- Sari & Esin 2001, *On the Synchrotron Self-Compton Emission from Relativistic Shock Waves and Its Implications for Gamma-Ray Burst Afterglows*.
- Granot & Sari 2002, *The Shape of Spectral Breaks in Gamma-Ray Burst Afterglows*.
- Blumenthal & Gould 1970, *Bremsstrahlung, Synchrotron Radiation, and Compton Scattering of High-Energy Electrons Traversing Dilute Gases*.
- Gould & Schreder 1967, gamma-gamma absorption in photon fields.
- Zhang 2014, *The Physics of Gamma-Ray Bursts & Relativistic Jets*.
- MAGIC Collaboration GRB 190114C TeV afterglow papers.
- LHAASO Collaboration 2023, GRB 221009A TeV afterglow paper.
- Laskar et al. 2023, radio to GeV afterglow of GRB 221009A.
