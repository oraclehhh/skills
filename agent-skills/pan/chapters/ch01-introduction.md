# Chapter 1: Introduction & Background

## Core Idea
Schizophrenia (SCZ) impairs social coordination, but the computational and neural mechanisms underlying this impairment in real-time, naturalistic settings remain poorly understood. This paper combines behavioral tasks, dynamical systems modeling (Kuramoto model), and fNIRS hyperscanning to test two competing hypotheses: the "coordination-by-synchrony" hypothesis (predicting decreased inter-brain synchronization/IBS in SCZ) vs. the "interpersonal adjustment" hypothesis (predicting increased IBS as compensation).

## Frameworks Introduced

- **Coordination-by-Synchrony Hypothesis**: Impaired social functioning in SCZ should manifest as decreased inter-brain synchronization (IBS) because coordination ability is deficient.
  - When to use: As a default null hypothesis for social dysfunction studies.
  - How: Predict that IBS (measured via wavelet coherence between dyad members' brain signals) will be lower in clinical dyads vs. healthy dyads.

- **Interpersonal Adjustment Hypothesis**: Social interaction deficits may require *increased* neural alignment (including IBS) as a compensatory mechanism. Higher social demands → higher IBS.
  - When to use: When studying populations where compensation is expected (ASD, SCZ).
  - How: Test whether IBS is elevated in clinical dyads, and whether elevated IBS positively correlates with behavioral performance.
  - Why it works: Achieving global coordination requires minimizing prediction errors for both self and partner; greater joint attention during interactions raises inter-brain alignment.

- **Kuramoto Model for Interpersonal Synchronization**: Each person is abstracted as a unit of two coupled oscillators (perception + action). Synchronization emerges from internal coupling (within-person perception-action link) and external coupling (between-person information flow).
  - When to use: For modeling dyadic coordination dynamics from behavioral time-series.
  - How: Fit a four-oscillator Kuramoto model to inter-tap interval data, systematically vary coupling weights (i, e), compare simulated cross-correlation lag patterns to real data.

## Key Concepts
- **Social coordination**: Process by which individuals engage in patterned, synchronized behaviors to achieve common goals during social interactions.
- **Interpersonal synchronization**: Elevated temporal alignment between interacting individuals, a hallmark of successful social coordination.
- **Inter-Brain Synchronization (IBS)**: Wavelet coherence between two individuals' brain signals — a multi-brain metric of neural coupling.
- **Hyperscanning**: Simultaneous measurement of brain activity from two or more interacting individuals.
- **fNIRS (functional near-infrared spectroscopy)**: Non-invasive neuroimaging that measures cortical HbO/HbR concentration changes.
- **Hyperbrain network**: The combined intra- and inter-brain connectivity system formed by interacting individuals.
- **Dynamical systems modeling**: Using differential equation models (like the Kuramoto model) to represent how coordinated behavior emerges.

## Mental Models
- Think of a dyad as **two units of dual oscillators** — each person has an internal perception-action loop, and the two people are linked by external sensory feedback.
- Think of IBS as a **neural effort signal** — higher IBS in clinical groups isn't "better", it signals that more neural resources are being recruited to achieve the same or worse behavioral output.
- Think of social coordination as a **coupled dynamical system** where coupling strength (internal vs. external) determines synchronization quality.

## Anti-patterns
- **Studying the social brain in isolation**: Single-brain neuroimaging misses the integration between mentalizing and action-observation networks crucial for real social cognition. Use hyperscanning instead.
- **Assuming higher IBS always means better**: In clinical populations, elevated IBS can reflect compensatory effort, not superior coordination.

## Key Takeaways
1. SCZ social coordination deficits can be understood at three levels: behavioral (synchronization indices), computational (Kuramoto coupling weights), and neural (IBS, intra-brain connectivity).
2. Two competing hypotheses about IBS in SCZ: decreased IBS (coordination-by-synchrony) vs. increased IBS (interpersonal adjustment).
3. Hyperscanning + dynamical systems modeling provides a multi-level mechanistic account unavailable from either method alone.
4. The Kuramoto model decomposes dyadic coordination into internal coupling (within-person) and external coupling (between-person).
5. SCZ patients may show an imbalance: preferentially allocating resources to internal rather than external coupling during interactions.

## Connects To
- **Ch 2**: Methods — the experimental design that operationalizes these constructs
- **Ch 4**: Behavioral results testing the two competing hypotheses
- **Ch 5**: Neural results showing elevated IBS in SCZ-HC dyads
- **Predictive coding / active inference**: Bayesian framework that could extend the Kuramoto model
