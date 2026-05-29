# 02 Afterglow Synchrotron Breaks and Closure Relations

状态：v0.1 课程讲义草案。本页把第一课的 Blandford-McKee dynamics 接到 forward-shock synchrotron spectrum，推导 \(\gamma_m\)、\(\gamma_c\)、\(\nu_m\)、\(\nu_c\)、\(F_{\nu,\max}\) 的来源，再把 break evolution 和 spectral segments 组合成 closure relations。

本页遵守辐射机制课程页的同一原则：先写 general expression 和 electron distribution，不从 sharp broken power law 或 delta approximation 开始；sharp breaks、Sari98 归一化和本地代码函数都放在近似 / implementation convention 层。

## 1. 物理图像

Forward shock 把外部介质加热成 shocked fluid。第一课已经给出 dynamics 入口：

```text
Gamma(t), R(t), n_ext(t)
  -> e'(t), n'(t), B'(t)
  -> accelerated electron distribution N'(gamma_e)
  -> synchrotron emissivity / cooling
  -> nu_m, nu_c, Fnu,max
  -> spectral segment
  -> light curve closure relation
```

这里的核心不是“背公式表”，而是看清每个 break 的物理来源：

- \(\nu_m\)：最低注入电子 \(\gamma_m\) 的 synchrotron characteristic frequency。
- \(\nu_c\)：在 dynamical time 内刚好冷却的电子 \(\gamma_c\) 的 characteristic frequency。
- \(F_{\nu,\max}\)：电子数、磁场、bulk boosting 和距离共同决定的谱归一化。
- closure relation：把 \(F_\nu(t)\propto t^{-\alpha}\nu^{-\beta_{\rm spec}}\) 中的 \(\alpha\)、\(\beta_{\rm spec}\)、\(p\) 连接起来。

## 2. 参考系与变量表

默认参考系：

- unprimed \(t_{\rm obs}\)、\(\nu\)、\(F_\nu\)：observer frame。
- primed \(B'\)、\(e'\)、\(n'\)、\(N'(\gamma)\)：shocked fluid comoving frame。
- \(\Gamma\)：shocked fluid bulk Lorentz factor。
- \(D_L\)：luminosity distance。

| 符号 | 含义 | 默认层级 |
| --- | --- | --- |
| \(p\) | electron power-law index | model parameter |
| \(\epsilon_e\) | shocked internal energy in nonthermal electrons | phenomenological |
| \(\epsilon_B\) | shocked internal energy in magnetic field | phenomenological |
| \(\xi_e\) | fraction of electrons accelerated | often set to 1 |
| \(\gamma_m\) | minimum injected electron Lorentz factor | derived for \(p>2\) |
| \(\gamma_c\) | cooling Lorentz factor | derived from loss equation |
| \(Y\) | Compton parameter for IC cooling | optional / convention-dependent |
| \(N_e\) | emitting electron number | geometry-dependent |
| \(\nu_a\) | synchrotron self-absorption break | deferred / radio boundary |

## 3. General Expression

### 3.1 Electron distribution

在 standard forward-shock model 中，只有一部分 shocked electrons 进入 nonthermal power law。写成 comoving-frame distribution：

$$
N'(\gamma_e)\,d\gamma_e
=
K\gamma_e^{-p}\,d\gamma_e,
\qquad
\gamma_e\ge\gamma_m.
$$

加速电子数密度为

$$
n'_{\rm acc}
=
\int_{\gamma_m}^{\infty}K\gamma^{-p}d\gamma
=
\xi_e n',
$$

其中 \(0<\xi_e\le1\)。很多 textbook formula 默认 \(\xi_e=1\)。

### 3.2 Synchrotron emissivity before broken-power-law approximation

comoving frame 的 synchrotron emissivity 一般应从 kernel 积分开始：

$$
j'_{\nu'}
=
{1\over4\pi}
\int_{\gamma_m}^{\infty}
N'(\gamma_e)P'_{\nu'}(\gamma_e,B')\,d\gamma_e.
$$

单电子谱功率可写成

$$
P'_{\nu'}(\gamma_e)
=
{\sqrt{3}e^3B'\sin\alpha\over m_ec^2}
F\!\left({\nu'\over\nu'_{\rm crit}}\right),
$$

其中

$$
\nu'_{\rm crit}
=
{3eB'\sin\alpha\over4\pi m_ec}\gamma_e^2,
\qquad
F(x)=x\int_x^\infty K_{5/3}(y)\,dy.
$$

这和基础同步辐射页一致：afterglow broken-power-law spectrum 是这个 kernel 积分在 power-law electrons、optically thin、asymptotic segment 下的近似结果，不是理论起点。

### 3.3 Observer-frame frequency and flux

对 on-axis relativistic blast wave，characteristic frequency 的 observer-frame 映射为

$$
\nu
\simeq
{\Gamma\over1+z}\nu'.
$$

峰值 flux density 的常用量级写成

$$
F_{\nu,\max}
\sim
{1+z\over4\pi D_L^2}
N_e\Gamma P'_{\nu,\max}.
$$

这一步已经含有 geometry、beaming 和 equal-arrival-time convention；所以不同论文和代码的 \(F_{\nu,\max}\) 前因子会不同。

## 4. Detailed Derivation I：Minimum Electron Lorentz Factor

### 4.1 目标公式

对 \(p>2\) 且 \(\gamma_m\gg1\)，目标是推出

$$
\gamma_m
=
{p-2\over p-1}
{\epsilon_e\over\xi_e}
{e'\over n'm_ec^2}
\simeq
{p-2\over p-1}
{\epsilon_e\over\xi_e}
{m_p\over m_e}\Gamma.
$$

Formula ID：`SYN-GAMMA-M-001`。

### 4.2 Number density integral

从

$$
N'(\gamma)=K\gamma^{-p}
$$

出发，电子数密度为

$$
n'_{\rm acc}
=
\int_{\gamma_m}^{\infty}K\gamma^{-p}d\gamma.
$$

当 \(p>1\)：

$$
\int_{\gamma_m}^{\infty}\gamma^{-p}d\gamma
=
\left[{\gamma^{1-p}\over1-p}\right]_{\gamma_m}^{\infty}
=
{\gamma_m^{1-p}\over p-1}.
$$

所以

$$
n'_{\rm acc}
=
{K\gamma_m^{1-p}\over p-1}.
$$

### 4.3 Energy density integral

相对论电子能量密度为

$$
u'_e
=
m_ec^2
\int_{\gamma_m}^{\infty}
K\gamma^{1-p}d\gamma.
$$

当 \(p>2\)：

$$
\int_{\gamma_m}^{\infty}\gamma^{1-p}d\gamma
=
\left[{\gamma^{2-p}\over2-p}\right]_{\gamma_m}^{\infty}
=
{\gamma_m^{2-p}\over p-2}.
$$

因此

$$
u'_e
=
{K m_ec^2\gamma_m^{2-p}\over p-2}.
$$

用 \(n'_{\rm acc}\) 消去 \(K\)：

$$
{u'_e\over n'_{\rm acc}}
=
{p-1\over p-2}
\gamma_m m_ec^2.
$$

而 microphysics parameterization 给出

$$
u'_e=\epsilon_e e',
\qquad
n'_{\rm acc}=\xi_e n'.
$$

所以

$$
\gamma_m
=
{p-2\over p-1}
{\epsilon_e e'\over\xi_e n' m_ec^2}.
$$

对 ultra-relativistic cold upstream strong shock，第一课给出

$$
e'\simeq4\Gamma^2n_{\rm ext}m_pc^2,
\qquad
n'\simeq4\Gamma n_{\rm ext}.
$$

相除得到

$$
{e'\over n'}
\simeq
\Gamma m_pc^2.
$$

于是

$$
\gamma_m
\simeq
{p-2\over p-1}
{\epsilon_e\over\xi_e}
{m_p\over m_e}\Gamma.
$$

当前本地代码 `minimum_electron_lorentz_factor()` 采用 \(\xi_e=1\) 且要求 \(p>2\)。若 \(1<p\le2\)，能量积分受高能 cutoff 控制，不能用这个短公式。

## 5. Detailed Derivation II：Cooling Lorentz Factor

### 5.1 目标公式

目标是从 cooling equation 推出

$$
\gamma_c
=
{6\pi m_ec(1+z)\over
\sigma_T B'^2\Gamma t_{\rm obs}(1+Y)}.
$$

Formula ID：`SYN-GAMMA-C-001`。

### 5.2 Loss equation

synchrotron total power 为

$$
P'_{\rm syn}
=
{4\over3}\sigma_TcU'_B\gamma_e^2,
\qquad
U'_B={B'^2\over8\pi}.
$$

若 IC cooling 可用 Thomson-like Compton parameter \(Y\) 表示，总 loss power 近似为

$$
P'_{\rm loss}
=
P'_{\rm syn}(1+Y).
$$

电子能量 \(E'_e=\gamma_e m_ec^2\)，所以

$$
{d\gamma_e\over dt'}
=
-{P'_{\rm loss}\over m_ec^2}
=
-{\sigma_TB'^2(1+Y)\over6\pi m_ec}\gamma_e^2.
$$

定义

$$
a
=
{\sigma_TB'^2(1+Y)\over6\pi m_ec}.
$$

则

$$
{d\gamma\over dt'}=-a\gamma^2.
$$

积分：

$$
\int_{\gamma_0}^{\gamma(t')}
{\gamma^{-2}}d\gamma
=
-a\int_0^{t'}dt,
$$

得到

$$
-{1\over\gamma(t')}+{1\over\gamma_0}
=
-at',
$$

即

$$
{1\over\gamma(t')}
=
{1\over\gamma_0}+at'.
$$

若初始 \(\gamma_0\) 很大，在时间 \(t'\) 后冷却到的临界 Lorentz factor 为

$$
\gamma_c={1\over at'}
=
{6\pi m_ec\over\sigma_TB'^2t'(1+Y)}.
$$

### 5.3 Comoving time convention

标准 afterglow toy convention 取

$$
t'\sim{\Gamma t_{\rm obs}\over1+z}.
$$

代入得到

$$
\gamma_c
=
{6\pi m_ec(1+z)\over
\sigma_TB'^2\Gamma t_{\rm obs}(1+Y)}.
$$

这里的 \(Y\) 是 cooling correction，不是 SSC spectrum 的完整解。若 KN suppression、time-dependent \(Y\)、adiabatic cooling 或 evolving microphysics 重要，\(\gamma_c\) 需要重新解 energy-loss equation。

## 6. Detailed Derivation III：Break Frequencies and Peak Flux

### 6.1 Characteristic frequency

使用 synchrotron kernel 的 characteristic frequency：

$$
\nu'_{\rm syn}(\gamma_e)
=
{3eB'\over4\pi m_ec}\gamma_e^2
$$

其中 pitch-angle factor 被吸收到 convention 中。observer-frame：

$$
\nu_{\rm syn}(\gamma_e)
=
{\Gamma\over1+z}
{3eB'\over4\pi m_ec}
\gamma_e^2.
$$

因此

$$
\nu_m
=
{\Gamma\over1+z}
{3eB'\over4\pi m_ec}
\gamma_m^2,
$$

$$
\nu_c
=
{\Gamma\over1+z}
{3eB'\over4\pi m_ec}
\gamma_c^2.
$$

Formula IDs：`SYN-NU-M-001`、`SYN-NU-C-001`。

### 6.2 Peak flux scale

令 emitting electron number 为

$$
N_e
\sim
{m_{\rm sw}\over m_p}.
$$

单电子 peak spectral power 的常用 scale 可写作

$$
P'_{\nu,\max}
\sim
{m_ec^2\sigma_TB'\over e},
$$

忽略 order-unity kernel / pitch-angle constants。observer-frame flux density：

$$
F_{\nu,\max}
\sim
{1+z\over4\pi D_L^2}
N_e\Gamma P'_{\nu,\max}.
$$

所以比例标度为

$$
F_{\nu,\max}
\propto
{N_e\Gamma B'\over D_L^2}.
$$

Formula ID：`SYN-FMAX-001`。

这就是为什么本地 `peak_flux_scale()` 只声称 proportional scale；`sari98_ism_reference_scales()` 才是 literature-scale normalized sanity check，而且只覆盖 spherical adiabatic ISM convention。

## 7. Detailed Derivation IV：Time Evolution for General \(k\)

### 7.1 BM dynamics input

第一课给出

$$
R\propto t_{\rm obs}^{1/(4-k)},
\qquad
\Gamma\propto t_{\rm obs}^{-(3-k)/[2(4-k)]}.
$$

外部密度为

$$
n_{\rm ext}\propto R^{-k}
\propto
t_{\rm obs}^{-k/(4-k)}.
$$

shock 后磁场满足

$$
B'^2\propto e'\propto\Gamma^2n_{\rm ext},
\qquad
B'\propto\Gamma n_{\rm ext}^{1/2}.
$$

代入时间标度：

$$
B'
\propto
t_{\rm obs}^{-(3-k)/[2(4-k)]}
t_{\rm obs}^{-k/[2(4-k)]}
=
t_{\rm obs}^{-3/[2(4-k)]}.
$$

### 7.2 Injection frequency

因为

$$
\gamma_m\propto\Gamma,
\qquad
\nu_m\propto\Gamma B'\gamma_m^2,
$$

所以

$$
\nu_m\propto\Gamma^3B'.
$$

代入

$$
\Gamma^3
\propto
t_{\rm obs}^{-3(3-k)/[2(4-k)]},
\qquad
B'\propto t_{\rm obs}^{-3/[2(4-k)]},
$$

得到

$$
\nu_m
\propto
t_{\rm obs}^{[-3(3-k)-3]/[2(4-k)]}
=
t_{\rm obs}^{-3/2}.
$$

这个结果对 ISM \(k=0\) 和 wind \(k=2\) 相同。

### 7.3 Cooling frequency

从

$$
\gamma_c\propto{1\over B'^2\Gamma t_{\rm obs}},
\qquad
\nu_c\propto\Gamma B'\gamma_c^2
$$

得到

$$
\nu_c
\propto
\Gamma B'
(B'^2\Gamma t_{\rm obs})^{-2}.
$$

整理幂指数：

$$
\nu_c
\propto
t_{\rm obs}^{(3k-4)/[2(4-k)]}.
$$

因此

$$
k=0:\quad \nu_c\propto t_{\rm obs}^{-1/2},
\qquad
k=2:\quad \nu_c\propto t_{\rm obs}^{1/2}.
$$

这就是 ISM / wind 诊断中最重要的差异之一。

### 7.4 Peak flux

电子数

$$
N_e\propto m_{\rm sw}\propto R^{3-k}
\propto t_{\rm obs}^{(3-k)/(4-k)}.
$$

而

$$
F_{\nu,\max}
\propto
N_e\Gamma B'.
$$

代入幂律：

$$
F_{\nu,\max}
\propto
t_{\rm obs}^{-k/[2(4-k)]}.
$$

因此

$$
k=0:\quad F_{\nu,\max}\propto t_{\rm obs}^{0},
\qquad
k=2:\quad F_{\nu,\max}\propto t_{\rm obs}^{-1/2}.
$$

Formula ID：`AG-SYN-BREAK-EVOL-K-001`。

## 8. Spectral Segments as Semi-Analytic Limits

### 8.1 Slow cooling

当 \(\nu_m<\nu_c\)，optically thin slow-cooling asymptotic spectrum 为

$$
F_\nu
=
F_{\nu,\max}
\begin{cases}
(\nu/\nu_m)^{1/3}, & \nu<\nu_m,\\
(\nu/\nu_m)^{-(p-1)/2}, & \nu_m<\nu<\nu_c,\\
(\nu_c/\nu_m)^{-(p-1)/2}(\nu/\nu_c)^{-p/2}, & \nu>\nu_c.
\end{cases}
$$

Formula ID：`SYN-SPEC-SLOW-001`。

### 8.2 Fast cooling

当 \(\nu_c<\nu_m\)，standard fast-cooling asymptotic spectrum 为

$$
F_\nu
=
F_{\nu,\max}
\begin{cases}
(\nu/\nu_c)^{1/3}, & \nu<\nu_c,\\
(\nu/\nu_c)^{-1/2}, & \nu_c<\nu<\nu_m,\\
(\nu_m/\nu_c)^{-1/2}(\nu/\nu_m)^{-p/2}, & \nu>\nu_m.
\end{cases}
$$

Formula ID：`SYN-SPEC-FAST-001`。

### 8.3 What is sacrificed

这些分段谱保留了 asymptotic slopes，但牺牲了：

- synchrotron kernel 的 smooth curvature。
- break 附近的 Granot-Sari smooth shape。
- self-absorption ordering。
- equal-arrival-time integration。
- SSC cooling feedback 和 KN correction。

因此代码中的 `synchrotron_flux_density()` 是 shared sanity API，不是 paper-level spectrum solver。

## 9. Detailed Derivation V：Closure Relations

### 9.1 Sign convention

本页采用

$$
F_\nu(t)\propto t^{-\alpha}\nu^{-\beta_{\rm spec}}.
$$

若论文使用 \(F_\nu\propto t^\alpha\nu^\beta\)，符号必须整体换算。

### 9.2 General closure recipe

固定观测频率时，把 spectrum 写成

$$
F_\nu(t)
=
F_{\nu,\max}(t)
\Phi\!\left[
{\nu\over\nu_m(t)},
{\nu\over\nu_c(t)},p
\right].
$$

定义幂指数

$$
\nu_m\propto t^m,
\qquad
\nu_c\propto t^c,
\qquad
F_{\nu,\max}\propto t^f.
$$

对 BM power-law medium：

$$
m=-{3\over2},
\qquad
c={3k-4\over2(4-k)},
\qquad
f=-{k\over2(4-k)}.
$$

### 9.3 Slow cooling \(\nu_m<\nu<\nu_c\)

谱段为

$$
F_\nu
=
F_{\nu,\max}
\left({\nu\over\nu_m}\right)^{-(p-1)/2}.
$$

固定 \(\nu\) 后

$$
F_\nu
\propto
F_{\nu,\max}\nu_m^{(p-1)/2}.
$$

所以时间幂指数为

$$
s=f+{p-1\over2}m.
$$

因为 \(F_\nu\propto t^{-\alpha}\)，

$$
\alpha=-s
=
-f-{p-1\over2}m.
$$

代入 ISM \(k=0\)：\(f=0\)、\(m=-3/2\)，

$$
\alpha={3(p-1)\over4}.
$$

同一谱段

$$
\beta_{\rm spec}={p-1\over2},
$$

因此

$$
\alpha={3\over2}\beta_{\rm spec}.
$$

代入 wind \(k=2\)：\(f=-1/2\)，

$$
\alpha
=
{1\over2}+{3(p-1)\over4}
=
{3p-1\over4},
$$

即

$$
\alpha={3\beta_{\rm spec}+1\over2}.
$$

Formula ID：`AG-CLOSURE-SLOW-MID-001`。

### 9.4 Slow cooling \(\nu>\nu_c\)

谱段为

$$
F_\nu
=
F_{\nu,\max}
\left({\nu_c\over\nu_m}\right)^{-(p-1)/2}
\left({\nu\over\nu_c}\right)^{-p/2}.
$$

固定 \(\nu\) 后收集 \(\nu_m\) 和 \(\nu_c\)：

$$
F_\nu
\propto
F_{\nu,\max}
\nu_m^{(p-1)/2}
\nu_c^{1/2}.
$$

所以

$$
s
=
f+{p-1\over2}m+{1\over2}c,
\qquad
\alpha=-s.
$$

对 \(k=0\) 或 \(k=2\)，代入对应 \(f,c,m\) 都得到

$$
\alpha={3p-2\over4}.
$$

该段 spectral index 为

$$
\beta_{\rm spec}={p\over2},
$$

所以

$$
\alpha
=
{3\beta_{\rm spec}-1\over2}.
$$

这解释了为什么只用 high-frequency X-ray decay 往往无法区分 ISM 和 wind。

Formula ID：`AG-CLOSURE-SLOW-HIGH-001`。

### 9.5 Fast cooling common segments

fast cooling 中，\(\nu_c<\nu<\nu_m\) 的 spectral index 是

$$
\beta_{\rm spec}={1\over2}.
$$

对 standard adiabatic ISM / wind，常见 closure 为

$$
\alpha={1\over4}.
$$

高频 \(\nu>\nu_m\) 段仍有

$$
\beta_{\rm spec}={p\over2},
\qquad
\alpha={3p-2\over4}
={3\beta_{\rm spec}-1\over2}.
$$

Formula ID：`AG-CLOSURE-FAST-001`。

## 10. Closure Tables

| Regime | Medium | Segment | \(\beta_{\rm spec}\) | \(\alpha\) | Closure |
| --- | --- | --- | --- | --- | --- |
| slow | ISM | \(\nu_m<\nu<\nu_c\) | \((p-1)/2\) | \(3(p-1)/4\) | \(\alpha=3\beta_{\rm spec}/2\) |
| slow | wind | \(\nu_m<\nu<\nu_c\) | \((p-1)/2\) | \((3p-1)/4\) | \(\alpha=(3\beta_{\rm spec}+1)/2\) |
| slow | ISM/wind | \(\nu>\nu_c\) | \(p/2\) | \((3p-2)/4\) | \(\alpha=(3\beta_{\rm spec}-1)/2\) |
| fast | ISM/wind | \(\nu_c<\nu<\nu_m\) | \(1/2\) | \(1/4\) | fixed segment |
| fast | ISM/wind | \(\nu>\nu_m\) | \(p/2\) | \((3p-2)/4\) | \(\alpha=(3\beta_{\rm spec}-1)/2\) |

## 11. Exact Analytic Status

| 对象 | 解析状态 | 说明 |
| --- | --- | --- |
| \(\gamma_m\) for \(p>2\) | closed form | depends on \(\xi_e\), \(\epsilon_e\), shock jump convention |
| \(\gamma_c\) with constant \(B'\), \(Y\) | closed form | solves \(d\gamma/dt'=-a\gamma^2\) |
| \(\nu_m,\nu_c\) | closed composition | uses characteristic-frequency convention |
| \(F_{\nu,\max}\) | proportional closed form | calibrated normalization is convention / geometry dependent |
| general synchrotron spectrum | kernel integral | no short broken-power-law exact form near breaks |
| slow/fast asymptotic spectra | semi-analytic | valid away from breaks and before SSA |
| closure relations | closed asymptotic | only for standard BM, pre-jet, constant microphysics |
| self-absorption \(\nu_a\) | regime-dependent | deferred to radio / SSA page |
| SSC-modified cooling | generally implicit | \(Y\) may require iteration and KN correction |

## 12. Approximation Hierarchy

| 层级 | 做法 | 保留 | 牺牲 |
| --- | --- | --- | --- |
| full synchrotron kernel | integrate \(N'(\gamma)P'_{\nu'}\) | spectral curvature | short closure table |
| asymptotic segments | use \(1/3\), \(-(p-1)/2\), \(-p/2\) slopes | analytic closure | smooth breaks |
| sharp broken power law | join segments at \(\nu_m,\nu_c\) | fast sanity API | physical break shape |
| smooth toy join | smooth-min numerical branch | plotting stability | calibrated Granot-Sari shape |
| Sari98 ISM normalization | literature-scale fixed point | sanity magnitudes | not general wind / EATS |
| external afterglow solver | numerical geometry / EATS | model comparison | benchmark-output only |

## 13. 从推导到代码的实现约定

当前本地实现分层如下：

| 物理量 | Formula ID | 代码 | 层级 |
| --- | --- | --- | --- |
| \(\gamma_m\) | `SYN-GAMMA-M-001` | `core/radiation/synchrotron.py::minimum_electron_lorentz_factor` | toy / literature-scale |
| \(\gamma_c\) | `SYN-GAMMA-C-001` | `core/radiation/synchrotron.py::cooling_lorentz_factor` | toy |
| characteristic frequency | `SYN-NU-M-001`, `SYN-NU-C-001` | `synchrotron_characteristic_frequency`, `injection_frequency_hz`, `cooling_frequency_hz` | toy / literature-scale |
| \(F_{\nu,\max}\) | `SYN-FMAX-001` | `peak_flux_scale`, `sari98_ism_reference_scales` | proportional / ISM reference |
| break evolution | `AG-SYN-BREAK-EVOL-K-001` | `standard_break_time_exponents` | ISM/wind lookup |
| slow/fast spectrum | `SYN-SPEC-SLOW-001`, `SYN-SPEC-FAST-001` | `synchrotron_flux_density` | sharp / toy |
| closure alpha/beta | `AG-CLOSURE-SLOW-MID-001`, `AG-CLOSURE-SLOW-HIGH-001` | `models/forward_shock/analytic_scalings.py` | literature-scale candidate |
| forward-shock composition | multiple | `models/forward_shock/model.py` | sanity / event-trend |
| forward-shock local zone | `AG-FS-LOCAL-ZONE-001` | `models/forward_shock/local_zone.py` | source-adapter smoke |

实现差异来源：

- 代码中 \(\xi_e=1\)，且 `minimum_electron_lorentz_factor()` 要求 \(p>2\)。
- `cooling_lorentz_factor()` 把 \(Y\) 当外部输入，不自洽求 SSC cooling。
- `synchrotron_characteristic_frequency()` 使用 \(3eB'/(4\pi m_ec)\) convention，不积分 pitch-angle distribution。
- `sari98_ism_reference_scales()` 只提供 ISM normalized fixed point；wind \(F_{\nu,\max}\) 归一化在 `ForwardShockParams` 中建议输入 calibrated value。
- `synchrotron_flux_density()` 的 smooth option 是 plotting convenience，不是 Granot & Sari 2002 calibrated spectrum。
- `nu_a` 当前只是 toy / parameterized interface；不能把 radio turnover 自动解释为 SSA。
- `forward_shock_radiation_screening_summary()` 复用 BM state 和 `SYN-B-001`，只把 \(B'\)、\(R'_{\rm screen}\) 和 caller-supplied \(U'_{\rm ph}\) 交给 radiation workbench；它不新增 synchrotron spectrum、closure relation 或 observed flux 公式。

## 14. Benchmark Boundary

`afterglowpy`、`VegasAfterglow`、BOXFIT、Granot-Sari tabulated shapes 或其他 mature solvers 可作为 benchmark / mature-method comparison，但不能反向定义本页公式。它们比较的是同参数、同 geometry、同 spectral convention 下的 trend 或 light curve，不是某个事件的唯一物理解释。

本地当前可以声称：

- \(\nu_m\)、\(\nu_c\)、\(F_{\nu,\max}\) 的 standard time exponents 已有代码入口。
- ISM Sari98 reference scale 可作数量级 fixed point。
- slow-cooling closure helpers 覆盖 `nu_m_to_nu_c` 和 `above_nu_c`。

不能声称：

- 已完成 full afterglow spectrum near breaks。
- 已完成 self-consistent SSC cooling。
- 已完成 radio SSA regime grid。
- 已完成 full EATS light-curve integral。
- 已完成 event-level broadband fit。

## 15. Interfaces to Later Pages

- Reverse shock：需要重新定义 \(\gamma_m\)、\(N_e\)、\(B'\) 和 crossing time。
- Jet break：closure relations 会因 geometry 和 EATS 改变。
- Structured jet：\(\alpha\) 可能是 angular structure 的 apparent slope，不再是单一区域 BM closure。
- SSC / TeV afterglow：\(Y\) 和 KN suppression 改变 \(\gamma_c\) 与 high-energy component。
- Radio / SSA：\(\nu_a\) 需要单独按 absorption coefficient 和 geometry 推导。

## 16. 不声称

- 不把 closure relation 当作 broadband fitting。
- 不用单一 X-ray slope 判定 ISM 或 wind。
- 不把 \(\epsilon_e\)、\(\epsilon_B\)、\(p\) 写成直接观测量。
- 不把 Sari98 ISM fixed point 套到 wind event。
- 不把 GRB 221009A 的 Laskar-style wind model 或其他模型写成唯一解释。

## 17. 参考来源

- Sari, Piran & Narayan 1998, *Spectra and Light Curves of Gamma-Ray Burst Afterglows*.
- Granot & Sari 2002, *The Shape of Spectral Breaks in Gamma-Ray Burst Afterglows*.
- Chevalier & Li 2000, *Wind Interaction Models for Gamma-Ray Burst Afterglows*.
- Piran 2004, *The Physics of Gamma-Ray Bursts*.
- Zhang 2014, *The Physics of Gamma-Ray Bursts & Relativistic Jets*.
- Rybicki & Lightman 1979, *Radiative Processes in Astrophysics*.
