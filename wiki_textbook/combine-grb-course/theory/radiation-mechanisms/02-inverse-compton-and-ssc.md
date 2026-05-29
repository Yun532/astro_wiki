# 02 Inverse Compton and Synchrotron Self-Compton

状态：v2.3 课程讲义草案。本页按 `general expression -> detailed derivation block -> exact analytic status -> analytic / semi-analytic limits -> numerical approximation` 的规则组织。先讲 inverse Compton scattering 的一般核，再把 Thomson kernel 从 Compton 运动学、Lorentz 变换、delta 函数、Jacobian 和角积分中推出，再讲 Klein-Nishina 与 SSC 的解析状态。

## 1. 阅读路线

本页的逻辑顺序是：

1. 单次散射的物理图像和参考系。
2. Thomson limit：经典低能截面、频率提升、冷却功率。
3. 完整 IC 谱：Blumenthal-Gould / Klein-Nishina kernel 的一般积分表达式。
4. 详细推导：不直接引用 \(f(q)\)，而是从散射运动学、delta 函数约束、Jacobian 和角积分推出 Thomson kernel。
5. 解析极限：保留 Thomson kernel 的 power-law 解析解，以及更快的 delta approximation。
6. Klein-Nishina：总截面解析式、微分核、低高能极限、为何一般完整谱要数值积分。
7. SSC：一般嵌套积分表达式、是否有闭式精确解析解、较精确的半解析路线。
8. 计算路线、数值实现边界、参考文献。

## 2. 物理图像与符号

普通 Compton scattering 中，高能 photon 把能量传给低能 electron，散射后 photon 能量降低。Inverse Compton 则相反：相对论 electron 携带大量动能，低能 seed photon 在 electron rest frame 中被蓝移，近似散射后再变回 lab frame，于是 photon energy 被提升。

核心链条是：

$$
\text{seed photons}
+
\text{relativistic electrons}
\rightarrow
\text{scattering kernel}
\rightarrow
\text{up-scattered spectrum}
\rightarrow
\text{electron cooling}.
$$

| 符号 | 含义 | 单位或量纲 |
| --- | --- | --- |
| $\epsilon=h\nu$ | 入射 seed photon energy | erg 或 eV |
| $\epsilon_s=h\nu_s$ | 散射后 photon energy | erg 或 eV |
| $\gamma$ | electron Lorentz factor | dimensionless |
| $\beta$ | $v/c$ | dimensionless |
| $n_e(\gamma)$ | electron Lorentz factor distribution | cm$^{-3}$ per $\gamma$ |
| $n_{\rm ph}(\epsilon)$ | seed photon number density per energy | cm$^{-3}$ erg$^{-1}$ |
| $U_{\rm ph}$ | seed photon energy density | erg cm$^{-3}$ |
| $U_B$ | magnetic energy density | erg cm$^{-3}$ |
| $\sigma_T$ | Thomson cross-section | cm$^2$ |
| $Y$ | IC cooling power / synchrotron cooling power | dimensionless |

常用参考系：

- lab frame：seed photon field 通常在这个系中定义。
- electron rest frame：单次散射的能量变化和截面最容易写出。

## 3. 单次散射：Thomson 极限

Thomson limit 要求 photon 在 electron rest frame 中的能量远小于电子静能：

$$
\epsilon'\ll m_ec^2.
$$

经典电子半径：

$$
r_e=\frac{e^2}{m_ec^2}.
$$

非偏振 Thomson differential cross-section：

$$
\frac{d\sigma}{d\Omega}
=
\frac{r_e^2}{2}(1+\cos^2\theta).
$$

对立体角积分：

$$
\sigma_T
=
2\pi\int_0^\pi
\frac{r_e^2}{2}(1+\cos^2\theta)\sin\theta\,d\theta.
$$

令 $\mu=\cos\theta$：

$$
\sigma_T
=
\pi r_e^2\int_{-1}^{1}(1+\mu^2)d\mu
=
\frac{8\pi}{3}r_e^2.
$$

## 4. 单次散射：能量提升

把 seed photon 从 lab frame 变到 electron rest frame：

$$
\epsilon'
=
\gamma\epsilon(1-\beta\cos\theta).
$$

对 head-on photon，$\cos\theta=-1$，强相对论时：

$$
\epsilon'\simeq2\gamma\epsilon.
$$

Thomson limit 下，electron rest frame 中散射近似弹性：

$$
\epsilon_s'\simeq\epsilon'.
$$

再变回 lab frame：

$$
\epsilon_s
=
\gamma\epsilon_s'(1+\beta\cos\theta_s').
$$

若散射后 photon 沿 electron 运动方向出射，$\cos\theta_s'\simeq1$：

$$
\epsilon_s\simeq4\gamma^2\epsilon.
$$

对各向同性 photon field 和角平均散射，常用：

$$
\langle\epsilon_s\rangle
\simeq
\frac{4}{3}\gamma^2\epsilon.
$$

这就是 IC 的 $\gamma^2$ boost。

## 5. 单电子冷却功率

Thomson limit 中，IC cooling power 为：

$$
P_{\rm IC}
=
\frac{4}{3}\sigma_Tc\beta^2\gamma^2U_{\rm ph}.
$$

强相对论时 $\beta\simeq1$：

$$
P_{\rm IC}
\simeq
\frac{4}{3}\sigma_Tc\gamma^2U_{\rm ph}.
$$

同步辐射冷却功率为：

$$
P_{\rm syn}
=
\frac{4}{3}\sigma_Tc\gamma^2U_B.
$$

所以：

$$
Y
\equiv
\frac{P_{\rm IC}}{P_{\rm syn}}
\simeq
\frac{U_{\rm ph}}{U_B}.
$$

电子 IC cooling time：

$$
t_{\rm IC}
=
\frac{\gamma m_ec^2}{P_{\rm IC}}
=
\frac{3m_ec}{4\sigma_T\gamma U_{\rm ph}}.
$$

## 6. 完整 IC 谱：Blumenthal-Gould 核

对各向同性 electrons 和各向同性 seed photons，最常用的一般表达式是：

$$
\frac{dN_\gamma}{dt\,d\epsilon_s}
=
c\int d\gamma\,n_e(\gamma)
\int d\epsilon\,n_{\rm ph}(\epsilon)
\frac{d\sigma_{\rm IC}}{d\epsilon_s}.
$$

完整 Klein-Nishina 微分核可写成：

$$
\frac{d\sigma_{\rm IC}}{d\epsilon_s}
=
\frac{3\sigma_T}{4\gamma^2\epsilon}
G(q,\Gamma_e),
$$

其中：

$$
G(q,\Gamma_e)
=
2q\ln q
+
(1+2q)(1-q)
+
\frac{(\Gamma_eq)^2(1-q)}
{2(1+\Gamma_eq)}.
$$

定义：

$$
\Gamma_e
=
\frac{4\gamma\epsilon}{m_ec^2},
$$

$$
q
=
\frac{\epsilon_s}
{\Gamma_e(\gamma m_ec^2-\epsilon_s)}.
$$

运动学范围：

$$
\frac{1}{4\gamma^2}
\le
q
\le
1,
$$

否则 kernel 取 0。

photon energy luminosity spectrum：

$$
L_{\epsilon_s}
=
\epsilon_s
\frac{dN_\gamma}{dt\,d\epsilon_s}.
$$

SED：

$$
\epsilon_sL_{\epsilon_s}
=
\epsilon_s^2c
\int d\gamma\,n_e(\gamma)
\int d\epsilon\,n_{\rm ph}(\epsilon)
\frac{3\sigma_T}{4\gamma^2\epsilon}
G(q,\Gamma_e).
$$

这才是包含 Thomson 到 Klein-Nishina 过渡的完整 IC 积分表达式。它通常需要数值积分，但不是 toy formula，也不是 delta approximation。

## 7. 详细解析推导：从 Compton 运动学到 Thomson kernel

这一节专门补上最容易被教材速写省略的一段：为什么 IC 单电子散射率可以写成一个 \(q\) 的核函数。它不是从 \(f(q)\) 开始，而是从 electron rest frame 中的 Compton 公式和散射截面开始。

为避免单位混乱，先使用无量纲 photon energy：

$$
a=\frac{\epsilon}{m_ec^2},
\qquad
a_1=\frac{\epsilon_s}{m_ec^2}.
$$

带撇号的量在 electron rest frame 中定义，不带撇号的量在 lab frame 中定义。入射 photon 在 electron rest frame 中的能量为：

$$
a'
=
\gamma a(1-\beta\mu),
$$

其中 \(\mu\) 是 lab frame 中入射 photon 方向与 electron 运动方向的夹角余弦。electron rest frame 中的 Compton 运动学给出：

$$
a_1'
=
\frac{a'}{1+a'(1-\mu')},
$$

其中 \(\mu'\) 是 electron rest frame 中散射角余弦。这个式子来自四动量守恒；当 \(a'\ll1\) 时，分母趋近 1，散射在 electron rest frame 中近似弹性，这就是 Thomson limit 的运动学含义。

为了在散射率积分中处理能量约束，引入变量：

$$
f
=
\frac{a'}{1+a'(1-\mu')}.
$$

于是能量守恒可由 delta function 写成 \(\delta(a_1'-f)\)。反解 \(a'\)：

$$
a'
=
\frac{f}{1-f(1-\mu')}.
$$

对 \(f\) 求微分，得到 Jacobian：

$$
da'
=
\frac{df}{\left[1-f(1-\mu')\right]^2}.
$$

这一项就是后面核函数中额外能量因子的来源之一。它的作用是把 Compton 公式中的非线性能量关系转成可被 delta function 积掉的变量。

再把散射后 photon 从 electron rest frame 变回 lab frame。定义角变量：

$$
\eta
=
1-\beta\mu'
\simeq
1-\mu',
$$

其中最后一步使用 ultra-relativistic approximation \(\beta\simeq1\)。散射后 photon energy 的变换为：

$$
a_1
=
\gamma a_1'\eta.
$$

因此：

$$
a_1'
=
\frac{a_1}{\gamma\eta},
\qquad
\frac{da_1'}{da_1}
=
\frac{1}{\gamma\eta}.
$$

这个 \(1/(\gamma\eta)\) 是把 electron rest frame 的能量分布改写成 lab-frame \(a_1\) 分布时必须保留的 Jacobian。

把上述关系代回散射率，并对 delta function 完成能量积分后，可以把剩余角积分写成：

$$
\frac{dN_{\gamma,a}}{dt\,da_1}
=
\frac{\pi c r_e^2 a_1 n(a)\,da}
{2\gamma^4a^2\left(1-\frac{a_1}{\gamma}\right)}
\int_{\eta_{\min}}^{2}
\left[
\eta^2-2\eta+2+
\frac{
\left(a_1/\gamma\right)^2
}
{
1-\frac{a_1}{\gamma}
}
\right]
\frac{d\eta}{\eta^2}.
$$

这里 \(r_e=e^2/(m_ec^2)\) 是 classical electron radius。上式的结构可以读成：

$$
\text{Compton kinematics}
+
\text{Lorentz transformation}
+
\delta\text{ function constraint}
+
\text{Jacobian}
+
\text{angular integral}.
$$

为了得到标准核函数，定义：

$$
q
=
\frac{a_1}
{4\gamma^2a\left(1-\frac{a_1}{\gamma}\right)}.
$$

在 Thomson limit 中，散射后 photon energy 仍满足 \(a_1/\gamma\ll1\)，于是：

$$
q
\simeq
\frac{a_1}{4\gamma^2a}.
$$

角积分下限由散射运动学给出：

$$
\eta_{\min}=2q,
\qquad
\eta_{\max}=2.
$$

令：

$$
x=\frac{a_1}{\gamma},
\qquad
C=\frac{x^2}{1-x}.
$$

则上面的角积分核心可写成：

$$
I(q)
=
\int_{2q}^{2}
\left[
1-\frac{2}{\eta}
+
\frac{2+C}{\eta^2}
\right]d\eta.
$$

逐项积分：

$$
I(q)
=
\left[
\eta
-2\ln\eta
-\frac{2+C}{\eta}
\right]_{2q}^{2}.
$$

代入上下限，得到：

$$
I(q)
=
1-2q+2\ln q+\frac{1}{q}
+
C\left(
\frac{1}{2q}-\frac{1}{2}
\right).
$$

再用：

$$
\sigma_T
=
\frac{8\pi r_e^2}{3},
$$

并把前因子与 \(I(q)\) 整理到标准形式，单电子对能量为 \(a\) 的 seed photons 的散射率可写成：

$$
\frac{dN_{\gamma,a}}{dt\,da_1}
=
\frac{3\sigma_Tc\,n(a)\,da}
{4\gamma^2a}
\mathcal{F}(q).
$$

完整 Klein-Nishina kernel 的同一套推导会给出：

$$
\mathcal{F}(q)
=
2q\ln q+(1+2q)(1-q)
+
\frac{(\Gamma q)^2(1-q)}
{2(1+\Gamma q)},
\qquad
\Gamma=4\gamma a.
$$

在 Thomson limit 中 \(\Gamma q\ll1\)，最后一项被 recoil correction 控制，可忽略，于是得到常见 Thomson kernel：

$$
f(q)
=
2q\ln q+(1+2q)(1-q),
\qquad
0<q<1.
$$

这一步说明了 \(f(q)\) 的来源：它不是经验函数，而是 Compton 运动学、微分截面、delta 函数能量约束和角积分共同留下的无量纲散射核。

## 8. 解析极限 I：保留 Thomson kernel，不做 delta approximation

第一层解析特例是：取 Thomson limit，但保留散射核的形状，而不是立刻使用 delta approximation。

设 seed photon 为单能、各向同性 photon bath：

$$
n_{\rm ph}(\epsilon)
=
n_0\delta(\epsilon-\epsilon_0).
$$

Thomson kernel：

$$
\frac{d\sigma_{\rm IC}}{d\epsilon_s}
=
\frac{3\sigma_T}{4\gamma^2\epsilon_0}
f(q),
$$

其中：

$$
q
=
\frac{\epsilon_s}{4\gamma^2\epsilon_0},
\qquad
0<q<1,
$$

$$
f(q)
=
2q\ln q+(1+2q)(1-q).
$$

代入 power-law electrons：

$$
N(\gamma)=K\gamma^{-p}.
$$

photon production spectrum：

$$
\frac{dN_\gamma}{dt\,d\epsilon_s}
=
cn_0
\int K\gamma^{-p}
\frac{3\sigma_T}{4\gamma^2\epsilon_0}
f(q)\,d\gamma.
$$

令：

$$
q
=
\frac{\epsilon_s}{4\epsilon_0\gamma^2},
\qquad
\gamma
=
\left(\frac{\epsilon_s}{4\epsilon_0q}\right)^{1/2},
$$

则：

$$
d\gamma
=
-\frac{\gamma}{2q}\,dq.
$$

代入后：

$$
\frac{dN_\gamma}{dt\,d\epsilon_s}
=
\frac{3\sigma_Tcn_0K}{8\epsilon_0}
\left(\frac{4\epsilon_0}{\epsilon_s}\right)^{(p+1)/2}
\int_0^1 q^{(p-1)/2}f(q)\,dq.
$$

定义：

$$
A(p)
=
\int_0^1 q^{(p-1)/2}
\left[
2q\ln q+(1+2q)(1-q)
\right]dq.
$$

积分可解析完成：

$$
A(p)
=
\frac{2}{p+1}
+
\frac{2}{p+3}
-
\frac{4}{p+5}
-
\frac{8}{(p+3)^2}.
$$

所以：

$$
\frac{dN_\gamma}{dt\,d\epsilon_s}
=
\frac{3\sigma_Tcn_0K}{8\epsilon_0}
\left(\frac{4\epsilon_0}{\epsilon_s}\right)^{(p+1)/2}
A(p).
$$

能量光度谱：

$$
L_{\epsilon_s}
=
\frac{3\sigma_Tcn_0K}{8\epsilon_0}
(4\epsilon_0)^{(p+1)/2}
A(p)
\epsilon_s^{-(p-1)/2}.
$$

SED：

$$
\epsilon_sL_{\epsilon_s}
\propto
\epsilon_s^{(3-p)/2}.
$$

这个解比 delta approximation 更完整：它保留了 Thomson scattering kernel 的形状，归一化常数是 $A(p)$。

## 9. 解析极限 II：delta approximation

delta approximation 把散射后 photon energy 近似集中在：

$$
\epsilon_s
=
a\gamma^2\epsilon_0,
\qquad
a=\frac{4}{3}.
$$

若电子总分布为 $N(\gamma)$：

$$
L_\epsilon(\epsilon_s)
=
\int N(\gamma)P_{\rm IC}(\gamma)
\delta(\epsilon_s-a\gamma^2\epsilon_0)\,d\gamma.
$$

反解：

$$
\gamma_\ast
=
\left(\frac{\epsilon_s}{a\epsilon_0}\right)^{1/2}.
$$

利用 delta function：

$$
L_\epsilon(\epsilon_s)
=
\frac{
N(\gamma_\ast)P_{\rm IC}(\gamma_\ast)
}{
2a\epsilon_0\gamma_\ast
}.
$$

若：

$$
N(\gamma)=K\gamma^{-p},
$$

则：

$$
L_\epsilon(\epsilon_s)
=
\frac{2\sigma_TcU_{\rm ph}}{3a\epsilon_0}
K
\left(
\frac{\epsilon_s}{a\epsilon_0}
\right)^{(1-p)/2}.
$$

所以：

$$
L_\epsilon\propto\epsilon_s^{-(p-1)/2},
\qquad
\epsilon_sL_\epsilon\propto\epsilon_s^{(3-p)/2}.
$$

若电子谱有指数 cutoff：

$$
N(\gamma)
=
K\gamma^{-p}
\exp\left(-\frac{\gamma}{\gamma_{\rm cut}}\right),
$$

则：

$$
L_\epsilon
\propto
\epsilon_s^{(1-p)/2}
\exp\left[
-
\left(
\frac{\epsilon_s}{a\epsilon_0\gamma_{\rm cut}^2}
\right)^{1/2}
\right].
$$

delta approximation 很适合教学、量级估计和代码 sanity check，但不能替代完整 kernel。

## 10. Klein-Nishina：为什么出现、怎样计算

Thomson scattering 是低能经典极限。当 photon 在 electron rest frame 中能量接近电子静能：

$$
\epsilon'\sim m_ec^2,
$$

电子反冲不可忽略，散射必须用相对论能量-动量守恒处理。electron rest frame 中的 Compton 公式为：

$$
\epsilon_s'
=
\frac{\epsilon'}
{1+\frac{\epsilon'}{m_ec^2}(1-\cos\theta')}.
$$

若 $\epsilon'\ll m_ec^2$，分母约为 1，回到 Thomson limit。若 $\epsilon'\gtrsim m_ec^2$，散射后 photon energy 被 recoil 限制。

定义：

$$
x=\frac{\epsilon'}{m_ec^2}.
$$

Klein-Nishina 总截面有闭式解析式：

$$
\sigma_{\rm KN}
=
\frac{3\sigma_T}{4}
\left[
\frac{1+x}{x^3}
\left(
\frac{2x(1+x)}{1+2x}
-
\ln(1+2x)
\right)
+
\frac{\ln(1+2x)}{2x}
-
\frac{1+3x}{(1+2x)^2}
\right].
$$

低能极限：

$$
x\ll1:
\qquad
\sigma_{\rm KN}
\simeq
\sigma_T(1-2x+\cdots).
$$

高能极限：

$$
x\gg1:
\qquad
\sigma_{\rm KN}
\simeq
\frac{3\sigma_T}{8x}
\left[
\ln(2x)+\frac{1}{2}
\right].
$$

所以 KN suppression 的直观含义是：高能 photon 不再把 electron 看作经典 Thomson scatterer，recoil 和量子效应让散射截面约按 $\ln x/x$ 下降。

要计算散射后的谱，不能只用总截面，而要用第 6 节的微分核。三层结论是：

- KN 总截面：有闭式解析式。
- KN 微分核：有闭式解析式。
- 任意 electron spectrum 和任意 seed photon spectrum 下的完整 IC 谱：一般没有短的闭式解析解，通常数值积分。

快速 kinematic cap 常写为：

$$
\epsilon_{s,\rm cap}
=
\min\left[
\frac{4}{3}\gamma^2\epsilon,\,
\gamma m_ec^2
\right].
$$

## 11. SSC：一般表达式、解析状态与近似层级

SSC 是 IC 的特殊闭环：同一群 electrons 先在磁场中产生 synchrotron photons，这些 photons 又成为 seed field，被同一群或同一区域 electrons 再次散射。

### 11.1 一般嵌套积分

同步 emissivity：

$$
j_\nu^{\rm syn}
=
\frac{1}{4\pi}
\int n_e(\gamma)P_\nu^{\rm syn}(\gamma)\,d\gamma.
$$

均匀 one-zone、optically thin、源区半径 $R$ 时：

$$
n_{\rm syn}(\epsilon)
\sim
\frac{4\pi R}{c}
\frac{j_\epsilon^{\rm syn}}{\epsilon}.
$$

first-order SSC：

$$
\frac{dN_\gamma^{\rm SSC}}{dt\,d\epsilon_s}
=
c\int d\gamma\,n_e(\gamma)
\int d\epsilon\,n_{\rm syn}(\epsilon)
\frac{d\sigma_{\rm IC}}{d\epsilon_s}.
$$

代入 $n_{\rm syn}$：

$$
\frac{dN_\gamma^{\rm SSC}}{dt\,d\epsilon_s}
\sim
4\pi R
\int d\gamma\,n_e(\gamma)
\int d\epsilon\,
\frac{j_\epsilon^{\rm syn}}{\epsilon}
\frac{d\sigma_{\rm IC}}{d\epsilon_s}.
$$

而：

$$
j_\epsilon^{\rm syn}
=
\frac{1}{4\pi}
\int d\gamma'\,
n_e(\gamma')P_\epsilon^{\rm syn}(\gamma').
$$

所以 SSC 是 synchrotron kernel integral 和 IC kernel integral 的嵌套问题。

### 11.2 SSC 有没有精确解析解？

一般没有短的闭式精确解析解。原因是：

- synchrotron seed spectrum 是宽谱，不是 monoenergetic photon bath。
- seed photon density 依赖源区几何、逃逸时间、self-absorption 和空间分布。
- IC kernel 在高能端进入 Klein-Nishina regime，积分边界随 $\gamma$、$\epsilon$、$\epsilon_s$ 变化。
- SSC 是自耦合问题，同一 $n_e(\gamma)$ 同时决定 seed field 和 scattering electrons。

但这不等于无法解析处理。正确做法是列出近似层级。

### 11.3 较精确的半解析路线

Rieke & Weekes 1969 和曲钦岳 1978 这类 SSC 处理的共同思想是：用 synchrotron spectrum 近似 seed photon field，再保留 IC kernel 积分，而不是立即退化到 delta approximation。

若观测或模型给出源内 synchrotron luminosity density $L_\epsilon^{\rm syn}$，均匀球源中的 photon density 可估为：

$$
n_{\rm syn}(\epsilon)
\simeq
\frac{L_\epsilon^{\rm syn}}
{4\pi R^2c\,\epsilon}.
$$

保留 Thomson kernel：

$$
\frac{dN_\gamma^{\rm SSC}}{dt\,d\epsilon_s}
=
c\int d\gamma\,n_e(\gamma)
\int d\epsilon\,n_{\rm syn}(\epsilon)
\frac{3\sigma_T}{4\gamma^2\epsilon}
f(q),
$$

其中：

$$
q=\frac{\epsilon_s}{4\gamma^2\epsilon},
\qquad
f(q)=2q\ln q+(1+2q)(1-q).
$$

若需要 KN 修正，把 Thomson kernel 替换成：

$$
\frac{d\sigma_{\rm IC}}{d\epsilon_s}
=
\frac{3\sigma_T}{4\gamma^2\epsilon}
G(q,\Gamma_e).
$$

这就是“精确核 + 近似 seed field”的半解析 SSC，比 delta approximation 更接近完整解。

实用层级：

| 层级 | 做法 | 用途 |
| --- | --- | --- |
| full formal | $n_{\rm syn}$ 由 synchrotron transfer 自洽给出，再与完整 IC/KN kernel 嵌套积分 | 最完整，通常数值求解 |
| semi-analytic kernel | 用观测或 broken-power-law synchrotron spectrum 近似 $n_{\rm syn}$，保留 Thomson 或 KN kernel | 较精确，适合 Rieke-Weekes / 曲钦岳式估算 |
| broken-power-law analytic | 用 synchrotron breaks 和 power-law 段推 SSC breaks、谱段斜率 | 快速解析诊断 |
| delta approximation | $\epsilon_s\simeq(4/3)\gamma^2\epsilon$ | 最快，适合 sanity check |

### 11.4 Broken-Power-Law SSC 解析层

若 synchrotron seed spectrum 可近似为 broken power law：

$$
L_\epsilon^{\rm syn}
\propto
\epsilon^a
$$

在某个能段内，同时 electrons 近似：

$$
N(\gamma)=K\gamma^{-p}.
$$

Thomson delta approximation 给出：

$$
\epsilon_s\simeq \frac{4}{3}\gamma^2\epsilon.
$$

用 delta function 写：

$$
L_{\epsilon_s}^{\rm SSC}
\propto
\int d\gamma\,N(\gamma)
\int d\epsilon\,n_{\rm syn}(\epsilon)
P_{\rm IC}(\gamma)
\delta\left(\epsilon_s-\frac{4}{3}\gamma^2\epsilon\right).
$$

对 \(\epsilon\) 积分时：

$$
\epsilon_\ast=\frac{3\epsilon_s}{4\gamma^2},
\qquad
\left|\frac{d}{d\epsilon}
\left(\epsilon_s-\frac{4}{3}\gamma^2\epsilon\right)\right|
=
\frac{4}{3}\gamma^2.
$$

因此：

$$
L_{\epsilon_s}^{\rm SSC}
\propto
\int d\gamma\,
K\gamma^{-p}
\gamma^2
n_{\rm syn}(\epsilon_\ast)
\frac{1}{\gamma^2}.
$$

若 \(n_{\rm syn}(\epsilon)\propto L_\epsilon^{\rm syn}/\epsilon\propto\epsilon^{a-1}\)，则：

$$
n_{\rm syn}(\epsilon_\ast)
\propto
\epsilon_s^{a-1}\gamma^{-2(a-1)}.
$$

所以在给定积分边界内：

$$
L_{\epsilon_s}^{\rm SSC}
\propto
\epsilon_s^{a-1}
\int d\gamma\,\gamma^{-p-2a+2}.
$$

这说明 SSC 的谱段斜率由 seed photon 斜率、electron slope 和积分上下限共同决定；不能只把 \(\nu_m^{SSC}\) 和 \(\nu_c^{SSC}\) 平移后就声称完整谱已确定。更精确的 broken-power-law analytic method 会逐段处理 \(\epsilon\)、\(\gamma\) 的上下限和 KN cutoff。

### 11.5 SSC 快速解析估计

特征频率：

$$
\nu_m^{\rm SSC}
\sim
\frac{4}{3}\gamma_m^2\nu_m,
\qquad
\nu_c^{\rm SSC}
\sim
\frac{4}{3}\gamma_c^2\nu_c.
$$

若源区 synchrotron luminosity 为 $L_{\rm syn}$：

$$
U_{\rm syn}
\sim
\frac{L_{\rm syn}}{4\pi R^2c}.
$$

磁场能量密度：

$$
U_B=\frac{B^2}{8\pi}.
$$

于是：

$$
Y_{\rm SSC}
\sim
\frac{U_{\rm syn}}{U_B}.
$$

若 $Y$ 已知，同步 cooling break 修正为：

$$
\gamma_{c,\rm IC}
=
\frac{\gamma_{c,\rm syn}}{1+Y},
\qquad
\nu_{c,\rm IC}
=
\frac{\nu_{c,\rm syn}}{(1+Y)^2}.
$$

## 12. 从推导到代码的实现约定

当前本地数值层分成三类，不能混读。允许代码采用成熟的半解析 kernel、数值积分和公开软件 convention；但如果它和课程推导的理想化表达式不逐项相同，必须在课程页说明差异来源。

### 12.1 课程 reference code

第一类是课程 reference code，对应本页的解析近似和完整各向同性数值核：

- Blumenthal-Gould / Klein-Nishina isotropic IC kernel。
- monoenergetic seed photon bath 的完整核积分。
- tabulated seed photon field 的完整核积分，可用于 CMB / blackbody / external photon bath。
- Thomson delta approximation。
- KN kinematic cap。
- KN cross-section ratio。

对应函数包括：

```text
blumenthal_gould_q()
blumenthal_gould_kernel()
inverse_compton_differential_cross_section_cgs()
inverse_compton_monoenergetic_sed_erg_cm2_s()
inverse_compton_tabulated_sed_erg_cm2_s()
blackbody_seed_photon_field()
synchrotron_seed_field_from_luminosity_grid()
ssc_one_zone_tabulated_sed_erg_cm2_s()
inverse_compton_delta_sed_erg_cm2_s()
ic_thomson_cooling_power_erg_s()
klein_nishina_suppression_ratio()
```

这些函数分成两层：`inverse_compton_tabulated_sed_erg_cm2_s()` 和 `inverse_compton_monoenergetic_sed_erg_cm2_s()` 是本页第 6 节的完整各向同性 BG/KN kernel 数值积分；`inverse_compton_delta_sed_erg_cm2_s()` 是第 9 节的快速解析近似，不能拿它直接要求等于任何完整 IC 外部实现。

课程 reference code 的积分结构是：

$$
\epsilon_s^2\frac{dN_\gamma}{dt\,d\epsilon_s}
=
\epsilon_s^2 c
\int dE_e\,N(E_e)
\int d\epsilon\,n_{\rm ph}(\epsilon)
\frac{d\sigma_{\rm IC}}{d\epsilon_s}.
$$

这里的代码约定是：

- \(N(E_e)\) 是总电子谱，单位 particles eV\(^{-1}\)，不是空间数密度。
- \(n_{\rm ph}(\epsilon)\) 是 seed photon number density spectrum，单位 cm\(^{-3}\) erg\(^{-1}\)。
- `blackbody_seed_photon_field()` 先生成 Planck photon number density，再交给 tabulated IC solver。
- 输出 SED：

$$
\epsilon_s F_{\epsilon_s}
=
\frac{\epsilon_s^2}{4\pi d^2}
\frac{dN_\gamma}{dt\,d\epsilon_s}.
$$

### 12.2 成熟数值方法与可替代 kernel

完整 BG/KN kernel 是本地 reference 的主线；但实际高能辐射软件常为了速度采用成熟近似，例如：

- Khangulyan, Aharonian & Kelner 类 blackbody IC semi-analytic approximation。
- log-log quadrature 或 adaptive quadrature。
- tabulated cross-section / kernel interpolation。
- 对 blackbody、greybody 或 broken-power-law seed field 预先做积分近似。
- 在 Thomson 区域切换到解析 power-law 或 delta approximation 做 sanity check。

这些方法可以用于 mature numerical method 层，但必须写清楚：

$$
\text{BG/KN reference integral}
\rightarrow
\text{semi-analytic or tabulated approximation}
$$

替换了哪一步。若曲线和课程 reference 不完全相等，常见原因包括 seed photon convention、积分变量、能量网格、KN 近似、低能 cutoff、单位从 per eV 到 per erg 的转换，以及是否使用黑体解析近似。

当前 SSC 的最小 mature-method 代码入口已经存在，但它不是 full self-consistent SSC solver：

```text
synchrotron_seed_density_from_luminosity_per_erg()
synchrotron_seed_field_from_luminosity_grid()
ssc_one_zone_tabulated_sed_erg_cm2_s()
```

它实现的是：

$$
L_\epsilon^{\rm syn}
\rightarrow
n_{\rm syn}(\epsilon)
\rightarrow
\text{BG/KN IC tabulated solver}.
$$

调用方必须说明 \(L_\epsilon^{\rm syn}\) 来自课程 fixed-pitch-angle reference、角平均成熟方法，还是 package-compatible benchmark 输出。

### 12.3 外部 benchmark compatibility code

第二类是外部 benchmark compatibility code：

```text
inverse_compton_<package>_compatible_sed()
```

这一层可以复刻某个公开软件的 IC kernel、seed photon convention、默认 electron grid 和积分规则。它的目标是 benchmark parity，不是替代本页第 6-9 节的课程推导。

简短地说：

| 层级 | 目标 | 物理/数值核 | 是否要求等于外部软件 |
| --- | --- | --- | --- |
| course/reference | 对应本页推导 | BG/KN full isotropic kernel、Thomson kernel、delta approximation、KN caveat | 不要求 |
| mature numerical method | 更快或更稳定的通用计算 | semi-analytic blackbody IC、tabulated kernel、log-log quadrature | 不要求，但必须解释差异 |
| package-compatible | benchmark parity | 对应软件的 IC kernel / seed convention | 只要求等于对应软件 |

如果课程公式和 benchmark compatibility 代码不同，必须说明差异来自 kernel、seed photon convention、积分网格或单位 convention，而不是把差异写成“模型错了”。benchmark 输出必须把本地课程 reference 和外部软件 compatibility 结果分列。

当前本地 reference layer 已实现：

- 完整 Blumenthal-Gould isotropic IC kernel 积分。
- 单能 seed photon bath 与 tabulated seed photon field。
- blackbody / CMB seed photon number density helper。
- one-zone tabulated SSC seed-field conversion + BG/KN IC solver reuse。

当前本地 reference layer 仍不实现：

- anisotropic seed photon field。
- SSC photon density 的自洽 radiative transfer。
- pair cascade 或多次散射 cascade。

因此本地 IC 曲线可以读作 isotropic single-scattering reference spectrum；SSC 曲线若使用 tabulated seed field，仍只能读作 semi-analytic / teaching-reference 层，而不是完整自洽科学拟合。

## v3 代码实现约定：agnpy-compatible SSC

为了把“课程推导”和“开源库 convention”分开，本轮新增 `agnpy_compat.py::synchrotron_self_compton_sed_agnpy_compatible_erg_cm2_s()`。

它复刻 `agnpy.SynchrotronSelfCompton` 的 one-zone 路线：

1. 先在 agnpy 默认 seed frequency grid 上计算 synchrotron SED；
2. 用球形 blob 近似把观测 SED 转成 comoving synchrotron photon energy density，
   \[
   u'_{\epsilon'} \propto {d_L^2(\nu F_\nu)\over c R_b^2\delta_D^4\epsilon'}
   \]
   并包含 agnpy 的球平均因子；
3. 再放入 isotropic IC kernel 积分
   \[
   \nu F_\nu^{SSC}\propto {\delta_D^4\over 4\pi d_L^2}
   \epsilon_s'^2
   \int d\epsilon'\int d\gamma\,
   {u'_{\epsilon'}\over \epsilon'^2}
   {N_e(\gamma)\over \gamma^2}
   K_{\rm IC}.
   \]

这条路线只用于 package-compatible parity；课程里的 `ssc_one_zone_tabulated_sed_erg_cm2_s()` 仍是更透明的 semi-analytic reference。两者差异主要来自 seed photon density、blob geometry、Doppler convention 和 synchrotron angle average。

## Cooling / Angle-kernel v1 补充

IC 冷却在 Thomson 极限下与同步辐射有平行结构：

$$
P_{\rm IC,T}={4\over 3}\sigma_T c\gamma^2 U_{\rm ph},
\qquad
t_{\rm IC,T}={\gamma m_ec^2\over P_{\rm IC,T}}.
$$

当电子静止系中的入射光子能量接近 \(m_ec^2\) 时，散射截面和能量转移都会被 Klein-Nishina recoil 抑制。代码中的 cooling envelope 使用

$$
x \simeq {4\gamma\epsilon\over m_ec^2},\qquad
P_{\rm IC,KN-env}=P_{\rm IC,T}{\sigma_{\rm KN}(x)\over\sigma_T}.
$$

这不是完整 IC cooling integral；完整计算应当对 seed photon spectrum 和 Blumenthal-Gould kernel 积分。它的作用是给动力学和教学图提供一个不会把高能 IC 无限外推的上界/包络。

对于各向异性入射光，最基本的 head-on / tail-on 差异来自

$$
\epsilon'=\gamma\epsilon(1-\beta\mu),
$$

其中 \(\mu\) 是电子速度与入射光子方向夹角余弦。教学层使用

$$
g_{\rm aniso}=(1-\beta\mu)^2
$$

作为几何增强因子：head-on \(\mu=-1\) 增强，tail-on \(\mu=1\) 抑制。production 层仍使用 isotropic Blumenthal-Gould / package-compatible convention，不声称完成 full anisotropic IC solver。

SSC cooling 本轮只采用 envelope：

$$
P_{\rm SSC}\simeq YP_{\rm syn}.
$$

这里的 \(Y\) 必须来自调用方选定的 one-zone convention、迭代估计或外部模型；本地不在此处解自洽 photon transfer、escape time、SSA feedback 或多次散射。

当前代码约定：

- production：`electron_ic_thomson_cooling_time_s()`、`electron_ic_kn_envelope_cooling_time_s()`、`electron_cooling_gamma_c()`。
- teaching：`teaching_anisotropic_ic_geometry_factor()`、`teaching_ssc_cooling_envelope_power_erg_s()`。
- benchmark：naima/agnpy 当前主要用于 SED parity；cooling API 不作为逐点外部标准。

## 13. 应用例子

IC 和 SSC 常用于 AGN jet、pulsar wind nebula、supernova remnant、GRB afterglow 等高能辐射源。应用页可以引用本页机制链，但必须同时检查 KN suppression、$\gamma\gamma$ opacity、seed photon field 和源区几何，不能把某个高能信号直接写成唯一解释。

## 14. 参考资料

- Blumenthal & Gould 1970, *Bremsstrahlung, Synchrotron Radiation, and Compton Scattering of High-Energy Electrons Traversing Dilute Gases*, Reviews of Modern Physics.
- Rybicki & Lightman, *Radiative Processes in Astrophysics*, Compton scattering chapters.
- Rieger, *High Energy Astrophysics 7: Inverse Compton Radiation*, https://www.mpi-hd.mpg.de/personalhomes/frieger/HEA7.pdf.
- NASA/GSFC lecture notes on inverse Compton scattering, https://asd.gsfc.nasa.gov/Volker.Beckmann/school/download/Longair_Radiation3.pdf.
- Rieke & Weekes 1969, *Production of cosmic gamma rays by Compton scattering in discrete sources*, https://www.osti.gov/biblio/4825709.
- 曲钦岳 1978，《同步加速辐射的自康普顿效应》，《南京大学学报（自然科学版）》1978 年第 3 期，第 25 页。
- Sari & Esin 2001, *On the Synchrotron Self-Compton Emission from Relativistic Shocks and Its Implications for Gamma-Ray Burst Afterglows*.
