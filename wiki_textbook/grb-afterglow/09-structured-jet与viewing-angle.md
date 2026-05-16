# 09 Structured jet 与 viewing angle

前面 jet-break 章节把喷流近似成 top-hat：喷流内部能量和 Lorentz factor 近似均匀，边界在 `θ_j` 处突然截断。这个模型足够解释许多 textbook-level beaming correction，但真实 GRB jet 很可能具有 angular structure：靠近轴线的 core 更快、更高能，远离轴线的 wing / cocoon material 更慢、更低能。本章把 top-hat jet 推广到 structured jet，并说明 viewing angle 如何改变 prompt `E_iso`、afterglow light curve、jet-break 形态和事件解释。

## 1. 从 top-hat 到 angular structure

Top-hat jet 的理想化写法是

```tex
\frac{dE}{d\Omega}(\theta)=
\begin{cases}
\mathcal{E}_0, & \theta<\theta_j,\\
0, & \theta>\theta_j,
\end{cases}
```

```tex
\Gamma_0(\theta)=
\begin{cases}
\Gamma_{\rm core}, & \theta<\theta_j,\\
1, & \theta>\theta_j.
\end{cases}
```

Structured jet 则把 sharp edge 改成连续或多段 profile：

```tex
\mathcal{E}(\theta) \equiv \frac{dE}{d\Omega}(\theta),
```

```tex
\Gamma_0 = \Gamma_0(\theta).
```

这里 `θ` 是相对于 jet axis 的 polar angle，不是 emitting element 与 observer line of sight 的夹角。观测者位置由 viewing angle `θ_v` 或 `θ_obs` 描述。后续所有 projection 都要同时区分：

- `θ`：喷流内部的角坐标；
- `θ_v`：观测者视线与 jet axis 的夹角；
- `ψ`：某个 emitting element 与观测者视线之间的夹角。

在轴对称 jet 中，若 emitting element 位于 `(θ, φ)`，则

```tex
\cos\psi = \cos\theta\cos\theta_v + \sin\theta\sin\theta_v\cos\phi.
```

Doppler factor 仍由第一章给出：

```tex
\delta(\theta,\phi,\theta_v)=
\frac{1}{\Gamma(\theta)\left[1-\beta(\theta)\cos\psi\right]}.
```

这就是 viewing-angle effect 的核心：同一个 angular profile 在不同 `θ_v` 下会被不同 Doppler weight 投影成不同 prompt brightness、afterglow peak time 和 apparent jet break。

## 2. 结构化喷流的物理来源

Salafia & Ghirlanda review 强调，GRB jet structure 不是单一阶段决定的，而是多个过程共同塑造：

- central engine launch：决定初始能量、磁化和 baryon loading；
- progenitor / envelope interaction：long GRB jet 穿出恒星时产生 cocoon 和 mixing；
- breakout：core 与 cocoon / wing 的角向分离变得明显；
- free expansion：prompt-emitting outflow 的 angular profile 可继续演化；
- external shock：afterglow 阶段不同角区按各自能量、Lorentz factor 和 external medium decelerate；
- lateral spreading / non-relativistic transition：late-time profile 可能被动力学重新塑形。

因此 `dE/dΩ(θ,t)` 和 `Γ(θ,t)` 有时需要显式写出时间依赖。课程层常先忽略径向结构，使用 coasting 或 deceleration 初期的 angular profile 作为参数化入口。

## 3. 常用 angular profile

### 3.1 Top-hat profile

Top-hat 是 structured jet 的极限情形：core 内均匀，edge 外无 relativistic ejecta。它的优点是解析简单；缺点是边界不自然，且无法描述 off-axis GRB、smooth jet break 或 cocoon-dominated wing。

### 3.2 Gaussian structured jet

Gaussian profile 常写成

```tex
\mathcal{E}(\theta)=\mathcal{E}_c
\exp\left(-\frac{\theta^2}{2\theta_c^2}\right),
```

```tex
\Gamma_0(\theta)-1 = [\Gamma_c-1]
\exp\left(-\frac{\theta^2}{2\theta_c^2}\right).
```

其中 `θ_c` 是 core angle。`θ\lesssim θ_c` 的区域近似是 bright core，`θ>θ_c` 是 wing。实际文献中也常让 `\mathcal{E}` 和 `Γ_0` 使用不同宽度或不同截断方式，所以引用 Gaussian profile 时必须说明具体参数化。

### 3.3 Power-law structured jet

Power-law profile 用 core + wing 的形式描述：

```tex
\mathcal{E}(\theta)=\mathcal{E}_c
\left[1+\left(\frac{\theta}{\theta_c}\right)^a\right]^{-1},
```

```tex
\Gamma_0(\theta)-1 = [\Gamma_c-1]
\left[1+\left(\frac{\theta}{\theta_c}\right)^b\right]^{-1}.
```

`a` 和 `b` 控制 wing 中能量和 Lorentz factor 下降的陡峭程度。较小的 `a` 表示 shallow energy profile，会让 off-core observer 仍能看到较亮的 emission；较大的 `a` 更接近 top-hat edge。

### 3.4 Two-component jet

Two-component jet 可视为 structured jet 的离散化：

```tex
\mathcal{E}(\theta)=
\begin{cases}
\mathcal{E}_n, & \theta<\theta_n,\\
\mathcal{E}_w, & \theta_n<\theta<\theta_w,\\
0, & \theta>\theta_w,
\end{cases}
```

并有对应的 `Γ_n`、`Γ_w`。它保留了 angular structure 的核心思想，但更强调 narrow / wide components 的 deceleration time、jet-break time 和 light-curve component transition。

### 3.5 Quasi-universal structured jet

Quasi-universal structured jet 是 population-level 假设：不同 GRB 的 intrinsic angular profile 近似相似，观测到的 `E_iso`、`E_peak`、duration 或 afterglow behavior 的差异很大程度来自 `θ_v`。这不是单个事件的必然结论，而是连接 luminosity function、rate 和 viewing-angle distribution 的统计模型。

## 4. 从三维流体到 angular energy profile

若保留径向结构，一个轴对称 relativistic outflow 的 kinetic energy per solid angle 可写成

```tex
\frac{\mathrm{d}E}{\mathrm{d}\Omega}(\theta,t)=
\int_0^\infty
[\Gamma(r,\theta,t)-1]\Gamma(r,\theta,t)\rho'(r,\theta,t)c^2 r^2\mathrm{d}r.
```

这里 `ρ'` 是 comoving mass density。对应的 energy-weighted average Lorentz factor 可写成

```tex
\Gamma(\theta,t)=
\left(\frac{\mathrm{d}E}{\mathrm{d}\Omega}\right)^{-1}
\int_0^\infty
[\Gamma(r,\theta,t)-1]\Gamma^2(r,\theta,t)\rho'(r,\theta,t)c^2 r^2\mathrm{d}r.
```

这个定义说明：`Γ(θ,t)` 不是某个任意 shell 的 Lorentz factor，而是按 kinetic energy 加权后的角向平均量。若 source 只给出 phenomenological `Γ(θ)`，需要检查它是否等价于这种 energy-weighted definition。

## 5. Viewing angle 对 prompt `E_iso` 的影响

Prompt emission 的 observed isotropic-equivalent energy 不是简单读取 `\mathcal{E}(θ_v)`。由于 relativistic beaming，观测者接收到的是整个可见 angular surface 的 Doppler-weighted 积分。

若 prompt radiative efficiency 写作 `η_γ(θ)`，常用形式可写成

```tex
E_{\rm iso}(\theta_v)=
\int_0^{2\pi}d\phi
\int_0^{\pi/2}\sin\theta\,d\theta\,
\frac{\delta^3(\theta,\phi,\theta_v)}{\Gamma(\theta)}
\eta_\gamma(\theta)\frac{dE}{d\Omega}(\theta).
```

这个式子的物理含义是：

- `dE/dΩ(θ)` 给出 intrinsic angular energy reservoir；
- `η_γ(θ)` 把 kinetic / total energy 转成 prompt gamma-ray energy；
- `δ^3/Γ` 表示 relativistic beaming 和 frame transformation 的权重；
- `θ_v` 通过 `ψ(θ,φ,θ_v)` 进入 `δ`。

当 `θ_v≈0` 时，bright core 被强烈 Doppler boosted，观测到的 `E_iso` 可远高于 true energy。若 `θ_v>θ_c`，prompt emission 可能显著变暗、变软或表现为 low-luminosity GRB / X-ray flash-like event，具体结果依赖 wing 的 `Γ(θ)` 和 `\mathcal{E}(θ)`。

## 6. True energy 与 beaming correction

Structured jet 中没有唯一 sharp opening angle，因此第七章的

```tex
E_{\rm true}\simeq f_b E_{\rm iso}
```

不能直接用一个 `θ_j` 套用。更自然的 total energy 是 angular integral：

```tex
E_{\rm tot}=\int \frac{dE}{d\Omega}(\theta)d\Omega
=2\pi\int_0^{\theta_{\rm max}}
\mathcal{E}(\theta)\sin\theta\,d\theta.
```

若 `\mathcal{E}(θ)` 有长 power-law wing，`E_tot` 对 outer cutoff `θ_max` 可能敏感。因此 structured-jet 论文给出的 true energy 通常依赖 profile form、outer truncation、radiative efficiency 和 viewing angle prior。

## 7. Afterglow 的角向拼接图像

External shock 阶段，每个 angular zone 近似有自己的 initial Lorentz factor、energy per solid angle 和 deceleration time。对一个角区，可用第三、四章的 deceleration scaling 粗略估计：

```tex
t_{\rm dec}(\theta)\propto
\left[\frac{\mathcal{E}(\theta)}{n\Gamma_0(\theta)^8}\right]^{1/3}
```

这是 uniform ISM、on-axis patch 的量级形式；wind medium 或 off-axis geometry 会改变指数和 normalization。它的用途不是直接拟合，而是提醒：wing 若 `Γ_0` 较低，即使能量不小，也会在较晚 observer time 才显著贡献。

对 off-core observer，afterglow 常可分成三个阶段理解：

1. **early line-of-sight dominated phase**：最早可见 emission 来自靠近视线的 material，即 `θ≈θ_v` 附近；若该处能量低或 Lorentz factor 小，early afterglow 可较暗。
2. **core entering the beaming cone**：随着 core decelerates，`1/Γ` 增大，bright core 的 beaming cone 逐渐覆盖 observer，light curve 可 rise、flatten 或形成 broad peak。
3. **post-peak / post-break decline**：当 core emission 已充分可见并继续减速，light curve 进入 decay；decay slope 取决于 angular profile、medium、spectral regime 和 lateral dynamics。

这解释了为什么 structured jet 可以产生 shallow rise、smooth peak、delayed brightening 或 apparently missing sharp jet break。

## 8. Peak time 的量级判断

对 off-axis top-hat 或 bright-core structured jet，afterglow peak 大致发生在 core Lorentz factor 下降到

```tex
\Gamma(t_{\rm pk}) \sim (\theta_v-\theta_c)^{-1},
```

其中 `θ_v>θ_c`。这个 relation 是几何量级判断：当 relativistic beaming cone 宽到能覆盖 observer 时，core contribution 变得显著。

若使用 ISM BM scaling `Γ∝t^{-3/8}`，则

```tex
t_{\rm pk}\propto (\theta_v-\theta_c)^{8/3}
```

在固定 energy 和 density 的近似下成立。真实 structured jet 中，line-of-sight material、wing emission、lateral spreading 和 profile slope 都会改变 peak shape，所以这个式子只应用作 intuition。

## 9. Light-curve diagnosis

Structured jet 的观测印记包括：

- prompt `E_iso` 和 `E_peak` 随 viewing angle 变化；
- afterglow early rise 或 shallow decay；
- smooth rather than sharp jet break；
- radio / optical / X-ray peak time 可能不同，但 SED 应保持 forward-shock consistency；
- polarization angle 或 polarization degree 演化；
- VLBI source size / centroid motion 对 off-axis geometry 特别关键；
- population level 的 luminosity function 和 event rate constraints。

单独的 bump 或 plateau 不足以确认 structured jet，因为 energy injection、density variation、reverse shock、two-component jet 或 scintillation 都可能产生类似 light-curve feature。

## 10. 与 energy injection 的区别

第八章的 energy injection 是同一 blast wave 的 energy 随时间增长：

```tex
E(t)\propto t^e.
```

Structured jet 则是不同 angular zones 在不同时间被 Doppler weighting 和 equal-arrival-time surface 投影出来。二者都可能让 light curve flatten，但物理图像不同：

- energy injection：blast wave total energy 真实增加；
- structured jet：observer 看到的 dominant emitting region 改变；
- two-component jet：离散 angular components 的 dominance 发生转换；
- density variation：external medium 改变 electron number 和 magnetic field。

区分时应检查 energetics、multi-band closure relations、SED consistency、polarization 和 imaging / centroid motion。

## 11. 与事件页面的接口

- GRB 030329：two-component model 可视为 structured outflow 的离散版本；narrow / wide components 的 angular energy 与 dynamical timescale 解释 early break 和 late radio behavior，但 refreshed shock 或 continuous structured jet 是需要并列比较的 alternatives。
- GRB 080319B：naked-eye burst 的 narrow core + wider component 解释说明 on-axis narrow core 可造成极端 apparent brightness；但 prompt optical / gamma mismatch 仍需独立辐射成分解释。
- GRB 221009A：极高 `E_iso`、TeV afterglow、narrow jet / structured jet core 和 shallow structured jet interpretation 都使 `θ_v`、`θ_c` 和 angular profile 成为核心模型量；true energy 与 beaming correction 高度模型依赖。
- GW170817 / GRB170817A：不是本教材当前事件主线，但它是 off-axis structured jet 的关键校准案例，说明 light curve alone 与 quasi-spherical outflow 简并，VLBI centroid motion 可打破简并。

## 12. 常见误区

- **把 `θ`、`θ_v` 和 `ψ` 混为一谈**：`θ` 是 jet 内角坐标，`θ_v` 是观测者相对 jet axis 的角度，`ψ` 是 emitting element 相对 observer 的角距。
- **把 `E_iso(θ_v)` 当作 `4π dE/dΩ(θ_v)`**：off-axis prompt observable 是 Doppler-weighted angular integral。
- **把 top-hat beaming correction 套到 structured jet**：structured jet 的 true energy 要积分 angular profile，并依赖 outer cutoff。
- **只凭 smooth break 判定 structured jet**：energy injection end、density variation 或 component transition 也可造成平滑转折。
- **忽略 source-specific parameterization**：Gaussian、power-law、two-component 的 `Γ(θ)` 和 `dE/dΩ(θ)` 定义可能不同，不能只比较名称。
- **把 review-level taxonomy 当作事件结论**：具体 GRB 的 `θ_c`、`θ_v`、profile slope 必须来自事件级 light curve / SED / imaging 拟合。

## 13. 和后续章节的接口

- Two-component jet：把 continuous angular profile 离散化为 narrow / wide components，并重点讨论 `t_{dec,w}` 与 `t_{jet,n}` 的相对时序。
- Event applications：把 GRB 030329、GRB 080319B、GRB 221009A 的 structured / two-component interpretation 放回观测事实和模型解释分离框架。
- Prompt observables：若后续展开 prompt emission model，需要把 `E_iso(θ_v)` 与 `E_peak(θ_v)`、radiative efficiency、spectral shape 和 detector threshold 一起处理。

## 来源

- O. S. Salafia and G. Ghirlanda, “The Structure of Gamma Ray Burst Jets,” arXiv:2206.11088。
- Bing Zhang, “The Physics of Gamma-Ray Bursts & Relativistic Jets,” arXiv:1410.0679。
- Tsvi Piran, “The Physics of Gamma-Ray Bursts,” Reviews of Modern Physics 76, 1143-1210 (2004), arXiv:astro-ph/0405503。
- J. E. Rhoads, “The Dynamics and Light Curves of Beamed Gamma-Ray Burst Afterglows,” ApJ 525, 737-749 (1999), arXiv:astro-ph/9903399。
- R. Sari, T. Piran and J. P. Halpern, “Jets in Gamma-Ray Bursts,” ApJL 519, L17-L20 (1999), arXiv:astro-ph/9903339。
- F. Peng, A. Königl and J. Granot, “Two-Component Jet Models of Gamma-Ray Burst Sources,” ApJ 626, 966-977 (2005), arXiv:astro-ph/0410384。
- B. O'Connor et al., “A structured jet explains the extreme GRB 221009A,” Science Advances 9, eadi1405 (2023), arXiv:2302.07906。
