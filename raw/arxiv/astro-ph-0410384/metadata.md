---
title: "Two-Component Jet Models of Gamma-Ray Burst Sources"
source_type: arxiv-paper
arxiv: "astro-ph/0410384"
doi: "10.1086/430045"
arxiv_doi: "10.48550/arXiv.astro-ph/0410384"
url: "https://arxiv.org/abs/astro-ph/0410384"
pdf: "raw/arxiv/astro-ph-0410384/astro-ph-0410384.pdf"
source_url: "https://arxiv.org/e-print/astro-ph/0410384"
source_package: "raw/arxiv/astro-ph-0410384/astro-ph-0410384-source.tar.gz"
journal: "The Astrophysical Journal 626, 966-977 (2005)"
status: ingested
related_source:
  - "wiki/50_模型/grb模型/two-component-jet.md"
  - "wiki/40_综合比较/模型比较/two-component-grb-models.md"
---

# Two-Component Jet Models of Gamma-Ray Burst Sources

## Source identity

- Authors: Fang Peng, Arieh Königl, Jonathan Granot.
- Journal: The Astrophysical Journal 626, 966-977 (2005).
- arXiv: astro-ph/0410384.
- DOI: 10.1086/430045.
- arXiv DOI: 10.48550/arXiv.astro-ph/0410384.

## Local raw files

- PDF: `raw/arxiv/astro-ph-0410384/astro-ph-0410384.pdf`
- arXiv source package: `raw/arxiv/astro-ph-0410384/astro-ph-0410384-source.tar.gz`

## Source package figure candidates

- `f1.eps`: R-band afterglow light curve from a two-component jet, with narrow and wide component contributions.
- `f2.eps`: light-curve behavior as function of wide/narrow component geometry and timing.
- `f3.eps`: R-band light curve model for GRB 030329 parameters.

## Key extracted claims

- The model assumes two distinct outflow components: a narrow, highly relativistic component and a wider, moderately relativistic component.
- Narrow component: opening half-angle θ_j,n; initial Lorentz factor η_n ≳ 10^2; prompt gamma-ray emission originates from this component.
- Wide component: opening half-angle θ_j,w ≲ 3 θ_j,n; initial Lorentz factor η_w ~ 10; surrounds the narrow component.
- The paper calculates R-band afterglow light curves using a simple synchrotron emission model.
- For viewing angles θ_obs < θ_j,n, the wide component is negligible if its kinetic energy E_w is much smaller than E_n, as expected in the collapsar jet-breakout picture.
- If E_w/E_n > 1 while E_iso,w/E_iso,n remains <1, the narrow component dominates early afterglow and the wide component can take over after its deceleration time t_dec,w, typically ~0.1-1 d.
- If t_dec,w is comparable to the narrow component jet-break time t_jet,n, emergence of the wide component can mask the narrow-component jet break and lead to overestimates of gamma-ray energy and emission efficiency.
- The model is also applied to X-ray flash sources interpreted as GRB jets viewed outside the narrow component.
- The authors argue that neutron-rich hydromagnetic outflows may naturally produce repeated brightening episodes such as those observed in GRB 021004 and GRB 030329.

## Caveats

- This is a model paper, not an observational discovery paper; use it to define two-component jet phenomenology and predicted light-curve behavior.
- Numerical conditions and flux-ratio formulae depend on synchrotron assumptions, viewing angle, component energies, component opening angles, Lorentz factors, and circumburst density.
- GRB 030329 and GRB 021004 examples are model interpretations of observed brightening episodes and should be marked as such until their event-specific sources are ingested.
