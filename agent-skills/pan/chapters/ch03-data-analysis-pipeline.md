# Chapter 3: Methods — Data Analysis Pipeline

## Core Idea
The multi-level analysis pipeline — behavioral indices → Kuramoto modeling → fNIRS processing → statistical testing — is the methodological backbone that enables triangulation across behavioral, computational, and neural levels of explanation.

## Frameworks Introduced

- **Three-Level Analysis Framework**: Behavior → Computation → Neural
  - Level 1 (Behavioral): Rhythm deviation, tapping variability, synchronization index
  - Level 2 (Computational): Four-oscillator Kuramoto model fitting (internal/external coupling weights)
  - Level 3 (Neural): Intra-brain synchronization, inter-brain synchronization (IBS), Granger causality
  - When to use: For any social neuroscience study seeking mechanistic depth beyond single-level description.

- **Coupling Weight Parameter Search**: Two-step grid search to fit the Kuramoto model:
  - Step 1: Systematic grid search over i₁, i₂, e₁, e₂ (1–10 in steps of 1 → 10,000 combinations), simulated 200× per combination, compare cross-correlation lag patterns (lag-1, lag0, lag+1) to real data.
  - Step 2: Refined search around best weights (±0.9, step 0.2), repeated 200× per combination, 35 overall iterations.
  - When to use: When fitting coupled oscillator models to behavioral time-series data.
  - How: Compute group-level (not individual-level) parameters for stability.

## Key Concepts
- **Rhythm Deviation**: Absolute difference between observed inter-tap interval (ITI) and the metronome ITI (500ms). Larger = worse rhythm control.
- **Tapping Variability**: MAD of the absolute asynchrony between partners' tap timings. Higher = less stable coordination.
- **Synchronization Index (SI)**: Circular variance of the relative phase distribution between partners' ITI time series. Ranges 0–1; >0.73 indicates synchronous behavior (Tognoli et al., 2007).
- **Wavelet Transform Coherence (WTC)**: Time-frequency measure of correlation between two signals; used here for both intra-brain (within-person ROI-ROI) and inter-brain (between-person ROI-ROI) synchronization in the 0.01–0.04 Hz band.
- **Granger Causality Analysis (GCA)**: Directional connectivity metric using state-space models (MVGC toolbox) — answers "does A's brain activity predict B's brain activity?"
- **Mahalanobis Distance**: Scale-invariant distance metric comparing individual-level IBS distributions to group-level computational coupling parameters.
- **Partial Least Squares Regression (PLSR)**: Dimensionality reduction + regularized regression for predicting symptom dimensions from high-dimensional IBS features.

## Mental Models
- Think of the Kuramoto parameter search as **inverse modeling** — vary model parameters until simulated behavior matches real behavior, then the best-fitting parameters reveal the underlying system properties.
- Think of wavelet coherence as a **time-resolved correlation** — unlike Pearson r, WTC shows when in time and at what frequency two signals are coupled.
- Think of the 0.01–0.04 Hz frequency band as the **social coordination band** — it excludes cardiac (~0.7+ Hz), respiratory (0.15–0.3 Hz), and very low frequency drift (<0.01 Hz).

## Code Examples *(technical)*
```matlab
% Synchronization Index calculation (circular variance of relative phase)
% θ₁(tₙ) and θ₂(tₙ) are phases at time n for participants 1 and 2
N = length(theta1);
SI = abs(1/N * sum(exp(1i * (theta1 - theta2))));
% SI ranges 0 (no sync) to 1 (perfect sync)
```

**What it demonstrates**: The core behavioral metric — circular variance formula for phase synchronization.

## Reference Tables
| Frequency Band | Source | Action |
|---|---|---|
| < 0.01 Hz | Very low frequency fluctuations | Exclude |
| 0.01–0.04 Hz | Target: social coordination | **Keep for analysis** |
| 0.15–0.3 Hz | Respiration | Exclude |
| > 0.7 Hz | Cardiac pulsation | Exclude |

## Worked Example
**Kuramoto model implementation in MATLAB**:
```matlab
% Four-oscillator Kuramoto model
% Coupling matrix K_np for 4 oscillators:
% Osc 1 (A-perception) ← i1→ Osc 2 (A-action)
% Osc 3 (B-perception) ← i2→ Osc 4 (B-action)
% External coupling: e1 links unit 1 (A), e2 links unit 2 (B)

% dθ_n/dt = ω + Σ_p K_np * sin(θ_p - θ_n) + ξ_n

% Coupling matrix structure:
% K = [0   i1  e1  0;    % A-perception
%      i1  0   0   0;     % A-action
%      e2  0   0   i2;    % B-perception
%      0   0   i2  0]     % B-action
```

**Parameter search logic**: For each of 10,000 coupling combinations (step 1), run 200 simulations starting from random phases. Extract lag-1, lag0, lag+1 cross-correlation patterns. Find the combination where simulated patterns best match real behavioral data. Refine in step 2.

## Key Takeaways
1. SI > 0.73 is the established threshold for classifying behavior as "synchronous".
2. The 0.01–0.04 Hz band is critical — it captures social coordination signals while excluding physiological noise.
3. Group-level (not individual-level) Kuramoto parameters provide stable coupling estimates.
4. Mahalanobis distance bridges computational parameters and neural data by finding which IBS connections best represent coupling weights.
5. PLSR handles multicollinearity among predictors — essential when IBS features from 12 ROIs produce 144 inter-brain connections.

## Connects To
- **Ch 2**: Experimental design — these analyses are applied to the four-condition data
- **Ch 4**: Behavioral results using these metrics
- **Ch 5**: Neural results using WTC and GCA
- **Ch 6**: PLSR symptom prediction results
