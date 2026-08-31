# Chapter 5: Results — Multi-brain Network Alterations in SCZ

## Core Idea
SCZ-HC dyads show a dissociative pattern: *decreased* intra-brain connectivity (within each person) but *increased* inter-brain synchronization (IBS) and Granger causality (between persons). This supports the interpersonal adjustment hypothesis — SCZ patients require stronger neural alignment to compensate for deficient coordination.

## Frameworks Introduced

- **Dissociative Multi-Brain Pattern**: ↓ intra-brain + ↑ inter-brain in clinical dyads.
  - When to use: As a signature of compensatory neural mechanisms in social dysfunction.
  - How: Compare intra-brain synchronization (within-person ROI-ROI coherence) and IBS (between-person ROI-ROI coherence) across groups. Expect opposite directions.

- **Directional Information Flow via Granger Causality**: Identifies which brain region in which person drives the inter-brain coupling.
  - When to use: To determine if the HC or SCZ partner is the "driver" of elevated IBS.
  - How: State-space GCA (MVGC toolbox). Test both directions (A→B, B→A). Report conditional GC values.

## Key Concepts
- **Intra-brain synchronization reduction**: 9 ROI combinations show significantly lower within-person synchronization in SCZ-HC vs. HC-HC dyads. 4 ROI combinations show Group×Role effects (SCZ patients have lower intra-brain sync than HCs within the same dyad).
- **Intra-brain GC reduction**: 9 of 11 ROI combinations show reduced directional within-brain connectivity in SCZ-HC group.
- **Three key IBS connections elevated in SCZ-HC**:
  1. RM_HC — RDLPFC_SCZ: ηp² = 0.05 (motor region to DLPFC)
  2. LM_HC — LA_SCZ: ηp² = 0.03 (motor region to auditory region)
  3. LM_HC — LDLPFC_SCZ: ηp² = 0.05 (motor region to DLPFC)
- **Inter-brain GC**: LF_HC → LA_SCZ is significantly higher in SCZ-HC (0.0025 vs 0.0019, ηp² = 0.05) — HC's frontopolar region drives SCZ's auditory region.
- **12 ROIs (per person)**: RA, RTPJ, RM, RDLPFC, RSFC, RF, LF, LSFC, LDLPFC, LM, LTPJ, LA.

## Mental Models
- Think of the multi-brain network as a **hyperbrain** — the two brains form one interconnected system with both within-brain and between-brain edges. Pathology can manifest at either level.
- Think of elevated IBS as a **neural volume knob turned up** — SCZ-HC dyads need stronger neural coupling to achieve the same (or worse) behavioral output. The "gain" is higher.
- Think of LF→LA Granger causality as an **implicit accommodation pathway** — the HC's frontopolar cortex (involved in behavioral switching and prediction) sends information that the SCZ patient's auditory cortex receives and processes.

## Reference Tables
| Finding Type | Direction in SCZ-HC | Key ROIs | Interpretation |
|---|---|---|---|
| Intra-brain sync | ↓ (9/9 significant) | Multiple | Brain disconnection in SCZ |
| Intra-brain GC | ↓ (9/11 significant) | Multiple | Reduced within-brain information flow |
| Inter-brain sync (IBS) | ↑ (3/144 significant after FDR) | RM-RDLPFC, LM-LA, LM-LDLPFC | Compensatory hyperalignment |
| Inter-brain GC | ↑ (1 significant) | LF_HC → LA_SCZ | HC drives SCZ auditory processing |
| Brain activation | No group effects | All 12 ROIs | Activation level is not the differentiator |

## Worked Example
**Interpreting the 3 elevated IBS connections functionally**:
1. **RM_HC — RDLPFC_SCZ**: HC's motor region couples with SCZ's DLPFC. The DLPFC is implicated in theory of mind and social functioning — SCZ patients may be recruiting cognitive resources to interpret the HC's motor signals.
2. **LM_HC — LA_SCZ**: HC's motor region couples with SCZ's auditory region. Direct sensory-motor coupling — SCZ patients listen more intently to the HC's tapping rhythm.
3. **LM_HC — LDLPFC_SCZ**: HC's motor region couples with SCZ's left DLPFC. This connection positively correlates with behavioral synchronization (r = 0.32) — it's the behaviorally meaningful IBS link.

## Key Takeaways
1. Intra-brain disconnection (↓ sync, ↓ GC) in SCZ is consistent with the dysconnection hypothesis of schizophrenia.
2. Elevated IBS in SCZ-HC dyads supports the interpersonal adjustment hypothesis over the coordination-by-synchrony hypothesis.
3. HC motor regions are the primary IBS hubs — HCs' motor output is the anchor for inter-brain coupling.
4. SCZ DLPFC and auditory regions are the primary IBS targets — SCZ patients recruit cognitive and sensory resources to track the HC.
5. LF_HC → LA_SCZ GC suggests HC frontopolar cortex implicitly accommodates SCZ patients by tracking and predicting their behavior.
6. Brain activation levels do not differ — connectivity (not magnitude) is the neural signature.

## Connects To
- **Ch 4**: Behavioral deficits that the neural alterations compensate for
- **Ch 6**: Brain-behavior correlations and symptom prediction
- **Ch 7**: The hyperbrain network concept and clinical implications
- **van den Heuvel & Fornito (2014)**: Brain network dysconnection in SCZ
