---
name: pan
description: "Knowledge base from \"A computational and multi-brain signature for aberrant social coordination in schizophrenia\" by Wang, Wen, Zheng, Chen, Lin & Pan (2024). Use when applying hyperscanning methodology, Kuramoto dynamical systems modeling, interpersonal synchronization analysis, or interpreting inter-brain synchronization in clinical populations."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# A Computational and Multi-Brain Signature for Aberrant Social Coordination in Schizophrenia
**Author**: Ya-Jie Wang, Yalan Wen, Leilei Zheng, Ji Chen, Zheng Lin, Yafeng Pan | **Journal**: Progress in Neuropsychopharmacology & Biological Psychiatry (2024) | **Pages**: 15 | **Sections**: 7 | **Generated**: 2026-07-04

## How to Use This Skill

- **Without arguments** — load core frameworks for reference
- **With a topic** — ask about `hyperscanning`, `Kuramoto model`, `IBS`, `PLSR`, or another indexed topic; I find and read the relevant chapter
- **With chapter** — ask for `ch04`; I load that specific section
- **Browse** — ask "what chapters do you have?" to see the full index

When you ask about a topic not covered in Core Frameworks below, I will read
the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

### The Two Competing Hypotheses

**Interpersonal Adjustment Hypothesis** (SUPPORTED): Social interaction deficits require *increased* inter-brain synchronization (IBS) as a compensatory mechanism. Higher social demands → higher IBS. SCZ-HC dyads show elevated IBS because the healthy partner implicitly accommodates the patient, and the patient recruits extra cognitive resources (DLPFC, auditory cortex) to track the partner's output. Use this as the default interpretive framework when you see ↑IBS in a clinical group.

**Coordination-by-Synchrony Hypothesis** (REFUTED here): Predicts decreased IBS in clinical groups because coordination ability is impaired. Use this as the null hypothesis — if IBS is lower, the deficit is primary; if higher, compensation is likely.

### The Hyperbrain Network Framework

Two interacting brains form one integrated system. The minimal unit of analysis is the **dyad**, not the individual. Key principle: intra-brain and inter-brain dynamics mutually constrain each other. Evidence: intra-brain synchronization (RSFC_SCZ—LSFC_SCZ) correlates with inter-brain synchronization (RM_HC—RDLPFC_SCZ) *only* in SCZ-HC dyads (r = 0.32). This correlation would be invisible in a single-brain study.

**When to apply**: Any social neuroscience question. Always compute both intra-brain (within-person ROI×ROI) and inter-brain (between-person ROI×ROI) connectivity. Test for correlations between the two levels.

### Three-Level Mechanistic Decomposition

Social coordination deficits must be understood at three converging levels:
1. **Behavioral**: Synchronization index (SI), rhythm deviation, tapping variability
2. **Computational**: Kuramoto model coupling weights (internal i, external e)
3. **Neural**: IBS, intra-brain synchronization, Granger causality

**When to apply**: Whenever you need mechanistic depth beyond single-level description. If all three levels converge on the same interpretation (here: self-other integration failure → internal coupling bias → elevated IBS), confidence is high.

### Kuramoto Model for Dyadic Coordination

Each person = two coupled oscillators (perception + action). The dyad = four oscillators.
- **Internal coupling (i₁, i₂)**: Within-person perception↔action link
- **External coupling (e₁, e₂)**: Between-person information flow

**Key finding**: SCZ-HC dyads show attenuated *external* coupling specifically when the healthy partner cannot hear the SCZ patient (Hearing A condition). In conditions where HC can hear SCZ feedback, coupling normalizes — the "normalcy" depends on HC accommodation.

**When to apply**: Model any dyadic time-series (tapping, conversational turn-taking, joint action). Use the two-step grid search: coarse (1–10, step 1) → fine (±0.9, step 0.2). Compute group-level parameters for stability.

### IBS as a Clinical Biomarker

IBS at **LM_HC—LDLPFC_SCZ** is the most behaviorally and clinically meaningful connection:
- Positively correlates with behavioral synchronization (r = 0.32, pFDR = 0.0006) — only in SCZ-HC, not HC-HC
- Positively predicts behavioral synchronization in Bayesian network analysis
- Together with other IBS connections, predicts all PANSS symptom dimensions (best: Cognitive R² = 0.54, Positive R² = 0.46)

**Decision rule**: When you find a group-difference IBS connection, always test: (1) Does it correlate with behavior? (2) Does it predict clinical symptoms? Only connections satisfying both criteria are viable intervention targets.

### The Dissociative Multi-Brain Pattern

SCZ-HC dyads show: ↓ intra-brain connectivity (within each person) + ↑ inter-brain connectivity (between persons). This dissociative pattern is the neural signature of compensation:
- **9/9** intra-brain synchronization ROI pairs are lower in SCZ-HC
- **9/11** intra-brain GC pairs are lower in SCZ-HC
- **3/144** IBS connections are significantly *higher* in SCZ-HC (surviving FDR correction)
- **1** inter-brain GC direction (LF_HC → LA_SCZ) is higher

**When to apply**: Look for this dissociative pattern in any clinical hyperscanning study. If you find it, the interpersonal adjustment hypothesis is the right interpretive frame. If both intra- and inter-brain are lower, the deficit is primary (coordination-by-synchrony). If both are higher, the group may be hyper-compensating.

### Predictive Coding Account (Theoretical Bridge)

SCZ involves a failure to prioritize shared (interpersonal) predictive models, with increased reliance on lower-order internal models. This unifies the findings:
- Internal coupling bias (Kuramoto) = over-weighting internal priors
- Reduced external coupling = under-weighting sensory evidence from partner
- Elevated IBS = the neural cost of resolving larger prediction errors

**When to apply**: As the theoretical bridge between computational and neural findings. Future models should integrate active inference into the Kuramoto framework.

---

## Chapter Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [ch01](chapters/ch01-introduction.md) | Introduction & Background | Coordination-by-synchrony, Interpersonal adjustment, Kuramoto model |
| [ch02](chapters/ch02-experimental-design.md) | Experimental Design & Participants | Joint finger-tapping paradigm, Four-condition coupling, PANSS 4-factor |
| [ch03](chapters/ch03-data-analysis-pipeline.md) | Data Analysis Pipeline | Three-level analysis, Kuramoto parameter search, Wavelet coherence, PLSR |
| [ch04](chapters/ch04-disrupted-social-coordination.md) | Disrupted Social Coordination | Cascading coordination deficit, Coupling imbalance, Mediation model |
| [ch05](chapters/ch05-multibrain-network-alterations.md) | Multi-brain Network Alterations | Dissociative multi-brain pattern, Hyperbrain, Granger causality direction |
| [ch06](chapters/ch06-brain-behavior-symptom-prediction.md) | Brain-Behavior & Symptom Prediction | IBS as behavioral facilitator, Bayesian networks, Mahalanobis mapping, PLSR |
| [ch07](chapters/ch07-discussion.md) | Discussion & Future Directions | Hyperbrain framework, Implicit accommodation, Predictive coding account |

## Topic Index

- **Bayesian network** → ch06
- **Coupling weights (i, e)** → ch01, ch04
- **fNIRS** → ch02, ch03
- **Granger causality (GC)** → ch03, ch05
- **Hyperbrain** → ch05, ch07
- **Hyperscanning** → ch01, ch02
- **Inter-brain synchronization (IBS)** → ch01, ch05, ch06
- **Interpersonal adjustment hypothesis** → ch01, ch05, ch07
- **Intra-brain synchronization** → ch05, ch07
- **Kuramoto model** → ch01, ch03, ch04
- **Mahalanobis distance** → ch03, ch06
- **Mediation analysis** → ch04
- **PANSS** → ch02, ch06
- **PLSR (Partial Least Squares Regression)** → ch03, ch06
- **Predictive coding** → ch07
- **Rhythm deviation** → ch03, ch04
- **Self-other integration** → ch07
- **Synchronization index (SI)** → ch03, ch04
- **Tapping variability** → ch03, ch04
- **Wavelet transform coherence (WTC)** → ch03

## Supporting Files

- [glossary.md](glossary.md) — all key terms with definitions
- [patterns.md](patterns.md) — all techniques and design patterns
- [cheatsheet.md](cheatsheet.md) — decision rules, thresholds, tells & smells

---

## Scope & Limits

This skill covers the paper's content only — its methodology, findings, and frameworks. For hands-on implementation of fNIRS hyperscanning, Kuramoto modeling, or PLSR in your own research, combine with domain-specific tools and packages (Homer2, MVGC toolbox, scikit-learn). The clinical findings are specific to SCZ; generalize to other populations (ASD, CHR) with caution and reference the original paper's discussion of population-specific effects.
