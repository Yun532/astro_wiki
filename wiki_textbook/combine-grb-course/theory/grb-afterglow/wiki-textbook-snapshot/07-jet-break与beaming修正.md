# 07 Jet break 与 beaming 修正

前面章节默认 blast wave 在观测者可见区域内近似 spherical-equivalent：只要 `Γ^{-1}` 小于 jet opening angle，观测者看不到喷流边界，动力学和辐射可先用 spherical BM 标度描述。本章讨论当 relativistic beaming cone 逐渐张开到喷流边界时，light curve 为什么会变陡，以及如何从 jet break 推断 opening angle 和 beaming-corrected energy。

## 1. 从 beaming cone 到 jet edge

Relativistic beaming 使 observer 主要看到 angular size 约为

```tex
\theta_{\rm beam} \sim \Gamma^{-1}
```

的区域。若 jet 是 top-hat jet，half-opening angle 为 `θ_j`，并且 observer 近似 on-axis，则早期满足

```tex
\Gamma^{-1} \ll \theta_j.
```

此时 observer 看不到 jet edge，light curve 近似 spherical-equivalent。随着 external shock deceleration，`Γ` 下降，beaming cone 变宽。当

```tex
\Gamma(t_j) \sim \theta_j^{-1}
```

时，jet edge 开始进入可见区域，观测到 achromatic steepening 的可能性增加。这个时间称为 jet-break time `t_j`。

## 2. Jet break 的两个物理效应

简单 top-hat jet 图像中，jet break 主要包含两个效应：

1. **edge effect**：可见区域不再随 `Γ^{-1}` 扩展成完整圆面，因为 jet 外没有同等能量的 emitting material；
2. **lateral expansion / hydrodynamic effect**：jet 可能发生 sideways expansion，使 energy per solid angle 下降更快。

早期解析模型常强调 lateral expansion，并给出 post-break decay 约 `α≈p` 的结果。但后续数值模拟和 structured-jet 研究显示，实际 break shape 可更平滑，sideways expansion 不一定极端快速，viewing angle 和 angular energy profile 也会强烈影响 light curve。

因此本章把 `Γ(t_j)≈θ_j^{-1}` 作为稳健的几何入口，把具体 post-break slope 作为模型依赖量。

## 3. ISM 中的 opening-angle scaling

第四章给出 adiabatic uniform ISM 中

```tex
\Gamma(t) \propto \left(\frac{E_{\rm iso}}{n}\right)^{1/8}
\left(\frac{t}{1+z}\right)^{-3/8}.
```

令 `Γ(t_j)=θ_j^{-1}`，得到

```tex
\theta_j \propto
\left(\frac{t_j}{1+z}\right)^{3/8}
\left(\frac{n}{E_{\rm iso}}\right)^{1/8}.
```

常见归一化形式可写成量级关系

```tex
\theta_j \sim 0.1
\left(\frac{t_j}{1\ {\rm day}}\right)^{3/8}
\left(\frac{1+z}{2}\right)^{-3/8}
\left(\frac{E_{\rm iso,53}}{n_0}\right)^{-1/8}.
```

不同文献的数值系数取决于 radiative efficiency、`E_iso` 是 gamma-ray energy 还是 kinetic energy、BM 系数、density normalization 和 `Γ` 定义。使用事件论文中的公式时，应保留作者的参数约定。

## 4. Wind medium 中的 opening-angle scaling

对 wind-like medium，第四章给出

```tex
\Gamma(t) \propto \left(\frac{E_{\rm iso}}{A}\right)^{1/4}
\left(\frac{t}{1+z}\right)^{-1/4}.
```

令 `Γ(t_j)=θ_j^{-1}`，得到

```tex
\theta_j \propto
\left(\frac{t_j}{1+z}\right)^{1/4}
\left(\frac{A}{E_{\rm iso}}\right)^{1/4}.
```

ISM 与 wind 的 exponent 不同，因此若介质类型判断错误，opening angle 和 beaming-corrected energy 都会系统偏移。GRB 080319B 使用 wind-like environment 的解释时，不能直接套用 ISM jet-opening formula。

## 5. Beaming fraction

若 top-hat jet 的 half-opening angle 为 `θ_j`，单侧 jet 覆盖的 solid angle 为

```tex
\Omega_j = 2\pi(1-\cos\theta_j).
```

相对于 isotropic sphere 的 beaming fraction 为

```tex
f_b = \frac{\Omega_j}{4\pi} = \frac{1-\cos\theta_j}{2}.
```

但 GRB 文献中常把 two-sided jet 的总能量和 single-sided isotropic-equivalent energy 配合使用，常用近似写作

```tex
f_b \simeq 1-\cos\theta_j \simeq \frac{\theta_j^2}{2},
\quad \theta_j \ll 1.
```

因此看到 `f_b` 时必须检查作者定义：是 one-sided solid-angle fraction，还是用于把 observed `E_iso` 转成 two-sided true energy 的 convention。

## 6. True energy correction

观测得到的 prompt gamma-ray isotropic-equivalent energy 是

```tex
E_{\gamma,{\rm iso}}.
```

若 top-hat jet on-axis 且采用常见 beaming correction，则 beaming-corrected gamma-ray energy 为

```tex
E_\gamma \simeq f_b E_{\gamma,{\rm iso}}
\simeq \frac{\theta_j^2}{2}E_{\gamma,{\rm iso}}.
```

类似地，afterglow kinetic energy 可写作

```tex
E_k \simeq f_b E_{k,{\rm iso}}.
```

Prompt radiative efficiency 可定义为

```tex
\eta_\gamma = \frac{E_\gamma}{E_\gamma + E_k}.
```

但事件论文中 `E_k`、`E_iso`、`E_true` 的定义经常不同：有的使用 isotropic-equivalent kinetic energy，有的已经做了 beaming correction；有的把 efficiency 放进 opening-angle formula，有的没有。不能只看符号，必须读变量定义。

## 7. Achromatic break 判据

标准 jet break 预期是几何效应，因此应当近似 achromatic：同一时间附近 optical、X-ray、radio 等多个能段都出现 light curve steepening，且 spectral index 不发生对应的剧烈变化。

若只在单一能段看到 break，可能原因包括：

- cooling break `ν_c` 穿过观测能段；
- density jump 或 density profile transition；
- reverse shock 或 central-engine component 消失；
- dust extinction / host absorption 修正问题；
- energy injection 结束；
- structured jet 或 off-axis geometry 造成 chromatic-looking transition。

因此 jet break 识别应结合 multi-band light curve、SED evolution 和模型拟合，而不是只用单段光变的 steepening。

## 8. Post-break decay slope

在简单 sideways-expanding top-hat jet 模型中，`ν>ν_m` 的 post-break decay 常近似为

```tex
F_\nu \propto t^{-p},
```

即

```tex
\alpha_{\rm post} \sim p.
```

若无显著 sideways expansion，仅 edge effect 也会使 light curve 变陡，但 steepening 更温和。实际观测中的 jet break 往往是平滑过渡，break time 和 break sharpness 与 fitting function 有关。

因此 `α_post≈p` 是一个有用的 textbook limit，不是所有 GRB afterglow 的硬性判据。

## 9. Structured jet 和 two-component jet 的 caveat

Top-hat jet 是最简单图像；structured jet 中 energy per solid angle 和 Lorentz factor 随角度变化：

```tex
E = E(\theta),\quad \Gamma_0 = \Gamma_0(\theta).
```

这时 light curve break 可能来自：

- bright core 进入视线；
- wing emission 衰减；
- observer viewing angle 与 core angle 的几何关系；
- 不同 angular component 的 deceleration time 差异。

Two-component jet 中，narrow component 的 jet break 还可能被 wide component 的 afterglow rise 或 plateau 掩盖。Peng, Königl & Granot 讨论的 `t_{dec,w}` 与 `t_{jet,n}` 相对时序正是这种情况的关键。

因此在 GRB 030329、GRB 080319B 和 GRB 221009A 这类结构化或多成分解释中，单一 top-hat `θ_j` 只应作为 effective parameter，而不是唯一真实几何。

## 10. 和事件页面的接口

- GRB 030329：early optical/X-ray break 和 late radio behavior 被 two-component interpretation 连接到 narrow / wide components；radio calorimetry 给出 late kinetic energy 约束，不能简单把单一 `t_j` 解释为唯一 opening angle。
- GRB 080319B：Racusin et al. 讨论 narrow core 与 wider component，并采用 wind-like environment；opening-angle scaling 需使用相应介质假设。
- GRB 221009A：极高 `E_iso`、structured jet 和 viewing-angle / angular-profile 模型使 beaming correction 高度模型依赖；true energy 不能只用一个 top-hat `θ_j` 粗略决定。

## 11. 常见误区

- **把任何光变变陡都叫 jet break**：cooling break、energy injection end、density change 或 component transition 都可能造成 break。
- **忽略 achromatic 要求**：标准几何 jet break 应尽量多波段同时出现。
- **把 `E_iso` 直接当 true energy**：需要 beaming correction，但 correction 本身依赖 `θ_j` 和 jet model。
- **混用 ISM 与 wind opening-angle formula**：两者 exponent 不同。
- **把 top-hat `θ_j` 用到 structured jet 而不说明 effective meaning**：structured jet 中不存在唯一 sharp edge。

## 12. 和后续章节的接口

- Energy injection and refreshed shock：plateau 结束可能被误认为 jet break，需要区分。
- Structured jet：把 top-hat edge 推广为 angular energy profile 和 viewing-angle effect。
- Two-component jet：解释 narrow / wide component 的 break masking 和 component transition。
- Event applications：对 GRB 030329、GRB 080319B、GRB 221009A 分别记录 jet-break interpretation 的模型依赖。

## 来源

- J. E. Rhoads, “The Dynamics and Light Curves of Beamed Gamma-Ray Burst Afterglows,” ApJ 525, 737-749 (1999), arXiv:astro-ph/9903399。
- R. Sari, T. Piran and J. P. Halpern, “Jets in Gamma-Ray Bursts,” ApJL 519, L17-L20 (1999), arXiv:astro-ph/9903339。
- D. A. Frail et al., “Beaming in Gamma-Ray Bursts: Evidence for a Standard Energy Reservoir,” ApJL 562, L55-L58 (2001), arXiv:astro-ph/0102282。
- Tsvi Piran, “The Physics of Gamma-Ray Bursts,” Reviews of Modern Physics 76, 1143-1210 (2004), arXiv:astro-ph/0405503。
- Bing Zhang, “The Physics of Gamma-Ray Bursts & Relativistic Jets,” arXiv:1410.0679。
- F. Peng, A. Königl and J. Granot, “Two-Component Jet Models of Gamma-Ray Burst Sources,” ApJ 626, 966-977 (2005), arXiv:astro-ph/0410384。
- O. S. Salafia and G. Ghirlanda, “The Structure of Gamma Ray Burst Jets,” arXiv:2206.11088。
