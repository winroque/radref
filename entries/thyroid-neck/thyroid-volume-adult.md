---
id: thyroid-volume-adult
title: Adult thyroid volume — the 18/25 mL limits, individualized reference equations (Ittermann 2025) and the ellipsoid correction factor (Shabana 2006)
type: reference-values
area: thyroid-neck
modalities: [US]
population: adults
source_version: "Ittermann 2025; Shabana 2006"
status: verified
verified_against: "full texts read by Claude on 2026-11-12: Ittermann 2025 (Eur J Endocrinol 2025;192:728–36 — abstract, methods, results, equations checked on the rendered page, limitations) and Shabana 2006 (AJR 2006;186:234–6 — whole text)"
verified_by: ""
verified_on: "2026-11-25"
sources: [ittermann-thyroid-volume-2025, shabana-thyroid-factor-2006]
supersedes: []
superseded_by: ""
related: [thyroid-volume-children-who-2004, acr-tirads-2017]
last_reviewed: 2026-11-12
---

# Adult thyroid volume

> The usual limits (**> 18 mL women, > 25 mL men**) come from Gutekunst 1988 (mean + 3 SD,
> method never detailed) and ignore age, height and weight. In 8,606 thyroid-healthy German
> adults the 95th percentile was **38.7 mL (men) and 28.6 mL (women)**; in the total study population
> (11,549) the old limits labelled 34% as "goitre", the individualized equations 7%. [ittermann-thyroid-volume-2025]

## 1. Scope

- **Ittermann:** three population cohorts (SHIP-START, SHIP-TREND, KORA-F4), 20–84 years,
  historically iodine-deficient Germany; healthy subset after excluding thyroid disease,
  treatment, abnormal TSH and pregnancy. Equations are meant for regions with similar iodine
  status. [ittermann-thyroid-volume-2025]
- **Shabana:** 19 adults (38 lobes) with normal thyroids on MDCT; ellipsoid diameters measured on
  CT and compared with automated CT volumetry. [shabana-thyroid-factor-2006]

## 2. Definitions

| Term | Definition | Source |
|---|---|---|
| Lobe volume (Ittermann) | length × width × depth × **0.479**, lobes summed | [ittermann-thyroid-volume-2025] |
| Correction factor | π/6 = 0.524 (ellipsoid); 0.479 adopted by WHO from Brunn's cadaver study | [shabana-thyroid-factor-2006] |

## 3. Criteria / categories

### Individualized upper reference limits (95th percentile, mL)

- **Men:** 9.066889 − 207.886 × (1/√age) + 0.31143 × height (cm) + 0.0472153 × weight (kg)
- **Women:** 0.049582 + 0.0024958 × age² + 0.0486403 × height (cm) + 0.1881983 × weight (kg)
- BSA versions: men 37.64908 − 181.379 × (1/√age) + 13.07982 × BSA; women −6.882714 +
  0.0025558 × age² + 15.88545 × BSA (goitre prevalence 7.4% with these).
  [ittermann-thyroid-volume-2025]

Example (computed by Claude from the equations): man 50 y, 180 cm, 80 kg → ≈ 39 mL; woman
50 y, 165 cm, 70 kg → ≈ 27 mL.

### Correction factor

- Volumes with 0.524 did not differ from CT volumetry (p = 0.748); volumes with 0.479 did
  (p = 0.007 in the text; Fig. 3 shows p = 0.01; 0.479 < 0.524, so it underestimates). Factors 0.494–0.554 were acceptable; the authors propose 0.529.
  [shabana-thyroid-factor-2006]

## 4. Management

- Not addressed. Goitre-related symptoms were similar between those classified by the old and the
  new limits; the authors state that a volume above the reference without symptoms, nodules or
  functional change has no clinical relevance. [ittermann-thyroid-volume-2025]
- Age-band limits (Figs. 6–7): 20–29 years 22.6 mL women / 27.2 mL men; 70–81 years 35.7 / 43.8
  mL. Volumes > 100 mL were excluded from the reference sample. [ittermann-thyroid-volume-2025]

## 5. Pitfalls

- Comparing a volume computed with 0.524 against limits built with 0.479 (≈ 9% inflation).
- Applying German (formerly iodine-deficient) limits to an iodine-sufficient population: the
  authors say they need evaluation elsewhere; a Chinese iodine-replete study found limits even
  lower than Gutekunst's. [ittermann-thyroid-volume-2025]

## 6. What the source does not say

- No Brazilian adult reference values.
- Shabana's diameters were measured on CT, not ultrasound; n = 19.

## 7. Disagreements and newer versions

- WHO convention 0.479 (Brunn 1981) vs Shabana's CT validation favouring 0.524–0.529.
- Gutekunst 1988 (Dtsch Med Wochenschr 1988;113:1109–12, doi 10.1055/s-2008-1067777) is the
  origin of 18/25 mL, as cited by Ittermann; not read for radref.

## 8. How to cite

- Upper limits: `ittermann-thyroid-volume-2025`; factor: `shabana-thyroid-factor-2006`

## 9. Change log

| Date | Change | By |
|---|---|---|
| 2026-11-12 | Created from the full texts | Claude |
| 2026-11-12 | Pre-check fixes: 34%/7% refer to the total population (11,549); p 0.007 vs 0.01 (Fig. 3); clinical relevance statement; age-band limits; > 100 mL exclusion | Claude |
