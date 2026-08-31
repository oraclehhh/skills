# Chapter 6: Results — Brain-Behavior Associations & Symptom Prediction

## Core Idea
IBS at LM_HC—LDLPFC_SCZ is the key functional connection: it correlates with behavioral synchronization, predicts it in Bayesian network analysis, and — together with other IBS connections — successfully predicts all four symptom dimensions of schizophrenia via PLSR.

## Frameworks Introduced

- **IBS as Behavioral Facilitator**: IBS positively predicts behavioral synchronization in SCZ-HC dyads, while rhythm deviation negatively predicts it. IBS and behavior are complementary channels.
  - When to use: To identify which neural connections are behaviorally meaningful (not just statistically significant).
  - How: Correlate each significant IBS connection with SI; validate with Bayesian network analysis.

- **Bayesian Network for Causal Discovery**: Hill-climbing algorithm on behavioral indices + IBS to infer directional dependencies without assumptions about their relationships.
  - When to use: When you have multiple correlated variables and want to discover their directional structure.
  - How: Generate directed acyclic graph (DAG) using hill-climbing. Bootstrap 1000×, retain edges appearing in ≥85% of networks and pointing in the same direction in ≥51%. Evaluate with BIC.

- **Mahalanobis Distance for Neural-Coupling Mapping**: Identifies which IBS connections best represent computational coupling parameters.
  - When to use: To bridge computational modeling and neural data — finding the neural substrate of model parameters.
  - How: Compute Mahalanobis distance between group-level coupling weights (e₁, e₂) and the distribution of individual-level IBS values across ROI pairs. Lower distance = better representation.

- **PLSR for Symptom Prediction**: Partial Least Squares Regression maps high-dimensional IBS features (144 inter-brain connections) onto low-dimensional symptom scores.
  - When to use: When predictors outnumber observations and are highly collinear.
  - How: Dimensionality reduction (find latent components that maximize covariance with symptom scores) → regression. Report r, R², and top-contributing ROI combinations.

## Key Concepts
- **IBS-Behavior Correlation**: Only LM_HC—LDLPFC_SCZ IBS correlates with SI in SCZ-HC (r = 0.32, pFDR = 0.0006). No correlation in HC-HC (r = 0.09, p = 0.22).
- **Intra-Inter Brain Coupling**: RSFC_SCZ—LSFC_SCZ intra-brain sync correlates with RM_HC—RDLPFC_SCZ IBS (r = 0.32, pFDR = 0.005) — SCZ's superior frontal cortex intra-connectivity is coupled to inter-brain alignment.
- **Bayesian Network Edges (SCZ-HC)**: Rhythm deviation → (negatively) behavioral synchronization ← (positively) IBS at LM—LDLPFC. IBS and rhythm deviation are independent predictors.
- **Coupling-IBS Mapping (Mahalanobis)**:
  - HC-HC: IBS at RDLPFC—RTPJ best represents both e₁ and e₂ (one neural system for external coupling)
  - SCZ-HC: IBS at LA—RTPJ represents e₁; IBS at RDLPFC—LSFC represents e₂ (two separate neural systems)
- **PLSR Symptom Prediction Performance**:
  - Cognitive symptom: r = 0.74, R² = 0.54 (best predicted)
  - Positive symptom: r = 0.68, R² = 0.46
  - Negative symptom: r = 0.58, R² = 0.33
  - Total PANSS: r = 0.58, R² = 0.34
  - Affective symptom: r = 0.54, R² = 0.29

## Mental Models
- Think of IBS as a **biomarker** — a quantifiable neural signal that predicts clinical symptom severity, not just a correlate of task performance.
- Think of the SCZ-HC brain as using **two separate channels for external coupling** (LA-RTPJ + RDLPFC-LSFC) vs. the HC-HC brain's **single unified channel** (RDLPFC-RTPJ). The SCZ brain recruits more regions to compensate.
- Think of Bayesian network edges as **causal candidates** (not proven causes) — they show consistent directional dependencies in the data, but experimental manipulation is needed to establish causality.

## Reference Tables
| Symptom Dimension | r | R² | Key Predictive IBS Connections |
|---|---|---|---|
| Cognitive | 0.74 | 0.54 | SFC, DLPFC, frontopolar, auditory |
| Positive | 0.68 | 0.46 | SFC, DLPFC, frontopolar, auditory |
| Negative | 0.58 | 0.33 | (same regions) |
| Total PANSS | 0.58 | 0.34 | (same regions) |
| Affective | 0.54 | 0.29 | (same regions) |

## Worked Example
**Bayesian network structure learning**:
1. Input: rhythm deviation, tapping variability, behavioral synchronization, IBS at LM—LDLPFC.
2. Algorithm: Hill-climbing with BIC scoring.
3. Bootstrap: 1000 resamples of the data, learn a DAG each time.
4. Edge retention filter: ≥85% frequency + direction consistency ≥51%.
5. Resulting DAG in SCZ-HC:
   ```
   Rhythm Deviation ──(−)──→ Behavioral Synchronization
   IBS (LM-LDLPFC) ──(+)──→ Behavioral Synchronization
   ```
   Tapping variability did not survive the bootstrap filter — it is indirectly related through rhythm deviation.

## Key Takeaways
1. LM_HC—LDLPFC_SCZ IBS is the single most behaviorally relevant neural connection — it correlates with performance and predicts it in the Bayesian network.
2. Cognitive symptoms are most predictable from IBS (R² = 0.54), suggesting IBS is particularly sensitive to the cognitive dimension of SCZ.
3. SCZ-HC dyads use a more distributed (less efficient) neural system to achieve external coupling compared to HC-HC dyads.
4. IBS predicts symptom severity above and beyond task performance — it captures clinically meaningful individual differences.
5. The Bayesian network confirms two independent routes to behavioral synchronization: one dampening (rhythm deviation) and one facilitating (IBS).

## Connects To
- **Ch 5**: The specific IBS connections whose functional significance is tested here
- **Ch 7**: IBS as an intervention target (neurofeedback, multi-brain stimulation)
- **Precision psychiatry**: Using neural biomarkers for personalized treatment
