---
id: estimated-fetal-weight-charts
title: Estimated fetal weight (EFW) — formulas and percentile charts compared (Hadlock 1991, INTERGROWTH-21st 2017, WHO 2017, FMF 2018)
type: reference-values
area: pelvis-obstetrics
modalities: [US]
population: pregnant
source_version: "1991–2018"
status: draft
verified_against: "full texts read by Claude on 2026-11-11: Hadlock 1985 (Table II equations, prospective test), Hadlock 1991 (text and Table 1, rendered page), Stirnemann 2017 (abstract, methods, formula), Kiserud 2017 WHO (abstract, methods), Nicolaides 2018 FMF (abstract, methods), ISUOG biometry 2019 (EFW section) — awaiting radiologist sign-off"
verified_by: ""
verified_on: ""
sources: [hadlock-efw-1985, hadlock-weight-standard-1991, ig21-efw-2017, who-fetal-growth-2017, fmf-weight-charts-2018, isuog-biometry-2019]
supersedes: []
superseded_by: ""
related: [fetal-biometry-isuog-2019, fgr-sga-isuog-2020]
last_reviewed: 2026-11-11
---

# Estimated fetal weight — formulas and charts

> An EFW percentile depends on **two** choices: the formula that turns biometry into grams and
> the chart that turns grams into a percentile. The four charts below differ in population,
> design and formula, so the same fetus can fall on different centiles. Report the EFW with its
> error (commonly 10–15%), the chart used and the percentile. [isuog-biometry-2019]

## 1. Scope

- **Applies to:** singleton fetuses with known GA, from about 20–22 weeks (chart-dependent).
- EFW is plotted on **fetal (EFW) charts**, never on birth-weight charts. [isuog-biometry-2019]

## 2. Definitions

| Term | Definition | Source |
|---|---|---|
| EFW error | Errors of 10–15% are common, larger in SGA and LGA fetuses; most formulas need AC, the hardest measure | [isuog-biometry-2019] |
| Descriptive reference | Describes a population at a given time (e.g. Hadlock 1991) | [isuog-biometry-2019] |
| Prescriptive standard | Describes growth under optimal conditions in healthy women (e.g. INTERGROWTH-21st) | [isuog-biometry-2019] |

## 3. Criteria / categories

### Hadlock formulas (1985, Table II; models from 276 fetuses)

Measurements in **cm**, weight in **g**; log = base 10. [hadlock-efw-1985, Table II]

| Parameters | Equation | Source |
|---|---|---|
| AC, FL | log₁₀ EFW = 1.304 + 0.05281 AC + 0.1938 FL − 0.004 AC × FL | [hadlock-efw-1985] |
| BPD, AC, FL | log₁₀ EFW = 1.335 − 0.0034 AC × FL + 0.0316 BPD + 0.0457 AC + 0.1623 FL | [hadlock-efw-1985] |
| **HC, AC, FL** | log₁₀ EFW = 1.326 − 0.00326 AC × FL + 0.0107 HC + 0.0438 AC + 0.158 FL | [hadlock-efw-1985] |
| BPD, HC, AC, FL | log₁₀ EFW = 1.3596 − 0.00386 AC × FL + 0.0064 HC + 0.00061 BPD × AC + 0.0424 AC + 0.174 FL | [hadlock-efw-1985] |

- Prospective test in 109 fetuses (scanned within 3 days of delivery in most cases): models
  combining head, abdomen and femur had random error 1 SD ≈ 7.5%, significantly better than
  head + abdomen models; the authors recommend the **HC + AC + FL** equation for general use,
  choosing another model when a measurement is unobtainable (e.g. deeply engaged head).
  [hadlock-efw-1985]
- Population: predominantly middle-class white patients, Houston, Texas. [hadlock-efw-1985]

### Charts

| Chart | Population and design | EFW formula | GA range | Source |
|---|---|---|---|---|
| **Hadlock 1991** | 392 predominantly middle-class white women (US), cross-sectional, one scan per fetus | Hadlock BPD + HC + AC + FL model (1985; random error 1 SD = 7.4%). Median curve: ln EFW (g) = 0.578 + 0.332 × GA − 0.00354 × GA² (GA in weeks); residual SD ≈ 12.7% | 10–40 weeks (table) | [hadlock-weight-standard-1991] |
| **INTERGROWTH-21st 2017** | Prescriptive; formula from 2,404 babies born within 14 days of the last scan; tables from 4,231 FGLS fetuses (eight countries) | ln EFW = 5.084820 − 54.06633 × (AC/100)³ − 95.80076 × (AC/100)³ × ln(AC/100) + 3.136370 × (HC/100); AC and HC in **cm**; FL not used | 22–40 weeks | [ig21-efw-2017] |
| **WHO 2017** | Longitudinal, 1,387 low-risk women in ten countries (including Brazil) | Hadlock's third formula (HC + AC + FL) | 14–40 weeks | [who-fetal-growth-2017] |
| **FMF 2018** (Nicolaides) | 5,163 EFW–birth-weight pairs (birth within 2 days) plus 95,579 routine EFWs at 20–36 weeks, London/Kent; Bayesian model with a common median for EFW and birth weight | Hadlock 1985 (HC + AC + FL) | 20 + 0 to 36 + 6 weeks (EFW validated) | [fmf-weight-charts-2018] |

Anchor values, Hadlock 1991 (Table 1): at 36 weeks, 10th / 50th / 90th centile = 2,335 /
2,813 / 3,291 g; median 3,619 g at 40 weeks. [hadlock-weight-standard-1991, Table 1]

## 4. Management

- Same formula and same chart for serial scans in one patient; state both in the report.
- Interpret EFW together with the individual measures (HC, AC) and their trajectory.
  INTERGROWTH-21st explicitly warns against focusing on a single value. [ig21-efw-2017]
- Thresholds (SGA < 10th, FGR < 3rd, etc.) are in `fetal-biometry-isuog-2019` and
  `fgr-sga-isuog-2020`.

## 5. Pitfalls

- Plotting an EFW from one formula on a chart built with another formula.
- Using birth-weight charts for EFW: they include many growth-restricted preterm babies, so
  preterm 10th centiles are too low. FMF built its birth-weight chart to include fetuses still
  in utero to correct this. [isuog-biometry-2019; fmf-weight-charts-2018]
- Using a percentile without the chart name: Hadlock (white US population), INTERGROWTH
  (prescriptive, multinational), WHO (multinational, country variation) and FMF (UK routine
  population) are not interchangeable.

## 6. What the source does not say

- None of the charts was built in a Brazilian-only population (Brazil contributed sites to
  INTERGROWTH-21st and WHO).
- Full centile tables are not reproduced here.

## 7. Disagreements and newer versions

- FMF found that the incidence of SGA by its EFW and birth-weight charts was higher in black
  than in white women. [fmf-weight-charts-2018]
- WHO reported significant differences in growth between countries and with fetal sex,
  suggesting local adjustment may be needed. [who-fetal-growth-2017]

## 8. How to cite

- Formula: `hadlock-efw-1985`
- The chart used: `hadlock-weight-standard-1991`, `ig21-efw-2017`, `who-fetal-growth-2017` or
  `fmf-weight-charts-2018`

## 9. Change log

| Date | Change | By |
|---|---|---|
| 2026-11-11 | Created from the full texts | Claude |
| 2026-11-11 | Added the four Hadlock 1985 EFW equations (Table II) from the full text and their reference | Claude |
