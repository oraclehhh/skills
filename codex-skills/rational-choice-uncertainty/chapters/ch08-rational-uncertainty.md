# Chapter 8: 理性思考“不确定性”

## Core Idea

理性处理不确定性需要明确样本空间、条件概率、基础率和行动后果。图表、概率树和自然频率能显著改善判断。

## Frameworks Introduced

- **Sample Space Construction**: define all possible outcomes before calculating.
- **Bayesian Update**: combine base rates with diagnostic evidence.
- **Natural Frequency Representation**: translate percentages into counts out of a population.
- **Decision Threshold**: act when expected value or expected utility crosses an action boundary.

## Key Concepts

- **Conditional probability**: probability of an event given another event.
- **False positive**: signal says event occurred when it did not.
- **False negative**: signal misses an event that occurred.
- **Probability tree**: branching display of sequential uncertainty.

## Mental Models

Use "1,000 people like this." Convert prevalence, hit rate, and false-alarm rate into counts before forming conclusions.

## Anti-patterns

- **Ignoring prevalence**: interpreting a test result without knowing base rate.
- **Ambiguous sample space**: solving a probability problem without specifying the rules that generate cases.

## Worked Example

For a medical screening test, start with 1,000 comparable people. Count how many have the disease. Apply the test sensitivity to that group and the false-positive rate to the non-disease group. The chance of disease after a positive test is true positives divided by all positives.

## Key Takeaways

1. Probability is clearer when represented as frequencies and trees.
2. Base rates are essential for diagnostic reasoning.
3. Rational action depends on both probability and payoff.

## Connects To

- **Ch 11**: formal decision theory builds on these representations.
- **Ch 12**: descriptive theory explains why people resist them.
