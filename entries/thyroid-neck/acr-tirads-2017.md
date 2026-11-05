---
id: acr-tirads-2017
title: ACR Thyroid Imaging, Reporting and Data System (TI-RADS), 2017 white paper
type: classification
area: thyroid-neck
modalities: [US]
population: adults
source_version: "2017"
status: draft
verified_against: "pending — migrated from Digitado-IA classificacoes.md and scripts/tirads.py (point values and size thresholds checked there against the white paper); not yet re-read for radref"
verified_by: ""
verified_on: ""
sources: [acr-tirads-2017]
supersedes: []
superseded_by: ""
related: [acr-incidental-thyroid-2015]
last_reviewed: 2026-11-05
---

# ACR TI-RADS (2017)

> Point-based risk stratification of thyroid nodules on ultrasound. Points from five feature
> groups are added to give a level (TR1–TR5); the level and the nodule's maximum diameter
> determine whether fine-needle aspiration (FNA) or follow-up is recommended. [acr-tirads-2017]

## 1. Scope

- **Applies to:** thyroid nodules seen on dedicated thyroid ultrasound. [acr-tirads-2017]
- **Not a grading of the gland:** a thyroid without nodules is not given a TR level in practice
  (the system scores nodules). [verify how the white paper phrases this]
- Incidental nodules seen on CT/MRI/PET or on non-thyroid ultrasound are triaged first by the
  incidental thyroid nodule white paper (`acr-incidental-thyroid-2015`).

## 2. Definitions — points

Choose **one** option in each of composition, echogenicity, shape and margin; add **all**
that apply in echogenic foci. [acr-tirads-2017]

| Feature | Option | Points | Source |
|---|---|---|---|
| Composition | Cystic or almost completely cystic | 0 | [acr-tirads-2017] |
| | Spongiform | 0 | [acr-tirads-2017] |
| | Mixed cystic and solid | 1 | [acr-tirads-2017] |
| | Solid or almost completely solid | 2 | [acr-tirads-2017] |
| Echogenicity | Anechoic | 0 | [acr-tirads-2017] |
| | Hyperechoic or isoechoic | 1 | [acr-tirads-2017] |
| | Hypoechoic | 2 | [acr-tirads-2017] |
| | Very hypoechoic | 3 | [acr-tirads-2017] |
| Shape | Wider-than-tall | 0 | [acr-tirads-2017] |
| | Taller-than-wide | 3 | [acr-tirads-2017] |
| Margin | Smooth | 0 | [acr-tirads-2017] |
| | Ill-defined | 0 | [acr-tirads-2017] |
| | Lobulated or irregular | 2 | [acr-tirads-2017] |
| | Extra-thyroidal extension | 3 | [acr-tirads-2017] |
| Echogenic foci | None or large comet-tail artefacts | 0 | [acr-tirads-2017] |
| | Macrocalcifications | 1 | [acr-tirads-2017] |
| | Peripheral (rim) calcifications | 2 | [acr-tirads-2017] |
| | Punctate echogenic foci | 3 | [acr-tirads-2017] |

### Scoring rules

- Spongiform nodules receive no additional points from other groups.
- Mixed cystic and solid: score the predominant solid component.
- Composition cannot be determined because of calcification: 2 points.
- Echogenicity cannot be determined: 1 point.
- Margin cannot be determined: 0 points.
- Only TR1 nodules can score 0; any other nodule scores at least 2 (a mixed nodule gets 1 for
  composition plus at least 1 for the echogenicity of its solid component).

## 3. Criteria / categories

| Points | Level | Source |
|---|---|---|
| 0 | TR1 — benign | [acr-tirads-2017] |
| 2 | TR2 — not suspicious | [acr-tirads-2017] |
| 3 | TR3 — mildly suspicious | [acr-tirads-2017] |
| 4–6 | TR4 — moderately suspicious | [acr-tirads-2017] |
| ≥ 7 | TR5 — highly suspicious | [acr-tirads-2017] |

There is no TR0 and no sub-levels.

## 4. Management

| Level | FNA if maximum diameter | Follow-up if | Source |
|---|---|---|---|
| TR1 | No FNA | — | [acr-tirads-2017] |
| TR2 | No FNA | — | [acr-tirads-2017] |
| TR3 | ≥ 2.5 cm | ≥ 1.5 cm | [acr-tirads-2017] |
| TR4 | ≥ 1.5 cm | ≥ 1.0 cm | [acr-tirads-2017] |
| TR5 | ≥ 1.0 cm | ≥ 0.5 cm | [acr-tirads-2017] |

- TR5 nodules of 5–9 mm: the white paper refers to the discussion on papillary
  microcarcinoma; not an automatic recommendation. [acr-tirads-2017]
- Recommendations are guidance, not a standard; the decision to biopsy also weighs the
  referrer's and patient's preferences and patient factors. [acr-tirads-2017]

## 5. Pitfalls

- Scoring a nodule when one of the five feature groups was not described: the level is then
  undetermined.
- Adding spongiform points to other groups.
- Forgetting that echogenic foci points are cumulative.

## 6. What the source does not say

- It does not aim to detect every thyroid cancer: the size thresholds deliberately balance
  detection of clinically important cancers against biopsy of benign nodules and indolent
  cancers (overdiagnosis is a stated concern). [acr-tirads-2017]
- It does not give a category to a gland without nodules.

## 7. Disagreements and newer versions

- Other systems (ATA 2015, EU-TIRADS, K-TIRADS) use pattern-based categories and different FNA
  thresholds. Not summarized here. [verify before adding comparisons]

## 8. How to cite

- Primary: `acr-tirads-2017`
- Licence: the ACR TI-RADS chart and figures are ACR material; this entry summarizes points
  and thresholds only.

## 9. Change log

| Date | Change | By |
|---|---|---|
| 2026-11-05 | Migrated from Digitado-IA `classificacoes.md` (house rules removed) | Claude |
