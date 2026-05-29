# 07 Open-Source Benchmark Matrix

鐘舵€侊細v2 Docs-first roadmap銆傛湰椤典笉鏄绋嬫帹瀵硷紝涔熶笉鏄妸澶栭儴杞欢鍙樻垚鏈湴 API銆傚畠鍙洖绛旓細鏈湴 radiation code 涓庡叕寮€浠ｇ爜搴旇鍦ㄤ粈涔堝眰绾ф瘮杈冿紱鑻ヤ唬鐮侀噰鐢ㄦ垚鐔熷弬鏁板寲鎴?package convention锛岃绋嬮〉蹇呴』濡備綍鎶湶銆?
## 1. 鎬诲師鍒?
鏈」鐩富瀹炵幇姘歌繙鏄細

```text
reproduce/grb/core/radiation/
```

澶栭儴寮€婧愪唬鐮佸彧鍋氫笁浠朵簨锛?
1. 瀵圭収鐩稿悓鍏紡鎴栫浉鍚?convention 涓嬬殑鏁板€艰緭鍑恒€?2. 鏆撮湶鍗曚綅銆佸綊涓€鍖栥€佺Н鍒嗙綉鏍笺€佺矑瀛愬垎甯?convention 閿欒銆?3. 瀵逛笉鑳界畝鍗曡В鏋愰棴鍚堢殑杩囩▼鎻愪緵 benchmark envelope銆?
澶栭儴浠ｇ爜涓嶈兘鍋氫笁浠朵簨锛?
1. 涓嶈兘鏇夸唬璇剧▼鎺ㄥ銆?2. 涓嶈兘鎴愪负鏈湴 core API 鐨勮繍琛屼緷璧栥€?3. 涓嶈兘鎶?benchmark-output 鍐欐垚澶╀綋浜嬩欢鐨勭瀛︾粨璁恒€?
## 2. 鏈湴浠ｇ爜灞傜骇

| 灞傜骇 | 鏈湴鐩爣 | 璇存槑 |
| --- | --- | --- |
| course/reference | 浠庤绋嬪叕寮忕洿鎺ュ疄鐜?| 瀵瑰簲鏈哄埗椤垫帹瀵硷紝閫傚悎瀛︿範鍜屽叕寮忚拷韪?|
| numerical/reference | 鐢ㄦ暟鍊肩Н鍒嗗疄鐜拌緝瀹屾暣 kernel | 渚嬪 \(F(x)\)銆丅G/KN IC銆丅reit-Wheeler |
| mature numerical method | 閲囩敤鏂囩尞鍙傛暟鍖栥€佽〃鏍兼牳銆佽骞冲潎鎴栧崐瑙ｆ瀽杩戜技 | 蹇呴』鍦ㄨ绋嬮〉鎶湶宸紓 |
| package-compatible | 澶嶅埢鏌愪釜澶栭儴杞欢 convention | 鍙敤浜?benchmark parity锛屼笉浠ｈ〃鏈湴鐗╃悊涓荤嚎 |
| order-of-magnitude | 寮哄瓙/绾ц仈绛夊厛鍋氶噺绾ф帴鍙?| 涓嶈兘澹扮О瀹屾暣璋辨垨 cascade |
| benchmark-output | 澶栭儴 adapter 杈撳嚭 | 涓嶄綔涓烘湰鍦?API 渚濊禆 |

## 3. 杞诲瓙銆佺儹杩囩▼涓庡惛鏀?benchmark 鍊欓€?
| 鏈哄埗 | 褰撳墠鏈湴涓荤嚎 | 绗竴瀵圭収 | 鍚庣画瀵圭収 | 姣旇緝鐩爣 |
| --- | --- | --- | --- | --- |
| synchrotron | fixed pitch-angle `F(x)` + SED integral | `naima.Synchrotron` | `agnpy`, `JetSeT`, `GAMERA` | pitch-angle/random-field convention銆佽氨褰€佸綊涓€鍖?|
| inverse Compton | Blumenthal-Gould / KN isotropic kernel | `naima.InverseCompton` | `agnpy`, `JetSeT`, `GAMERA` | Thomson/KN 杩囨浮銆乻eed photon convention銆丼ED 鍗曚綅 |
| SSC | formal integral + semi-analytic hierarchy锛涗唬鐮佷粛鍋?toy/reference | `agnpy`, `JetSeT` | `GAMERA` | synchrotron seed field銆丼SC peak銆並N suppression |
| thermal free-free | Planck/Kirchhoff/free-free cgs helper | `naima.Bremsstrahlung` for nonthermal only | GAMERA/Gammapy 鐢熸€?| thermal/nonthermal 鍖哄垎銆佹埅闈?convention |
| nonthermal bremsstrahlung | simplified trend helper | `naima.Bremsstrahlung` | GAMERA/Gammapy | Haug/Koch-Motz/BG 鎴潰宸紓 |
| gamma-gamma opacity | Breit-Wheeler kernel + toy opacity | EBL tables / `ebltable` | Gammapy/CRPropa/ELMAG | opacity convention銆丒BL model銆乤ngle/spectrum integral |

褰撳墠鏈満瀹夎鐘舵€侊細

| package | 褰撳墠鐘舵€?| 澶囨敞 |
| --- | --- | --- |
| `naima` | installed / adapter exists | 鍏堜綔涓轰竴涓閮ㄥ鐓э紝涓嶆槸鍞竴鏍囧噯 |
| `afterglowpy` | installed / afterglow trend adapter exists | 涓昏鏄?afterglow light curve锛屼笉鏄熀纭€杈愬皠 kernel |
| `VegasAfterglow` | installed / afterglow trend adapter exists | 涓昏鏄?afterglow trend |
| `agnpy` | not installed | 閫傚悎鍚庣画 SSC / external Compton / absorption 瀵圭収 |
| `Gammapy` | not installed | 閫傚悎楂樿兘璋辨ā鍨嬬敓鎬佸鐓э紝闇€鏄庣‘ radiative model 瑕嗙洊鑼冨洿 |
| `JetSeT` | not installed | 閫傚悎 synchrotron / SSC / EC / blazar-style one-zone 瀵圭収 |
| `GAMERA` | not installed | 閫傚悎 leptonic + hadronic population modeling 瀵圭収 |
| `CRPropa` / `ELMAG` | not installed | 鏇村亸浼犳挱銆佽兘鎹熷拰 cascade envelope锛屼笉鏄?one-zone SED 鐩存帴鏇夸唬 |

## 4. 寮哄瓙涓庨潪瑙ｆ瀽杩囩▼ benchmark 鍊欓€?
寮哄瓙杩囩▼瑕佸尯鍒嗕笁灞傦細

- threshold / energy partition锛氬彲浠ユ湰鍦拌В鏋愭垨鏁伴噺绾у疄鐜般€?- emissivity kernel锛氬彲浠ュ仛鎴愮啛鍙傛暟鍖栨垨 tabulated benchmark銆?- full cascade锛氶€氬父闇€瑕佷笓闂?transport code锛屽綋鍓嶄笉鍐呯疆銆?
| 鏈哄埗 | 鏈湴绗竴灞?| 澶栭儴 benchmark 鍊欓€?| 姣旇緝鐩爣 | 涓嶈兘澹扮О |
| --- | --- | --- | --- | --- |
| \(pp\to\pi^0\to\gamma\gamma\) | threshold銆乮nelasticity銆乬amma energy scale | `naima.PionDecay`, GAMERA, Kelner/Aharonian/Kafexhiu parameterization | gamma-ray SED 褰㈢姸鍜屽嘲浣?| 瀹屾暣 hadronic cascade |
| \(p\gamma\) pion production | Delta resonance threshold銆乪nergy partition | SOPHIA/NeuCosmA/AM3銆並elner & Aharonian tables | threshold銆乶eutrino/gamma energy scale | 瀹屾暣 photohadronic cascade |
| Bethe-Heitler pair production | threshold/cooling formalism only | CRPropa銆乻pecialized loss-rate tables | cooling length / loss rate trend | one-zone photon SED 瀹屾暣姹傝В |
| proton synchrotron | characteristic frequency | GAMERA銆丣etSeT/agnpy 鑻ユ敮鎸?| 棰戠巼銆佸喎鍗淬€佽氨褰㈣秼鍔?| 鑷姩瑙ｉ噴 TeV 淇″彿 |
| electromagnetic cascade | 鏆備笉鏈湴瀹炵幇 | ELMAG/CRPropa/EBL 宸ュ叿閾?| cascade envelope | paper-level cascade model |

## 5. 褰撳墠宸插畬鎴愪笌缂哄彛

宸插畬鎴愶細

- 鏈湴 synchrotron course/reference kernel 涓?SED integral銆?- 鏈湴 IC Blumenthal-Gould / Klein-Nishina isotropic kernel 涓?tabulated seed helper銆?- Breit-Wheeler gamma-gamma cross-section numerical kernel銆?- gamma-gamma isotropic monoenergetic / tabulated target-field absorption helpers銆?- one-zone tabulated SSC seed-field conversion + BG/KN IC reuse helper銆?- thermal blackbody銆乸hotosphere銆乼hermal free-free cgs helpers銆?- synchrotron / IC 鐨?`naima` package-compatible parity grid銆?- convention-aware comparison script锛歵eaching-reference銆乸ackage-compatible銆乥enchmark-output 鍒嗗眰杈撳嚭 ratio銆?- Docs-first mature-method disclosure rule銆?
缂哄彛锛?
- SSC 宸叉湁 tabulated one-zone semi-analytic helper锛屼絾杩樻病鏈夎嚜娲?synchrotron transfer / SSA / multi-scattering solver銆?- nonthermal bremsstrahlung 浠嶆槸 simplified trend helper锛屾湭瀹炵幇 Haug/Koch-Motz/BG 绾ф埅闈€?- gamma-gamma 宸叉湁 isotropic target spectrum + angle integral helper锛屼絾杩樻病鏈?EBL/cosmology table 鎴栫┖闂翠緷璧?transfer銆?- hadronic 杩樺仠鍦?order-of-magnitude锛屾湭鍋氳氨绾ф湰鍦?parameterization銆?- cascade 绫昏繃绋嬪皻鏈繘鍏ユ湰鍦板疄鐜般€?
## 6. 涓嬩竴姝ユ墽琛岄『搴?
1. Docs-first锛氭墍鏈夋満鍒堕〉鍏堣ˉ榻愨€滀粠鎺ㄥ鍒颁唬鐮佺殑瀹炵幇绾﹀畾鈥濄€?2. thermal / nonthermal bremsstrahlung锛氫紭鍏堝疄鐜版垨 adapter 鍖栨垚鐔熸埅闈€?3. SSC锛氬疄鐜?one-zone semi-analytic seed-field + BG/KN IC kernel solver銆?4. gamma-gamma锛氬疄鐜?isotropic target spectrum optical-depth helper銆?5. \(pp\) pion-decay锛氭湰鍦?Kelner/Aharonian/Kafexhiu-level reference 鎴?package-compatible benchmark銆?6. \(p\gamma\)銆丅ethe-Heitler銆乧ascade锛氬厛寤虹珛 benchmark envelope锛屼笉鎬ョ潃鍐欐垚瀹屾暣妯″瀷銆?
## 7. Adapter 寮€鍙戣鍒?
姣忔帴鍏ヤ竴涓閮ㄥ簱锛屽繀椤绘柊澧炵嫭绔?adapter锛屼笉鍏佽鎶婂閮ㄥ簱閫昏緫鍐欒繘鏈湴 `core/radiation`锛?
```text
reproduce/grb/validation_lab/benchmark_adapters/<package>_radiation_adapter.py
```

adapter 鍙鏈湴鍙傛暟锛岃緭鍑?CSV/PNG/report锛涙湰鍦?`core/radiation` 涓?import 澶栭儴 benchmark package銆?
姣忎釜 benchmark 蹇呴』杈撳嚭锛?
```text
package_name
package_version
mechanism
parameter_set_id
local_model_class
external_model_class
energy_grid
local_sed
external_sed
ratio
finite_domain
known_convention_difference
must_not_claim
```

濡傛灉鏈湴浠ｇ爜鍜岃绋嬫帹瀵间笉鍚岋紝蹇呴』棰濆杈撳嚭锛?
```text
course_reference_sed
package_compatible_sed
reason_for_difference
```

## 8. 鍙傝€冨叆鍙?
- `naima` documentation: https://naima.readthedocs.io/
- `agnpy` documentation: https://agnpy.readthedocs.io/
- `JetSeT` documentation: https://jetset.readthedocs.io/
- `GAMERA` documentation: https://libgamera.github.io/GAMERA/docs/tutorials_main.html
- `CRPropa3` modules: https://crpropa.github.io/CRPropa3/pages/Simulation-Modules.html

## 9. 2026-05-21 澶氬簱 benchmark 鎺ュ叆璁板綍

鏈疆寮€濮嬫墽琛屸€滀笉瑕佸彧鐩镐俊涓€涓閮ㄥ簱鈥濈殑瑙勫垯銆傚綋鍓嶅彲杩愯鍜屼笉鍙繍琛岀姸鎬佸涓嬶細

| package | 鐘舵€?| 宸叉帴鍏ュ唴瀹?| convention 杈圭晫 |
| --- | --- | --- | --- |
| `naima` | installed / adapter runnable | synchrotron銆両C銆乶onthermal bremsstrahlung銆丳ionDecay 杈撳嚭锛泂ynchrotron/IC 鏈?package-compatible parity 灞?| `naima` 鏄竴涓?benchmark-output锛屼笉鏄敮涓€鏍囧噯 |
| `agnpy` | installed by `--no-deps` / adapter runnable | one-zone synchrotron 涓?SSC 鍚屽弬鏁?SED/ratio | `agnpy` 浣跨敤 blob銆丏oppler銆佷綋瀵嗗害銆佸悇鍚戝悓鎬?瑙掑钩鍧?convention锛涙湰鍦颁唬鐮佷娇鐢?total `dN/dE` 涓庤绋?reference锛岄渶瑕佹樉寮忔崲绠?|
| `ebltable` | installed / adapter runnable | Dominguez銆丗inke銆丗ranceschini 绛?EBL `tau(E,z)` 涓?`exp(-tau)` 鏇茬嚎 | 鏈湴 `gamma_gamma` 涓嶅唴缃?EBL model锛屽彧鎺ュ彈澶栭儴缁欏畾鐨?`tau_EBL` |
| `gammapy` | installed / EBL data not configured | adapter 浼氭娴?`EBLAbsorptionNormSpectralModel` 鏄惁鍙敤 | 瀹夎 package 涓嶇瓑浜?benchmark 鍙繍琛岋紱缂哄皯 `$GAMMAPY_DATA` 鏃跺繀椤绘爣涓?skipped |
| `JetSeT` | attempted / failed in current Python 3.13 Windows env | 鏆傛棤 adapter | 渚濊禆鏃?`scipy<=1.13.1`锛屽綋鍓嶇幆澧冮渶瑕佷粠婧愮爜缂栬瘧 scipy 鑰屽け璐?|
| `GAMERA` / `CRPropa` / cascade tools | not installed | 鍚庣画鍊欓€?| 鏇撮€傚悎 hadronic/cascade envelope锛屼笉搴旀贩鎴愭湰鍦板凡瀹屾垚瀹炵幇 |

鏂板杈撳嚭鏂囦欢锛?
- `benchmark_agnpy_local_sed_ratio.csv/png`锛氭湰鍦?synchrotron/SSC 涓?`agnpy` 鐨勫悓鍙傛暟 one-zone 瀵圭収銆?- `benchmark_ebltable_tau_curves.csv/png`锛欵BL optical depth 涓?attenuation envelope銆?- `benchmark_manifest.csv`锛氳褰?`gammapy` 鍥犳暟鎹湭閰嶇疆鑰?skipped锛屼互鍙?`agnpy`/`ebltable` 鐨?generated 鐘舵€併€?
瑙ｉ噴瑙勫垯锛?
1. `package-compatible` 灞傛墠瑕佹眰鐐瑰鐐规帴杩戝閮ㄥ簱銆?2. `teaching-reference` 鎴?`semi-analytic-one-zone` 灞傚厑璁镐笌澶栭儴搴撴湁绯荤粺宸紓锛屼絾 CSV 蹇呴』璇存槑宸紓鏉ヨ嚜 pitch-angle銆丏oppler銆佷綋瀵嗗害/鎬荤矑瀛愭暟銆乻eed photon geometry銆乪scape time銆佺Н鍒嗙綉鏍兼垨鎴潰鍙傛暟鍖栥€?3. 瀵?SSC銆丒BL銆乭adronic銆乧ascade 杩欑被閫氬父娌℃湁绠€鍗曢棴寮忕簿纭В鐨勮繃绋嬶紝瑕佷紭鍏堟瘮杈冭秼鍔裤€佸嘲浣嶃€佸彲姣旇兘娈点€佹暟閲忕骇鍜?convention锛岃€屼笉鏄亣瑁呮墍鏈夊簱蹇呴』缁欏嚭鍚屼竴鏉℃洸绾裤€?
## 10. v3 package-compatible parity 鏇存柊

鏈疆鎶娾€滈€愮偣涓€鑷粹€濋檺瀹氬湪 package-compatible 灞傦紝骞舵柊澧?`check_radiation_package_parity_v3.py` 浣滀负楠屾敹鍏ュ彛銆?
| 鏈哄埗 | package-compatible 鏈湴灞?| 澶栭儴 benchmark | 褰撳墠楠屾敹 |
| --- | --- | --- | --- |
| synchrotron | `naima_compat.py` / `agnpy_compat.py` | `naima.Synchrotron`, `agnpy.Synchrotron` | naima 鏁板€艰宸骇锛沘gnpy one-zone 灏忎簬 `2e-2 dex` |
| IC(CMB) | `naima_compat.py` | `naima.InverseCompton` | 鏁板€艰宸骇 |
| SSC | `agnpy_compat.py::synchrotron_self_compton_sed_agnpy_compatible_erg_cm2_s` | `agnpy.SynchrotronSelfCompton` | 灏忎簬 `2e-2 dex` |
| nonthermal bremsstrahlung | `naima_compat.py::nonthermal_bremsstrahlung_sed_naima_compatible_erg_cm2_s` | `naima.Bremsstrahlung` | 灏忎簬 `1e-3 dex`锛屾湁闄愬煙姣旇緝 |
| pp pion decay | `hadronic.py::pp_kafexhiu_lut_pion_decay_sed_erg_cm2_s` | `naima.PionDecay` Kafexhiu14 LUT | 灏忎簬 `1e-3 dex` |
| proton synchrotron | `hadronic.py::proton_synchrotron_sed_erg_cm2_s` | 鏈湴 fixed-point锛沘gnpy proton synch 鍊欓€?| 姝ｅ€笺€佺鍦哄搷搴斻€侀珮鑳?cutoff 鏈夐檺 |
| EBL attenuation | `gamma_gamma.py::ebl_attenuation_factor` | `ebltable` tau tables | `exp(-tau)` helper 閫愮偣涓€鑷?|

閲嶈杈圭晫锛歚package-compatible` 鏄负浜嗗鍒绘寚瀹氳蒋浠?convention锛屼笉浠ｈ〃璇剧▼鎺ㄥ鍙湁杩欎竴绉嶅啓娉曘€俙teaching-reference` 鑻ヤ笌 package-compatible 涓嶅悓锛屽繀椤诲悓鏃惰緭鍑哄樊寮傛潵婧愶紝鑰屼笉鏄妸鍏朵腑涓€涓潤榛樿鐩栨帀銆?
## 11. v3 package-compatible parity 鏇存柊锛堜腑鏂囨牎姝ｇ増锛?
鏈疆鎶娾€滈€愮偣涓€鑷粹€濋檺瀹氬湪 `package-compatible` 灞傦紝骞剁敤
`check_radiation_package_parity_v3.py` 浣滀负楠屾敹鍏ュ彛銆俙teaching-reference`
灞傚彲浠ヤ繚鐣欒绋嬫帹瀵煎舰寮忥紱濡傛灉瀹冨拰澶栭儴搴撲笉涓€鏍凤紝蹇呴』杈撳嚭宸紓鏉ユ簮銆?
| 鏈哄埗 | 鏈湴 package-compatible 灞?| 澶栭儴 benchmark | 褰撳墠楠屾敹 |
| --- | --- | --- | --- |
| synchrotron | `naima_compat.py` / `agnpy_compat.py` | `naima.Synchrotron`, `agnpy.Synchrotron` | naima 璇樊 `6.77e-14 dex`锛沘gnpy one-zone 璇樊 `4.34e-3 dex` |
| IC(CMB) | `naima_compat.py` | `naima.InverseCompton` | 璇樊 `1.05e-13 dex` |
| SSC | `agnpy_compat.py::synchrotron_self_compton_sed_agnpy_compatible_erg_cm2_s` | `agnpy.SynchrotronSelfCompton` | 璇樊 `8.69e-3 dex` |
| nonthermal bremsstrahlung | `naima_compat.py::nonthermal_bremsstrahlung_sed_naima_compatible_erg_cm2_s` | `naima.Bremsstrahlung` | 璇樊 `7.12e-4 dex` |
| pp pion decay | `hadronic.py::pp_kafexhiu_lut_pion_decay_sed_erg_cm2_s` | `naima.PionDecay` Kafexhiu14 LUT | 璇樊 `3.93e-4 dex` |
| proton synchrotron | `agnpy_compat.py::proton_synchrotron_sed_agnpy_compatible_erg_cm2_s` | `agnpy.ProtonSynchrotron` | 璇樊 `4.34e-4 dex` |
| EBL attenuation | `gamma_gamma.py::ebl_attenuation_factor` | `ebltable` tau tables | 缁欏畾 tau 鍚?`exp(-tau)` 閫愮偣涓€鑷?|

鍥惧儚瑙ｉ噴瑙?[08 v3 Package-Compatible Parity Report](08-v3-package-parity-report.md)銆?

## 12. Cooling / Angle-kernel v1 benchmark 边界

本轮新增 `radiation_cooling_angle_v1_checks.csv`，但它和 SED parity 的含义不同：

| 类别 | 本地状态 | 外部库状态 | 解释方式 |
| --- | --- | --- | --- |
| synchrotron cooling | production/local fixed-point | active adapters 不提供统一 cooling API | 用解析标度和文献固定点验证 |
| IC Thomson/KN cooling | Thomson production；KN envelope | naima 用于 SED，不作为 cooling API | KN envelope 只能说明 suppression trend |
| SSC cooling | teaching `Y P_syn` envelope | agnpy 用于 SSC SED parity | 不声称 self-consistent cooling feedback |
| gamma-gamma angle | 本地 isotropic angle integral | ebltable 提供传播 tau，不提供源内角核 | 本地角核与 EBL table 是不同层 |
| nonthermal brems loss | order-of-magnitude loss envelope | SED parity 用 naima；cooling API 未对齐 | 只能判断动力学重要性，不替代谱核 |
| pp/pγ/BH loss | pp loss envelope；pγ/BH threshold envelope | naima/GAMERA/SOPHIA 等按机制候选 | threshold/loss envelope 不是 spectrum/cascade |

因此，`production-parity` 目前仍主要指 SED/attenuation parity；cooling 和 angle-kernel 本轮多为 `local-fixed-point`、`teaching-only` 或 `external-unavailable`。后续若某个外部库提供明确 loss-rate API，才能升级为逐点 cooling parity。

