# 16 Polarization 与 VLBI geometric diagnostics

Light curve 和 SED 可以约束 afterglow dynamics、radiation regime 和 energy budget，但它们通常不能唯一确定 jet geometry。Polarization、source size、centroid motion 和 VLBI imaging 提供了额外的几何信息：它们直接或间接探测 magnetic-field ordering、viewing angle、jet structure 和 apparent expansion。

本章的目标不是推导完整 polarized radiative transfer，而是建立几何诊断语言：什么时候 polarization 支持 jet break，什么时候 centroid motion 支持 off-axis structured jet，什么时候 radio size 对 calorimetry 有帮助，以及这些诊断为什么仍然不是直接“成像喷流结构”。

## 1. Synchrotron polarization 的基本来源

Afterglow synchrotron emission 来自 power-law electrons 在 magnetic field 中辐射。单个均匀磁场区域的 optically thin synchrotron 可以有很高的 linear polarization。对 electron distribution

```tex
N(γ_e)\propto γ_e^{-p},
```

最大线偏振度为

```tex
Π_{max}=\frac{p+1}{p+7/3}.
```

对典型 `p\sim2.2`，`Π_max` 可达几十个百分点。但实际 afterglow polarization 通常更低，因为 emitting region 中 magnetic field 方向部分随机，且 equal-arrival-time surface 上不同区域的 polarization vectors 会相互抵消。

## 2. Ordered field 与 shock-generated field

Afterglow polarization 取决于 magnetic-field geometry：

- **Shock-generated random field**：磁场在 shock plane 内随机，局部 polarization 高，但整体对称性会抵消。
- **Ordered field**：若 ejecta 或 ambient medium 携带 large-scale field，可产生更高 polarization 或稳定 position angle。
- **Patchy field**：多个 coherence patches 会导致 polarization degree 和 position angle 随时间随机变化。

因此 polarization 不仅诊断 jet geometry，也诊断 magnetic-field origin。把 polarization signal 直接解释成 jet opening angle 会过度简化。

## 3. Top-hat jet 的 polarization signature

On-axis spherical outflow 在理想对称情况下净 polarization 近似抵消。Top-hat jet 在接近 jet break 时对称性被打破，可能产生 polarization peak，并伴随 position angle rotation。

直观原因是：当 `Γ^{-1}` 小于 `θ_j` 时，observer 看到的 emitting region 近似对称；当 beaming cone 扩大到 jet edge，缺失的一侧打破轴对称，产生 net polarization。

Jet-break 条件仍是

```tex
Γ(t_j)\sim θ_j^{-1}.
```

但 polarization peak 的时间、幅度和 angle rotation 取决于 magnetic-field configuration、lateral spreading、viewing offset 和 observing band。

## 4. Structured / off-axis jet 的 polarization

Structured jet 中，energy 和 Lorentz factor 随 angle 变化：

```tex
\mathcal{E}=\mathcal{E}(θ),\quad Γ=Γ(θ).
```

如果 observer 位于 off-axis，早期主要看到靠近 line of sight 的较弱 material；随着 blast wave decelerates，bright core 的 emission 逐渐进入 beaming cone。这会导致 light curve rise/peak，同时也可能产生有特征的 polarization evolution。

Off-axis structured jet 的 polarization 诊断价值在于：

- polarization peak 可接近 light-curve peak 或 jet-structure transition；
- position angle evolution 与 top-hat jet 可能不同；
- polarization degree 对 `θ_v/θ_c`、profile shape 和 magnetic field 敏感。

但实际区分需要高 cadence、多波段 polarization data，通常很难单独完成。

## 5. VLBI source size

Radio VLBI 可直接或间接约束 afterglow angular size。若 angular diameter 为 `θ_s`，luminosity distance / angular-diameter distance 给出 source size：

```tex
R_\perp \sim D_A θ_s.
```

这里 `R_\perp` 是 sky-projected size，`D_A` 是 angular-diameter distance。Source size 对 late radio calorimetry 很重要，因为它约束 emitting volume、brightness temperature、self-absorption 和 expansion speed。

GRB 030329 的 radio size measurement 曾为 expansion velocity、energy 和 geometry 提供关键约束，但这些解释仍依赖 synchrotron modeling 与 scintillation treatment。

## 6. Centroid motion 与 apparent velocity

Off-axis jet 会产生 centroid motion：随着 bright core 逐渐主导 emission，image centroid 在 sky plane 上移动。表观速度可写成

```tex
β_{app}=\frac{v_{app}}{c}.
```

对 relativistic motion，apparent velocity 可超过 1，这是 light-travel-time effect，不代表物质超光速。更完整地，对速度 `βc`、与视线夹角 `θ` 的 moving feature，有

```tex
β_{app}=\frac{β\sin θ}{1-β\cos θ}.
```

GW170817/GRB 170817A 的 VLBI centroid motion 是 off-axis structured jet interpretation 的经典几何证据。它说明：当 imaging/centroid data 存在时，geometry constraint 可以远强于 light curve alone。

## 7. 和 polarization 的互补

Polarization 与 VLBI imaging 提供不同信息：

| 诊断 | 主要约束 | 主要 caveat |
| --- | --- | --- |
| polarization degree | field ordering、asymmetry、viewing geometry | dust polarization、稀疏采样、field model degeneracy |
| position angle | symmetry axis、field geometry | 180° ambiguity、host/ISM contamination |
| source size | expansion、energy、brightness temperature | angular resolution、scintillation、model dependence |
| centroid motion | off-axis geometry、structured jet | 需要高精度 VLBI 和 nearby event |

组合这些 diagnostics 才能更稳健地区分 top-hat、structured jet、two-component jet 和 cocoon-like outflow。

## 8. 事件接口

- **GRB 030329**：radio size 和 calorimetry 对 energy / geometry 有重要约束，但 two-component interpretation 仍是模型解释。
- **GRB 170817A / GW170817**：VLBI superluminal centroid motion 支持 successful structured jet viewed off-axis，是 structured jet geometry diagnostic 的代表案例。
- **GRB 221009A**：极亮 afterglow 适合讨论 polarization / geometry diagnostics，但不同波段的 model interpretation 仍需分开。

## 9. 常见误区

- **把 polarization detection 当作 jet detection**：polarization 也可能来自 ordered magnetic field 或 dust contamination。
- **把 `Π_max` 当作观测 polarization**：实际净 polarization 通常远低于理论最大值。
- **把 apparent superluminal motion 当作真实超光速**：它是 projection 与 light-travel-time effect。
- **用 light curve alone 断言 geometry**：geometry diagnostics 需要 polarization、imaging、source size 或 centroid motion 支持。
- **忽略 host / Galactic polarization correction**：尤其 optical polarization 需要 foreground subtraction。

## 来源

- R. Sari, afterglow polarization work。
- J. Granot and A. Königl, GRB afterglow polarization and magnetic-field geometry work。
- O. S. Salafia and G. Ghirlanda, “The Structure of Gamma Ray Burst Jets,” arXiv:2206.11088。
- G. Mooley et al., GW170817 / GRB 170817A VLBI superluminal motion papers。
- G. B. Taylor et al. and related GRB 030329 radio size / VLBI literature。
- G. B. Rybicki and A. P. Lightman, “Radiative Processes in Astrophysics,” Wiley (1979)。
