# AI-Style Prose Risk Audit

## 1. 定义边界

“AI 味”不是可验证的作者身份属性。本审计只识别可观察、可解释、可修改的写作模式：模板化修辞、重复功能、低信息密度、元话语和不必要的防御性表达。

不得根据单个词、短语、破折号、句长、词频或 detector 分数判断 AI 写作。常见表达只有在上下文中不承担必要科学功能时才构成风险。

## 2. 检查维度

### 修辞脚手架

检查 `Taken together`、`Overall`、`These findings suggest`、`Notably` 等表达是否承载新信息。若删除后科学内容不变，可能是 `PROSE_GENERIC_SUMMARY` 或 `PROSE_FORMULAIC_TRANSITION`；若用于准确限定证据，则保留。

### 重复与信息密度

建立 claim repetition map。一个发现首次完整呈现后，再次出现应增加解释、比较、边界或意义。仅换词重复标为 `PROSE_REPEATED_CONCLUSION`。区分必要的摘要回顾与同一章节内冗余复述。

### 段落功能

为每段标记主要功能：背景、gap、假设、方法、结果、解释、替代解释、贡献、局限或结论。多个相邻段落功能相同且无新增证据时，考虑合并。不要强迫每段都有主题句、总结句和过渡句。

### 元话语与残留

识别写作过程残留、给审稿人的回应语气、占位符、版本说明、机械预告、重复 caveat，以及“本文将在下文……”但无导航价值的表达。

### 过度防御或宣传

同一 claim 应精确校准一次，不要连续堆叠 may/might/could/cannot demonstrate。反向也要检查 `reveals`、`proves`、`groundbreaking`、`robust` 等超出证据的宣传性语言。

### 具体性

优先具体变量、条件和方向，而非抽象的“X is important”“provides a new perspective”。但不要为了更直接而删除必要不确定性或限定范围。

## 3. 标签

- `PROSE_REPETITION`
- `PROSE_GENERIC_SUMMARY`
- `PROSE_FORMULAIC_TRANSITION`
- `PROSE_EXCESSIVE_HEDGING`
- `PROSE_META_DISCOURSE`
- `PROSE_REVIEWER_RESPONSE_VOICE`
- `PROSE_DRAFTING_RESIDUE`
- `PROSE_PROMOTIONAL_LANGUAGE`
- `PROSE_LOW_INFORMATION_DENSITY`
- `PROSE_REDUNDANT_FUNCTION`
- `PROSE_ABSTRACT_NOUN_STACKING`
- `PROSE_VAGUE_INTERPRETATION`

这些标签描述文本风险，不描述作者身份。

## 4. 处理动作

只使用：`KEEP`、`DELETE`、`MERGE`、`MOVE`、`REWRITE`。

建议必须说明：问题如何削弱科学表达，以及处理后必须保留的事实、限定语和引文。审计模式不进行全文 paraphrase。

## 5. 输出表

| 位置 | 原文/模式 | 标签 | 科学表达问题 | 建议动作 | 必须保留内容 |
|---|---|---|---|---|---|
