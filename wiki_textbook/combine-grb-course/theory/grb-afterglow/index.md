# GRB 余辉理论课程

状态：v0.2 agent 审稿整合后的课程主线。这个目录是 `wiki-textbook-snapshot/` 之外的新理论课程层，按辐射机制页已经固定的规则组织：先给 general expression，再给 detailed derivation block，再给 exact analytic status、approximation hierarchy、code convention 和 benchmark boundary。

旧目录 `wiki-textbook-snapshot/` 保留为迁移来源，不再作为新课程页的最终结构。

## 课程入口

- [01 Blandford-McKee 与 external shock 动力学](01-blandford-mckee-and-external-shock.md)
- [02 余辉 synchrotron breaks 与 closure relations](02-afterglow-synchrotron-breaks-and-closure-relations.md)
- [03 Reverse shock 与早期 optical flash](03-reverse-shock-and-early-optical-flash.md)
- [04 Jet break、structured jet 与 EATS 几何](04-jet-break-structured-jet-and-eats.md)
- [05 Energy injection、density variation 与余辉简并](05-energy-injection-density-variation-and-degeneracies.md)
- [06 Non-relativistic transition 与 radio calorimetry](06-non-relativistic-transition-and-radio-calorimetry.md)
- [07 Two-component jet 与 component decomposition](07-two-component-jet-and-component-decomposition.md)
- [08 Polarization、VLBI 与几何诊断](08-polarization-vlbi-and-geometric-diagnostics.md)
- [09 Afterglow fitting workflow 与参数简并](09-afterglow-fitting-workflow-and-parameter-degeneracy.md)
- [10 SSC 与 TeV 余辉](10-ssc-and-tev-afterglow.md)
- [11 粒子加速与最大能量](11-particle-acceleration-and-maximum-energy.md)
- [12 Cascade、neutrino 与传播边界](12-cascade-neutrino-and-propagation-boundaries.md)
- [13 事件解释链](13-event-interpretation-chain.md)
- [14 课程路线图与公式审计](14-course-roadmap-and-formula-audit.md)
- [15 符号、参考系与约定注册表](15-notation-frames-and-convention-registry.md)
- [16 章节总结与 Must-Not-Claim 索引](16-chapter-summary-and-must-not-claim-index.md)
- [Formula Index / 公式索引](formula-index.md)

## 完成度速查

这里的“完成”指讲义级 formal boundary，不是完整数值反演系统。

| 模块 | 当前状态 | 代码关系 | 仍缺什么 |
| --- | --- | --- | --- |
| BM / external shock dynamics | formal derivation covered | dynamics helpers partial-code | full hydrodynamic solver |
| synchrotron breaks / closure | formal derivation covered | synchrotron helpers partial-code | smooth transfer / full broadband fit |
| reverse shock | scale derivation covered | toy helpers | full reverse-shock hydrodynamics |
| jet / structured jet / EATS | geometry boundary covered | angular / EATS toy helpers | full structured-jet light curve |
| injection / density variation | theory-only boundary covered | no production solver | hydro response and EATS smoothing |
| non-relativistic / radio calorimetry | diagnostic boundary covered | theory / teaching | trans-relativistic solver, radio fitter |
| two-component / component decomposition | diagnostic boundary covered | theory-only | two-component hydro light curve |
| polarization / VLBI | diagnostic boundary covered | theory-only | polarized transfer / image synthesis |
| fitting workflow | report discipline covered | event diagnostics | MCMC / Bayesian inference |
| SSC / TeV / KN / opacity | formal kernel boundary covered | toy / benchmark / opacity helpers | self-consistent SSC transfer |
| acceleration / maximum energy | closed-limit boundary covered | source-agnostic screening helpers | afterglow-specific full timescale registry |
| cascade / neutrino / propagation | formal boundary covered | partial hadronic scales | full cascade、\(p\gamma\)、BH、event-rate |
| event interpretation | claim discipline covered | report workflow | unique event inference |

## 当前主线

```text
relativistic kinematics
  -> external shock dynamics
  -> synchrotron break evolution
  -> closure relations
  -> reverse shock
  -> jet break / structured jet / EATS
  -> energy injection / density variation / degeneracies
  -> non-relativistic transition / radio calorimetry
  -> two-component jet / component decomposition
  -> polarization / VLBI / geometric diagnostics
  -> fitting workflow / parameter degeneracy
  -> SSC / TeV afterglow
  -> particle acceleration / maximum energy
  -> cascade / neutrino / propagation boundaries
  -> event-model interpretation
  -> claim discipline / report checklist
  -> course roadmap / formula audit
  -> notation / frame / convention registry
  -> chapter summary / must-not-claim index
```

## 边界

本目录不是事件拟合报告，也不把 `afterglowpy`、`VegasAfterglow` 或任何单个外部包写成唯一标准。外部包只属于 benchmark-output 或 mature-method comparison；课程推导必须保留自己的假设、变量、参考系和代码差异说明。
