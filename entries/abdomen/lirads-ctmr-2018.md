---
id: lirads-ctmr-2018
title: CT/MRI LI-RADS version 2018 — diagnostic algorithm for liver observations in patients at risk of HCC
type: classification
area: abdomen
modalities: [CT, MRI]
population: adults
source_version: "v2018"
status: draft
verified_against: "pending — migrated from Digitado-IA classificacoes.md (diagnostic table and references checked there on 2026-10-22); not yet re-read against the full text for radref"
verified_by: ""
verified_on: ""
sources: [lirads-ctmr-2018, acr-lirads-ctmr-core-2018]
supersedes: []
superseded_by: ""
related: [acr-incidental-liver-2017]
last_reviewed: 2026-11-05
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
  [lirads-ctmr-2018] [verify full exclusion list in the core document]

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
| LR-3 | Repeat or alternative imaging in 3–6 months | [lirads-ctmr-2018] |
| LR-4 | Multidisciplinary discussion; repeat/alternative imaging or biopsy | [lirads-ctmr-2018] |
| LR-5 | HCC diagnosis without biopsy; multidisciplinary discussion | [lirads-ctmr-2018] |

[verify LR-1/LR-2/LR-M/LR-TIV management wording against the core document]

## 5. Pitfalls

- Applying LI-RADS to patients outside the at-risk population (e.g. no cirrhosis and no
  chronic HBV).
- Using ancillary features to reach LR-5 (not allowed).
- Calling a 10–19 mm APHE observation with capsule only LR-5 (it is LR-4).

## 6. What the source does not say

- The diagnostic algorithm does not apply to ultrasound (see US LI-RADS, entry pending).
- It does not cover treatment response beyond the LR-TR algorithm (not summarized here).

## 7. Disagreements and newer versions

- ACR released an update of the **treatment response** algorithm (LR-TR) in 2024; according to
  Digitado-IA's notes, the **diagnostic** algorithm remains v2018. [verify on the ACR page]
- The ACR general incidental liver lesion white paper (`acr-incidental-liver-2017`) lists
  cirrhosis under "high risk"; LI-RADS is the specific system for that population.

## 8. How to cite

- Primary: `lirads-ctmr-2018`
- Core document: `acr-lirads-ctmr-core-2018`

## 9. Change log

| Date | Change | By |
|---|---|---|
| 2026-11-05 | Migrated from Digitado-IA `classificacoes.md` (house rules removed) | Claude |
