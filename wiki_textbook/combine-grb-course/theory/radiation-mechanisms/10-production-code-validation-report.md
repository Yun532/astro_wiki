# 10 Production 辐射代码验证报告

状态：v1.1 production-suite。本文只回答一个问题：后续动力学和事件诊断应该调用哪一层代码，以及这些代码是否已经和外部成熟库或固定点对照过。

2026-05-25 纠偏记录：source-agnostic foundation 与 accelerator screening 已有 production code 和 validation，但此前没有专门物理推导/实现反馈页。现已新增 `theory/radiation-mechanisms/11-source-agnostic-foundation-and-acceleration.md`，这些 helper 的理论状态在本报告中统一标为 `draft-derived / implementation-feedback / local-fixed-point`，不能说成完整 course-complete 或完整 accelerator solver。

## 1. 结论

后续默认调用绿色层：

```text
reproduce/grb/core/radiation/production.py
```

新增总入口：

```powershell
python -m reproduce.grb.validation_lab.check_radiation_production_suite_v1
```

这不是审计页，而是会实际运行：

- `naima` 对照：synchrotron、IC(CMB)、nonthermal bremsstrahlung、pp pion decay。
- `agnpy` 对照：one-zone synchrotron、SSC、proton synchrotron。
- `ebltable` 对照：给定外部 `tau(E,z)` 后，本地 `exp(-tau)` helper 逐点一致。
- 本地 fixed-point：cooling time、KN envelope、pitch-angle、gamma-gamma angle average、secondary cooling/decay envelope。
- source-agnostic foundation：局域 `B`、`U_ph`、tabulated photon field energy density、electron cooling curve、electron cooling time-series。
- source-agnostic accelerator screening：Hillas confinement、Bohm-like acceleration time、escape envelopes、electron synchrotron loss ceiling。
- source-adapter bridge：给定 local `B,R,U_ph` 后，`evaluate_local_zone_screening_summary()` 输出 field/cooling/acceleration summary。
- local gamma-gamma opacity workbench：给定 local target spectrum 与 path length 后，`evaluate_local_gamma_gamma_opacity_screening()` 输出 opacity curve。
- forward-shock gamma-gamma opacity screen：给定 BM local zone 与 caller-supplied mono target envelope 后，输出 `alpha_gg`、`tau_gg` 和 attenuation。
- production dispatcher smoke test：`evaluate_production_sed_curve()` 能直接批量算谱。
- gamma-gamma target spectrum opacity smoke test：给定 source-local target photon field 后，绿色层能批量输出 `alpha_gg`、`tau_gg` 和 attenuation。

GRB forward-shock BM state 到 local-zone bridge 的检查属于 afterglow source-adapter 验证，入口是 `python -m reproduce.grb.validation_lab.check_forward_shock_local_zone_v1`；forward-shock gamma-gamma opacity screen 的入口是 `python -m reproduce.grb.validation_lab.check_forward_shock_gamma_gamma_opacity_v1`。二者都已纳入 validation-lab trace manifest；它们不是 radiation production suite 的外部库 parity 项。

对应理论/实现反馈页：

| 代码范围 | 对应页面 | 当前理论状态 |
| --- | --- | --- |
| source-agnostic fields / cooling arrays | `11-source-agnostic-foundation-and-acceleration.md` | `draft-derived / implementation-feedback` |
| accelerator screening helpers | `11-source-agnostic-foundation-and-acceleration.md`; `../grb-afterglow/11-particle-acceleration-and-maximum-energy.md` | `draft-derived / source-screening` |

## 2. 当前逐点对照结果

| 机制 | 后续调用的绿色函数 | 蓝色外部库 | 最大 `|log10(local/external)|` | 状态 |
| --- | --- | --- | --- | --- |
| synchrotron | `synchrotron_sed_naima_parity` | `naima.Synchrotron` | `6.77e-14` | pass |
| inverse Compton CMB | `inverse_compton_cmb_sed_naima_parity` | `naima.InverseCompton(CMB)` | `1.05e-13` | pass |
| nonthermal bremsstrahlung | `nonthermal_bremsstrahlung_sed_naima_parity` | `naima.Bremsstrahlung` | `7.12e-4` | pass |
| pp pion decay | `pp_pion_decay_sed_naima_parity` | `naima.PionDecay` | `3.93e-4` | pass |
| one-zone synchrotron | `synchrotron_sed_agnpy_one_zone_parity` | `agnpy.Synchrotron` | `4.34e-3` | pass |
| SSC one-zone | `ssc_sed_agnpy_one_zone_parity` | `agnpy.SynchrotronSelfCompton` | `8.69e-3` | pass |
| proton synchrotron | `proton_synchrotron_sed_agnpy_one_zone_parity` | `agnpy.ProtonSynchrotron` | `4.34e-4` | pass |
| EBL attenuation helper | `ebl_attenuation_factor` | `ebltable` 给定 `tau` 后的 `exp(-tau)` | `0` | pass |

新增 source-local gamma-gamma opacity 不是外部 EBL parity，而是 numerical-kernel / fixed-point 验证：

| 机制 | 后续调用的绿色函数 | 验证 | 状态 |
| --- | --- | --- | --- |
| mono target opacity | `gamma_gamma_monoenergetic_absorption_coefficient_cgs` | Breit-Wheeler angle integral smoke | pass |
| target spectrum opacity | `gamma_gamma_target_spectrum_absorption_coefficient_cgs` | `alpha_gg` 随 target density 线性、零密度为零 | pass |
| target spectrum optical depth | `gamma_gamma_target_spectrum_optical_depth` | `tau_gg=alpha_gg l`，随 path length 线性 | pass |
| target opacity curve | `evaluate_gamma_gamma_target_spectrum_opacity_curve` | 批量输出有限正值 `alpha/tau/attenuation` | pass |

新增 source-agnostic foundation 结果：

| 基础接口 | 后续调用的绿色函数 | 验证 | 状态 |
| --- | --- | --- | --- |
| tabulated photon energy density | `photon_energy_density_from_tabulated_field` | blackbody table 积分对 \(U=aT^4\)，误差 < 5% | pass |
| magnetic field energy density | `magnetic_energy_density` / `MagneticField.energy_density_erg_cm3` | \(U_B\propto B^2\)，双倍 B 得到 4 倍 \(U_B\) | pass |
| electron cooling curve | `evaluate_electron_cooling_curve` | \(t_{\rm syn}\propto\gamma^{-1}\)、\(t_{\rm IC}\propto\gamma^{-1}\)、total cooling 按功率相加 | pass |
| electron cooling time-series | `evaluate_electron_cooling_timeseries` | 若 `B(t)\propto t^{-1/2}`、`U_ph(t)\propto t^{-1}`，固定 `gamma` 的 \(t_{\rm syn}\)、\(t_{\rm IC}\)、total cooling 均随 `t` 线性增长 | pass |
| KN envelope | `evaluate_electron_cooling_curve` | high-\(\gamma\) 时 KN envelope 比 Thomson cooling 慢 | pass |

新增 accelerator foundation 结果：

| 基础接口 | 后续调用的绿色函数 | 验证 | 状态 |
| --- | --- | --- | --- |
| Hillas energy | `hillas_max_energy` | \(E_{\max}\propto B,R,Z\) | pass |
| Bohm-like acceleration time | `bohm_acceleration_time` | \(t_{\rm acc}\propto\gamma/B\) | pass |
| electron synchrotron loss limit | `electron_synchrotron_loss_limited_gamma_max` | \(\gamma_{\max}\propto B^{-1/2}\) | pass |
| escape envelopes | `light_crossing_escape_time`, `bohm_diffusion_escape_time` | light escape \(\propto R\)，Bohm diffusion escape \(\propto B\) at fixed gamma/R | pass |

新增 local-zone workbench 结果：

| 基础接口 | 后续调用的绿色函数 | 验证 | 状态 |
| --- | --- | --- | --- |
| source-adapter local-zone summary | `evaluate_local_zone_screening_summary` | \(U_B\propto B^2\)、\(t_{\rm syn}\propto B^{-2}\)、Hillas \(E\propto B,R\)、\(t_{\rm esc}\propto R\)、\(t_{\rm IC}\propto U_{\rm ph}^{-1}\) | pass |
| local gamma-gamma target-spectrum opacity screen | `evaluate_local_gamma_gamma_opacity_screening` | 与 direct target-spectrum opacity curve 一致；density/path 线性；zero target spectrum 给 \(\alpha=\tau=0\)、attenuation=1 | pass |

新增 GRB forward-shock source adapter 结果：

| 基础接口 | 后续调用的函数 | 验证 | 状态 |
| --- | --- | --- | --- |
| BM state to local-zone screening | `forward_shock_radiation_screening_summary` | ISM/wind 中 \(\Gamma,R,B',R'_{\rm screen},U'_{\rm ph},E_{\rm Hillas}\) 的 log-time slopes 与 BM 标度一致 | pass |
| BM local zone to cooling / acceleration time series | `forward_shock_cooling_acceleration_timeseries` | ISM/wind 中 \(t_{\rm syn},t_{\rm IC},t_{\rm acc},t_{\rm esc},\gamma_{\rm syn},E_{\rm Hillas}\) 的 log-time slopes 与 BM 标度一致 | pass |
| BM local zone to gamma-gamma opacity screen | `forward_shock_gamma_gamma_opacity_screening` | ISM/wind 中 \(n'_{\rm target}\)、\(\alpha_{\gamma\gamma}\)、\(\tau_{\gamma\gamma}\) 的 log-time slopes 与 BM/local-size 标度一致；target density 和 path length 固定点线性通过 | pass |
| BM local zone to tabulated target opacity screen | `forward_shock_gamma_gamma_target_spectrum_screening` | caller-supplied target shape 归一化到 \(U'_{\rm ph}=f_{\rm ph}e'\) 后，ISM/wind 中 normalization、target density、\(\alpha_{\gamma\gamma}\)、\(\tau_{\gamma\gamma}\) 标度通过；shape rescaling 不改变 opacity | pass |

这些结果说明：在明确采用 package-compatible convention 时，绿色代码已经能逐点复刻对应外部库。红色 teaching 层可以不同，因为它保留课程近似；真正需要贴近蓝色外部库的是绿色层。

## 3. 总览图

![production suite overview](file:///E:/combine/reproduce/grb/validation_lab/outputs/figures/radiation_production_suite_v1_overview.png)

左图是绿色 production SED 与蓝色外部库的最大 log 比值误差；右图是本轮检查的验证层级统计。完整曲线仍看：

- `file:///E:/combine/reproduce/grb/validation_lab/outputs/figures/benchmark_naima_local_lepton_sed_ratio.png`
- `file:///E:/combine/reproduce/grb/validation_lab/outputs/figures/benchmark_agnpy_local_sed_ratio.png`
- `file:///E:/combine/reproduce/grb/validation_lab/outputs/figures/radiation_cooling_curves_v1.png`
- `file:///E:/combine/reproduce/grb/validation_lab/outputs/figures/radiation_angle_kernels_v1.png`

## 4. 还能不能直接用

可以直接用于后续衔接动力学的部分：

- 光子谱：synchrotron、IC(CMB)、nonthermal bremsstrahlung、pp pion decay、one-zone synchrotron、SSC、proton synchrotron。
- 通用场量：magnetic field、isotropic photon field、tabulated photon-field energy density、electron cooling curve、electron cooling time-series。
- 加速器筛选：Hillas confinement、Bohm-like acceleration time、light/Bohm escape envelope、electron synchrotron loss-limited gamma。
- source adapter bridge：`evaluate_local_zone_screening_summary()`，用于未来 GRB/AGN/PWN/SNR/TDE adapter 提交 local zones 后统一比较。
- local gamma-gamma opacity bridge：`evaluate_local_gamma_gamma_opacity_screening()`，用于未来 source adapters 在已给出 target photon spectrum 和 path length 后统一比较 opacity。
- 冷却：electron synchrotron cooling、IC Thomson cooling、IC KN envelope cooling、thermal free-free cooling、nonthermal brems loss envelope、pp loss envelope。
- 角核和 opacity：synchrotron isotropic pitch-angle convention、gamma-gamma isotropic angle-averaged cross-section、source-local gamma-gamma target spectrum opacity。

仍然不能声称完成的部分：

- full anisotropic IC solver。
- self-consistent SSC radiative transfer。
- complete p-gamma Monte Carlo。
- Bethe-Heitler pair injection spectrum。
- complete hadronic / EM cascade。
- neutrino event-rate prediction。

## 5. 产物

| 类型 | 路径 |
| --- | --- |
| 绿色代码清单 | `reproduce/grb/validation_lab/outputs/tables/radiation_production_registry_v1.csv` |
| 生产验证总表 | `reproduce/grb/validation_lab/outputs/tables/radiation_production_suite_v1_summary.csv` |
| 基础场量检查表 | `reproduce/grb/validation_lab/outputs/tables/radiation_foundation_v1_checks.csv` |
| 基础 cooling curve 表 | `reproduce/grb/validation_lab/outputs/tables/radiation_foundation_cooling_curve_v1.csv` |
| 基础 cooling time-series 表 | `reproduce/grb/validation_lab/outputs/tables/radiation_foundation_cooling_timeseries_v1.csv` |
| 加速器固定点检查表 | `reproduce/grb/validation_lab/outputs/tables/radiation_acceleration_v1_checks.csv` |
| 加速器 B-R 扫描表 | `reproduce/grb/validation_lab/outputs/tables/radiation_acceleration_limit_scan_v1.csv` |
| local-zone workbench summary | `reproduce/grb/validation_lab/outputs/tables/radiation_source_workbench_v1_summary.csv` |
| local-zone workbench checks | `reproduce/grb/validation_lab/outputs/tables/radiation_source_workbench_v1_checks.csv` |
| local gamma-gamma opacity summary | `reproduce/grb/validation_lab/outputs/tables/local_gamma_gamma_opacity_screening_v1_summary.csv` |
| local gamma-gamma opacity checks | `reproduce/grb/validation_lab/outputs/tables/local_gamma_gamma_opacity_screening_v1_checks.csv` |
| forward-shock local-zone summary | `reproduce/grb/validation_lab/outputs/tables/forward_shock_local_zone_v1_summary.csv` |
| forward-shock local-zone checks | `reproduce/grb/validation_lab/outputs/tables/forward_shock_local_zone_v1_checks.csv` |
| forward-shock cooling / acceleration summary | `reproduce/grb/validation_lab/outputs/tables/forward_shock_cooling_acceleration_v1_summary.csv` |
| forward-shock cooling / acceleration checks | `reproduce/grb/validation_lab/outputs/tables/forward_shock_cooling_acceleration_v1_checks.csv` |
| forward-shock gamma-gamma opacity summary | `reproduce/grb/validation_lab/outputs/tables/forward_shock_gamma_gamma_opacity_v1_summary.csv` |
| forward-shock gamma-gamma opacity checks | `reproduce/grb/validation_lab/outputs/tables/forward_shock_gamma_gamma_opacity_v1_checks.csv` |
| forward-shock tabulated target opacity summary | `reproduce/grb/validation_lab/outputs/tables/forward_shock_gamma_gamma_target_spectrum_v1_summary.csv` |
| forward-shock tabulated target opacity checks | `reproduce/grb/validation_lab/outputs/tables/forward_shock_gamma_gamma_target_spectrum_v1_checks.csv` |
| 生产验证总览图 | `reproduce/grb/validation_lab/outputs/figures/radiation_production_suite_v1_overview.png` |
| 基础 cooling curve 对照图 | `reproduce/grb/validation_lab/outputs/figures/radiation_foundation_cooling_curves_v1.png` |
| 加速器筛选对照图 | `reproduce/grb/validation_lab/outputs/figures/radiation_acceleration_limits_v1.png` |
| local-zone workbench 图 | `reproduce/grb/validation_lab/outputs/figures/radiation_source_workbench_v1.png` |
| local gamma-gamma opacity 图 | `reproduce/grb/validation_lab/outputs/figures/local_gamma_gamma_opacity_screening_v1.png` |
| forward-shock local-zone 图 | `reproduce/grb/validation_lab/outputs/figures/forward_shock_local_zone_v1.png` |
| forward-shock cooling / acceleration 图 | `reproduce/grb/validation_lab/outputs/figures/forward_shock_cooling_acceleration_v1.png` |
| forward-shock gamma-gamma opacity 图 | `reproduce/grb/validation_lab/outputs/figures/forward_shock_gamma_gamma_opacity_v1.png` |
| forward-shock tabulated target opacity 图 | `reproduce/grb/validation_lab/outputs/figures/forward_shock_gamma_gamma_target_spectrum_v1.png` |
| 绿色代码入口说明 | `reproduce/grb/core/radiation/README.md` |
| 生产代码入口 | `reproduce/grb/core/radiation/production.py` |

![radiation foundation cooling curves](file:///E:/combine/reproduce/grb/validation_lab/outputs/figures/radiation_foundation_cooling_curves_v1.png)

![radiation acceleration limits](file:///E:/combine/reproduce/grb/validation_lab/outputs/figures/radiation_acceleration_limits_v1.png)

![radiation source workbench](file:///E:/combine/reproduce/grb/validation_lab/outputs/figures/radiation_source_workbench_v1.png)

## 6. 下一步代码目标

下一步不是继续写审计页，而是按物理缺口补 production 层：

- 基于 `evaluate_local_zone_screening_summary()` 继续写更多具体 source adapters；GRB forward-shock local zone 已完成 v1，后续 AGN/PWN/SNR/TDE 必须同样记录 \(B,R,U_{\rm ph}\) 的来源和 frame convention。
- 下一条 source adapter 应从 AGN blob、PWN/SNR shell 或 TDE outflow 中选择，并沿用 `AG-FS-LOCAL-ZONE-001` 的 provenance 纪律：Formula ID、函数名、单位、验证等级、课程差异和 must-not-claim 必须同时登记。
- 把 gamma-gamma opacity 接到具体动力学/事件 target photon field 生成器，但仍要显式记录 target spectrum provenance。
- 强子侧只新增能被成熟库或固定点约束的 production helper；p-gamma、Bethe-Heitler、cascade 仍先保留 theory/teaching/benchmark boundary。
