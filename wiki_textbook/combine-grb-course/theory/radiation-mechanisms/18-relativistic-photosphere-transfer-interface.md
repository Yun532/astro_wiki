# 18 Relativistic Photosphere Transfer 接口

状态：v0.1 讲义级理论接口页。本页把 12 页中的 `RAD-GAP-PHOTOSPHERE-INTERFACE-001` 展开为 relativistic photosphere / thermal transfer 的安全入口。它不是 photosphere spectrum solver，也不新增 production code；目标是把 static blackbody helper、baryonic photosphere radius scale、moving outflow optical-depth surface、Doppler-boosted transfer、equal-arrival-time integration、spectral broadening 和 code boundary 分开。

核心原则：不能从 fitted blackbody radius、single-temperature Planck curve 或 `baryonic_photosphere_radius()` 开始定义 GRB photospheric spectrum。安全起点是 moving outflow 中的 radiative transfer 与 optical-depth surface；静态黑体半径只能作为 effective emitting area 或数量级 sanity check。

## 1. 物理图像

GRB photosphere 不是一个静止球面黑体炉口，而是一个相对论外流中 photon 最后散射概率显著下降的区域。最小链条是：

```text
n'(r,theta), Gamma(r,theta), opacity kappa
  -> optical-depth surface tau(r,theta) ~ 1
  -> comoving emissivity / source function / heating history
  -> Doppler and redshift transform
  -> equal-arrival-time surface integration
  -> observed thermal-like but broadened spectrum
```

Formula ID：`PHOTOSPHERE-PICTURE-001`。

因此，photosphere 可以产生 quasi-thermal component，但 quasi-thermal 不等于 single Planck。角向 Doppler 展宽、径向温度梯度、subphotospheric dissipation、Comptonization、pair opacity 和 multi-zone outflow 都会把谱形从窄黑体展宽。

## 2. 变量与参考系

本页区分 lab/source frame、comoving frame 和 observer frame。带撇号的量在 outflow comoving frame；观测频率带 `obs`。

| 符号 | 含义 |
| --- | --- |
| \(r,\theta\) | lab/source frame 中的半径和相对视线夹角 |
| \(\Gamma,\beta\) | bulk Lorentz factor 和 \(v/c\) |
| \(\rho'\), \(n_e'\) | comoving mass / electron density |
| \(\kappa\) | opacity per mass，常用 electron scattering scale |
| \(\tau(r,\theta)\) | 从位置到逃逸方向的 optical depth |
| \(T'(r,\theta)\) | comoving radiation / matter effective temperature |
| \(I'_{\nu'}\), \(S'_{\nu'}\) | comoving intensity / source function |
| \(\delta_D=[\Gamma(1-\beta\mu)]^{-1}\) | Doppler factor |
| \(d_L\) | luminosity distance |
| \(t_{\rm obs}\) | observer time |

Formula ID：`PHOTOSPHERE-VARIABLES-001`。

若课程页或代码使用 \(R_{\rm bb}\)、\(T_{\rm obs}\) 或 \(L_{\rm bb}\)，必须说明它们是 effective observables，还是外流中的物理半径与 comoving temperature。二者通常不同。

## 3. Optical-depth surface

moving medium 中 photon 的光深不是简单的 \(n\sigma_T R\)。沿 photon path 的 differential optical depth 可写成

$$
d\tau
=
\kappa \rho'\Gamma(1-\beta\mu)\,ds,
$$

其中 \(\mu=\hat v\cdot\hat k\) 是流体速度方向与 photon 传播方向的夹角。于是 photospheric surface 由

$$
\tau(r,\theta)
=
\int_{s(r,\theta)}^\infty
\kappa\rho'(s)\Gamma(s)\left[1-\beta(s)\mu(s)\right]ds
\sim 1
$$

定义。

Formula ID：`PHOTOSPHERE-TAU-SURFACE-001`。

这个公式说明三件事：

- 光深面依赖方向，不一定是球面 \(r=R_{\rm ph}\)。
- \(\Gamma(1-\beta\mu)\) 是相对论运动介质中的路径 / 密度转换因子，不能省略后再称为 moving photosphere。
- \(\tau=1\) 是 last-scattering probability 的数量级标记，不保证谱形就是 Planck。

## 4. Moving surface 的强度变换

辐射转移中最重要的不变量之一是

$$
{I_\nu\over\nu^3}
=
{I'_{\nu'}\over{\nu'}^3}.
$$

若局域 comoving photon 频率为 \(\nu'\)，观测频率为

$$
\nu_{\rm obs}
=
{\delta_D\over1+z}\nu',
\qquad
\delta_D
=
{1\over\Gamma(1-\beta\mu)}.
$$

则强度变换为

$$
I_{\nu_{\rm obs}}
=
\left({\delta_D\over1+z}\right)^3 I'_{\nu'}.
$$

Formula ID：`PHOTOSPHERE-DOPPLER-INVARIANT-001`。

如果 comoving source function 近似为 \(B_{\nu'}(T')\)，观测到的局部 patch 仍会因为 \(\delta_D(\theta)\) 的角向变化而呈现不同 color temperature。把所有 patch 积分后，一般不再是单温黑体。

## 5. Equal-arrival-time flux integral

观测 flux 不是某一瞬间 lab 球面的直接面积乘黑体强度，而是 equal-arrival-time surface 上的积分。schematic 形式可写成

$$
F_{\nu_{\rm obs}}(t_{\rm obs})
=
{1+z\over d_L^2}
\int_{\rm EATS}
\delta_D^3
I'_{\nu'}(r,\theta,t')
d\Sigma_\perp .
$$

Formula ID：`PHOTOSPHERE-EATS-FLUX-001`。

这里 \(d\Sigma_\perp\) 是投影面积元素；不同 convention 可把 redshift 因子、角距离 \(D_A\) 或 luminosity distance \(d_L\) 写成等价形式。重要的是：必须同时给出 Doppler factor、arrival-time condition 和 surface/volume emissivity convention。

若用 emissivity 而不是 photospheric surface intensity，形式会变成 volume transfer：

$$
F_{\nu_{\rm obs}}
\sim
{1+z\over d_L^2}
\int_{\rm EATS}
\delta_D^3
j'_{\nu'}e^{-\tau_\nu}
dV',
$$

但这仍然是 transfer integral，不是 \(4\pi R^2\sigma T^4\) 的直接替换。

## 6. Effective blackbody radius 不等于 photosphere radius

观测中常从 thermal component 写

$$
L_{\rm bb}
=
4\pi R_{\rm bb}^2\sigma_{\rm SB}T_{\rm obs}^4.
$$

Formula ID：`PHOTOSPHERE-BB-EFFECTIVE-RADIUS-001`。

这里的 \(R_{\rm bb}\) 是 effective radius：它把 luminosity、color temperature、distance 和 beaming convention 压缩成一个面积参数。它通常不是外流中 \(\tau=1\) 的半径，差异来自：

- \(T_{\rm obs}\) 已包含 Doppler boost 和 redshift，不是 \(T'\)。
- emitting area 是 EATS 上的投影与 beaming 权重，不是完整球面。
- scattering photosphere 可有 finite width，不是无限薄面。
- subphotospheric heating 会改变 color correction。

因此，`blackbody_radius_from_luminosity()` 只能反解 effective emitting radius，不能直接报告为 GRB physical photosphere radius。

## 7. Coasting baryonic scale 与实现约定

对 steady baryonic coasting outflow，数量级估计常从

$$
L\simeq \Gamma\dot M c^2,
\qquad
n'\simeq{\dot M\over4\pi R^2m_p\Gamma c}
$$

出发。若径向光深取 \(\tau_T\sim n'\sigma_T R/\Gamma\sim1\)，可得

$$
R_{\rm ph}
\sim
{L\sigma_T\over4\pi m_pc^3\Gamma^3}.
$$

Formula ID：`PHOTOSPHERE-COASTING-SCALE-001`。

当前 `thermal.py::baryonic_photosphere_radius()` 保留同一 \(\Gamma^{-3}\) 标度，但写成

$$
R_{\rm ph}
=
{L\sigma_T\over f_{\rm geom}\pi m_pc^3\Gamma^3}.
$$

`geometry_factor=8` 是实现 convention，用来暴露几何和厚度因子的数量级不确定性。它不是 relativistic transfer 结果，也不是唯一标准系数。不同文献因 shell thickness、acceleration/coasting phase、角结构、pair loading 和 optical-depth path convention 可差数值因子。

## 8. 谱展宽来源

若 comoving 局部源函数近似黑体，

$$
I'_{\nu'}\simeq B_{\nu'}(T'),
$$

观测谱仍可写成多温叠加：

$$
F_{\nu_{\rm obs}}
\propto
\int d\Omega\,dR\,
W(R,\theta,t_{\rm obs})
B_{\nu'}(T'(R,\theta)),
\qquad
\nu'={1+z\over\delta_D}\nu_{\rm obs}.
$$

Formula ID：`PHOTOSPHERE-SPECTRAL-BROADENING-001`。

常见展宽机制包括：

| 机制 | 影响 |
| --- | --- |
| angular Doppler spread | 不同 \(\theta\) 有不同 \(\delta_D\)，叠加成多 color temperature |
| radial temperature profile | \(T'(R)\) 与 photosphere finite width 造成多温叠加 |
| subphotospheric dissipation | heating / shocks / magnetic reconnection 改变 photon distribution |
| Comptonization | 电子散射改变高能尾和 peak 宽度 |
| pair opacity | \(e^\pm\) 改变 \(n_e'\)、\(\tau\) 和 effective photosphere |
| angular structure | \(\Gamma(\theta)\)、\(L(\theta)\)、\(T'(\theta)\) 改变 EATS 权重 |

所以 photospheric component 的正确问题不是“是否等于黑体”，而是：哪一层近似下可把它压缩为 blackbody、multi-color blackbody、Comptonized spectrum 或 full transfer。

## 9. 接口契约

未来 relativistic photosphere helper 至少需要：

| 类别 | 输入 / 输出 | 说明 |
| --- | --- | --- |
| outflow model | \(L(r,\theta,t)\), \(\Gamma(r,\theta,t)\), \(\rho'(r,\theta,t)\) | 决定光深面和 EATS |
| opacity | \(\kappa(\nu',T',Y_e,e^\pm)\) | Thomson 是最简近似；pair opacity 可变 |
| heating / dissipation | \(Q'_{\rm heat}(r,\theta,t)\) | 决定是否仍可用 Planck source |
| local radiation state | \(I'_{\nu'}\), \(S'_{\nu'}\), \(T'\) 或 photon distribution | 黑体只是闭合选择之一 |
| geometry | viewing angle, angular grid, shell width | 影响 Doppler 和 arrival time |
| transfer solver | surface integral or volume transfer | 必须记录 \(d\Sigma\)、\(dV\)、redshift convention |
| outputs | \(F_\nu(t)\), color temperature, effective radius, photospheric map | 区分 observable fit parameter 与 physical radius |

Formula ID：`PHOTOSPHERE-INTERFACE-CONTRACT-001`。

建议代码层级：

```text
outflow state builder
  -> opacity / optical-depth surface
  -> local radiation closure
  -> Doppler + EATS integrator
  -> observed spectrum / diagnostic parameters
  -> benchmark adapter
```

不要把 \(R_{\rm ph}(L,\Gamma)\)、\(R_{\rm bb}(L,T)\)、Planck SED 和 observed thermal component fitter 写进一个黑箱函数。

## 10. 当前代码边界

当前本地代码有：

| 代码 | 层级 | 边界 |
| --- | --- | --- |
| `thermal.py::blackbody_luminosity` | static effective blackbody | no Doppler / no EATS |
| `thermal.py::blackbody_spectral_luminosity_nu_cgs` | static \(L_\nu=4\pi^2R^2B_\nu\) | spherical effective emitter |
| `thermal.py::blackbody_sed_erg_cm2_s` | observed static blackbody SED | distance dilution only |
| `thermal.py::blackbody_radius_from_luminosity` | effective radius inversion | not physical photosphere radius |
| `thermal.py::baryonic_photosphere_radius` | coasting baryonic scale | order-of-magnitude, geometry factor convention |
| `04-thermal-and-bremsstrahlung.md` | Planck / free-free derivation | no relativistic transfer |

Formula ID：`PHOTOSPHERE-CODE-BOUNDARY-001`。

因此当前可声称：已有 Planck、Stefan-Boltzmann、effective blackbody SED、effective radius inversion 和 baryonic photosphere radius scale。不能声称：已有 moving photospheric transfer、thermal prompt spectrum predictor、multi-color blackbody solver、subphotospheric Comptonization、pair-loaded photosphere、EATS-integrated photosphere light curve 或事件级 thermal component fit。

## 11. Exact analytic status

| 对象 | 状态 | 说明 |
| --- | --- | --- |
| Planck function | closed form | LTE local source function |
| Stefan-Boltzmann law | closed form | static blackbody surface |
| effective blackbody radius | algebraic inversion | observable compression |
| coasting baryonic \(R_{\rm ph}\) scale | analytic order-of-magnitude | coefficient convention dependent |
| optical-depth surface in structured outflow | generally numerical | depends on \(\rho'\), \(\Gamma\), \(\theta\), opacity |
| EATS-integrated spectrum | generally numerical | angular and time integration required |
| subphotospheric dissipation spectrum | kinetic / transfer problem | often requires numerical radiation transfer |

Formula ID：`PHOTOSPHERE-EXACT-STATUS-001`。

## 12. Benchmark boundary

| Benchmark / mature route | 可检查 | 不能证明 |
| --- | --- | --- |
| analytic coasting \(R_{\rm ph}\) estimates | \(\Gamma^{-3}\) scale and units | full spectrum |
| multi-color blackbody fits | broadening intuition | physical uniqueness of photosphere |
| specialized GRB photosphere transfer codes | same-input convention comparison | local theory replacement |
| radiation-hydrodynamics / Monte Carlo transfer papers | spectral shape benchmark | event interpretation without same outflow model |
| current static blackbody helpers | Planck normalization and \(T^4\) law | moving photosphere |

Formula ID：`PHOTOSPHERE-BENCHMARK-BOUNDARY-001`。

任何 benchmark 都必须记录 outflow profile、opacity source、heating model、frame convention、redshift / Doppler convention、observer angle 和 output quantity。外部代码能生成 broadened thermal spectrum，不等于本地理论页可以跳过 optical-depth surface 与 transfer integral。

## 13. 不声称

- 不声称本页实现 relativistic photosphere solver。
- 不声称 fitted blackbody radius 等于 \(\tau=1\) physical radius。
- 不声称 `baryonic_photosphere_radius()` 是完整 photospheric transfer。
- 不声称 single-temperature blackbody 可解释所有 thermal-like GRB spectra。
- 不声称 subphotospheric dissipation、pair opacity、Comptonization 或 angular structure 已在本地实现。
- 不声称当前本地代码能预测任何 GRB 的 prompt thermal component。

## 14. 参考入口

- `04-thermal-and-bremsstrahlung.md`
- `12-missing-process-interface-roadmap.md`
- `00-radiative-transfer-foundations.md`
- `theory/grb-afterglow/15-notation-frames-and-convention-registry.md`
- `reproduce/grb/core/radiation/thermal.py`
