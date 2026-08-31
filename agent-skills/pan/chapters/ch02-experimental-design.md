# Chapter 2: Methods — Experimental Design & Participants

## Core Idea
The joint finger-tapping paradigm with controlled auditory coupling conditions, combined with fNIRS hyperscanning, creates a tractable experimental model for measuring real-time social coordination in schizophrenia — separating internal (self-driven) from external (partner-driven) coupling.

## Frameworks Introduced

- **Joint Finger-Tapping Paradigm** (Konvalinka et al., 2010): Two participants tap an isochronous rhythm (120 bpm) together while receiving controlled auditory feedback.
  - When to use: To quantify interpersonal synchronization in a simple, well-controlled motor coordination task.
  - How: Participants tap with their right index finger on sensor pads. After a metronome cue (8 beats), they continue tapping without the metronome, receiving auditory feedback from either self or partner depending on condition.

- **Four-Condition Coupling Manipulation**: Systematically varies who hears whom to isolate coupling direction:
  - **Hearing Self (non-coupled)**: Both hear only their own beats → baseline internal coupling
  - **Hearing Each Other (bidirectionally coupled)**: Both hear each other's beats → mutual external coupling
  - **Hearing A (unidirectionally coupled)**: Both hear only Participant A → one-way coupling
  - **Hearing B (unidirectionally coupled)**: Both hear only Participant B → reverse one-way coupling
  - When to use: To disentangle internal vs. external contributions to synchronization and identify direction-specific deficits.

## Key Concepts
- **Tap Arduino**: Arduino-based microcontroller providing low-latency auditory feedback for sensorimotor synchronization experiments.
- **HC-HC dyad**: Healthy control paired with healthy control (reference group, N=44 dyads).
- **SCZ-HC dyad**: Schizophrenia patient paired with healthy control (clinical group, N=35 dyads).
- **Role assignment**: In SCZ-HC dyads, the patient always takes Role B; in HC-HC dyads, roles are random.
- **PANSS (Positive and Negative Syndrome Scale)**: 30-item clinician-rated instrument assessing SCZ symptoms on a 7-point scale, decomposed into 4 dimensions: positive, negative, affective, cognitive.
- **SCID-5**: Structured Clinical Interview for DSM-5, used for patient diagnosis confirmation.

## Mental Models
- Think of the four coupling conditions as a **2×2 between-person information flow matrix**: each cell reveals whether information flows from A→B, B→A, both, or neither.
- Think of the dyad as the **unit of analysis**, not the individual — the key measurements are interpersonal (synchronization index, IBS) not intrapersonal.

## Anti-patterns
- **Ignoring role asymmetry**: In clinical dyads, Role B is always the patient. Main effects of Role must be interpreted in context of Group×Role interactions.
- **Assuming equal task difficulty across conditions**: Hearing Self is fundamentally different from the coupled conditions — it's not just "less coupling," it's a different coordination regime.

## Worked Example
**Trial structure**: Each condition has 10 trials. One trial:
1. Metronome plays 8 beats at 120 bpm (500ms ISI) → participants synchronize to the metronome.
2. Metronome stops → participants continue tapping, now receiving auditory feedback per their assigned condition.
3. After 32 total button presses (both participants combined), the trial auto-ends.
4. Order of 4 conditions is randomized across dyads. Total of 40 trials (4 conditions × 10 trials).

**fNIRS setup during task**: Two NirSmart-6000A devices with 21 sources + 16 detectors each → 48 channels per participant. Optodes placed over standard 10-20 system locations. Source-detector distance ~3 cm. Sampling at 11 Hz, two wavelengths (730nm, 850nm).

## Key Takeaways
1. The four-condition design isolates the direction of coupling (none, bidirectional, A→both, B→both).
2. Always assigning the SCZ patient to Role B controls for role effects while enabling Group comparison via Role A (always HC).
3. PANSS 4-dimensional decomposition (positive, negative, affective, cognitive) is more stable and generalizable than the traditional 3-subscale structure.
4. 180-second resting-state fNIRS collected at the start provides baseline for z-score normalization.

## Connects To
- **Ch 1**: Introduction — operationalizes the Kuramoto model's internal/external coupling distinction
- **Ch 3**: Data analysis pipeline — how behavioral indices and neural metrics are computed from this design
- **Ch 4**: Behavioral results from these four conditions
