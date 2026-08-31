# Logic Audit

## 1. 建立论证链

为每个核心结论绘制最短链条：

`研究问题/假设 → 设计与测量 → 分析 → 结果 → 解释 → 结论`

每个箭头都应回答“前一步是否足以支持后一步”。区分数据直接显示、作者推论、外部理论和合理但未检验的解释。

## 2. 核心检查

### 研究问题与假设

- 假设是否来自理论、既往证据、预注册或分析前计划；
- 是否根据结果反向增加方向、频段、ROI、参数或条件；
- 理论只支持“可能不同”时，是否被写成过度具体的方向性假设；
- exploratory 结果是否被重新包装为 confirmatory。

### 设计与推断

- 设计是否允许因果推断；
- 操作化是否真正测量标题和结论中的 construct；
- 对照条件是否排除关键替代解释；
- 共同输入、任务结构、测量误差和多重比较是否被合理处理；
- 样本和情境是否支持当前推广范围。

### 分析层级

- individual、dyad、condition、trial、ROI 和 group-level 是否混用；
- pooled condition effect 是否被写成稳定个体差异；
- group-level model fit 是否被写成参与者策略；
- condition-level behavioral、EEG 和 model patterns 是否在没有 cross-level test 时被称为 convergence、dissociation 或 mechanism。

### 统计结论

- `p > .05` 是否被写成无效应或无关系；
- 多重比较校正、置信区间和不确定性是否与表述一致；
- effect direction、condition labels、样本数和数值是否跨正文、图表一致；
- 相关是否被写成因果，预测是否被写成解释机制。

### 跨章节一致性

对同一 finding 比较标题、摘要、Results、Discussion 和 Conclusion。检查是否从“associated”漂移为“caused”，从“consistent with”漂移为“demonstrates”，或把间接/模型派生 construct 写成直接测量。

### 段落与全篇结构

- Introduction 的 gap 是否由证据支持，并由当前设计真正回应；
- Discussion 的理论贡献是否对应 Introduction 建立的 gap；
- 结论是否引入新结果、理论或文献；
- 相邻段落是否存在真实逻辑关系，而非只靠连接词；
- 是否存在循环论证、偷换概念、错误二分、过度概括或忽略替代解释。

## 3. 标签

- `LOGIC_GAP`：推理链缺少必要桥梁。
- `DESIGN_INFERENCE_MISMATCH`：设计不足以支持结论。
- `CAUSAL_OVERREACH`：非因果证据被写成因果。
- `MECHANISM_OVERREACH`：未直接检验的机制被写成已证实。
- `LEVEL_MISMATCH`：分析层级与结论层级不一致。
- `HARKING_RISK`：假设疑似由结果反推；没有过程证据时用“风险”而非定论。
- `CLAIM_STRENGTH_DRIFT`：同一发现跨章节强度升级或不一致。
- `INTERNAL_CONTRADICTION`：文本、数值、标签或方向内部矛盾。
- `ALTERNATIVE_EXPLANATION_OMITTED`：关键替代解释被忽略。
- `GAP_DESIGN_MISMATCH`：设计没有实际解决所宣称的 research gap。
- `CIRCULAR_REASONING`：结论被用作自身前提。
- `SCOPE_OVERGENERALIZATION`：推广超出样本、任务或证据范围。

## 4. 输出表

| 位置 | 前提/证据 | 当前推论 | 标签 | 严重度 | 为什么不成立或不充分 | 最小修复建议 |
|---|---|---|---|---|---|---|

严重度使用 `BLOCKING`、`MAJOR`、`MINOR`。不要仅因不同理论解释可行就判逻辑错误；说明哪些是确定缺陷，哪些只是合理替代解释。
