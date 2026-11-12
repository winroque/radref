---
id: birads-2025
title: ACR BI-RADS v2025 — assessment categories and main changes from the 5th edition
type: classification
area: breast
modalities: [MG, US, MRI]
population: adults
source_version: "v2025"
status: draft
verified_against: "Minichetti 2026 full text (AJR, Tables 1–2 and text) read by Claude on 2026-11-11; ACR What's New (Nov 2025), Schijf & Smithuis 2026 (mammography and US pages, text only), UNICAMP Dr. Pixel (US app) and Ndirangu 2026 (PDF supplied by the radiologist) read on 2026-11-12; the v2025 manual body was not read by Claude (eBook terms forbid AI analysis) — category 0 and vascular-calcification wording checked in the manual by the radiologist on 2026-11-12 — awaiting radiologist sign-off"
verified_by: ""
verified_on: ""
sources: [acr-birads-2025, acr-birads-2025-whats-new, minichetti-birads-2026, schijf-birads-mg-2026, schijf-birads-us-2026, unicamp-birads-us-2025, ndirangu-bac-2026]
supersedes: []
superseded_by: ""
related: []
last_reviewed: 2026-11-12
---

# ACR BI-RADS v2025

> BI-RADS v2025 extends the 5th edition (2013). The "Atlas" became a "Manual" (to reflect the
> extent and variety of content), versioning changed from edition numbers to the year of
> publication to align with the other ACR RADS, and contrast-enhanced mammography (CEM) is an
> intrinsic section rather than a supplement. [acr-birads-2025-whats-new] This entry is a **summary** of assessment
> categories and of the changes that affect reporting; it does not reproduce the lexicon,
> which is proprietary. [acr-birads-2025; minichetti-birads-2026]

## 1. Scope

- **Applies to:** mammography (including tomosynthesis), breast ultrasound, breast MRI and CEM
  (the radref schema has no CEM modality value; CEM is listed under MG).
- **Not covered here:** the full lexicon, audit section and report templates (see the manual).

## 2. Definitions

Selected changes in v2025, from Minichetti 2026, the ACR What's New table and the Schijf & Smithuis summaries.

| Topic | v2025 change | Source |
|---|---|---|
| Report structure | Structured clinical indication categories (screening, diagnostic workup, known cancer); comparison with priors placed **before** technique; tissue composition and technique/acquisition as dedicated sections | [minichetti-birads-2026, Table 1] |
| Tissue composition | Breast density remains the core element for mammography and CEM; fibroglandular tissue (FGT) for MRI; **glandular tissue component (GTC)** introduced for US, in four grades — minimal < 25%, mild 25–49%, moderate 50–74%, marked ≥ 75% of the fibroglandular tissue [schijf-birads-us-2026] — which can be simplified to low/high | [minichetti-birads-2026] |
| Lesion location | Standardized across modalities: laterality → quadrant and/or clock face → distance from nipple (whole cm) and/or depth; DBT slice number recommended; on US also the tissue layer | [minichetti-birads-2026] |
| Shape | **"Lobulated"** reintroduced as a shape descriptor across modalities, replacing "lobular" | [minichetti-birads-2026, Table 1] |
| Margin | **"Microlobulated" removed from mammography, MRI and CEM** (replaced by "indistinct"); it **remains in the US lexicon** (US non-circumscribed margins: indistinct, microlobulated, angular, spiculated) | [minichetti-birads-2026; schijf-birads-us-2026] |
| DBT | A mass may be defined on a **single DBT projection**; when margins are obscured on DM but circumscribed on DBT, classify by the DBT appearance | [minichetti-birads-2026, Table 2] |
| MG calcifications (typically benign) | "Popcorn-like" and "dystrophic" merged into **"coarse"**; "punctate" replaced by **"round"**; "milk of calcium" replaced by **"layering"**; vascular calcifications **should** be reported (cardiovascular risk) — manual wording checked by the radiologist on 2026-11-12 [acr-birads-2025]; Minichetti's text says "may" and its Table 2 "should". No formal guideline yet defines BAC grading or follow-up; reporting is inconsistent (41–62% of radiologists report it routinely; 96% of surveyed women want it disclosed) [ndirangu-bac-2026] | [minichetti-birads-2026, Table 2] |
| MG asymmetry | Descriptor **"developing asymmetry" removed**; interval change still matters | [minichetti-birads-2026, Table 2] |
| Dilated ducts | New term "multiple dilated ducts" (typically benign); a true **solitary dilated duct** (tubular/branching structure > 5 mm from the nipple) in an asymptomatic patient without associated suspicious findings may now be category 2 (Minichetti); the ACR and Schijf say only that it "can be considered benign" when there are no associated clinical or imaging findings; the ACR adds that a solitary dilated duct on a baseline exam, in a symptomatic woman or with other suspicious features should prompt additional evaluation and possible tissue diagnosis [acr-birads-2025-whats-new] (previously usually 4A) | [minichetti-birads-2026, Table 2] |
| US composition | "Complex cystic and solid" replaced by **"mixed solid and cystic"**; the solid component determines assessment | [minichetti-birads-2026, Table 2] |
| US posterior features | **"Combined pattern" removed**; "shadowing" prioritized when it coexists with enhancement | [minichetti-birads-2026, Table 2] |
| US nonmass lesion | New finding: visible in three dimensions, different from surrounding tissue, without definable shape or margins; described by distribution, echotexture and posterior features; reported malignancy rates ~10–54%, above the probably-benign threshold, so consider sampling (Schijf: "biopsy recommended if PPV > 2%") when suspicious features (linear/segmental distribution, shadowing, duct changes, calcifications), a cross-modality correlate or symptoms are present | [minichetti-birads-2026, Table 2; text] |
| US perilesional features | **Echogenic pseudocapsule** (thin, uniform rim around a circumscribed mass; typically benign) and **echogenic rind** (thick, irregular band; associated with malignancy, also seen in e.g. fat necrosis; **include in the lesion size**) | [minichetti-birads-2026] |
| Lymph nodes | Separate reporting category: assessed by morphology (cortex, hilum, shape, change, vascularity); stations follow TNM (intramammary, axillary levels I–III by the pectoralis minor, internal mammary, supraclavicular); Node-RADS not incorporated | [minichetti-birads-2026, Tables 1–2] |
| MG calcifications (suspicious) | New PPV table by **morphology**; the risk-by-distribution table removed. A fat-containing mass does not exclude malignancy; architectural distortion on DBT has lower PPV | [minichetti-birads-2026] |
| MRI | "Focus" removed (findings ≤ 5 mm become mass or non-mass enhancement); minimal BPE includes "no enhancement"; "thick rim enhancement" replaces "rim enhancement"; T2 signal (hyper vs not, relative to lymph node) as adjunct descriptor; peritumoral oedema; early post-contrast phase at ~60–120 s; abbreviated protocol recognized; DWI outside the lexicon | [minichetti-birads-2026] |
| CEM | "Multiple regions" removed from non-mass enhancement; "invasion" of nipple/skin becomes "involvement" | [minichetti-birads-2026] |
| Audit | Category 0 is temporary and excluded; the final 1–5 assessment counts; positive/negative defined by clinical indication; specific audit for preoperative MRI | [minichetti-birads-2026] |
| US calcifications | Macro- vs microcalcifications, described by anatomic context (in or outside a mass/nonmass lesion; within a duct) | [minichetti-birads-2026, Table 2] |

## 3. Criteria / categories

| Category | Meaning | Source |
|---|---|---|
| 0 | Incomplete — two scenarios distinguished: **need for additional imaging evaluation** and **need for comparison with prior examinations**; at **screening**, category 0 also applies to a suspicious finding that needs diagnostic workup (manual checked by the radiologist on 2026-11-12; Minichetti says the opposite — see §7) | [acr-birads-2025; schijf-birads-mg-2026] |
| 1 | Negative (no findings) [schijf-birads-mg-2026]; likelihood of malignancy ~0% (US teaching app) [unicamp-birads-us-2025] | secondary summaries |
| 2 | Benign [schijf-birads-mg-2026]; ~0% (US teaching app) [unicamp-birads-us-2025] | secondary summaries |
| 3 | Probably benign; likelihood of malignancy > 0 to ≤ 2% (US teaching app) | [unicamp-birads-us-2025] |
| 4 | Suspicious: 4A > 2 to ≤ 10%, 4B > 10 to ≤ 50%, 4C > 50 to < 95% (US teaching app) [unicamp-birads-us-2025]; subdivision 4A/4B/4C — **newly introduced for MRI** in v2025 (reported MRI PPVs: 4A 2.5–14.2%, 4B 21.4–41.2%, 4C 77.2–83.3%) | [minichetti-birads-2026] |
| 5 | Highly suggestive of malignancy; ≥ 95% (US teaching app) [unicamp-birads-us-2025]; on mammography "no single mammographic feature confers a > 95% likelihood of malignancy" [schijf-birads-mg-2026] | secondary summaries |
| 6 | Known biopsy-proven malignancy | [acr-birads-2025-whats-new] |

> Categories 1–5 and their management rest on open secondary summaries of the v2025 manual
> (Schijf & Smithuis 2026; UNICAMP Dr. Pixel, based on the ACR 2025 edition) and were not read
> in the manual by Claude (its eBook terms forbid AI analysis). The category 0 wording was
> checked in the manual by the radiologist; category 6 rests on the ACR What's New.

## 4. Management

| Category | Recommendation | Source |
|---|---|---|
| 0 | Additional imaging, or comparison with prior images (state which; wording follows the 2024 FDA MQSA amendments: "Need Additional Imaging Evaluation" / "Need Prior Imaging for Comparison"); at screening this includes a suspicious finding needing diagnostic workup (manual, checked by the radiologist) | [acr-birads-2025-whats-new; acr-birads-2025] |
| 1–2 | Continue or resume screening at the appropriate interval | [schijf-birads-mg-2026] |
| 3 | Short-interval follow-up; imaging at 6, 12 and 24 months "may be appropriate" [schijf-birads-mg-2026]; UNICAMP phrases it as 6-month follow-up while stability is < 12 months, then annual [unicamp-birads-us-2025] | secondary summaries |
| 4–5 | Biopsy, stating the recommended method (stereotactic, US- or MR-guided) | [schijf-birads-mg-2026] |
| 6 | Management wording changed from "surgical excision when clinically appropriate" to "clinical follow-up with surgeon and/or oncologist, and definitive local therapy (usually surgery) when clinically appropriate", recognizing non-surgical definitive therapies [acr-birads-2025-whats-new]. Biopsy-proven malignancy before definitive local therapy (usually surgery), including during neoadjuvant treatment monitoring even with complete imaging response; timing and type of treatment decided by the multidisciplinary team | [minichetti-birads-2026] |

- MRI, category 6 ("additional close findings", ACFs): additional contiguous or closely adjacent findings with similar morphology
  may be included in category 6 (no separate category) when they are **within 2 cm** of the
  index malignancy, increase total disease extent by **≤ 2 cm**, and are not expected to alter
  management; report their extent and relation to the known cancer. [minichetti-birads-2026;
  acr-birads-2025-whats-new]
- Ablation and active surveillance of low-risk DCIS are not yet incorporated into BI-RADS.
  [minichetti-birads-2026]
- Audit (What's New): a positive screening exam is the acquisition of any images beyond the
  standard screening protocol, in any modality; "cancer" now includes pleomorphic or florid LCIS;
  outcomes of initial category 3 assessments join the basic audit. [acr-birads-2025-whats-new]

## 5. Pitfalls

- Category 0 without saying which of the two v2025 variants applies.
- Measuring a mass with an echogenic rind without including the rind.
- Using "microlobulated" as a margin on mammography, MRI or CEM (removed there; still valid
  on US), or confusing "lobulated" (shape) with "indistinct" (margin).

## 6. What the source does not say

- This entry does not reproduce the lexicon definitions; consult the manual for exact wording.
- The summaries used here are secondary reviews of the manual (Minichetti, Schijf & Smithuis,
  UNICAMP) plus the ACR What's New table; exact lexicon definitions and
  any transition guidance must be taken from the ACR manual.

## 7. Disagreements and newer versions

- **Category 0 with a suspicious finding:** Minichetti 2026 says category 0 should not be used
  when a finding is already suspicious (assign 4 or 5 without delay); Schijf 2026 (mammography)
  describes category 0 in screening as used for any abnormality "even if suspicious" that needs
  diagnostic workup. The manual agrees with Schijf: category 0 applies to suspicious findings
  (checked by the radiologist on 2026-11-12). Minichetti does not qualify its statement by
  setting; the disagreement stands. [acr-birads-2025; minichetti-birads-2026; schijf-birads-mg-2026]

- v2025 supersedes the 5th edition (2013). Other reviews of the v2025 changes exist
  (e.g. Song 2026, Ultrasonography; Arenas Rivera 2026, Radiología) — not yet added.

## 8. How to cite

- Primary: `acr-birads-2025` (proprietary manual; summarize only)
- Secondary: `acr-birads-2025-whats-new` (ACR, public), `minichetti-birads-2026`,
  `schijf-birads-mg-2026`, `schijf-birads-us-2026`, `unicamp-birads-us-2025`; BAC context:
  `ndirangu-bac-2026`

## 9. Change log

| Date | Change | By |
|---|---|---|
| 2026-11-05 | Migrated from Digitado-IA `classificacoes.md` (house rules removed) | Claude |
| 2026-11-11 | Checked against the full text of Minichetti 2026: **corrected "microlobulated" (removed from MG/MRI/CEM, still in US)**; removed unsupported rows (US orientation and vascularity renaming, US calcification size); rebuilt change table; category 0/4/6 wording from the paper; [verify] marks resolved | Claude |
| 2026-11-12 | Pre-check fixes: 'lobulated' Table 1 and replaces 'lobular'; manual naming claim marked unverified; solitary duct may be 2; vascular calcification may/should inconsistency; lymph nodes, MG PPV, MRI, CEM, US GTC grades and audit changes added | Claude |
| 2026-11-12 | ACR What's New (Nov 2025) added as a source and read in full: Atlas→Manual and year-based versioning confirmed; category 0 FDA wording; category 6 management wording and ACFs; solitary dilated duct caveat; audit changes. Manual citation updated to the ACR-recommended form (editors). Manual body not read: eBook terms forbid AI analysis | Claude |
| 2026-11-12 | US nonmass lesion: reported malignancy range (10–54%) and strongest predictors from the Minichetti text | Claude |
| 2026-11-12 | Radiology Assistant (Schijf & Smithuis 2026, mammography and US) added: categories 1/2/5 and management corroborated; category 3 follow-up 6/12/24 months; GTC percentage grades; US margin list (microlobulated kept); solitary duct wording; nonmass PPV > 2%; category 0 disagreement recorded | Claude |
| 2026-11-12 | UNICAMP Dr. Pixel BI-RADS US 2025 added: likelihood ranges 1–5 (incl. 3 ≤ 2%, 4A/4B/4C, 5 ≥ 95%) and category 3 follow-up; Ndirangu 2026 (BAC review) added for vascular calcification context | Claude |
| 2026-11-12 | Radiologist checked the v2025 manual: vascular calcifications 'should' be reported; category 0 applies to suspicious findings (at screening). Entry updated accordingly | Claude |
| 2026-11-12 | Checagem fixes: [acr-birads-2025] removed where the manual was not read; likelihood ranges labelled as from a US teaching app; category 0 row no longer cites Minichetti and §7 drops our reconciliation; §2/§6/§8 updated | Claude |
| 2026-11-12 | Round-3: note under §3 reconciled with the radiologist-checked category 0; category 6 cites What's New only; CEM/schema note; verified_against lists all sources | Claude |
