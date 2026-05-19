# Laskar LT photometry power-law sanity check

验证对象：Liverpool Telescope optical AB magnitudes fitted with a single per-filter power-law decay.

模型：`F_nu(t) proportional to t^-alpha`, so `m_AB(t) = m_ref + 2.5 alpha log10(t / 1 day)`.

Input: `reproduce/grb/events/grb_221009a/data/laskar_lt_photometry.csv`
Output: `reproduce/grb/events/grb_221009a/outputs/laskar_lt_powerlaw_fit.csv`

Caveat: this is a phenomenological sanity check only. The input table is not corrected for Milky Way extinction, host extinction, or host-galaxy light. It does not model color evolution, spectral breaks, supernova/host contamination, or multi-component afterglow physics.

## Results

| filter | n | alpha | alpha_err | chi2/dof |
| --- | ---: | ---: | ---: | ---: |
| g | 7 | 1.25084 | 0.0331168 | 3.24818 |
| i | 22 | 1.32988 | 0.00361522 | 11.8989 |
| r | 22 | 1.33349 | 0.00637134 | 2.4627 |
| z | 19 | 1.31623 | 0.00379508 | 18.1095 |

人工检查：待用户验证。

下一步：加入 extinction policy，把 AB mag 转为 flux density，并与 radio / X-ray 数据做 first-pass multi-band comparison。
