# Cheatsheet

## Decision Rules

| When… | Do… | Because… |
|---|---|---|
| Studying social interaction in clinical populations | Use hyperscanning, not single-brain neuroimaging | Social brain cannot be understood in isolation; single-brain misses integration between mentalizing and action-observation networks |
| Interpreting elevated IBS in a clinical group | Check correlation with behavioral performance | ↑IBS + ↓behavior = compensation (interpersonal adjustment). ↑IBS + ↑behavior = facilitation |
| Want to isolate coupling direction in dyads | Use 4-condition design (Self / Each Other / A / B) | Uncovers whether deficit is in sending, receiving, or bidirectional coupling |
| Behavioral data from joint tapping | Fit Kuramoto model with 2-step grid search | Reveals internal vs. external coupling weights not visible in raw behavior |
| fNIRS preprocessing for hyperscanning | Use wavelet denoising + 0.01–0.04 Hz band | Excludes cardiac (~0.7Hz), respiratory (0.15–0.3Hz), VLF drift (<0.01Hz) |
| High-dimensional neural prediction of symptoms | Use PLSR, not standard multiple regression | Handles multicollinearity; works when predictors > observations |
| Inferring directional dependencies among variables | Use Bayesian networks with bootstrap stability (≥85% frequency, ≥51% direction) | More robust than single DAG fit; controls for overfitting |

## Thresholds & Rules of Thumb

| Metric | Threshold | Meaning |
|---|---|---|
| Synchronization Index (SI) | > 0.73 | Classified as synchronous behavior (Tognoli et al., 2007) |
| WTC frequency band | 0.01–0.04 Hz | Social coordination band (excludes physiological noise) |
| fNIRS sampling rate | 11 Hz (here) | Adequate for hemodynamic response; ensure >5 Hz minimum |
| Source-detector distance (fNIRS) | ~3 cm | Standard for cortical penetration |
| Resting-state baseline | 3 min eyes-closed | For z-score normalization of task HbO data |
| PLSR component selection | Based on explained variance | Balance prediction accuracy vs. overfitting |
| Bayesian network bootstrap | 1000× resampling | Standard for stability selection |
| Edge retention cutoff (Bayesian) | ≥85% frequency + ≥51% direction | Conservative stability filter |
| Medication effect check | Split SCZ by medicated/non-medicated; test all key metrics | Controls for medication confound |

## Trade-off Matrix: Interpretive Frameworks

| Framework | IBS Prediction | Supported? | Best for… |
|---|---|---|---|
| Coordination-by-synchrony | ↓ IBS in SCZ-HC | ✗ | Default null hypothesis |
| Interpersonal adjustment | ↑ IBS in SCZ-HC | ✓ | Compensatory accounts of social dysfunction |
| Predictive coding | Internal > external coupling bias | ✓ | Unifying behavioral + neural findings |

## Tells & Smells

| You see… | You're probably seeing… |
|---|---|
| ↑IBS + ↓intra-brain connectivity in the same dyad | Compensatory hyperbrain — clinical group needing more neural effort |
| IBS correlates with behavior only in clinical group | Neural compensation, not general facilitation — the coupling benefits those who need it most |
| No group difference in brain activation but differences in connectivity | The neural signature is in coupling, not magnitude — don't stop at activation maps |
| LF→LA Granger causality elevated | HC implicitly accommodating SCZ patient — frontopolar tracking of partner's behavior |
| External coupling drops only when HC can't hear SCZ | The deficit is in the SCZ's signal, not in the HC's ability to use it — but both are needed for normal coupling |
| Two separate IBS connections encode external coupling (vs. one in HCs) | Less efficient, more distributed neural resource allocation in clinical group |

## Quick Reference: Key Brain Regions & Their Role

| Region | Function in Task | Role in SCZ-HC |
|---|---|---|
| Motor (M) | Finger tapping execution | HC motor = IBS hub sending signals |
| Auditory (A) | Processing tapping feedback | SCZ auditory = IBS target receiving HC signals |
| DLPFC | Theory of mind, cognitive control, behavioral sequencing | SCZ DLPFC = recruited for tracking HC output |
| Superior Frontal Cortex (SFC) | Social cooperation, modeling others' behavior | SCZ SFC intra-brain sync coupled to IBS |
| FrontoPolar (F) | Prediction, behavioral switching, evidence accumulation | HC FP drives SCZ auditory (LF→LA GC) |
| Temporal-Parietal Junction (TPJ) | Self-other distinction | Encodes external coupling in HC-HC (RDLPFC-RTPJ) |
