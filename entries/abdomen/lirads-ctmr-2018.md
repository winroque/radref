---
id: lirads-ctmr-2018
title: CT/MRI LI-RADS version 2018 — diagnostic algorithm for liver observations in patients at risk of HCC
type: classification
area: abdomen
modalities: [CT, MRI]
population: adults
source_version: "v2018"
status: draft
verified_against: "full-text PDFs read by Claude on 2026-11-11: Chernyak 2018 (Radiology) and the ACR CT/MRI LI-RADS v2018 Core (population, Diagnostic Table, management table, threshold growth, ancillary feature rules); 2024 treatment response cores consulted for version scope — awaiting radiologist sign-off"
verified_by: ""
verified_on: ""
sources: [lirads-ctmr-2018, acr-lirads-ctmr-core-2018]
supersedes: []
superseded_by: ""
related: [acr-incidental-liver-2017]
last_reviewed: 2026-11-12
---

# CT/MRI LI-RADS version 2018

> Standardized categories (LR-1 to LR-5, LR-M, LR-TIV) for liver observations on multiphase
> CT or MRI in patients at high risk of hepatocellular carcinoma (HCC). LR-5 allows a
> non-invasive diagnosis of HCC. [lirads-ctmr-2018]

## 1. Scope

- **Applies to:** patients with cirrhosis, chronic hepatitis B, or current/prior HCC.
  [lirads-ctmr-2018]
- **Does not apply to:** patients < 18 years; cirrhosis due to vascular disorders; congenital
  hepatic fibrosis. Outside scope, observations are described without a LI-RADS category.
  The core also lists cirrhosis due to a vascular disorder such as hereditary haemorrhagic
  telangiectasia, Budd-Chiari syndrome, chronic portal vein occlusion, cardiac congestion or
  diffuse nodular regenerative hyperplasia, and patients without the risk factors above.
  Requires **multiphase** CT or MRI. [acr-lirads-ctmr-core-2018]

## 2. Definitions

| Term | Definition | Source |
|---|---|---|
| Major features | Non-rim arterial phase hyperenhancement (APHE), non-peripheral "washout", enhancing "capsule", size, threshold growth | [lirads-ctmr-2018] |
| Threshold growth | Size increase ≥ 50% in ≤ 6 months | [lirads-ctmr-2018] |
| Ancillary features | Features that may adjust the category by **one** step up or down; cannot upgrade to LR-5 | [lirads-ctmr-2018] |

## 3. Criteria / categories

### Diagnostic table (LR-3 to LR-5)

| APHE | Size | No additional major feature | One additional | ≥ 2 additional | Source |
|---|---|---|---|---|---|
| No APHE or rim APHE | < 20 mm | LR-3 | LR-3 | LR-4 | [lirads-ctmr-2018] |
| No APHE or rim APHE | ≥ 20 mm | LR-3 | LR-4 | LR-4 | [lirads-ctmr-2018] |
| Non-rim APHE | < 10 mm | LR-3 | LR-4 | LR-4 | [lirads-ctmr-2018] |
| Non-rim APHE | 10–19 mm | LR-3 | LR-4 if capsule only; **LR-5** if washout or threshold growth | LR-5 | [lirads-ctmr-2018] |
| Non-rim APHE | ≥ 20 mm | LR-4 | LR-5 | LR-5 | [lirads-ctmr-2018] |

### Other categories

| Category | Meaning | Source |
|---|---|---|
| LR-1 | Definitely benign | [lirads-ctmr-2018] |
| LR-2 | Probably benign | [lirads-ctmr-2018] |
| LR-M | Probably or definitely malignant, not HCC-specific (e.g. rim APHE, peripheral washout, targetoid restriction) | [lirads-ctmr-2018] |
| LR-TIV | Tumour in vein | [lirads-ctmr-2018] |

## 4. Management

| Category | Usual management | Source |
|---|---|---|
| Negative (no observation) | Return to surveillance in 6 months | [acr-lirads-ctmr-core-2018] |
| LR-NC (not categorizable) | Repeat or alternative diagnostic imaging in ≤ 3 months | [acr-lirads-ctmr-core-2018] |
| LR-1 | Return to surveillance in 6 months | [acr-lirads-ctmr-core-2018] |
| LR-2 | Return to surveillance in 6 months; consider repeat diagnostic imaging in ≤ 6 months | [acr-lirads-ctmr-core-2018] |
| LR-3 | Repeat or alternative diagnostic imaging in 3–6 months | [acr-lirads-ctmr-core-2018] |
| LR-4 | Multidisciplinary discussion for tailored workup; may include biopsy | [acr-lirads-ctmr-core-2018] |
| LR-5 | HCC confirmed (no biopsy needed); multidisciplinary discussion for consensus management | [acr-lirads-ctmr-core-2018] |
| LR-M | Multidisciplinary discussion for tailored workup; often includes biopsy | [acr-lirads-ctmr-core-2018] |
| LR-TIV | Multidisciplinary discussion for tailored workup; may include biopsy | [acr-lirads-ctmr-core-2018] |

The core advises avoiding report language that compels biopsy. [acr-lirads-ctmr-core-2018]

## 5. Pitfalls

- Applying LI-RADS to patients outside the at-risk population (e.g. no cirrhosis and no
  chronic HBV).
- Using ancillary features to reach LR-5 (not allowed).
- Calling a 10–19 mm APHE observation with capsule only LR-5 (it is LR-4).
- When unsure whether a major feature is present, characterize it as **absent**.
  [acr-lirads-ctmr-core-2018]
- Categorizing lesions already proven by pathology (malignant, or benign non-hepatocellular such
  as haemangioma): the core says not to. [acr-lirads-ctmr-core-2018]
- Adjusting when ancillary features favouring malignancy and benignity coexist (do not adjust);
  ancillary features favouring malignancy upgrade to LR-4 at most. [acr-lirads-ctmr-core-2018]

## 6. What the source does not say

- The diagnostic algorithm does not apply to ultrasound (see `us-lirads-surveillance-2024`).
- It does not cover treatment response beyond the LR-TR algorithm (not summarized here).

## 7. Disagreements and newer versions

- ACR released **treatment response** algorithms in 2024 (separate cores for radiation-based
  and non-radiation locoregional therapy). Those cores still refer to the CT/MRI LI-RADS v2018
  reporting, i.e. the **diagnostic** algorithm remains v2018.
- The ACR general incidental liver lesion white paper (`acr-incidental-liver-2017`) lists
  cirrhosis under "high risk"; LI-RADS is the specific system for that population.

## 8. How to cite

- Primary: `lirads-ctmr-2018`
- Core document: `acr-lirads-ctmr-core-2018`

## 9. Change log

| Date | Change | By |
|---|---|---|
| 2026-11-05 | Migrated from Digitado-IA `classificacoes.md` (house rules removed) | Claude |
| 2026-11-11 | Checked against the article and the ACR v2018 core: full exclusion list, management for every category, version scope after the 2024 treatment-response cores; [verify] marks resolved | Claude |
| 2026-11-12 | Pre-check fixes: US LI-RADS cross-reference; proven-lesion and conflicting-AF rules from the core | Claude |
