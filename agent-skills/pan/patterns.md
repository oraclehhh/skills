# Patterns & Techniques

## Four-Condition Coupling Design
**When to use**: When you need to isolate direction-specific contributions to dyadic coordination.
**How**: Create conditions where auditory feedback flows in different directions: (1) neither hears partner (baseline internal), (2) both hear each other (bidirectional), (3) both hear only A (A→both), (4) both hear only B (B→both).
**Trade-offs**: Requires precise experimental control of sensory feedback channels. Role asymmetry must be accounted for in analysis.

## Multi-Level Mechanistic Decomposition
**When to use**: For social neuroscience studies seeking mechanistic depth.
**How**: Analyze the same dyadic interaction at three levels — behavioral (synchronization indices), computational (Kuramoto coupling weights), and neural (IBS, intra-brain connectivity) — and test for convergence across levels.
**Trade-offs**: Computationally intensive; requires expertise in signal processing, dynamical systems, and neuroimaging. Group-level parameter estimation trades individual precision for stability.

## Kuramoto Parameter Search (Two-Step Grid)
**When to use**: Fitting coupled oscillator models to empirical behavioral time-series.
**How**:
1. Coarse grid: systematically vary 4 coupling weights (i₁, i₂, e₁, e₂) from 1–10 in steps of 1 → 10,000 combinations. Simulate 200× per combination from random initial phases. Compare simulated cross-correlation lag patterns (lag-1, lag0, lag+1) to real data.
2. Fine grid: refine around best weights (±0.9, step 0.2). Repeat 200× per combination, 35 overall iterations.
**Trade-offs**: Group-level parameters are stable but mask individual differences. Model assumes continuous coupling, which may not capture discrete behavioral adjustments.

## Wavelet Coherence for Inter-Brain Synchronization
**When to use**: Computing neural synchronization between two individuals' fNIRS/EEG signals.
**How**: Use wcoherence function (MATLAB) on z-scored HbO time series. Average coherence in 0.01–0.04 Hz band. Apply to all 12×12 ROI combinations within and between participants.
**Trade-offs**: The 0.01–0.04 Hz band excludes physiological noise but may miss faster neural dynamics. WTC requires careful parameterization (mother wavelet, scales).

## Mahalanobis Distance Neural-Coupling Mapping
**When to use**: Bridging computational model parameters with neural data.
**How**: Treat group-level coupling weights as a point, individual-level IBS distributions as the reference distribution. Compute Mahalanobis distance for each IBS ROI pair. Lowest distance = best neural representation of the coupling parameter.
**Trade-offs**: Assumes multivariate normality of IBS distributions. Only works when computational parameters and neural data come from the same individuals.

## Partial Least Squares Regression for High-Dimensional Neural Prediction
**When to use**: When neural features (e.g., 144 IBS connections) outnumber observations and are highly collinear.
**How**: PLSR finds latent components that maximize covariance between IBS matrix (X) and symptom scores (y). Report correlation and R² between predicted and actual scores. Extract top-weighted ROI combinations for each component.
**Trade-offs**: PLSR is a linear method — non-linear relationships may be missed. Components are optimized for prediction, not interpretability.

## Bayesian Network Causal Discovery with Bootstrap Stability
**When to use**: When you have multiple correlated behavioral/neural variables and want to infer their directional structure.
**How**:
1. Run hill-climbing algorithm (BIC scoring) to learn DAG structure.
2. Bootstrap 1000×: learn a DAG on each resample.
3. Retain edges present in ≥85% of bootstraps with direction consistency ≥51%.
4. Evaluate edge significance with BIC.
**Trade-offs**: Bayesian networks assume no latent confounders and no cycles. Results indicate consistent probabilistic dependencies, not proven causation.

## State-Space Granger Causality for Directional Neural Inference
**When to use**: Determining which partner's brain activity drives the other's during social interaction.
**How**: Fit state-space models to paired ROI time series (MVGC toolbox). Compute conditional GC in both directions (A→B, B→A). Report the direction with significantly higher GC.
**Trade-offs**: GC assumes linear predictability. State-space models offer better statistical power than autoregressive estimators but are more complex to specify.
