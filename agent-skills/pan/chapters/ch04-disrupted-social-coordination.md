# Chapter 4: Results — Disrupted Social Coordination in SCZ

## Core Idea
SCZ patients exhibit a cascading deficit in social coordination: poor rhythm control → unstable tapping behavior → reduced interpersonal synchronization. The Kuramoto model reveals that this is driven by attenuated *external* coupling specifically when the healthy partner cannot receive feedback from the SCZ patient.

## Frameworks Introduced

- **Cascading Coordination Deficit Model**: Rhythm deviation → Tapping variability → Reduced synchronization.
  - When to use: To decompose social coordination deficits into sequential, testable components.
  - How: Test mediation: rhythm deviation → tapping variability → synchronization index (PROCESS v3.5 mediation model).

- **Coupling Imbalance Pattern**: SCZ patients show a bias toward internal coupling over external coupling during social interactions.
  - When to use: Interpreting computational modeling results in clinical populations.
  - How: Compare internal (i₁, i₂) vs. external (e₁, e₂) coupling weights across groups and conditions.

## Key Concepts
- **Rhythm deviation in SCZ**: Median 44.80 ± 21.90 ms (SCZ) vs. 29.40–34.50 ms (all HCs), Cohen's d = 0.71–0.99. SCZ patients are worse at maintaining a steady beat.
- **Tapping variability group effect**: SCZ-HC dyads (371.00 ± 259.00 ms) show significantly more variability than HC-HC dyads (233.00 ± 107.00 ms), ηp² = 0.14.
- **Synchronization index group effect**: SCZ-HC group (0.43 ± 0.26) vs. HC-HC group (0.65 ± 0.23), ηp² = 0.22 — SCZ-HC dyads are markedly less synchronized.
- **Hearing A condition attenuation**: SCZ-HC dyads show reduced external coupling specifically in Hearing A (when both participants hear only the HC). e₁ drops to 2.00 and e₂ to 2.90 in SCZ-HC vs. 5.70/7.90 in HC-HC.

## Mental Models
- Think of SCZ social coordination as a **broken feedback loop**: the healthy partner can't adjust without receiving the SCZ partner's behavioral signal. When the feedback channel is cut (Hearing A/Self conditions), external coupling collapses.
- Think of internal vs. external coupling as a **resource allocation problem**: SCZ patients preferentially allocate to internal (within-self) rather than external (between-people) coupling.
- The correlation pattern (rhythm deviation ↔ tapping variability ↔ synchronization) exists **only in SCZ, not in HC** — the cascade is a pathological, not universal, pattern.

## Reference Tables
| Condition | HC-HC i₁/e₁/i₂/e₂ | SCZ-HC i₁/e₁/i₂/e₂ | Key Difference |
|---|---|---|---|
| Hearing Self | 8.20/2.10/9.40/1.70 | 9.50/2.30/8.80/3.10 | Both show high internal, low external |
| Hearing Each Other | 8.00/9.50/10.20/10.30 | 8.00/10.20/9.10/10.70 | Both show high external — comparable |
| Hearing A (HC role) | 9.10/5.70/9.40/7.90 | 9.40/2.00/9.50/2.90 | **SCZ-HC external coupling dramatically lower** |
| Hearing B (SCZ role) | 10.20/6.40/9.30/6.00 | 9.20/5.80/9.40/4.80 | Comparable external coupling |

## Worked Example
**Mediation pathway**: Rhythm Deviation → Tapping Variability → Synchronization Index
- Direct effect (RD → SI): β = −0.31, p < 0.001
- Indirect path (RD → TV → SI): β = −0.04, 95% CI [−0.17, −0.01]
- Total effect: β = −0.35, p < 0.001
- Interpretation: ~11% of rhythm deviation's effect on synchronization is mediated through tapping variability. The rest is direct — poor rhythm directly undermines dyadic coordination even when behavior is stable.

## Key Takeaways
1. SCZ patients have worse rhythm control (Cohen's d ≈ 0.9), and this directly impairs dyadic synchronization.
2. Hearing B and Hearing Each Other conditions show "normal" coupling because the HC can receive and adjust to the SCZ partner's feedback.
3. The critical deficit emerges in Hearing A/Self — when HC lacks SCZ feedback, external coupling collapses in SCZ-HC but not HC-HC dyads.
4. The "normalcy" of some conditions depends on HC accommodation — the HC implicitly compensates.
5. Medication status did not affect behavioral outcomes (all Fs < 1.88, ps > 0.18).

## Connects To
- **Ch 1**: Supports the interpersonal adjustment hypothesis over coordination-by-synchrony
- **Ch 5**: Neural signatures of this behavioral deficit
- **Ch 7**: Discussion — self-other integration failure as the core mechanism
- **Predictive coding**: The internal coupling bias suggests SCZ patients rely on internal models rather than sensory evidence from partners
