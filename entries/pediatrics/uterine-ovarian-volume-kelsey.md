---
id: uterine-ovarian-volume-kelsey
title: Normative uterine (Kelsey 2016) and ovarian (Kelsey 2013) volume by age
type: reference-values
area: pediatrics
modalities: [US]
population: all
source_version: "2013 (ovary); 2016 (uterus)"
status: draft
verified_against: "pending — migrated from Digitado-IA pediatria.md (uterine table and model checked there against Kelsey 2016 Table 5 for ages 9–13); not yet re-read for radref"
verified_by: ""
verified_on: ""
sources: [kelsey-uterus-2016, kelsey-ovary-2013]
supersedes: []
superseded_by: ""
related: [pcom-2023]
last_reviewed: 2026-11-05
---

# Uterine and ovarian volume by age (Kelsey)

> Normative models of uterine volume (birth to 40 years; n = 1,418; r² = 0.84) and ovarian
> volume (birth to 82 years; n = 59,470; r² = 0.69) by **chronological age**, from pooled
> ultrasound data. [kelsey-uterus-2016; kelsey-ovary-2013]

## 1. Scope

- **Applies to:** comparison of a measured uterine or ovarian volume with age-specific norms.
- **Limitation stated by the authors:** the models are by chronological age, not pubertal
  stage. [kelsey-uterus-2016] [verify wording]
- Uterine model censored at **40 years** (only 2 data points above). [kelsey-uterus-2016]

## 2. Definitions

| Term | Definition | Source |
|---|---|---|
| Uterine volume | Modified ellipsoid with factor **0.5** (not 0.523; difference 4.6%) | [kelsey-uterus-2016] |
| Ovarian volume | Per ovary, factor **π/6** | [kelsey-ovary-2013] |

## 3. Criteria / categories

### Uterus — volume (cm³) by age (years)

| Age | P2.5 | P16 | P50 | P84 | P97.5 | Source |
|---|---|---|---|---|---|---|
| 6 | 0 | 0.6 | 1.7 | 3.6 | 6.7 | [kelsey-uterus-2016, Table 5] |
| 7 | 0 | 0.6 | 1.7 | 3.7 | 6.9 | [kelsey-uterus-2016, Table 5] |
| 8 | 0 | 0.7 | 1.8 | 3.9 | 7.2 | [kelsey-uterus-2016, Table 5] |
| 9 | 0.1 | 0.8 | 2.1 | 4.4 | 8.0 | [kelsey-uterus-2016, Table 5] |
| 10 | 0.4 | 1.3 | 3.0 | 5.9 | 10.5 | [kelsey-uterus-2016, Table 5] |
| 11 | 1.3 | 2.8 | 5.5 | 10.2 | 17.8 | [kelsey-uterus-2016, Table 5] |
| 12 | 3.6 | 6.7 | 12.2 | 21.6 | 37.0 | [kelsey-uterus-2016, Table 5] |
| 13 | 7.8 | 13.8 | 24.4 | 42.6 | 72.3 | [kelsey-uterus-2016, Table 5] |
| 14 | 12.3 | 21.3 | 37.2 | 64.5 | 109.0 | [kelsey-uterus-2016, Table 5] |
| 15 | 15.0 | 25.8 | 44.9 | 77.8 | 131.2 | [kelsey-uterus-2016, Table 5] |
| 16 | 16.1 | 27.7 | 48.2 | 83.3 | 140.5 | [kelsey-uterus-2016, Table 5] |
| 17 | 16.5 | 28.3 | 49.3 | 85.2 | 143.7 | [kelsey-uterus-2016, Table 5] |
| 18 | 16.7 | 28.6 | 49.8 | 86.1 | 145.3 | [kelsey-uterus-2016, Table 5] |

Continuous model (ten-parameter rational function, x = age in years, UV = uterine volume):

```
log10(UV + 1) = (a + c·x + e·x² + g·x³ + i·x⁴) / (1 + b·x + d·x² + f·x³ + h·x⁴ + j·x⁵)
a = 0.217809   b = 0.4488971   c = 0.2611778   d = -0.0992615   e = -0.0390802
f = 0.0058979  g = 0.000399    h = -0.0001055  i = 0.000102     j = 0.0000015
```

Check (Digitado-IA): returns 3.10 at 10 years (table 3.0), 5.53 at 11 (5.5), 12.33 at 12 (12.2).
[kelsey-uterus-2016]

### Ovary — volume per ovary (mL) by age (years)

| Age | −2 SD | −1 SD | Mean | +1 SD | +2 SD | Source |
|---|---|---|---|---|---|---|
| 0 | 0.0 | 0.0 | 0.2 | 0.5 | 0.8 | [kelsey-ovary-2013] |
| 2 | 0.1 | 0.4 | 0.7 | 1.0 | 1.5 | [kelsey-ovary-2013] |
| 4 | 0.3 | 0.6 | 0.9 | 1.3 | 1.8 | [kelsey-ovary-2013] |
| 6 | 0.5 | 0.8 | 1.2 | 1.7 | 2.3 | [kelsey-ovary-2013] |
| 8 | 0.8 | 1.2 | 1.7 | 2.3 | 3.0 | [kelsey-ovary-2013] |
| 10 | 1.3 | 1.9 | 2.5 | 3.3 | 4.3 | [kelsey-ovary-2013] |
| 12 | 2.1 | 2.8 | 3.7 | 4.7 | 6.0 | [kelsey-ovary-2013] |
| 14 | 3.0 | 3.9 | 5.0 | 6.4 | 8.0 | [kelsey-ovary-2013] |
| 16 | 3.9 | 5.0 | 6.4 | 8.0 | 10.0 | [kelsey-ovary-2013] |
| 18 | 4.5 | 5.8 | 7.3 | 9.2 | 11.4 | [kelsey-ovary-2013] |
| 20 | 4.8 | 6.1 | 7.7 | 9.6 | 12.0 | [kelsey-ovary-2013] |

[verify which table/figure of Kelsey 2013 these values come from]

## 4. Management

Not applicable (reference values).

## 5. Pitfalls

- **Do not use the degree-14 polynomial published for the ovary:** its coefficients have 3
  significant figures and the curve diverges above 14 years (returns 3.6 mL at 20 years vs 7.7
  in the table; negative at 30). Interpolate in the table instead.
- Mixing volume factors (0.5, 0.523, π/6) between measurement and reference.
- Neonatal uterus is larger than prepubertal (maternal oestrogen); norms are not monotonic in
  the first months. [verify source]

## 6. What the source does not say

- It does not define pathology (e.g. precocious puberty) by volume alone.

## 7. Disagreements and newer versions

- Older tables (Orsini; Cohen-Shapiro) are superseded in practice by these larger pooled
  models. [verify]

## 8. How to cite

- Uterus: `kelsey-uterus-2016`
- Ovary: `kelsey-ovary-2013`

## 9. Change log

| Date | Change | By |
|---|---|---|
| 2026-11-05 | Migrated from Digitado-IA `pediatria.md` (Uterus and ovary section; house rules removed) | Claude |
