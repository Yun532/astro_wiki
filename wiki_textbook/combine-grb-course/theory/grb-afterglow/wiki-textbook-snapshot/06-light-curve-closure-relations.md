# 06 Light curve closure relations

Closure relations 把 afterglow spectrum 的 spectral index 和 light curve 的 temporal index 联系起来，是 GRB afterglow 模型诊断中最常用的工具之一。第五章给出 synchrotron broken-power-law spectrum，第四章给出 ISM / wind 中的动力学时间标度。本章把二者组合，得到 `α`、`β`、`p` 之间的关系，并说明这些关系的适用边界。

## 1. 记号约定

本章采用常见 afterglow 约定：

```tex
F_\nu(t) \propto t^{-\alpha}\nu^{-\beta_{\rm spec}}.
```

这里：

- `α` 是 temporal decay index；
- `β_spec` 是 spectral index；
- `p` 是 electron power-law index；
- 为避免和速度 `β=v/c` 混淆，本章把谱指数写成 `β_spec`。

如果某篇论文使用 `F_ν ∝ t^α ν^β`，则符号会整体差一个负号。比较 closure relation 前必须先检查作者的 convention。

## 2. Closure relation 的推导逻辑

对固定观测频率 `ν_obs`，第五章给出的 spectrum 可写成

```tex
F_\nu(t) = F_{\nu,\max}(t)\,\Phi[\nu/\nu_m(t),\nu/\nu_c(t),p].
```

因此每个 spectral segment 的 light curve slope 来自三部分：

1. `F_{ν,max}(t)` 的时间演化；
2. `ν_m(t)` 的时间演化；
3. `ν_c(t)` 的时间演化。

例如 slow cooling 且 `ν_m < ν < ν_c` 时：

```tex
F_\nu = F_{\nu,\max}\left(\frac{\nu}{\nu_m}\right)^{-(p-1)/2}.
```

固定 `ν` 后，

```tex
F_\nu \propto F_{\nu,\max}\nu_m^{(p-1)/2}.
```

在 ISM 中 `F_{ν,max}∝t^0`、`ν_m∝t^{-3/2}`，所以

```tex
F_\nu \propto t^{-3(p-1)/4},
```

即

```tex
\alpha = \frac{3(p-1)}{4}.
```

同一谱段的 spectral index 是

```tex
\beta_{\rm spec}=\frac{p-1}{2},
```

因此得到 closure relation：

```tex
\alpha = \frac{3}{2}\beta_{\rm spec}.
```

其他 closure relations 都按同样步骤得到。

## 3. Slow cooling：`ν_m < ν_c`

Slow cooling 是 afterglow 中最常见的工作区间。忽略 self-absorption 时，两个最常用的 optically thin spectral segments 是 `ν_m<ν<ν_c` 和 `ν>ν_c`。

### 3.1 Uniform ISM

对 adiabatic ISM：

```tex
\nu_m \propto t^{-3/2},\quad \nu_c \propto t^{-1/2},\quad F_{\nu,\max}\propto t^0.
```

| Spectral segment | `β_spec` | `α` | Closure relation |
| --- | --- | --- | --- |
| `ν_m < ν < ν_c` | `(p-1)/2` | `3(p-1)/4` | `α = 3β_spec/2` |
| `ν > ν_c` | `p/2` | `(3p-2)/4` | `α = (3β_spec-1)/2` |

因此若 optical 和 X-ray 分别位于 `ν_m<ν<ν_c` 与 `ν>ν_c`，它们的 spectral index 相差约 `1/2`，temporal index 相差约 `1/4`。

### 3.2 Wind-like medium

对 adiabatic wind：

```tex
\nu_m \propto t^{-3/2},\quad \nu_c \propto t^{1/2},\quad F_{\nu,\max}\propto t^{-1/2}.
```

| Spectral segment | `β_spec` | `α` | Closure relation |
| --- | --- | --- | --- |
| `ν_m < ν < ν_c` | `(p-1)/2` | `(3p-1)/4` | `α = (3β_spec+1)/2` |
| `ν > ν_c` | `p/2` | `(3p-2)/4` | `α = (3β_spec-1)/2` |

注意 high-frequency segment `ν>ν_c` 在 ISM 和 wind 中给出相同的 `α(p)` 标度；因此仅用 X-ray 单波段 decay slope 往往不能唯一判断介质类型。

## 4. Fast cooling：`ν_c < ν_m`

Fast cooling 常用于非常早期 afterglow 或高密度 / 高 `ε_B` 情形。忽略 self-absorption 时，常用 optically thin segments 为 `ν_c<ν<ν_m` 和 `ν>ν_m`。

| Medium | Spectral segment | `β_spec` | `α` | Closure relation |
| --- | --- | --- | --- | --- |
| ISM | `ν_c < ν < ν_m` | `1/2` | `1/4` | `α = 1/4` |
| ISM | `ν > ν_m` | `p/2` | `(3p-2)/4` | `α = (3β_spec-1)/2` |
| Wind | `ν_c < ν < ν_m` | `1/2` | `1/4` | `α = 1/4` |
| Wind | `ν > ν_m` | `p/2` | `(3p-2)/4` | `α = (3β_spec-1)/2` |

Fast-cooling closure relations 的实际诊断力通常低于 slow cooling，因为早期数据更容易受到 prompt tail、reverse shock、energy injection 或 detector coverage 的影响。

## 5. Low-frequency segment 与 self-absorption

在 `ν < ν_m` 或 `ν < ν_c` 的 low-frequency synchrotron segment，未吸收谱常有

```tex
F_\nu \propto \nu^{1/3}.
```

但 radio band 常受到 synchrotron self-absorption，需引入 `ν_a`。`ν_a` 的时间演化依赖 cooling regime、medium、electron distribution 和 geometry，因此 radio closure relation 不应简单用 optically thin table 外推。

对 GRB 030329 这类 radio coverage 很好的事件，radio data 的价值恰恰在于约束 `ν_a`、source size、late kinetic energy 和 possible component transition，而不只是给一个 `α`。

## 6. 用 closure relation 诊断介质

实际使用时，常按以下流程：

1. 从同一时间段的 SED 得到 spectral index `β_spec`；
2. 从同一时间段的 light curve 得到 temporal index `α`；
3. 判断观测频率相对 `ν_m`、`ν_c`、`ν_a` 的位置；
4. 在 ISM / wind、slow / fast cooling、pre-jet-break / post-jet-break 中选择对应 closure relation；
5. 检查推出的 `p` 是否在合理范围，且不同能段是否一致。

若 optical 和 X-ray 的 `β_spec`、`α` 无法由同一个 `p` 解释，可能说明：

- `ν_c` 位于 optical 与 X-ray 之间；
- extinction 或 absorption 修正不充分；
- X-ray 含 central-engine component；
- optical 含 reverse shock 或 supernova / kilonova component；
- energy injection、density jump、jet structure 或 evolving microphysics 破坏了标准 closure。

## 7. Jet break 后的 closure 改变

本章表格默认 spherical-equivalent, pre-jet-break BM evolution。当

```tex
\Gamma(t_j)\theta_j \sim 1
```

后，observer 看到 jet edge，light curve 通常 steepen。简单 sideways-expansion top-hat jet 模型中，常见近似为

```tex
\alpha \sim p
```

适用于 `ν>ν_m` 的 optically thin segments。但真实 jet break 的 steepening 取决于 lateral expansion、angular structure、viewing angle 和 equal-arrival-time surface，不应把 `α=p` 当作普适定律。

后续 jet-break 章节会把这一点展开。

## 8. Energy injection 与 plateau

若 blast wave energy 随时间增加，

```tex
E = E(t),
```

则第四章使用的 adiabatic constant-energy BM 标度被改变，closure relation 也会变平。X-ray plateau、optical rebrightening、shallow decay 等现象常可用 energy injection 或 refreshed shock 解释，但也可能来自 jet structure、density variation 或 viewing-angle effect。

因此当观测到 `α` 比标准 closure relation 更小，不应直接判定模型失败；应先检查是否存在 sustained central-engine activity 或 slower ejecta catching up。

## 9. 和事件页面的接口

- GRB 221009A：TeV / GeV / X-ray / optical / radio 多波段 closure 需要同时考虑 synchrotron、SSC、EBL absorption、jet structure 和仪器能段；单一 `α–β` 关系不足以完成模型判别。
- GRB 080319B：prompt optical 与 gamma-ray mismatch 不应只用 forward-shock closure relation 解释；afterglow 阶段还需考虑 wind-like environment 与 narrow/wide component。
- GRB 030329：early optical break、late radio bump 和 supernova contamination 会破坏单一 power-law closure；two-component jet 和 radio calorimetry 是更合适的解释框架。

## 10. 常见误区

- **只用一个 band 判定介质类型**：ISM 与 wind 在某些 spectral segment 给出相同或非常接近的 closure relation。
- **忽略谱段位置**：不知道 `ν_obs` 在 `ν_m`、`ν_c`、`ν_a` 哪一侧时，`α–β` 关系没有唯一解释。
- **把 photon index 直接当作 `β_spec`**：X-ray photon index `Γ_ph` 与 spectral index 常有 `β_spec = Γ_ph - 1` 的关系，需检查定义。
- **忘记 extinction / absorption**：optical extinction 和 X-ray absorption 会改变观测 spectral index。
- **把 closure relation 当作拟合模型本身**：closure relation 是诊断表，不替代 broadband forward modeling。

## 11. 和后续章节的接口

- Jet break and beaming correction：closure relation 失效或 steepening 是识别 jet break 的入口之一。
- Energy injection and refreshed shock：解释 shallow decay / plateau / bumps。
- Structured / two-component jet：angular structure 会让不同时间段由不同 emitting region 主导，改变 apparent `α`。
- Event applications：对 GRB 030329、GRB 080319B、GRB 221009A 分别检查哪些时间段适合使用标准 closure。

## 12. 事件级代码映射

GRB 221009A 的第一版 closure 代码不做拟合，只把数据入口、break evolution 和 closure caveat 放进同一张诊断表：

| formula / diagnostic | Python reference | 事件输出 | 验证等级 |
| --- | --- | --- | --- |
| spectral segment classification relative to `ν_a,ν_m,ν_c` | `events/grb_221009a/scripts/08_multiband_closure_diagnosis.py` | `outputs/multiband_closure_diagnosis.csv` | `event-trend` |
| wind slow-cooling closure `α(p),β(p)` | `models/forward_shock/analytic_scalings.py` | `outputs/multiband_closure_diagnosis.csv` | `literature-scale candidate` |
| model-chain comparison and forbidden claims | `events/grb_221009a/scripts/09_model_chain_summary.py` | `outputs/model_chain_summary.csv` | `event-trend` |

这些输出依赖 Laskar forward-shock model-inferred breaks，因此只能用来检查一致性和缺口，不能替代 extinction-corrected SED 或 broadband fit。

## 来源

- R. Sari, T. Piran and R. Narayan, “Spectra and Light Curves of Gamma-Ray Burst Afterglows,” ApJL 497, L17-L20 (1998), arXiv:astro-ph/9712005。
- R. A. Chevalier and Z.-Y. Li, “Wind Interaction Models for Gamma-Ray Burst Afterglows: The Case for Two Types of Progenitors,” ApJ 536, 195-212 (2000), arXiv:astro-ph/9908272。
- Tsvi Piran, “The Physics of Gamma-Ray Bursts,” Reviews of Modern Physics 76, 1143-1210 (2004), arXiv:astro-ph/0405503。
- Bing Zhang, “The Physics of Gamma-Ray Bursts & Relativistic Jets,” arXiv:1410.0679。
- J. Granot and R. Sari, “The Shape of Spectral Breaks in Gamma-Ray Burst Afterglows,” ApJ 568, 820-829 (2002), arXiv:astro-ph/0108027。
