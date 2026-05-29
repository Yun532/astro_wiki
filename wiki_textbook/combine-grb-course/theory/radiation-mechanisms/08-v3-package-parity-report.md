# 08 杈愬皠鏈哄埗浠ｇ爜 v3 閫愮偣楠岃瘉鎶ュ憡

鐘舵€侊細v3 package-compatible parity銆傛湰鏂囧彧鍥炵瓟鈥滄湰鍦拌緪灏勬満鍒朵唬鐮佸湪鍚屼竴鍙傛暟涓嬫槸鍚﹁兘澶嶅埢鎴愮啛寮€婧愬簱鐨勬暟鍊艰緭鍑衡€濓紝涓嶅洖绛?GRB 221009A 鐨勪簨浠惰В閲娿€?
## 1. 涓夊眰浠ｇ爜绾﹀畾

鏈」鐩幇鍦ㄦ妸杈愬皠鏈哄埗浠ｇ爜鍒嗘垚涓夊眰锛?
| 灞傜骇 | 鐩殑 | 鏄惁瑕佹眰閫愮偣涓€鑷?| 渚嬪瓙 |
| --- | --- | --- | --- |
| `teaching-reference` | 瀵瑰簲璇剧▼鎺ㄥ锛屼繚鐣欑墿鐞嗛€忔槑鎬?| 涓嶈姹?| fixed pitch-angle synchrotron銆乨elta IC銆乨elta pp |
| `package-compatible` | 澶嶅埢鏌愪釜鎴愮啛搴撴垨鏂囩尞 convention | 瑕佹眰 | `naima_compat.py`銆乣agnpy_compat.py`銆並afexhiu LUT |
| `benchmark-output` | 澶栭儴搴?adapter 杩愯缁撴灉 | 浣滀负瀵圭収锛屼笉杩涘叆 core 渚濊禆 | `naima`銆乣agnpy`銆乣ebltable`銆乣gammapy` |

鍥犳鍥鹃噷鐨勭孩绾垮拰钃濈嚎涓嶄竴瀹氬簲璇ラ噸鍚堛€傜湡姝ｈ璐村悎澶栭儴搴撶殑鏄?`package-compatible` 绾匡紱`teaching-reference` 绾垮鏋滀笉鍚岋紝蹇呴』瑙ｉ噴宸紓鏉ヨ嚜鍝噷銆?
## 2. 褰撳墠閫愮偣缁撴灉

褰撳墠楠屾敹鍏ュ彛锛?
```powershell
python -m reproduce.grb.validation_lab.check_radiation_package_parity_v3
```

杈撳嚭琛細

```text
E:\combine\reproduce\grb\validation_lab\outputs\tables\radiation_package_parity_v3_checks.csv
```

褰撳墠閫氳繃椤癸細

| 鏈哄埗 | 鏈湴 package-compatible 灞?| 澶栭儴 benchmark | 鏈€澶?log10 姣斿€艰宸?| 鐘舵€?|
| --- | --- | --- | --- | --- |
| synchrotron | `synchrotron_sed_naima_compatible_erg_cm2_s` | `naima.Synchrotron` | `6.77e-14 dex` | pass |
| inverse Compton | `inverse_compton_cmb_sed_naima_compatible_erg_cm2_s` | `naima.InverseCompton(CMB)` | `1.05e-13 dex` | pass |
| nonthermal bremsstrahlung | `nonthermal_bremsstrahlung_sed_naima_compatible_erg_cm2_s` | `naima.Bremsstrahlung` | `7.12e-4 dex` | pass |
| pp pion decay | `pp_kafexhiu_lut_pion_decay_sed_erg_cm2_s` | `naima.PionDecay` | `3.93e-4 dex` | pass |
| one-zone synchrotron | `synchrotron_sed_agnpy_compatible_erg_cm2_s` | `agnpy.Synchrotron` | `4.34e-3 dex` | pass |
| SSC | `synchrotron_self_compton_sed_agnpy_compatible_erg_cm2_s` | `agnpy.SynchrotronSelfCompton` | `8.69e-3 dex` | pass |
| proton synchrotron | `proton_synchrotron_sed_agnpy_compatible_erg_cm2_s` | `agnpy.ProtonSynchrotron` | `4.34e-4 dex` | pass |
| EBL attenuation | `ebl_attenuation_factor` | `ebltable` 缁欏畾 tau 鍚庣殑 `exp(-tau)` | `0` | pass |

杩欎簺鏁板€艰鏄庯細鍦ㄦ槑纭噰鐢ㄥ搴?package convention 鏃讹紝鏈湴浠ｇ爜宸茬粡鑳介€愮偣澶嶅埢澶栭儴搴撹緭鍑恒€傚畠涓嶈〃绀?teaching-reference 鍏紡鍜屽閮ㄥ簱蹇呴』瀹屽叏涓€鏍凤紝涔熶笉琛ㄧず澶栭儴搴撳氨鏄敮涓€姝ｇ‘鏍囧噯銆?
## 3. 鍥鹃噷鐨勭嚎濡備綍璇?
缁熶竴棰滆壊瑙勫垯锛?
- 钃濊壊锛氬閮ㄥ簱 `benchmark-output`锛屼笉鏄湰椤圭洰鍚庣画鍔ㄥ姏瀛﹂粯璁よ皟鐢ㄧ殑浠ｇ爜銆?- 绾㈣壊/姗欒壊锛氭湰鍦?`teaching-reference` 鎴?semi-analytic reference锛屾渶鎺ヨ繎璇剧▼鎺ㄥ銆?- 缁胯壊锛氭湰鍦?`package-compatible`锛岀敤浜庡鍒绘煇涓紑婧愬簱 convention 骞跺仛閫愮偣 parity銆?
`benchmark_naima_local_lepton_sed_ratio.png`锛?
- 宸﹀垪鏄?SED 鏇茬嚎锛屾í杞存槸 photon energy锛岀旱杞存槸 \(E^2 dN/dE\) 鎴栫瓑浠风殑 \(\nu F_\nu\)銆?- 宸﹀垪鐜板湪鍚屾椂鐢?external benchmark銆乼eaching-reference銆乸ackage-compatible銆?- 鍙冲垪鏄?ratio锛岀敾 `package-compatible / external benchmark`銆?- 姣忎竴琛屽搴斾竴涓満鍒讹細synchrotron銆両C銆乥remsstrahlung銆乸ion_decay銆?
`benchmark_agnpy_local_sed_ratio.png`锛?
- 宸﹀垪鍚屾椂鐢?external benchmark銆乼eaching/semi-analytic銆乤gnpy-compatible銆?- 鍙冲垪鍙鏌?`agnpy-compatible / agnpy`銆?- 褰撳墠琛屽寘鎷?synchrotron銆丼SC銆乸roton_synchrotron銆?
濡傛灉钃濈嚎鍜岀孩绾夸笉鍚岋紝鍏堢湅鍥句緥锛?
- 鑻ヨ摑绾挎槸 external銆佺孩绾挎槸 teaching-reference锛屼笉鍚屾槸鍏佽鐨勶紝浣嗗繀椤绘湁 convention 瑙ｉ噴銆?- 鑻ョ豢鑹叉垨 package-compatible 绾垮拰 external 鏄庢樉涓嶅悓锛屾墠鏄?parity bug 鎴栧弬鏁?鍗曚綅杞崲 bug銆?
## 4. 涓轰粈涔?teaching-reference 浼氫笉鍚?
鍚屾杈愬皠锛?
- 璇剧▼椤靛父浠庡浐瀹?pitch-angle 鐨?single-particle kernel \(P_\nu\) 鎺ㄥ銆?- `naima`/`agnpy` 甯搁噰鐢?angle-averaged 鎴?random-field approximation銆?- 涓よ€呭嘲鍊间綅缃€佸綊涓€鍖栥€佷綆鑳界鏂滅巼甯告暟鍙互涓嶅悓锛屼絾鍚屼竴鐗╃悊鏋侀檺涓嬭秼鍔夸竴鑷淬€?
IC锛?
- 璇剧▼椤靛彲浠?Thomson/KN 鐨?general kernel 鎺ㄥ埌瑙ｆ瀽鏋侀檺銆?- `naima` 瀵?CMB IC 浣跨敤 Khangulyan/Aharonian/Kelner 2014 鐨勮繎浼兼牳銆?- delta approximation 鍙互缁欒В鏋愯氨鎸囨暟鍜屽嘲浣嶇洿瑙夛紝浣嗕笉鑳介€愮偣澶嶅埢瀹屾暣 kernel銆?
SSC锛?
- teaching-reference 浣跨敤鈥滃厛缁?synchrotron seed luminosity锛屽啀鏋勯€?photon density锛屽啀鐢?IC kernel 绉垎鈥濈殑閫忔槑璺嚎銆?- `agnpy` 浣跨敤 one-zone blob convention锛氫綋绉€丏oppler銆乺edshift銆乻eed photon density銆乪scape/geometry factor 閮芥湁鍥哄畾绾﹀畾銆?- 鎵€浠?SSC 鏈€瀹规槗鍑虹幇鍥犲瓙绾у樊寮傦紱v3 鐨?`agnpy-compatible` 灞傚氨鏄负娑堥櫎杩欎簺 convention 宸紓鑰屽啓鐨勩€?
Bremsstrahlung锛?
- thermal free-free 鍜?nonthermal bremsstrahlung 鏄笉鍚岄棶棰樸€?- v3 鐨?package-compatible 瀵圭収澶嶅埢鐨勬槸 `naima.Bremsstrahlung` 鐨?nonthermal Baring et al. 1999 cross-section convention銆?- thermal free-free 浠嶇敱鏈湴 `bremsstrahlung.py` 鐨?cgs 鍏紡鍋?fixed-point 楠岃瘉锛屼笉鎷?`naima.Bremsstrahlung` 鐩存帴褰?thermal benchmark銆?
Hadronic锛?
- `pp_delta_pion_decay_sed` 鏄暀瀛?閲忕骇灞傘€?- `pp_kafexhiu_lut_pion_decay_sed` 鏄?package-compatible 灞傦紝澶嶅埢 `naima.PionDecay` 榛樿 Kafexhiu14 LUT 璺嚎銆?- proton synchrotron 宸叉湁 teaching-reference SED 鍜?`agnpy-compatible` SED锛沺-gamma銆丅ethe-Heitler銆乧ascade 浠嶅彧鍋?threshold/envelope锛屼笉浼鎴愬畬鏁磋氨銆?
## 5. 褰撳墠浠嶄笉鑳藉０绉颁粈涔?
- 涓嶈兘澹扮О宸茬粡瀹屾垚瀹屾暣 hadronic cascade銆?- 涓嶈兘澹扮О p-gamma銆丅ethe-Heitler pair injection 鎴?EM cascade 宸叉湁瀹屾暣璋变唬鐮併€?- 涓嶈兘鎶?`naima`銆乣agnpy` 鎴?`ebltable` 鐨勮緭鍑哄啓鎴?GRB 浜嬩欢缁撹銆?- 涓嶈兘鎶?package-compatible 灞傛浛浠ｈ绋嬫帹瀵硷紱瀹冨彧鏄槑纭?convention 鍚庣殑鏁板€煎鍒诲眰銆?
## 6. 涓昏浜х墿

| 绫诲瀷 | 璺緞 |
| --- | --- |
| v3 楠屾敹琛?| `reproduce/grb/validation_lab/outputs/tables/radiation_package_parity_v3_checks.csv` |
| naima summary | `reproduce/grb/validation_lab/outputs/tables/benchmark_naima_local_lepton_ratio_summary.csv` |
| agnpy summary | `reproduce/grb/validation_lab/outputs/tables/benchmark_agnpy_local_ratio_summary.csv` |
| naima 鍥?| `reproduce/grb/validation_lab/outputs/figures/benchmark_naima_local_lepton_sed_ratio.png` |
| agnpy 鍥?| `reproduce/grb/validation_lab/outputs/figures/benchmark_agnpy_local_sed_ratio.png` |
| EBL 鍥?| `reproduce/grb/validation_lab/outputs/figures/benchmark_ebltable_tau_curves.png` |


## 7. 代码文件分层约定

从本轮开始，代码文件不再只靠函数名区分用途，而是固定为三类入口：

| 层级 | 入口文件 | 颜色 | 用途 |
| --- | --- | --- | --- |
| 后续计算 / production | `reproduce/grb/core/radiation/production.py` | 绿色 | 给动力学、事件诊断和正式数值流程调用；结果尽量逐点复刻成熟库 convention |
| 教学 / teaching | `reproduce/grb/core/radiation/teaching.py` | 红色/橙色 | 给课程推导、示例和插图调用；允许简化，但必须解释和 production 的差异 |
| 外部库 / external benchmark | `reproduce/grb/validation_lab/external_radiation_libraries.py` 与 `benchmark_adapters/` | 蓝色 | 只 import 外部库，只做参考和检验，不进入 core 运行依赖 |

分层检查入口：

```powershell
python -m reproduce.grb.validation_lab.check_radiation_layer_boundaries
```

这个检查会确认 `production.py` 和 `teaching.py` 没有 import `naima`、`agnpy`、`gammapy` 等外部库，并确认三个层级的入口文件都存在。后续新增机制时，必须先进入对应层级，再进入 benchmark adapter。
