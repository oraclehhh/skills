# Glossary

- **Bayesian Network**: Probabilistic graphical model representing variables as nodes and conditional dependencies as directed edges. Used here for causal discovery via hill-climbing algorithm with bootstrap stability selection (Ch 6).
- **Coupling Weights (i, e)**: In the Kuramoto model, *i* = internal coupling (perception-action link within a person); *e* = external coupling (information flow between persons). Higher values = stronger coupling (Ch 1, 4).
- **fNIRS (functional Near-Infrared Spectroscopy)**: Non-invasive neuroimaging measuring cortical HbO/HbR concentration changes via near-infrared light absorption at 730nm/850nm (Ch 2, 3).
- **Granger Causality Analysis (GCA)**: Directional connectivity method testing whether past values of signal X improve prediction of signal Y. Implemented via state-space models (MVGC toolbox) (Ch 3, 5).
- **Hyperbrain Network**: The combined system of intra-brain (within-person) and inter-brain (between-person) connectivity formed by interacting individuals (Müller et al., 2018) (Ch 7).
- **Hyperscanning**: Simultaneous measurement of brain activity from two or more interacting individuals (Montague et al., 2002) (Ch 1).
- **Inter-Brain Synchronization (IBS)**: Wavelet transform coherence between two individuals' brain signals in the 0.01–0.04 Hz band. A measure of neural coupling between interacting partners (Ch 1, 3, 5).
- **Interpersonal Adjustment Hypothesis**: Predicts that social interaction deficits require *increased* inter-brain synchronization as a compensatory mechanism (Pan et al., 2021a) (Ch 1).
- **Kuramoto Model**: Coupled phase oscillator model where each oscillator's phase evolves based on its natural frequency and coupling to other oscillators. Used here to model dyadic synchronization (Acebrón et al., 2005) (Ch 1, 4).
- **Mahalanobis Distance**: Scale-invariant distance metric that accounts for covariance structure. Used to find which IBS connections best match computational coupling parameters (Ch 3, 6).
- **PANSS (Positive and Negative Syndrome Scale)**: 30-item clinician-rated SCZ assessment on 7-point scale, decomposed into 4 dimensions: positive, negative, affective, cognitive (Chen et al., 2020) (Ch 2, 6).
- **Partial Least Squares Regression (PLSR)**: Dimensionality reduction + regularized regression for high-dimensional, collinear predictors. Used to predict symptom dimensions from IBS (Ch 3, 6).
- **Rhythm Deviation**: Absolute difference between observed inter-tap interval and metronome interval (500ms). Index of individual rhythm control ability (Ch 3, 4).
- **Self-Other Integration**: The ability to simultaneously represent and distinguish information about oneself and an interaction partner. Impaired in SCZ (Ch 7).
- **Synchronization Index (SI)**: Circular variance of the relative phase distribution. Ranges 0–1; >0.73 = synchronous. Computed as |1/N Σ exp(i(θ₁−θ₂))| (Ch 3, 4).
- **Tapping Variability**: Median Absolute Deviation (MAD) of the absolute asynchrony between partners' fingertap timings. Higher = less stable coordination (Ch 3, 4).
- **Wavelet Transform Coherence (WTC)**: Time-frequency measure of correlation between two signals, suited for non-stationary data. Used for both intra-brain and inter-brain synchronization computation (Ch 3).
