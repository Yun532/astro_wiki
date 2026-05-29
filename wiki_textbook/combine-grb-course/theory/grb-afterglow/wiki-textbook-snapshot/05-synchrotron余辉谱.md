# 05 Synchrotron 余辉谱

前两章给出 observer-frame 转换，第三、四章给出 fireball 与 external shock 动力学。本章把 shocked external medium 中的 microphysics 接到 synchrotron radiation，推导 GRB afterglow 标准谱的三个核心量：`ν_m`、`ν_c`、`F_{ν,max}`。Light curve closure relations 放到下一章。

## 1. Shock microphysics 参数化

External shock 中，bulk kinetic energy 转化为 shocked fluid 的 internal energy density `e'`。标准 afterglow 模型不从 first principles 计算 collisionless shock 的电子加速和磁场放大，而用几个 phenomenological parameters：

```tex
\epsilon_e \equiv \frac{\hbox{electron energy density}}{e'},
```

```tex
\epsilon_B \equiv \frac{\hbox{magnetic energy density}}{e'}.
```

因此 comoving magnetic field 满足

```tex
\frac{B'^2}{8\pi} = \epsilon_B e'.
```

利用第四章的 ultra-relativistic shock jump 量级关系

```tex
e' \sim 4\Gamma^2 n_{\rm ext}m_p c^2,
```

得到

```tex
B' \sim \left(32\pi \epsilon_B \Gamma^2 n_{\rm ext}m_p c^2\right)^{1/2}.
```

这说明磁场强度不仅由 `ε_B` 决定，也随 blast wave Lorentz factor 和外部密度演化。

## 2. Electron power-law distribution

标准 forward-shock afterglow 假设一部分 shocked electrons 被加速为 power-law distribution：

```tex
N(\gamma_e)d\gamma_e \propto \gamma_e^{-p}d\gamma_e,
\quad \gamma_e \ge \gamma_m.
```

这里 `γ_e` 是 electron Lorentz factor in comoving frame，`p` 是 electron spectral index。对 `p>2`，电子能量主要集中在低能端，因此最小 Lorentz factor 可由 electron energy fraction 估计：

```tex
\gamma_m \sim \epsilon_e \frac{p-2}{p-1}\frac{m_p}{m_e}\Gamma.
```

若只有 fraction `ξ_e` 的电子被加速，常见变体是

```tex
\gamma_m \sim \frac{\epsilon_e}{\xi_e}\frac{p-2}{p-1}\frac{m_p}{m_e}\Gamma.
```

很多教材或论文默认 `ξ_e=1`。若拟合结果比较 `ε_e`、`E_k` 或 density，必须检查是否采用了这个约定。

## 3. 单个电子的 synchrotron characteristic frequency

在 comoving frame 中，Lorentz factor 为 `γ_e` 的电子的 characteristic synchrotron frequency 量级为

```tex
\nu'_{\rm syn}(\gamma_e) \sim \frac{q_e B'}{2\pi m_e c}\gamma_e^2.
```

更精确的表达常含 `3/4π` 和 pitch-angle 因子。对 on-axis relativistic blast wave，observer-frame frequency 约为

```tex
\nu_{\rm obs} \sim \frac{\Gamma}{1+z}\nu'.
```

因此由 `γ_m` 对应的 injection / characteristic frequency 为

```tex
\nu_m \sim \frac{\Gamma}{1+z}\frac{q_e B'}{2\pi m_e c}\gamma_m^2.
```

由于 `γ_m ∝ Γ`、`B' ∝ Γ n_{\rm ext}^{1/2}`，`ν_m` 对 blast wave deceleration 非常敏感。

## 4. Cooling Lorentz factor 与 cooling frequency

电子会通过 synchrotron radiation 失能。comoving frame 中 synchrotron cooling timescale 量级为

```tex
t'_{\rm cool}(\gamma_e) \sim \frac{6\pi m_e c}{\sigma_T B'^2 \gamma_e}.
```

如果 inverse Compton cooling 也重要，常写成

```tex
t'_{\rm cool}(\gamma_e) \sim \frac{6\pi m_e c}{\sigma_T B'^2 \gamma_e(1+Y)},
```

其中 `Y` 是 Compton parameter。

定义 cooling Lorentz factor `γ_c`：在 dynamical time 内刚好显著冷却的电子 Lorentz factor。取 comoving dynamical time `t' ~ Γ t_obs/(1+z)`，得到

```tex
\gamma_c \sim \frac{6\pi m_e c(1+z)}{\sigma_T B'^2 \Gamma t_{\rm obs}(1+Y)}.
```

对应 cooling frequency：

```tex
\nu_c \sim \frac{\Gamma}{1+z}\frac{q_e B'}{2\pi m_e c}\gamma_c^2.
```

`ν_c` 的位置决定 X-ray / optical 是否处于 cooled spectral segment，是 closure relation 诊断外部介质和 cooling regime 的关键。

## 5. Peak spectral flux

峰值 flux density 可由 emitting electron number、单电子 peak spectral power 和距离估计。swept-up electron number 量级为

```tex
N_e \sim \frac{m_{\rm sw}}{m_p}.
```

comoving frame 单电子 synchrotron peak spectral power 量级为

```tex
P'_{\nu,\max} \sim \frac{m_e c^2 \sigma_T B'}{q_e}.
```

observer-frame peak flux density 量级为

```tex
F_{\nu,\max} \sim \frac{1+z}{4\pi D_L^2}N_e \Gamma P'_{\nu,\max}.
```

因此 `F_{ν,max}` 对 emitting electron number、magnetic field、bulk Lorentz factor 和 luminosity distance 敏感。和 `ν_m`、`ν_c` 不同，`F_{ν,max}` 是谱的归一化入口。

## 6. Slow cooling 与 fast cooling

比较 `γ_m` 和 `γ_c`，或等价地比较 `ν_m` 和 `ν_c`，得到两类 cooling regime：

- **slow cooling**：`γ_m < γ_c`，即 `ν_m < ν_c`；多数电子在 dynamical time 内没有显著冷却。
- **fast cooling**：`γ_c < γ_m`，即 `ν_c < ν_m`；刚被加速的高能电子会快速冷却。

GRB afterglow 早期可能 fast cooling，随后常转入 slow cooling。观测上是否 fast cooling 取决于 `ε_B`、density、time、inverse Compton cooling 和能段。

## 7. Slow-cooling spectrum

忽略 synchrotron self-absorption 且采用 sharp broken-power-law approximation，slow cooling `ν_m < ν_c` 时：

```tex
F_\nu \propto
\begin{cases}
\nu^{1/3}, & \nu < \nu_m, \\
\nu^{-(p-1)/2}, & \nu_m < \nu < \nu_c, \\
\nu^{-p/2}, & \nu > \nu_c.
\end{cases}
```

若考虑低频 self-absorption，还会引入 `ν_a`，在 radio band 尤其重要。`ν_a` 的位置依赖 density、geometry、electron distribution 和 cooling regime，本章只把它作为后续 radio modeling 的接口。

## 8. Fast-cooling spectrum

fast cooling `ν_c < ν_m` 时，忽略 self-absorption 的标准谱为

```tex
F_\nu \propto
\begin{cases}
\nu^{1/3}, & \nu < \nu_c, \\
\nu^{-1/2}, & \nu_c < \nu < \nu_m, \\
\nu^{-p/2}, & \nu > \nu_m.
\end{cases}
```

其中 `ν^{-1/2}` 段来自已经冷却的 electron distribution。实际 prompt-to-afterglow 早期数据常比这个简单图像复杂，因为 reverse shock、energy injection、high-latitude emission、IC cooling 和 dust extinction 都可能影响观测谱。

## 9. ISM 与 wind 中的时间标度

把第四章动力学代入 `B'`、`γ_m`、`γ_c`、`N_e`，可得到标准 adiabatic afterglow 的 characteristic quantity 标度。

对 uniform ISM：

```tex
\nu_m \propto t_{\rm obs}^{-3/2},
```

```tex
\nu_c \propto t_{\rm obs}^{-1/2},
```

```tex
F_{\nu,\max} \propto t_{\rm obs}^{0}.
```

对 wind-like medium：

```tex
\nu_m \propto t_{\rm obs}^{-3/2},
```

```tex
\nu_c \propto t_{\rm obs}^{1/2},
```

```tex
F_{\nu,\max} \propto t_{\rm obs}^{-1/2}.
```

注意 `ν_m` 在 ISM 和 wind 中有相同的 `t^{-3/2}` 标度，但 `ν_c` 和 `F_{ν,max}` 的演化方向不同。这正是 multi-band closure relations 可以诊断 circumburst medium 的原因之一。

## 10. 从 spectrum 到 light curve

固定观测频率 `ν_obs` 时，光变曲线来自三个量共同演化：

```tex
F_\nu(t) = F_{\nu,\max}(t)\,\Phi[\nu/\nu_m(t),\nu/\nu_c(t),\nu/\nu_a(t),p].
```

因此同一个 frequency band 在不同时间可能穿过不同 spectral segment。例如 optical band 可能从 `ν<ν_m` 进入 `ν_m<ν<ν_c`，radio band 常受 `ν_a` 和 scintillation 影响，X-ray band 常位于 `ν>ν_c` 或受到 inverse Compton / central engine contamination。

下一章 closure relations 会把本章谱段斜率和第四章动力学时间标度组合起来，得到 `F_ν ∝ t^{-α}ν^{-β}` 的诊断表。

## 11. 和事件页面的接口

- GRB 221009A：radio-to-GeV afterglow modeling 需要同时检查 synchrotron maximum energy、SSC contribution、EBL absorption 和 jet structure；不能把所有高能 photon 自动归入单一区域 synchrotron。
- GRB 080319B：prompt optical flash 可能包含 reverse shock 或 internal component；forward-shock synchrotron spectrum 适合解释 afterglow 主体，但不应直接替代 prompt optical/gamma mismatch 的讨论。
- GRB 030329：dense radio monitoring 对 `ν_a`、`F_{ν,max}`、late calorimetry 和 component transition 特别重要；radio band 不能只用 optically thin broken power law。

## 11.5 代码接口：从微物理量到可观测谱

为了让复现代码跟随推导，本章采用一组 toy-level 函数接口。它们不是 paper-level normalization，而是把每一步的物理量显式拆开，便于验证和替换。

### 11.5.1 最小电子 Lorentz factor

对 `p>2` 的 power-law electron distribution，常用量级为

```tex
\gamma_m =
\frac{p-2}{p-1}\epsilon_e \frac{m_p}{m_e}\Gamma .
```

如果 `1<p<=2`，低能端对总能量的贡献不再由该简单表达式决定，代码必须拒绝或要求用户给出上下限。

### 11.5.2 Cooling Lorentz factor

采用本章第 4 节的 convention：

```tex
\gamma_c =
\frac{6\pi m_e c(1+z)}
{\sigma_T B'^2 \Gamma t_{\rm obs}(1+Y)} .
```

`Y=0` 时为 pure synchrotron cooling；SSC cooling 会通过 `1+Y` 降低 `γ_c`，从而降低 `ν_c`。

### 11.5.3 Characteristic frequency

给定任意电子 Lorentz factor `γ_e`：

```tex
\nu_{\rm syn,obs} =
\frac{\Gamma}{1+z}
\frac{3 q_e B'}{4\pi m_e c}\gamma_e^2 .
```

因此代码中 `nu_m` 和 `nu_c` 都应调用同一个 `synchrotron_characteristic_frequency`，只替换 `γ_m` / `γ_c`。

### 11.5.4 Peak flux 的 toy normalization

完整 `F_{\nu,max}` 依赖几何、equal-arrival-time surface 和精确谱函数。第一轮采用可验证的 proportional 接口：

```tex
F_{\nu,max} \propto
\frac{N_e \Gamma B'}{D_L^2}.
```

代码函数只返回该 scale，不把它伪装成论文级 flux density。

### 11.5.5 Self-absorption frequency placeholder

SSA 的 `ν_a` 对 radio/mm 很关键，但严格表达式依赖 cooling regime、density profile、geometry 和 electron distribution。第一轮只提供一个参数化接口：

```tex
\nu_a = \nu_{a,0}
\left(\frac{n}{n_0}\right)^{a_n}
\left(\frac{E}{E_0}\right)^{a_E}
\left(\frac{t}{t_0}\right)^{a_t}.
```

这只用于 radio sanity check。GRB 221009A 的 radio turnover 不能自动解释为 SSA，还需要检查 scintillation、calibration caveat 和 extra component。

### 11.5.6 Unified spectrum API

代码层把 forward shock、reverse shock 和 structured jet 的局部 patch 都收敛到同一个谱接口：

```text
SpectralBreaks(nu_a_hz, nu_m_hz, nu_c_hz, fnu_max_mjy, p)
SpectrumOptions(cooling_regime, smoothness, apply_ssa, ssa_slope)
synchrotron_flux_density(nu, breaks, p, options)
```

慢冷 sharp broken power-law 仍以 `SYN-SPEC-SLOW-001` 表示。快冷分段增加 `SYN-SPEC-FAST-001`：

```tex
F_\nu = F_{\nu,\max}
\begin{cases}
(\nu/\nu_c)^{1/3}, & \nu<\nu_c,\\
(\nu/\nu_c)^{-1/2}, & \nu_c<\nu<\nu_m,\\
(\nu_m/\nu_c)^{-1/2}(\nu/\nu_m)^{-p/2}, & \nu>\nu_m .
\end{cases}
```

平滑断点的 toy 接口用 `SYN-SPEC-SMOOTH-001` 标记。当前实现采用两个 asymptotic branch 的 smooth-min 形式：

```tex
F_{\rm smooth}=(F_1^{-s}+F_2^{-s})^{-1/s},
```

其中 `s` 是 `smoothness`。这只用于避免 event sanity 图在 break 附近出现不物理的尖锐折线；paper-level spectrum 仍应回到 Granot & Sari 这类谱形或数值积分。

SSA suppression 的 toy 接口用 `SYN-SSA-SUPPRESS-001` 标记：

```tex
F_{\nu,\rm obs}=F_{\nu,\rm thin}
\left(\frac{\nu}{\nu_a}\right)^{s_a},\qquad \nu<\nu_a .
```

默认 `s_a=2` 只是 monotonic sanity check。它不能被写成“radio turnover 已由 SSA 解释”。

慢冷 SSA 的第一轮解析 regime 用 `SYN-SSA-REGIME-001` 标记：

```text
nu_a < nu_m < nu_c  -> optically thick sanity slope 2
nu_m < nu_a < nu_c  -> optically thick sanity slope 5/2
```

代码只把这两个 ordering 暴露为 sanity interface；其它 ordering 必须显式标为 unsupported，避免把 radio peak 自动解释成 SSA。

## 12. 常见误区

- **把 `p` 和 photon index 混淆**：`p` 是 electron energy distribution index，观测 spectral index `β` 需要通过具体 spectral segment 转换。
- **忘记 cooling regime**：同一个 `p` 在 `ν_m<ν<ν_c` 和 `ν>ν_c` 中给出不同谱斜率。
- **把 `ε_e`、`ε_B` 当作直接可观测量**：它们是模型参数，和 `E_k`、density、geometry、IC cooling 有简并。
- **忽略 self-absorption**：radio band 常受 `ν_a` 影响，不能直接套用 optically thin slope。
- **把 broken power law 当作真实尖锐断点**：真实 spectrum 在 break 附近是平滑过渡，精确拟合需要 smooth broken power-law 或数值 synchrotron spectrum。

## 13. 和后续章节的接口

- Light curve closure relations：把 spectral index `β` 和 temporal index `α` 联系起来。
- Jet break：当 geometry 改变 `F_{ν,max}` 和 arrival-time surface，light curve slope 会 steepen。
- Energy injection：会改变 `E(t)`，从而改变 `ν_m`、`ν_c`、`F_{ν,max}` 的时间标度。
- SSC / high-energy afterglow：inverse Compton cooling 通过 `Y` 改变 `γ_c`，并可贡献 GeV–TeV emission。

## 14. Sari et al. 1998 数量级对照

为了让代码验证有一个清楚的 literature-scale anchor，本章采用 Sari, Piran & Narayan (1998) 的 spherical adiabatic ISM 标准数量级作为第一轮固定点，而不是把它当作 GRB 221009A 的最佳拟合公式。

在常用归一化 `E_52=E_iso/10^52 erg`、`epsilon_e,-1=epsilon_e/0.1`、`epsilon_B,-2=epsilon_B/0.01`、`D_28=D_L/10^28 cm`、`t_d=t_obs/1 d` 下，ISM 慢冷却数量级可写为：

```tex
\nu_m \sim 5.7\times10^{14}
\epsilon_{e,-1}^{2}\epsilon_{B,-2}^{1/2}E_{52}^{1/2}t_d^{-3/2}\ {\rm Hz},
```

```tex
\nu_c \sim 2.7\times10^{12}
\epsilon_{B,-2}^{-3/2}E_{52}^{-1/2}n_0^{-1}t_d^{-1/2}\ {\rm Hz},
```

```tex
F_{\nu,\max}\sim 1.1\times10^5
\epsilon_{B,-2}^{1/2}E_{52}n_0^{1/2}D_{28}^{-2}\ \mu{\rm Jy}.
```

这些表达式只用于验证 `nu_m`、`nu_c`、`Fnu,max` 的数量级和时间依赖。不同论文会因红移因子、`p` 相关的 `gamma_m` 系数、几何、equal-arrival-time surface 和精确谱函数而使用不同归一化；进入事件拟合前必须在 sidecar 或 validation record 中写明 convention。

Wind-like medium 第一轮只采用标度边界：

```tex
\nu_m\propto t^{-3/2},\qquad
\nu_c\propto t^{1/2},\qquad
F_{\nu,\max}\propto t^{-1/2}.
```

因此代码层新增两个层级：`standard_break_time_exponents(medium=...)` 负责 ISM/wind 时间标度；`sari98_ism_reference_scales(...)` 只负责 ISM reference fixed point。Laskar et al. 对 GRB 221009A 采用 low-density wind-like FS，因此 Sari98 ISM fixed point 只能证明公式接口和数量级 convention 没跑偏，不能替代 Laskar 的 wind-model fit。

## 15. 公式 ID 与代码映射

| formula ID | 内容 | Python reference | C++ kernel | 验证 |
| --- | --- | --- | --- | --- |
| `SYN-B-001` | `B'^2/(8π)=epsilon_B e'` | `core/dynamics/blastwave.py::post_shock_magnetic_field` | none | `forward_shock_afterglow_program_check.md` |
| `SYN-GAMMA-M-001` | minimum electron Lorentz factor | `core/radiation/synchrotron.py::minimum_electron_lorentz_factor` | none | `radiation_mechanism_library_check.md` |
| `SYN-GAMMA-C-001` | cooling Lorentz factor | `core/radiation/synchrotron.py::cooling_lorentz_factor` | none | `radiation_mechanism_library_check.md` |
| `SYN-NU-M-001` | injection frequency `nu_m` | `core/radiation/synchrotron.py::injection_frequency_hz` and `models/forward_shock/model.py::break_frequencies` | none | `forward_shock_afterglow_program_check.md` |
| `SYN-NU-C-001` | cooling frequency `nu_c` | `core/radiation/synchrotron.py::cooling_frequency_hz` and `models/forward_shock/model.py::break_frequencies` | none | `forward_shock_afterglow_program_check.md` |
| `SYN-FMAX-001` | `Fnu,max` reference normalization | `core/radiation/synchrotron.py::sari98_ism_reference_scales` and `models/forward_shock/model.py::break_frequencies` | none | `radiation_mechanism_library_check.md` |
| `SYN-GAMMA-FROM-NU-001` | invert characteristic synchrotron frequency to electron Lorentz factor | `core/radiation/synchrotron.py::electron_lorentz_factor_from_synch_frequency` | none | `radiation_mechanism_library_check.md` |
| `SYN-SPEC-SLOW-001` | sharp slow-cooling spectrum | `core/radiation/synchrotron.py::broken_power_law_spectrum` and `synchrotron_flux_density` | future spectral batch kernel | `forward_shock_afterglow_program_check.md`; `radiation_mechanism_library_check.md` |
| `SYN-SPEC-FAST-001` | sharp fast-cooling spectrum | `core/radiation/synchrotron.py::synchrotron_flux_density` | future spectral batch kernel | `radiation_mechanism_library_check.md` |
| `SYN-SPEC-SMOOTH-001` | smooth broken-power-law toy join | `core/radiation/synchrotron.py::synchrotron_flux_density` | future spectral batch kernel | `radiation_mechanism_library_check.md` |
| `SYN-SSA-TOY-001` | parameterized SSA sanity interface | `core/radiation/synchrotron.py::self_absorption_frequency_toy` | none | `radiation_mechanism_library_check.md` |
| `SYN-SSA-REGIME-001` | slow-cooling SSA ordering and optically thick toy slopes | `core/radiation/synchrotron.py::slow_cooling_ssa_regime` and `ssa_suppression_slope_for_regime` | none | `radiation_mechanism_library_check.md` |
| `SYN-SSA-SUPPRESS-001` | low-frequency SSA suppression toy | `core/radiation/synchrotron.py::apply_ssa_suppression` and `synchrotron_flux_density` | none | `radiation_mechanism_library_check.md` |

## 来源

- G. B. Rybicki and A. P. Lightman, “Radiative Processes in Astrophysics,” Wiley (1979)：用于 synchrotron radiation 基础公式。
- R. Sari, T. Piran and R. Narayan, “Spectra and Light Curves of Gamma-Ray Burst Afterglows,” ApJL 497, L17-L20 (1998), arXiv:astro-ph/9712005。
- J. Granot and R. Sari, “The Shape of Spectral Breaks in Gamma-Ray Burst Afterglows,” ApJ 568, 820-829 (2002), arXiv:astro-ph/0108027。
- R. A. Chevalier and Z.-Y. Li, “Wind Interaction Models for Gamma-Ray Burst Afterglows: The Case for Two Types of Progenitors,” ApJ 536, 195-212 (2000), arXiv:astro-ph/9908272。
- Tsvi Piran, “The Physics of Gamma-Ray Bursts,” Reviews of Modern Physics 76, 1143-1210 (2004), arXiv:astro-ph/0405503。
- Bing Zhang, “The Physics of Gamma-Ray Bursts & Relativistic Jets,” arXiv:1410.0679。
