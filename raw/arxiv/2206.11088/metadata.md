---
title: "The Structure of Gamma Ray Burst Jets"
source_type: arxiv-review
arxiv: "2206.11088"
doi: null
arxiv_doi: "10.48550/arXiv.2206.11088"
url: "https://arxiv.org/abs/2206.11088"
pdf: "raw/arxiv/2206.11088/2206.11088.pdf"
source_url: "https://arxiv.org/e-print/2206.11088"
source_package: "raw/arxiv/2206.11088/2206.11088-source.tar.gz"
status: ingested
last_updated: 2026-05-10
related_source:
  - "wiki/50_模型/grb模型/two-component-jet.md"
  - "wiki/50_模型/grb模型/afterglow-dynamics.md"
  - "wiki/40_综合比较/模型比较/two-component-grb-models.md"
  - "wiki/00_总览/术语表.md"
  - "wiki_textbook/grb-afterglow/公式索引.md"
  - "wiki_textbook/grb-afterglow/来源脉络.md"
---

# The Structure of Gamma Ray Burst Jets

## Citation

- Authors: Om Sharan Salafia and Giancarlo Ghirlanda.
- Title: "The Structure of Gamma Ray Burst Jets".
- arXiv: 2206.11088.
- arXiv DOI: 10.48550/arXiv.2206.11088.
- Source package: `raw/arxiv/2206.11088/2206.11088-source.tar.gz`.
- Local PDF: `raw/arxiv/2206.11088/2206.11088.pdf`.

## Source type

Review / pedagogical source for GRB jet structure, prompt / afterglow viewing-angle effects, luminosity function implications, and GW170817 / GRB170817A as an off-axis structured-jet test bed.

## Key extracted claims

1. Due to relativistic bulk motion, jet structure and orientation strongly affect how GRBs appear to observers.
2. The review summarizes two decades of GRB jet-structure work, from universal structured jet ideas to central-engine and progenitor-interaction processes that shape jet structure.
3. At fixed time, assuming axisymmetry and radial expansion, full jet structure may be described by functions of radius and polar angle including four-velocity, comoving density, enthalpy and magnetization.
4. When radial structure is not central and the focus is kinetic energy, a commonly used angular description uses kinetic energy per unit solid angle dE/dΩ(θ,t) and average Lorentz factor Γ(θ,t).
5. Jet structure evolves through launch, propagation / cocoon formation / breakout, free expansion, external shock deceleration, lateral spreading and non-relativistic transition; no single definition is universally appropriate for all applications.
6. Simulations generally find a narrow core with approximately uniform Lorentz factor and energy density, surrounded by wider wings / cocoon-dominated material where Lorentz factor and energy density decrease with angle.
7. Structured jets imprint viewing-angle dependence on Eiso, Epeak, Liso, light curves, luminosity functions, and afterglow image / centroid evolution.
8. For off-core observers, early afterglow can be dominated by material near the line of sight; later emission can become progressively dominated by material closer to the jet axis.
9. GW170817 / GRB170817A made structured jets a key test case: light curves alone left degeneracies with quasi-spherical outflows, while VLBI centroid motion and compact image size favored an off-axis structured jet scenario.
10. The review emphasizes that the field is active and fast-evolving; structured-jet reconstruction requires high-cadence multiwavelength data and VLBI can break degeneracies.

## Formula candidates

- Angular kinetic energy profile:

```tex
\frac{\mathrm{d}E}{\mathrm{d}\Omega}(\theta,t)=\int_0^\infty (\Gamma(r,\theta,t)-1)\Gamma(r,\theta,t)\rho'(r,\theta,t)c^2 r^2\mathrm{d}r
```

- Average Lorentz factor profile:

```tex
\Gamma(\theta,t)=\left(\frac{\mathrm{d}E}{\mathrm{d}\Omega}\right)^{-1}\int_0^\infty (\Gamma(r,\theta,t)-1)\Gamma^2(r,\theta,t)\rho'(r,\theta,t)c^2 r^2\mathrm{d}r
```

- Viewing-angle isotropic-equivalent energy:

```tex
E_\mathrm{iso}(\theta_\mathrm{v}) = \int_0^{2\pi}\mathrm{d}\phi\int_0^{\pi/2}\sin\theta\,\mathrm{d}\theta\,\frac{\delta^3(\theta,\phi,\theta_\mathrm{v})}{\Gamma(\theta)}\eta_\gamma(\theta)\frac{\mathrm{d}E}{\mathrm{d}\Omega}(\theta)
```

## Figure candidates

Source package includes `figures/` files useful for later provenance-checked figure indexing, including `Eiso_struct_examples.pdf`, `Gottlieb22_GRMHD.pdf`, `LF.pdf`, `offaxis-sj-examples.pdf`, `GRB170817A_afterglow.pdf`, `jet_cocoon_images.pdf`, and `GRB170817_VLBI_image.pdf`.

## Ingest notes

- This source is a review and should be used to define the model taxonomy and source-priority context, not as an event-specific data source except where it summarizes GW170817 / GRB170817A literature.
- Formula content belongs primarily in `wiki_textbook/` or model-theory pages; ordinary event pages should link to those derivation chains rather than duplicate derivations.
- DOI was not found in the TeX metadata during this ingest; use arXiv identifier unless a journal DOI is independently verified later.
