---
id: liver-fat-ct-2018
title: Liver fat fraction estimated from unenhanced CT attenuation — Pickhardt 2018
type: reference-values
area: abdomen
modalities: [CT]
population: adults
source_version: "2018"
status: draft
verified_against: "full-text PDF (AJR 2018;211(3):W151–W157), read by Claude on 2026-11-11: Abstract, Materials and Methods (ROI and CT technique), Results, Figs. 1–4, Discussion, limitations — awaiting radiologist sign-off"
verified_by: ""
verified_on: ""
sources: [pickhardt-liver-fat-2018]
supersedes: []
superseded_by: ""
related: []
last_reviewed: 2026-11-11
---

# Liver fat fraction from unenhanced CT (Pickhardt 2018)

> Linear conversion of mean liver attenuation on **unenhanced 120-kV CT** (HU) into an
> estimated MRI proton density fat fraction (PDFF), derived from a phantom and a retrospective
> clinical cohort with CT and confounder-corrected chemical shift–encoded MRI.
> [pickhardt-liver-fat-2018]

## 1. Scope

- **Applies to:** unenhanced CT at **120 kV**. Contrast-enhanced CT was excluded from the study.
  [pickhardt-liver-fat-2018]
- **Derivation cohort:** 72 patients with 120-kV CT within 1 month of MRI PDFF (from 221
  patients with both exams, 2007–2017; single institution; GE 8- to 64-MDCT scanners).
  [pickhardt-liver-fat-2018]
- **Not established for:** other tube voltages (80, 100, 140 kV — too few data to derive
  equations), other vendors, or livers with iron overload. [pickhardt-liver-fat-2018]

## 2. Definitions

| Term | Definition | Source |
|---|---|---|
| PDFF | MRI proton density fat fraction (confounder-corrected chemical shift–encoded MRI), 0–100% | [pickhardt-liver-fat-2018] |
| ROI method | One large ROI (**1000 mm²**) in the **right hepatic lobe**, avoiding vessels, ducts, focal lesions and artefacts, co-registered with the MRI ROI; CT reconstructed 5 mm at 3-mm intervals | [pickhardt-liver-fat-2018] |
| Steatosis grades (MRI PDFF) used in the study | Mild 5–14%; moderate 14–28%; severe > 28% | [pickhardt-liver-fat-2018] |

## 3. Criteria / categories

| Formula | Source |
|---|---|
| **MRI PDFF (%) = −0.58 × CT attenuation (HU) + 38.2** (120 kV, CT within 1 month of MRI; r² = 0.828) | [pickhardt-liver-fat-2018] |

- Phantom: r² = 0.986, with slope and intercept very close to the clinical formula.
- Moderate steatosis (≥ 30% of hepatocytes with fat on histology) corresponds to about
  **14% PDFF** and **42 HU** on unenhanced CT, according to the authors' data.
- Worked values (arithmetic from the formula): 57 HU ≈ 5%; 42 HU ≈ 14%; 20 HU ≈ 27%.
  [pickhardt-liver-fat-2018]

## 4. Management

Not applicable. The authors propose reporting liver fat as a continuous percentage instead of
a binary attenuation threshold, and CT as an opportunistic screening tool that may select
patients for MRI PDFF follow-up. [pickhardt-liver-fat-2018]

## 5. Pitfalls

| Factor | Effect | Source |
|---|---|---|
| CT–MRI interval > 1 month | Correlation drops (r² 0.565; > 1 year r² 0.560) | [pickhardt-liver-fat-2018] |
| Tube voltage other than 120 kV | Correlation drops (r² 0.554); no separate equations | [pickhardt-liver-fat-2018] |
| **Iron overload** | Raises attenuation and masks steatosis: CT underestimated fat in all cases with significant iron overload (e.g. 60.4 HU → predicted 3.5% vs MRI 23.2%); attenuation ≥ 75 HU suggests haemochromatosis | [pickhardt-liver-fat-2018] |
| Low fat content | Human correlation weaker than phantom, especially at low fat concentrations | [pickhardt-liver-fat-2018] |

- Contrast-enhanced phases: out of scope (not studied).
- The estimate is a regression prediction, not a measurement.

## 6. What the source does not say

- No validated cut-off for "any steatosis" on CT; the 5% PDFF threshold is an MRI grading
  boundary, and the formula is least reliable at low fat content.
- No equations for kV other than 120, for dual-energy CT, or for contrast-enhanced CT.
- Effect of lesser degrees of hepatic iron was not assessed.

## 7. Disagreements and newer versions

- Older CT practice uses a binary unenhanced threshold of about 45–50 HU for moderate or
  greater steatosis (≈ 30% fat on histology); the authors' data place moderate steatosis at
  about 42 HU. [pickhardt-liver-fat-2018]

## 8. How to cite

- Primary: `pickhardt-liver-fat-2018`

## 9. Change log

| Date | Change | By |
|---|---|---|
| 2026-11-05 | Created from the formula in Digitado-IA `CLAUDE.md` (house rules removed) | Claude |
| 2026-11-11 | Rewritten from the full text: 120-kV restriction, ROI method, cohort, confounders, 42 HU/14% correspondence; [verify] marks resolved | Claude |
