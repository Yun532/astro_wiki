# 14 各向异性 Inverse Compton 接口

状态：v0.1 讲义级理论接口页。本页把 12 页中的 `RAD-GAP-ANISO-IC-INTERFACE-001` 展开为可推导、可审计、可映射到代码边界的课程内容。它不新增 production solver，也不把 `anisotropic_ic_geometry_factor` 升级成完整各向异性 IC 核。

核心原则：各向异性 IC 不能从 \(\nu_s\sim\gamma^2\nu\)、常数 \(U_{\rm ph}\)、head-on / tail-on 几何因子或 delta approximation 开始。安全起点是带方向的 photon phase-space distribution、电子方向分布以及双微分 Compton kernel。所有角度平均、Thomson 极限、head-on envelope 和 package-compatible benchmark 都应放在后置层。

## 1. 物理图像

各向同性 IC 只需要 photon energy density spectrum \(n_{\rm ph}(\epsilon)\)。各向异性 IC 的基本对象则是

$$
n_{\rm ph}(\epsilon,\Omega),
$$

其中 \(\Omega\) 是入射光子方向。散射后还要保留出射方向 \(\Omega_s\)，因为外部光场、盘光子、prompt photons、jet sheath photons、off-axis geometry 或 EATS 上的局域 photon beam 都会让 observer direction 改变谱形和归一化。

Formula ID：`IC-ANISO-PICTURE-001`。

最小物理链条是：

```text
anisotropic seed photons n_ph(epsilon, Omega)
  + electron distribution n_e(gamma, Omega_e)
  + Compton kinematics in electron rest frame
  -> directional emissivity j_epsilon_s(Omega_s)
  -> optional cooling rate / angular moments
```

若把 \(n_{\rm ph}(\epsilon,\Omega)\) 先压成 \(U_{\rm ph}\)，就已经丢掉了 head-on 与 tail-on 权重、散射方向和 beaming 信息；后面无法再从 scalar \(U_{\rm ph}\) 恢复它们。

## 2. 变量与参考系

本页使用源内 local comoving frame 作为未加撇号的工作系。电子瞬时运动方向为 \(\hat{\boldsymbol p}_e\)，入射光子方向为 \(\hat{\boldsymbol k}\)，散射光子方向为 \(\hat{\boldsymbol k}_s\)。电子 rest frame 用双撇号表示。

| 符号 | 含义 |
| --- | --- |
| \(\epsilon\) | 入射光子能量 |
| \(\epsilon_s\) | 散射后光子能量 |
| \(\Omega\), \(\Omega_s\) | 入射 / 出射光子方向 |
| \(\Omega_e\) | 电子方向 |
| \(\gamma\), \(\beta\) | 电子 Lorentz factor 与速度 |
| \(\mu=\hat{\boldsymbol p}_e\cdot\hat{\boldsymbol k}\) | 入射光子相对电子运动方向的余弦 |
| \(\mu_s=\hat{\boldsymbol p}_e\cdot\hat{\boldsymbol k}_s\) | 出射光子相对电子运动方向的余弦 |
| \(\Theta''\) | electron rest frame 中入射与出射光子的夹角 |

Formula ID：`IC-ANISO-FRAME-VARIABLES-001`。

能量变换的第一步是把 seed photon 变到 electron rest frame：

$$
\epsilon''
=
\gamma\epsilon(1-\beta\mu).
$$

Formula ID：`IC-ANISO-REST-FRAME-SEED-001`。

这条式子给出各向异性 IC 的第一层物理直觉：head-on photon 对应 \(\mu=-1\)，\(\epsilon''\simeq\gamma\epsilon(1+\beta)\)；tail-on photon 对应 \(\mu=1\)，\(\epsilon''\simeq\gamma\epsilon(1-\beta)\)。但它只说明碰撞能量如何变换，还不是完整 emissivity。

## 3. 一般发射率表达式

最一般的 directional photon production rate 应保留电子能量、电子方向、seed photon 能量、seed photon 方向和出射方向：

$$
{d\dot n_\gamma\over d\epsilon_s d\Omega_s}
=
c
\int d\gamma\int d\Omega_e\,
n_e(\gamma,\Omega_e)
\int d\epsilon\int d\Omega\,
n_{\rm ph}(\epsilon,\Omega)
(1-\beta\mu)
{d\sigma_{\rm IC}\over d\epsilon_s d\Omega_s}.
$$

能量发射率为

$$
j_{\epsilon_s}(\Omega_s)
=
\epsilon_s
{d\dot n_\gamma\over d\epsilon_s d\Omega_s}.
$$

Formula ID：`IC-ANISO-GENERAL-EMISSIVITY-001`。

这里的 \((1-\beta\mu)c\) 是 electron 和 photon 的相对通量因子。它不能被提前角平均，否则各向异性 seed field 的主要信息会被抹掉。若电子各向同性，可写

$$
n_e(\gamma,\Omega_e)={n_e(\gamma)\over4\pi},
$$

但这只允许先对 \(\Omega_e\) 做平均；不能把 \(n_{\rm ph}(\epsilon,\Omega)\) 同时替换成 \(n_{\rm ph}(\epsilon)/(4\pi)\)，除非物理问题本身就是 isotropic photon bath。

## 4. Kernel 来源：先在 electron rest frame 写散射

Compton 散射最干净的微分截面写在 electron rest frame。Klein-Nishina 角微分截面为

$$
{d\sigma''\over d\Omega_s''}
=
{r_e^2\over2}
\left({\epsilon_s''\over\epsilon''}\right)^2
\left[
{\epsilon_s''\over\epsilon''}
+{\epsilon''\over\epsilon_s''}
-\sin^2\Theta''
\right],
$$

其中散射后能量由能量动量守恒给出

$$
\epsilon_s''
=
{\epsilon''\over
1+{\epsilon''\over m_ec^2}(1-\cos\Theta'')}.
$$

Formula ID：`IC-ANISO-KN-REST-KERNEL-001`。

把这个 kernel 变回 local comoving frame，需要同时变换能量、方向和立体角 Jacobian。课程上最重要的不是背诵某个封装后的公式，而是保留计算依赖关系：

```text
(epsilon, Omega, gamma, Omega_e)
  -> epsilon'' and incident direction in electron rest frame
  -> scatter with KN angular kernel
  -> transform (epsilon_s'', Omega_s'') back to (epsilon_s, Omega_s)
  -> integrate over electron and seed photon distributions
```

这也是为什么各向异性 IC 不能直接复用 angle-integrated Blumenthal-Gould kernel：BG kernel 已经把 photon direction 和 emitted direction 的信息压缩掉了。

## 5. 各向同性极限必须作为检验，而不是起点

若 seed photons 与 electrons 都各向同性，且只关心 angle-integrated emissivity，方向积分可约化为熟悉的 isotropic IC / Blumenthal-Gould 形式：

$$
{d\dot n_\gamma\over d\epsilon_s}
=
c
\int d\gamma\,n_e(\gamma)
\int d\epsilon\,n_{\rm ph}(\epsilon)
{d\sigma_{\rm BG}\over d\epsilon_s}.
$$

Formula ID：`IC-ANISO-ISOTROPIC-LIMIT-001`。

这条式子是 full angular expression 的降阶极限。代码中的 `inverse_compton_differential_cross_section_cgs`、`blumenthal_gould_q` 和 `blumenthal_gould_kernel` 应理解为这个 isotropic / angle-integrated 路线的 production kernel，而不是各向异性 IC 的替代品。

## 6. 教学几何因子的位置

在 Thomson limit 且只想看碰撞几何的能量损失趋势时，可以从 electron rest-frame seed energy 的变换得到近似 envelope：

$$
P_{\rm IC}(\mu)
\propto
\gamma^2 U_{\rm ph} (1-\beta\mu)^2.
$$

Formula ID：`IC-ANISO-TEACHING-GEOM-001`。

这个因子能解释 head-on photon 比 tail-on photon 更有效，也能帮助画 angle diagnostic 图。但它不是谱核，因为它没有给出 \(\epsilon_s\) 分布、没有出射方向 \(\Omega_s\)、没有 KN angular redistribution，也没有把实际 \(n_{\rm ph}(\epsilon,\Omega)\) 积分进去。

当前代码中的 `cooling_angle.py::anisotropic_ic_geometry_factor` 对应旧 Formula ID `ANG-IC-ANISO-GEOM-001`，应继续标为 `teaching-only`。若未来新建 solver，应使用新的 `IC-ANISO-*` Formula ID，而不是覆盖旧教学 ID。

## 7. 接口契约

未来如果要实现 anisotropic IC，最小接口应显式接收和输出以下对象：

| 类别 | 必需输入 / 输出 | 说明 |
| --- | --- | --- |
| electron distribution | \(n_e(\gamma,\Omega_e)\) 或 isotropic \(n_e(\gamma)\) | 必须写清 density / total-number convention |
| photon field | \(n_{\rm ph}(\epsilon,\Omega)\) | 不能只给 scalar \(U_{\rm ph}\) |
| grids | \(\epsilon\), \(\Omega\), \(\gamma\), optional \(\Omega_e\) | 角网格、moments 或 symmetry assumption 必须登记 |
| observer direction | \(\Omega_s\) 或需要输出的 angular bins | directional emissivity 的目标方向 |
| kernel convention | rest-frame KN angular kernel / literature approximation / package convention | 不能把外部 convention 写成唯一标准 |
| frame convention | local comoving / lab / observer frame | Doppler 与 redshift 不应藏在 kernel 内 |
| outputs | \(j_{\epsilon_s}(\Omega_s)\), optional cooling \(\dot\gamma(\Omega_e)\), angular moments | cooling 与 emissivity 不一定共享同一角平均 |

Formula ID：`IC-ANISO-INTERFACE-CONTRACT-001`。

一个安全的 Python 层级应类似：

```text
seed photon angular field builder
  -> anisotropic IC kernel evaluator
  -> directional emissivity integrator
  -> optional cooling/moment reducer
```

这样既能让 benchmark 对齐某个成熟实现，也能在课程页中解释每层近似来自哪里。

## 8. 当前代码实现约定

当前本地代码的边界如下：

| 函数 / 文件 | 当前层级 | 说明 |
| --- | --- | --- |
| `inverse_compton.py::inverse_compton_differential_cross_section_cgs` | isotropic BG/KN production kernel | angle-integrated；不输出 \(\Omega_s\) |
| `inverse_compton.py::blumenthal_gould_q` | isotropic kinematic helper | 用于 BG kernel 的 \(q\) 变量 |
| `inverse_compton.py::blumenthal_gould_kernel` | isotropic kernel helper | 不能描述 anisotropic seed photon field |
| `leptonic_spectra.py::inverse_compton_tabulated_sed_erg_cm2_s` | supplied isotropic seed SED | caller supplies photon spectrum；没有 angular field |
| `cooling_angle.py::anisotropic_ic_geometry_factor` | teaching-only envelope | 只描述 head-on / tail-on 几何趋势 |

Formula ID：`IC-ANISO-CODE-BOUNDARY-001`。

因此当前网页和代码可以声称：已有 isotropic IC / BG-KN kernel、tabulated seed photon SED、以及教学级 anisotropic encounter factor。不能声称：已有 directional anisotropic IC emissivity、external Compton angular solver、anisotropic cooling table、off-axis IC light curve 或 anisotropic package parity。

## 9. Exact analytic status

| 对象 | 状态 | 说明 |
| --- | --- | --- |
| electron rest-frame Compton kinematics | closed | 单次散射能量角度关系可闭式写出 |
| KN angular differential cross-section | closed | 在 electron rest frame 中闭式 |
| 任意 \(n_{\rm ph}(\epsilon,\Omega)\) 的 directional emissivity | generally numerical | 多维角度和能量积分 |
| isotropic limit | semi-analytic / numerical kernel | 可降到 BG kernel |
| Thomson head-on envelope | analytic scaling | 只给趋势，不给谱 |
| external Compton light curve | geometry-dependent numerical | 还需要源结构、EATS、Doppler、时间延迟 |

Formula ID：`IC-ANISO-EXACT-STATUS-001`。

## 10. Benchmark boundary

各向异性 IC 的 benchmark 可以来自文献 kernel、专门的 external-Compton code 或成熟 package，但必须记录同一组输入：

| Benchmark 类型 | 可检查 | 不能证明 |
| --- | --- | --- |
| rest-frame KN angular kernel | 单次散射角分布与 kinematic limits | 完整源几何 |
| isotropic limit 回归 BG kernel | angular solver 在 isotropic field 下收敛到现有 IC | anisotropic case 已对 |
| mono-directional photon beam test | head-on / tail-on 极限、能量边界 | 任意 seed field 都正确 |
| external package same-convention comparison | 单 convention 下的 directional SED ratio | package convention 是唯一理论标准 |
| afterglow / prompt photon geometry test | 量级趋势、角度敏感性 | 事件唯一解释 |

Formula ID：`IC-ANISO-BENCHMARK-BOUNDARY-001`。

最低可接受验证路线应先做三件事：各向同性极限回归现有 BG kernel；mono-directional photon beam 的 head-on / tail-on 极限检查；能量守恒和 KN 上限检查。只有这些通过以后，才适合接 external Compton 或 afterglow geometry。

## 11. 不声称

- 不声称本页实现了 anisotropic IC solver。
- 不声称 `ANG-IC-ANISO-GEOM-001` 可以给出谱或方向发射率。
- 不声称 isotropic BG/KN kernel 可直接用于外部定向 photon beam。
- 不声称 scalar \(U_{\rm ph}\) 足以描述 prompt photons、disk photons、jet photons 或 off-axis seed field。
- 不声称 delta approximation、\(\nu_s\sim\gamma^2\nu\) 或 head-on envelope 是理论起点。
- 不声称任何 external package 的输出是本课程的理论证明；它只能作为 same-convention benchmark。

## 12. 参考入口

- `02-inverse-compton-and-ssc.md`
- `03-gamma-gamma-opacity.md`
- `12-missing-process-interface-roadmap.md`
- `13-self-consistent-ssc-transfer.md`
- `reproduce/grb/core/radiation/inverse_compton.py`
- `reproduce/grb/core/radiation/cooling_angle.py`
