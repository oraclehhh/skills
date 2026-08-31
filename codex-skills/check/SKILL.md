---
name: check
description: 独立核验学术论文、学位论文、综述和研究报告中的引用幻觉、文献身份、主张—证据匹配、无引文重要主张、论证逻辑、结论强度、跨章节一致性、construct-status drift、信息密度、question-led / figure-led narrative，以及常被称为“AI味”的模板化、过度对称、机械总结、过度铺垫、重复 caveat 和低信息密度写作风险。用户提到检查引用真假、citation hallucination、引用是否支持原句、逻辑是否合理、论证漏洞、AI味、机器腔、套话、重复总结、过度铺垫、最终稿审计或修改后复检时都应使用。本 skill 不用 AI detector 判断作者身份；默认只审计，只有用户明确要求修改时才进入证据约束下的最小返修流程，并优先交由 repair skill 执行。
---

# Check

把本 skill 作为独立内容审计层。

目标不是判断文本是否由 AI 创作，而是回答五个可核验问题：

1. 每个重要外部主张是否由真实、可定位的来源支持？
2. 研究问题、设计、分析、结果、解释与结论之间是否存在有效且一致的逻辑链？
3. 核心 construct 在全文中的“证据身份”是否保持一致，没有从派生指标或解释性概念漂移成直接测量机制？
4. 每个段落是否承担必要科学功能，并以足够高的信息密度推进论证？
5. 文本是否存在模板化、过度对称、机械总结、重复 caveat 或其他降低科学表达效率的 prose risk？

优先级为：

**研究事实安全 > 来源真实性 > 主张—证据忠实度 > 推理有效性 > construct-status 一致性 > 结论边界 > 信息密度 > 表达自然度。**

---

# 一、职责边界

- 本 skill 检查内容真实性、引用、逻辑、结构和文风风险。
- 本 skill 不负责判断作者是否使用 AI。
- 本 skill 不把 AI detector、困惑度、词频或单个短语当作作者身份依据。
- 需要撰写或系统重写内容时使用 `neirong`。
- 需要根据审计报告执行系统修复时优先使用 `repair`。
- 需要 DOCX、Word、EndNote、OOXML、字体、颜色或分页检查时使用 `geshi`。
- 审计请求不授权修改原稿。
- 只有用户明确要求“检查并修改”“根据报告返修”等操作时，才进入返修模式。
- 不覆盖唯一源文件；修改时输出新文件并保留修改日志。
- “AI味”在本 skill 中始终指**可观察的文本风险模式**，不是作者身份判断。
- 若目标期刊未指定，不擅自套用 Nature、Science、Cell 等特定期刊风格。
- 若用户明确指定目标期刊，可启动 Target-Journal Prose Fit 模块，但不得把“期刊风格”凌驾于证据边界。

---

# 二、选择模式

根据用户请求选择最小充分范围：

- `FULL_AUDIT`：同时核验引用、逻辑、construct status、结构、信息密度和 prose risk。
- `CITATION_AUDIT`：只核验文献身份、主张—证据关系和漏引。
- `LOGIC_AUDIT`：只核验论证、设计—结论匹配、分析层级、construct status 和跨章节一致性。
- `PROSE_RISK_AUDIT`：只检查模板化、重复、元话语、过度对称、重复 caveat、低信息密度表达，同时保护科学限定语。
- `STRUCTURE_AUDIT`：重点检查 paragraph function、question-led / figure-led narrative、claim repetition、section architecture 和信息密度。
- `TARGET_JOURNAL_AUDIT`：在用户指定期刊时，额外检查 prose fit、readership fit 和 claim presentation；不替代 citation / logic audit。
- `EVIDENCE_CONSTRAINED_REPAIR`：用户已明确授权修改；先核验证据，再做最小返修。若存在 `repair` skill，优先移交给 `repair`。
- `REAUDIT`：将修改稿视为新稿，重新检查完整受影响范围，不只检查改动句。

若用户未限定范围，“引用幻觉 + AI 味 + 逻辑”默认使用：

`FULL_AUDIT`

只生成审计报告，不改正文。

---

# 三、必要输入

尽量取得：

- 完整稿件及稳定的章节/段落定位；
- 完整参考文献表或文献库；
- 用户提供的原始 PDF、补充材料、数据说明或统计结果；
- 可访问的出版商、DOI、PubMed、Crossref、Zotero 或其他可靠来源；
- 研究设计；
- 目标期刊要求（若用户指定）。

缺少材料时：

- 继续完成可完成部分；
- 将受影响项目标为 `UNVERIFIED`；
- 说明缺少什么；
- 说明如何完成核验。

不要用模型记忆补足证据。

---

# 四、核心工作流

## 4.1 建立文稿地图

完整读取目标范围，记录：

- 章节；
- 段落功能；
- 研究问题；
- 假设；
- 方法；
- 核心结果；
- 主要解释；
- 结论；
- 主要外部文献支撑点；
- 关键 construct；
- 关键 figure / table；
- 目标期刊（若有）。

为每个问题提供可复核位置，例如：

`Discussion > Paragraph 3 > Sentence 2`

页码不稳定时不要猜页码。

---

## 4.2 建立 atomic claim inventory

把可独立核验的实质性主张拆成 atomic claims。

例如：

> “Previous studies show that interpersonal synchrony increases trust by enhancing shared neural representations (Smith, 2020).”

至少拆成：

1. previous studies observed a relation between synchrony and trust；
2. synchrony increases trust；
3. the relation is causal；
4. the mechanism is shared neural representations；
5. Smith (2020) 是否分别支持 1–4。

一个句子包含事实、机制和群体推广时，应拆成多个主张分别核验。

优先纳入：

- 外部事实；
- 理论主张；
- 实证结果；
- 方法判断；
- 数字；
- 趋势；
- 比较；
- 因果；
- 机制；
- 共识；
- 首次；
- 普遍性；
- research gap；
- novelty；
- 可能需要引文但当前无引文的重要主张。

---

## 4.3 核验引用

执行 `references/citation-audit.md`。

先确认：

- 文献是否存在；
- 作者；
- 年份；
- 标题；
- 期刊；
- DOI / PMID；
- 正文 citation 与 reference list 是否一致。

然后读取可用的原始证据，最后判断每个 atomic claim 是否得到支持。

核心原则：

> **引用真实存在不等于引用支持当前句子。**

---

## 4.4 核验逻辑

执行 `references/logic-audit.md`。

检查：

- 研究问题 → 设计；
- 设计 → 分析；
- 分析 → 结果；
- 结果 → 解释；
- 解释 → 结论；
- 替代解释；
- 因果边界；
- 分析层级；
- 假设来源；
- construct-status consistency；
- 跨章节 claim-strength drift；
- null result interpretation；
- novelty / gap evidence。

---

## 4.5 核验结构与信息密度

执行：

- paragraph-function map；
- claim repetition map；
- information-density audit；
- question-led / figure-led narrative audit；
- caveat repetition map。

不要只问：

> “这一段写得顺不顺？”

还必须问：

> “这一段是否推进了 scientific question？”

---

## 4.6 核验 AI 风格风险

执行 `references/prose-risk-audit.md`，并强制参考本 skill 的“具体模式库”。

只标记：

- 可观察句法模式；
- 段落组织模式；
- 信息密度问题；
- 科学功能冗余；
- 过度对称；
- 过度总结；
- 过度防御性表达；
- abstract-value language；
- mechanical closure。

不判定 AI 作者身份。

关键词只能作为检索线索，必须结合上下文和段落功能判断。

---

## 4.7 建立阻断问题

以下通常属于 blocking issues：

- 明确错误或不存在的参考文献身份；
- `MISMATCH`；
- 关键 `OVERSTATED`；
- 关键 `UNCITED_CLAIM`；
- 结论与设计、统计结果或分析层级不相容；
- Abstract、Results、Discussion、标题之间出现关键事实矛盾；
- 未经支持的因果、机制、普遍性、共识或 novelty 主张；
- construct status 从 indirect / derived 漂移成 direct / mechanistic；
- 关键来源只能标为 `UNVERIFIED`，导致核心论证无法确认；
- figure / result 与 manuscript narrative 明显冲突。

AI 风格风险通常不是 blocking issue，除非它同时造成：

- claim-strength inflation；
- evidence obscuring；
- factual ambiguity；
- duplicated but inconsistent conclusions；
- 限制条件被修辞覆盖；
- construct status 被语言升级。

---

## 4.8 输出而不越权

按照 `references/report-and-repair.md` 输出：

- 审计摘要；
- claim-level 表；
- 逻辑问题表；
- construct-status 表；
- 文风风险表；
- structure / information-density findings；
- blocking issues；
- 优先级建议。

审计模式中不直接改正文。

若用户已明确授权返修，则先完成审计，再进入 evidence-constrained repair；若存在 `repair` skill，优先移交给 `repair`。

---

# 五、科学安全约束

未经作者提供证据并明确授权，不得改变或补造：

- 样本；
- 设计；
- 变量；
- 方法；
- 模型设定；
- 数值；
- 统计量；
- 显著性；
- 效应量；
- 置信区间；
- 图表数据；
- 研究问题；
- 预注册假设；
- 本研究事实。

材料内部冲突且无法判断正确版本时，标记：

`[AUTHOR VERIFICATION REQUIRED]`

不要选择“看起来更合理”的版本。

不得为了去除“AI 味”而：

- 删除必要引文；
- 删除必要限定语；
- 随机改变句式；
- 随机改变句长；
- 把相关写成因果；
- 提高机制语言；
- 提高确定性语言；
- 用同义词替换掩盖证据缺口；
- 把正常、准确的学术表达仅因常见而删除。

---

# 六、证据规则

- 优先使用用户提供的原文、正式全文或可靠数据库记录。
- 搜索片段、AI 摘要、其他论文的转述和模型记忆只能帮助发现来源，不能支持 `VERIFIED`。
- 只有摘要时标记 `ABSTRACT_ONLY`，且只核验摘要明确表达的内容。
- 记录真实 locator：页码、章节、段落、表或图；没有稳定 locator 时明确说明。
- 不得虚构 DOI、页码、引文、原文证据或检索过程。
- citation cluster 必须拆分到 atomic claim 层面。
- 一个来源只支持句子的一部分时，不得整句判 `VERIFIED`。

---

# 七、统一判定

引用判定只使用：

- `VERIFIED`：原始证据明确支持该 atomic claim 及其强度和范围。
- `PARTIALLY_SUPPORTED`：仅支持主张的一部分或更窄范围。
- `OVERSTATED`：方向可能有依据，但因果、机制、范围或确定性超过来源。
- `MISMATCH`：来源与主张实质不符或支持相反结论。
- `REFERENCE_NOT_FOUND`：经合理身份检索仍未定位到对应文献，但不足以断言伪造。
- `FABRICATED_REFERENCE`：只有在元数据存在明确矛盾且经过充分权威检索后才使用，并写明证据。
- `UNCITED_CLAIM`：重要外部主张缺少应有引文。
- `UNVERIFIED`：因来源不可访问或证据不足无法可靠判断。

逻辑问题使用：

- `LOGIC_DESIGN_CLAIM_MISMATCH`
- `LOGIC_CAUSAL_LEAP`
- `LOGIC_MECHANISM_LEAP`
- `LOGIC_SCOPE_LEAP`
- `LOGIC_LEVEL_MISMATCH`
- `LOGIC_ALTERNATIVE_IGNORED`
- `LOGIC_HYPOTHESIS_RESULT_DRIFT`
- `LOGIC_CROSS_SECTION_CONFLICT`
- `LOGIC_CONCLUSION_EXCEEDS_RESULTS`
- `LOGIC_NOVELTY_UNSUPPORTED`
- `LOGIC_CONSTRUCT_STATUS_DRIFT`
- `LOGIC_EVIDENCE_NARRATIVE_MISALIGNMENT`

文风风险使用：

- `PROSE_NOT_X_BUT_Y`
- `PROSE_NOT_ONLY_BUT_ALSO`
- `PROSE_GENERIC_SUMMARY`
- `PROSE_FORMULAIC_TRANSITION`
- `PROSE_EXCESSIVE_HEDGING`
- `PROSE_META_DISCOURSE`
- `PROSE_REVIEWER_RESPONSE_VOICE`
- `PROSE_REPETITIVE_PARALLELISM`
- `PROSE_LOW_INFORMATION_DENSITY`
- `PROSE_PROMOTIONAL_CLAIM`
- `PROSE_REPEATED_CONCLUSION`
- `PROSE_REDUNDANT_PARAGRAPH_FUNCTION`
- `PROSE_OVEREXPLAINED_CAVEAT`
- `PROSE_THREE_PART_RHETORIC`
- `PROSE_ABSTRACT_NOUN_STACKING`
- `PROSE_MECHANICAL_PARAGRAPH_CLOSURE`
- `PROSE_REPEATED_EPISTEMIC_CAVEAT`
- `PROSE_ANALYSIS_LED_NARRATIVE`

---

# 八、AI 风格风险：判定原则

“AI味”不能根据单个词判定。

例如：

> “Taken together, these findings suggest...”

只出现一次，而且确实整合了多组结果时，完全可能是正常学术写法。

真正需要标记的是：

1. 同一模板高频重复；
2. 模板没有承担新的科学功能；
3. 句子可删除而不损失信息；
4. 模板把简单结果包装成复杂论证；
5. 模板反复制造“先否定、再升级、再总结”的人工对称结构；
6. 句子主要在告诉读者“如何理解这句话”，而不是直接提供科学信息；
7. 一段中抽象评价词显著多于变量、条件、效应和证据；
8. 同一个 caveat 在多个章节机械重复；
9. 同一个 finding 在多个章节只是换词重述；
10. narrative 由分析步骤驱动，而不是 scientific question 驱动。

所以：

> **检测模式，不检测词。**

---

# 九、具体模式库 A：最典型的“不是……而是……”

## 9.1 `不是 X，而是 Y`

典型中文：

> “这一结果并不是简单反映运动同步，而是揭示了个体间自我—他人整合机制。”

典型英文：

> “This pattern does not simply reflect motor synchrony; rather, it reveals an interpersonal self–other integration mechanism.”

风险：

- 先人为构造一个较弱解释 X；
- 再用 `而是 / rather` 强行升级成更强解释 Y；
- Y 往往是机制性、理论性、价值更高的表述；
- 容易把 Level 1 数据直接推到 Level 3 机制。

检查：

1. 原文是否真的排除了 X？
2. 是否有设计能够区分 X 与 Y？
3. Y 是否被直接测量？
4. `reveals` 是否超过证据上限？

若没有：

标记：

`PROSE_NOT_X_BUT_Y`

如果同时越过证据边界：

再加：

`LOGIC_MECHANISM_LEAP` 或 `OVERSTATED`

审计模式只给修复方向，不直接改稿。

---

## 9.2 `不仅 X，而且 Y`

典型中文：

> “该结果不仅表明个体能够调整运动行为，而且揭示了社会互动中的预测性控制机制。”

典型英文：

> “These findings not only show behavioral adaptation but also reveal a predictive control mechanism in social interaction.”

风险：

- 前半句通常是直接结果；
- 后半句突然提升到机制；
- “not only...but also...”制造人工递进；
- 常见于把普通结果包装成更大贡献。

检查：

- “而且”后的部分是否有独立证据？
- 如果删掉“不仅……而且……”，科学信息是否更清楚？
- 是否只是为了增加“重要性”？

标签：

`PROSE_NOT_ONLY_BUT_ALSO`

如有 claim-strength 升级，再标逻辑问题。

---

## 9.3 `并非仅仅……更重要的是……`

典型：

> “这一效应并非仅仅意味着时间上的同步，更重要的是，它说明伙伴信息已经被整合进自身运动控制。”

风险：

- “更重要的是”属于评价性元话语；
- 后半句常常把 indirect inference 写成 direct conclusion；
- 容易人为制造 hierarchy。

标签：

`PROSE_META_DISCOURSE`

可能附加：

`LOGIC_MECHANISM_LEAP`

---

# 十、具体模式库 B：机械总结与拔高

## 10.1 `这些结果表明/说明/提示`

典型：

> “These findings suggest that interpersonal coordination is a complex and dynamic process.”

风险：

- “complex and dynamic”通常不可证伪、信息量低；
- 前面的具体变量被抽象词替代；
- 删除后可能没有任何科学信息损失。

标签：

`PROSE_GENERIC_SUMMARY`

检查：

> 删除这句话后，是否损失新的变量、方向、条件或理论关系？

如果没有，属于高风险模板句。

---

## 10.2 `Taken together / Collectively / Overall`

典型：

> “Taken together, these findings highlight the importance of flexible self–other integration in interpersonal coordination.”

风险：

- `highlight the importance of` 是典型价值判断；
- “importance”没有告诉读者具体发现；
- 常用于段尾机械收束。

标签：

`PROSE_MECHANICAL_PARAGRAPH_CLOSURE`

但如果句子真正整合多个结果，例如：

> “Taken together, the three analyses show that partner weighting increased only in the alternating condition and only during late adaptation.”

这种句子有新的 synthesis，可保留。

---

## 10.3 `Importantly / Notably / Critically`

典型：

> “Importantly, this effect was observed across all participants.”

如果“across all participants”是关键结果，`Importantly` 本身可能多余，但科学信息真实。

若连续多段：

> “Importantly...”
> “Notably...”
> “Critically...”

而每句都只是引入普通结果：

标记：

`PROSE_FORMULAIC_TRANSITION`

---

# 十一、具体模式库 C：三段式与过度对称修辞

## 11.1 `A, but B, therefore C`

典型：

> “Although synchrony has been widely studied, its role in self–other weighting remains unclear. The present findings therefore provide a novel perspective on how interpersonal coordination is dynamically regulated.”

风险：

- 第一句制造 gap；
- 第二句立刻用 `therefore` 宣称 novelty；
- 中间缺少具体证据链。

标签：

`PROSE_THREE_PART_RHETORIC`

同时检查：

- `widely studied` 是否有 citation；
- `remains unclear` 是否有 systematic basis；
- `novel perspective` 是否只是宣传。

---

## 11.2 `一方面……另一方面……因此……`

典型：

> “一方面，个体需要维持自身运动目标；另一方面，他们还需要整合伙伴信息。因此，人际协调依赖一种动态的自我—他人平衡机制。”

风险：

- 对称性漂亮，但不一定是实证推理；
- “因此”可能把直觉性描述升级成理论结论。

标签：

`PROSE_REPETITIVE_PARALLELISM`

如结论超证据：

`LOGIC_MECHANISM_LEAP`

---

## 11.3 `既……又……同时……`

典型：

> “该机制既保证个体运动稳定性，又支持伙伴适应，同时促进更高水平的社会协调。”

风险：

- 一个 construct 被分配多个功能；
- 常见于没有逐项证据的“功能堆叠”。

检查：

每个功能是否有独立证据。

如果没有：

`PROSE_ABSTRACT_NOUN_STACKING`

---

# 十二、具体模式库 D：过度限定与防御性语言

## 12.1 `consistent with, but does not demonstrate`

单次使用通常合理。

高风险情况：

> “This pattern is consistent with X but does not demonstrate X.”
>
> “It should therefore not be interpreted as evidence for Y.”
>
> “Rather, it may reflect Z.”
>
> “However, this possibility cannot be ruled out.”

一个段落连续四层防御。

风险：

- 读者注意力被“如何不误读”占满；
- 主要结果反而不清楚；
- 常见于模型过度追求谨慎。

标签：

`PROSE_OVEREXPLAINED_CAVEAT`

原则：

> 同一个 epistemic limitation 通常精确校准一次即可。

---

## 12.2 `may / might / could / possibly` 连续堆叠

典型：

> “This effect may possibly reflect a mechanism that could potentially contribute to...”

风险：

- hedge 叠加；
- 语义没有更精确，只更模糊。

标签：

`PROSE_EXCESSIVE_HEDGING`

---

# 十三、具体模式库 E：元话语

## 13.1 告诉读者“重点是什么”

典型：

> “The important point here is that...”
>
> “The key takeaway is that...”
>
> “What is particularly important is...”
>
> “这里真正关键的是……”

风险：

- 句子在评论论证，而不是提供论证。

标签：

`PROSE_META_DISCOURSE`

除非是在明确的 review / perspective 体裁中有必要，否则优先建议直接陈述科学内容。

---

## 13.2 告诉读者“应该怎么解释”

典型：

> “A more appropriate interpretation is...”
>
> “It is more defensible to view this pattern as...”
>
> “这一结果更合理的解释是……”

风险：

- 可能是 reviewer-response 残留；
- 应直接说明证据和 interpretation，而不是评论写作选择。

标签：

`PROSE_REVIEWER_RESPONSE_VOICE`

---

# 十四、具体模式库 F：低信息密度抽象词

高风险抽象表达：

- important implications；
- valuable insights；
- novel perspective；
- deeper understanding；
- complex dynamics；
- multifaceted process；
- intricate relationship；
- broader significance；
- important role；
- critical mechanism；
- dynamic interplay；
- meaningful contribution；
- valuable framework；
- rich understanding；
- provides a foundation；
- sheds light on；
- underscores the importance；
- highlights the complexity。

中文常见：

- “具有重要意义”；
- “提供了新的视角”；
- “深化了我们对……的理解”；
- “揭示了复杂而动态的关系”；
- “凸显了……的重要性”；
- “为进一步研究奠定了基础”；
- “提供了有价值的启示”；
- “丰富了现有理论框架”。

这些词不自动删除。

检查：

1. 后面是否有具体变量？
2. 是否说明“新”在哪里？
3. 是否说明“重要”对哪个理论问题重要？
4. 删除后是否损失事实？

如果没有：

标记：

`PROSE_LOW_INFORMATION_DENSITY`

---

# 十五、具体模式库 G：机械段尾

连续多个段落若均以类似句式结束：

> “These findings therefore suggest...”
>
> “Taken together, these results indicate...”
>
> “Overall, this pattern highlights...”
>
> “Thus, the present findings demonstrate...”

即使每句单独都通顺，全文级上仍可能出现机器腔。

检查：

- 是否每段都强制 closure；
- 是否 closure 只是重述上一句；
- 是否“结果 → 抽象总结”模板重复。

标签：

`PROSE_MECHANICAL_PARAGRAPH_CLOSURE`

---

# 十六、具体模式库 H：重复同一结论

例如：

Results 末尾：

> “Partner weighting increased during alternating coordination.”

Discussion 开头：

> “The main finding was that partner weighting increased during alternating coordination.”

Discussion 第二段末尾：

> “Thus, alternating coordination appears to increase partner weighting.”

Conclusion：

> “In conclusion, partner weighting was greater during alternating coordination.”

如果后续没有增加：

- mechanism；
- literature comparison；
- boundary；
- implication；

则属于换词重复。

标签：

`PROSE_REPEATED_CONCLUSION`

原则：

> 一个 finding 第一次完整报告，之后只能在新的解释层级下再次出现。

---

# 十七、具体模式库 I：过度平行和排比

典型：

> “At the behavioral level..., at the interpersonal level..., and at the theoretical level...”

或：

> “This finding informs how people act, how they adapt, and how they understand others.”

风险：

- 人工三分；
- 分类可能不是数据驱动；
- 常用于制造完整感。

如果每一层都有独立证据，可保留。

否则：

`PROSE_REPETITIVE_PARALLELISM`

---

# 十八、具体模式库 J：伪 gap 与伪 novelty

典型：

> “Although many studies have examined interpersonal coordination, few have considered self–other weighting.”

风险：

- `many` 与 `few` 都是领域数量判断；
- 通常需要系统检索依据。

更高风险：

> “To our knowledge, no previous study has...”

如果没有系统检索：

标记：

`UNCITED_CLAIM`

或：

`LOGIC_NOVELTY_UNSUPPORTED`

文风上可附：

`PROSE_PROMOTIONAL_CLAIM`

---

# 十九、具体模式库 K：把限制写成“亮点”

典型：

> “Although the study used a small homogeneous sample, this controlled design allowed us to isolate the core mechanism.”

风险：

- limitation 被修辞性反转成 mechanism evidence；
- 可能掩盖 generalizability 问题。

逻辑标签：

`LOGIC_SCOPE_LEAP`

文风标签：

`PROSE_PROMOTIONAL_CLAIM`

---

# 二十、具体模式库 L：假平衡结构

典型：

> “The findings neither support a purely individual account nor imply complete interpersonal coupling; instead, they point to a flexible middle ground.”

风险：

- 看起来“平衡、成熟”；
- 但 `middle ground` 可能不是数据定义的理论位置；
- 属于典型模型式折中表达。

标签：

`PROSE_NOT_X_BUT_Y`

必要时：

`LOGIC_MECHANISM_LEAP`

---

# 二十一、具体模式库 M：定义—拔高—意义链

典型：

> “Self–other weighting refers to the relative contribution of self-generated and partner-related information. This dynamic balance may enable flexible interpersonal coordination. Understanding this balance therefore provides important insights into social interaction.”

风险：

- 第一层是定义；
- 第二层是功能推测；
- 第三层是意义拔高；
- 句子之间证据层级逐步升高，但 citation 可能只支持第一层。

检查：

每一句分别找证据。

标签可组合：

- `PARTIALLY_SUPPORTED`
- `PROSE_GENERIC_SUMMARY`
- `PROSE_PROMOTIONAL_CLAIM`

---

# 二十二、具体模式库 N：先替读者设疑，再自己回答

典型：

> “One might ask whether this effect simply reflects task difficulty. However, this explanation is unlikely because...”

风险：

- 若 manuscript 没有真实理论争议或 reviewer comment，这种“自问自答”容易显得生成式；
- 但如果确实在处理重要 alternative explanation，则可以保留。

标签：

`PROSE_META_DISCOURSE`

真正存在 alternative explanation 时应同时执行逻辑核验，而不是仅因句式删除。

---

# 二十三、具体模式库 O：段落功能过满

一个段落同时完成：

1. 回顾文献；
2. 重述结果；
3. 提出机制；
4. 排除 alternative；
5. 说明 limitation；
6. 宣称意义。

风险：

- 常见于为了“完整”把所有功能塞进一段；
- 每句话都对，但段落缺少主功能。

标签：

`PROSE_REDUNDANT_PARAGRAPH_FUNCTION`

检查方法：

给段落只选一个 primary function。

如果无法选出：

说明段落可能过载。

---

# 二十四、具体模式库 P：引用与修辞联动风险

典型：

> “A large body of research has consistently demonstrated that interpersonal synchrony robustly enhances social bonding (A; B; C; D).”

这句话包含多个高风险成分：

- `large body of research`
- `consistently`
- `demonstrated`
- `robustly`
- `enhances`

即使引用都真实，也必须逐层核验：

1. 是否真的是 large body？
2. 是否 consistent？
3. 是否 causal？
4. 是否 robust？
5. social bonding 的定义是否一致？

不能因为 citation cluster 很长就判定可靠。

---

# 二十五、具体模式库 Q：中英文风险词只作为检索入口

以下词出现时，只触发上下文检查，不自动判错。

英文：

- importantly
- notably
- critically
- taken together
- collectively
- overall
- therefore
- rather
- not merely
- not simply
- highlights
- underscores
- demonstrates
- reveals
- sheds light on
- provides insight into
- complex
- dynamic
- multifaceted
- robust
- novel
- important
- meaningful

中文：

- 值得注意的是
- 重要的是
- 尤其值得指出的是
- 综合来看
- 总体而言
- 因此
- 并非……而是……
- 不仅……而且……
- 不只是……更是……
- 进一步说明
- 充分表明
- 有力证明
- 揭示了
- 凸显了
- 深化了理解
- 提供了新视角
- 具有重要意义
- 复杂而动态
- 多层次
- 多维度
- 系统性
- 全面地

原则：

> **关键词出现 ≠ prose risk 成立。**

> **关键词 + 重复模板 + 低信息密度 + 无新增科学功能，才构成真正的 prose risk。**

---

# 二十六、Information Density Audit

不要只检查“句子是否像 AI”。

还要检查：

> **这一段有多少 scientific payload，有多少 rhetorical payload？**

## 26.1 Scientific payload

包括：

- 新事实；
- 新结果；
- quantitative evidence；
- source evidence；
- theoretical contrast；
- alternative explanation；
- boundary condition；
- limitation；
- direct implication；
- methodological rationale。

## 26.2 Rhetorical payload

包括：

- 说结果“重要”；
- 提醒读者“关键点”；
- 再次总结；
- 对称化转折；
- 写作过程评论；
- generic significance；
- vague novelty；
- mechanical closure；
- 重复 caveat；
- 不增加信息的抽象名词。

## 26.3 段落分类

每个段落内部可归入：

- `ESSENTIAL`
- `USEFUL_BUT_COMPRESSIBLE`
- `BETTER_IN_METHODS`
- `BETTER_IN_EXTENDED_DATA`
- `BETTER_IN_SUPPLEMENT`
- `REDUNDANT`
- `REMOVABLE`

这些标签是审计建议，不直接移动稿件。

## 26.4 例子

低信息密度：

> “Taken together, these findings highlight the important and dynamic role of self–other integration in interpersonal coordination.”

高信息密度：

> “Across auditory and audiovisual trials, partner weighting increased during alternating but not simultaneous coordination.”

前者主要是 rhetorical payload。

后者主要是 scientific payload。

---

# 二十七、Question-led / Figure-led Narrative Audit

检查 manuscript 的叙事顺序究竟由什么驱动。

## 27.1 Analysis-led narrative

典型：

> “First, we analyzed theta. Next, we analyzed alpha. We then examined beta. Finally, we analyzed gamma.”

风险：

- 顺序来自 analysis inventory；
- 读者不知道 scientific question；
- 容易形成“统计输出列表”。

标签：

`PROSE_ANALYSIS_LED_NARRATIVE`

若结果顺序与 central question 明显错位：

`LOGIC_EVIDENCE_NARRATIVE_MISALIGNMENT`

## 27.2 Question-led narrative

更合理的结构：

> “We first tested whether coordination mode altered inter-brain coupling. The effect was confined to theta-band wPLI...”

这里：

scientific question → result → quantitative evidence

## 27.3 Figure-led audit

对每张主图检查：

- scientific question；
- key result；
- evidence ceiling；
- narrative role；
- current manuscript location；
- 是否与 section order 一致；
- 是否被正文过度解读；
- 是否重要图反而被埋没。

Figure-led narrative 不等于：

> “按 Figure 1、Figure 2、Figure 3 顺序念图。”

真正目标是：

> **让 figure 服务 scientific question。**

---

# 二十八、Results Narrative Audit

Results 应尽量形成：

**scientific question → key result → quantitative evidence → immediate implication**

检查是否存在：

- statistic → statistic → statistic → generic summary；
- analysis-by-analysis inventory；
- 每个 subsection 末尾机械加入 “These findings indicate...”；
- 大量 pairwise comparisons 逐项口述但不改变解释；
- 图表已经表达的数据被正文完整重复；
- 文献综述大量进入 Results；
- observation 与 mechanism interpretation 混写。

审计模式只提出压缩或重排建议。

不得为了“更紧凑”建议删除必要统计信息。

---

# 二十九、Caveat Repetition Map

不仅检查 hedge 是否过多，还要检查：

> **同一个 epistemic limitation 是否跨章节被重复解释。**

例如：

Introduction：

> “Inter-brain synchrony does not necessarily imply information transfer.”

Results：

> “This pattern should not be interpreted as evidence of information transfer.”

Discussion：

> “Importantly, synchrony alone cannot demonstrate direct information transfer.”

Conclusion：

> “These findings therefore should not be taken as demonstrating information transfer.”

每句单独看都严谨。

全文看却可能是：

`PROSE_REPEATED_EPISTEMIC_CAVEAT`

## 29.1 Caveat 类型

追踪：

- causality caveat；
- mechanism caveat；
- generalizability caveat；
- sample caveat；
- measurement caveat；
- information-transfer caveat；
- model interpretation caveat；
- null-result caveat。

## 29.2 判断

如果同一 caveat 在多个章节重复：

检查每次是否承担不同功能。

例如：

- Introduction：限定研究问题；
- Discussion：解释结果边界。

这可能合理。

如果只是换词重复：

标记为重复。

原则：

> **Calibrate each epistemic boundary once per necessary rhetorical function.**

---

# 三十、Construct-Status Consistency Audit

对全文关键 construct 建立“证据身份”。

允许状态：

- `DIRECTLY_MEASURED`
- `DERIVED_METRIC`
- `MODEL_PARAMETER`
- `INFERRED_CONSTRUCT`
- `THEORETICAL_INTERPRETATION`

## 30.1 典型漂移

Results：

> model-derived partner-weight parameter

Discussion：

> self–other weighting

Abstract：

> self–other integration

Title：

> neural mechanisms of self–other representation

如果这些概念在全文中越来越“实”：

标记：

`LOGIC_CONSTRUCT_STATUS_DRIFT`

## 30.2 检查问题

对每个关键 construct 问：

1. 它直接测量了吗？
2. 它是派生指标吗？
3. 它来自模型参数吗？
4. 它只是理论解释吗？
5. 标题/摘要是否把 interpretive construct 写成 direct measurement？
6. Discussion 是否把 model parameter 写成心理机制？
7. neural synchrony 是否被写成 literal information transmission？
8. behavioral adaptation 是否被写成 self–other representation？

## 30.3 Evidence ceiling

construct 在任何章节中的表述不得高于其最强可辩护状态。

---

# 三十一、Epistemic-Level Consistency

对同一 finding 检查：

- heading；
- Results；
- Discussion；
- Abstract；
- title。

不得出现 claim-strength drift。

重点词：

- promotes；
- reveals；
- demonstrates；
- proves；
- causes；
- drives；
- mechanism；
- communication；
- representation；
- integration；
- robust；
- established；
- definitive。

例如：

Results：

> “X was associated with Y.”

Discussion：

> “X may contribute to Y.”

Abstract：

> “X promotes Y.”

Title：

> “X drives Y.”

这是典型：

`LOGIC_CROSS_SECTION_CONFLICT`

或：

`LOGIC_CONCLUSION_EXCEEDS_RESULTS`

---

# 三十二、Heading Audit

检查：

- Results heading；
- Discussion heading；
- Abstract subheading（若有）；
- Title。

Heading 应：

- short；
- factual；
- specific；
- non-promotional；
- evidence-calibrated。

高风险：

- `X reveals...`
- `X promotes...`
- `X demonstrates...`
- `X establishes...`
- `X drives...`

如果正文仅支持 association 或 derived construct：

必须标记。

---

# 三十三、Introduction Audit

Introduction 应形成：

1. broad scientific problem；
2. what is known；
3. unresolved problem；
4. why current design addresses it；
5. present study；
6. hypotheses / RQs。

检查：

- background 过长；
- gap 人为夸大；
- `few studies / no previous study / first` 无系统依据；
- 提前塞入完整 Discussion；
- 提前解释所有 caveats；
- reviewer-response voice；
- citation inventory 代替论证；
- construct 定义与研究实际测量不一致。

标签可包括：

- `LOGIC_NOVELTY_UNSUPPORTED`
- `PROSE_REVIEWER_RESPONSE_VOICE`
- `PROSE_LOW_INFORMATION_DENSITY`

---

# 三十四、Discussion Synthesis Audit

Discussion 不应机械按照：

Result 1 → repeat  
Result 2 → repeat  
Result 3 → repeat

组织。

优先检查：

- central finding；
- conceptual meaning；
- literature relationship；
- alternative explanation；
- boundary condition；
- limitation；
- broader implication。

如果 Discussion 只是 Results 换词重述：

`PROSE_REPEATED_CONCLUSION`

如果每段都：

finding → caveat → alternative → summary

且模板重复：

`PROSE_THREE_PART_RHETORIC`

---

# 三十五、Target-Journal Prose Fit

只有用户明确指定目标期刊时启用。

## 35.1 通用原则

Target-journal fit 不能覆盖：

- citation integrity；
- evidence ceiling；
- scientific fact；
- construct status；
- design limitations。

## 35.2 Nature-style audit

若 target journal = Nature / Nature family：

检查：

- specialist precision；
- non-specialist readability；
- central scientific contribution 是否早出现；
- jargon 是否必要；
- figure-led narrative 是否清楚；
- Abstract 是否 context → unresolved problem → approach → main result → implication；
- Results 是否 question-led；
- Discussion 是否 synthesis-led；
- prose 是否 compressed 而非 over-edited；
- importance 是否由证据体现，而不是 promotional wording。

不得把：

> “像 Nature”

解释成：

- 更夸张；
- 更机制化；
- 更因果；
- 更 universal；
- 更少 limitations。

## 35.3 Target-journal 输出标签

可使用：

- `JOURNAL_FIT_READABILITY`
- `JOURNAL_FIT_CONCISION`
- `JOURNAL_FIT_ARGUMENT_ORDER`
- `JOURNAL_FIT_OVERPROMOTION`
- `JOURNAL_FIT_SPECIALIST_JARGON`
- `JOURNAL_FIT_BREADTH_OVERCLAIM`

---

# 三十六、AI 风格风险严重度

## LOW

- 单次模板化表达；
- 不影响 claim；
- 不影响逻辑；
- 删除或保留都不影响科学意义。

## MEDIUM

- 同一模板跨多个段落重复；
- 明显降低信息密度；
- 产生机械段尾；
- meta-discourse 较多；
- caveat 重复；
- 需要结构压缩。

## HIGH

- 模板化修辞造成 claim-strength inflation；
- “不是 X 而是 Y”实际上在无证据排除 X；
- “不仅 X 而且 Y”把直接结果升级成机制；
- promotional language 掩盖 limitation；
- 机械总结导致 Abstract / Discussion 比 Results 更强；
- rhetoric 直接造成科学误导；
- construct status 被语言升级。

HIGH prose risk 可以进入 blocking issues。

---

# 三十七、AI 风格审计表

`PROSE_RISK_AUDIT` 至少输出：

| 位置 | 原文 | 风险标签 | 具体模式 | 科学问题 | 严重度 | 建议处理 |
|---|---|---|---|---|---|---|

建议处理只使用：

- `KEEP`
- `DELETE`
- `MERGE`
- `MOVE`
- `REWRITE`
- `VERIFY_EVIDENCE`

示例：

| Discussion P3 S4 | “This finding does not merely reflect synchrony; rather, it reveals...” | PROSE_NOT_X_BUT_Y | 先否定较弱解释，再升级到机制 | 未证明已排除 synchrony，也未直接测量 mechanism | HIGH | VERIFY_EVIDENCE / REWRITE |

---

# 三十八、Information Density Audit 表

至少输出：

| 位置 | Primary function | Scientific payload | Rhetorical payload | Density judgment | Recommendation |
|---|---|---|---|---|---|

Density judgment 使用：

- `ESSENTIAL`
- `USEFUL_BUT_COMPRESSIBLE`
- `BETTER_IN_METHODS`
- `BETTER_IN_EXTENDED_DATA`
- `BETTER_IN_SUPPLEMENT`
- `REDUNDANT`
- `REMOVABLE`

---

# 三十九、Construct-Status Audit 表

至少输出：

| Construct | First appearance | Current status | Later wording | Drift? | Risk | Recommendation |
|---|---|---|---|---|---|---|

例如：

| Partner-weight parameter | Results | MODEL_PARAMETER | “self–other integration mechanism” in Discussion | Yes | LOGIC_CONSTRUCT_STATUS_DRIFT | Narrow interpretation |

---

# 四十、Logic Audit 具体例子

## 40.1 相关 → 因果

原文：

> “Higher interpersonal synchrony predicted greater trust.”

论文：

> “Synchrony increased trust.”

若设计不是干预或因果识别：

`LOGIC_CAUSAL_LEAP`

---

## 40.2 行为结果 → 心理机制

结果：

> Alternating coordination showed higher partner weighting.

Discussion：

> Alternating coordination engages predictive social inference.

若 predictive inference 未直接测量：

`LOGIC_MECHANISM_LEAP`

---

## 40.3 特定样本 → 普遍人群

研究：

> 36 healthy young adults.

Conclusion：

> Humans flexibly integrate others during coordination.

若没有外部 generality evidence：

`LOGIC_SCOPE_LEAP`

---

## 40.4 单一实验 → 学界共识

一篇研究发现 X。

论文：

> “It is well established that X.”

标记：

`OVERSTATED`

并检查 consensus evidence。

---

## 40.5 非显著 → 无效应

结果：

> p = .18

论文：

> “There was no difference between conditions.”

如果没有 equivalence test / Bayes factor / adequate justification：

`LOGIC_CONCLUSION_EXCEEDS_RESULTS`

---

# 四十一、引用幻觉具体例子

## 41.1 文献存在，但不支持原句

论文：

> “Smith et al. (2021) showed that synchrony causally increases trust.”

原文：

> “Synchrony was associated with self-reported trust.”

判定：

`OVERSTATED`

不是：

`FABRICATED_REFERENCE`

---

## 41.2 标题相关，但正文没有这个结果

论文引用：

> “Jones (2020) demonstrated neural coupling during motor coordination.”

实际文献标题含 “neural coupling”，但正文研究的是 resting-state connectivity。

判定：

`MISMATCH`

---

## 41.3 找不到论文，但不能断言伪造

正文：

> Zhang & Lee, 2019

在 Crossref / PubMed / publisher 等合理检索后未定位。

判定：

`REFERENCE_NOT_FOUND`

除非存在明确元数据矛盾，否则不要直接写：

`FABRICATED_REFERENCE`

---

## 41.4 DOI 明确指向另一篇文章

参考文献：

> Smith, 2022, “Interpersonal coordination...”, DOI: 10.xxxx/abc

实际 DOI 指向：

> “Visual attention in birds”

且作者、期刊、年份不匹配。

可判：

`FABRICATED_REFERENCE`

必须记录检索证据。

---

# 四十二、跨章节一致性检查

检查：

## Abstract vs Results

是否 Abstract 写得更强。

## Results vs Discussion

是否 Discussion 增加未测量机制。

## Discussion vs Conclusion

是否 Conclusion 扩大 population / scope。

## Title vs正文

是否标题使用：

- reveals；
- determines；
- promotes；
- mechanism；

但正文只支持 association。

## Hypothesis vs Results

是否出现 HARKing：

原先 exploratory 结果被 Discussion 写成 predicted。

标签：

`LOGIC_HYPOTHESIS_RESULT_DRIFT`

---

# 四十三、Citation Cluster Audit

若一句话后有：

`(A, 2018; B, 2020; C, 2022)`

不得把整个 cluster 视为一个证据块。

必须判断：

- A 支持什么；
- B 支持什么；
- C 支持什么；
- 是否所有来源都支持同一 atomic claim；
- 是否只有一个来源真正相关；
- 是否 citation cluster 被用于掩盖 claim-source mismatch；
- 是否一个综述被用来代替可获得的 primary evidence。

---

# 四十四、无引文重要主张扫描

重点搜索：

- previous studies show；
- research suggests；
- it is well established；
- widely accepted；
- consistently shown；
- few studies；
- little is known；
- remains unclear；
- no previous study；
- first study；
- unique；
- widely used；
- robustly established。

这些表达通常包含可外部验证的领域判断。

不得因为听起来像“常识”就默认无需 citation。

---

# 四十五、审计模式下的停止规则

🔴 CHECKPOINT · 🛑 STOP：审计模式只报告、不改稿。

如果当前任务是正式审计：

完成后：

**不得直接修改正文。**

必须先交付：

- claim-level citation audit；
- logic audit；
- construct-status audit；
- structure / density audit；
- prose-risk audit；
- blocking issues。

如果用户后续明确要求修改：

优先调用 `repair`。

---

# 四十六、返修模式

只有用户明确授权时进入。

优先使用 `repair` skill。

如果当前环境没有独立 `repair`：

才在本 skill 中执行最小 evidence-constrained repair。

返修原则：

1. 重新核对原始证据；
2. 删除错误 citation；
3. 降低 claim strength；
4. 缩小 scope；
5. causation → association；
6. mechanism → interpretation；
7. 删除非必要 unsupported claim；
8. 最后才考虑新增已核验 citation。

不得：

> 为保留原句给它强行寻找一个看起来相关的引用。

---

# 四十七、Re-audit

任何修改后：

把修改稿视为新稿。

重新检查：

- citation-bearing claims；
- uncited claims；
- numbers；
- causal language；
- mechanism；
- universality；
- consensus；
- novelty；
- construct status；
- Abstract / Results / Discussion / Title consistency；
- prose templates；
- repeated conclusions；
- repeated caveats；
- question-led narrative；
- information density；
- new unsupported claims。

不得只检查改动句。

---

# 四十八、完整 FULL_AUDIT 输出

至少包含：

## A. Scope

- audited file；
- audited sections；
- sources available；
- unavailable evidence；
- audit mode；
- target journal（若有）。

## B. Citation integrity summary

- total atomic claims；
- VERIFIED；
- PARTIALLY_SUPPORTED；
- OVERSTATED；
- MISMATCH；
- REFERENCE_NOT_FOUND；
- FABRICATED_REFERENCE；
- UNCITED_CLAIM；
- UNVERIFIED。

## C. Claim-level citation table

| 位置 | Atomic claim | Citation | Evidence | Locator | Verdict | Problem | Suggested repair | Confidence |
|---|---|---|---|---|---|---|---|---|

## D. Logic audit table

| 位置 | Claim / reasoning step | LOGIC tag | Why problematic | Evidence needed | Severity |
|---|---|---|---|---|---|

## E. Construct-status table

| Construct | Evidence status | Current wording | Drift location | Risk | Recommendation |
|---|---|---|---|---|---|

## F. Information-density / structure table

| 位置 | Primary function | Scientific payload | Rhetorical payload | Density | Recommendation |
|---|---|---|---|---|---|

## G. Prose-risk table

| 位置 | 原文 | PROSE tag | Pattern | Scientific consequence | Severity | Recommended treatment |
|---|---|---|---|---|---|---|

## H. Caveat repetition map

列：

- caveat type；
- locations；
- 是否每次承担新功能；
- 是否建议合并 / 删除。

## I. Question-led / figure-led findings

列：

- scientific question；
- supporting figure / table；
- current narrative position；
- narrative alignment；
- issue；
- recommendation。

## J. Blocking issues

单独列出。

## K. Priority

- P0 integrity；
- P1 logic / construct status；
- P2 structure / density；
- P3 prose。

审计模式：

**不直接修改正文。**

---

# 四十九、完成条件

交付前确认：

- 审计范围和未审计范围清楚；
- 复合句已按 atomic claims 拆分；
- 每个 `VERIFIED` 都有实际访问的证据和 locator；
- 没把“文献存在”误当成“主张被支持”；
- 没把检索不到轻率判为伪造；
- 关键无引文主张已扫描；
- 逻辑审计覆盖设计、分析层级、替代解释和跨章节一致性；
- construct-status drift 已检查；
- information-density audit 已执行；
- question-led / figure-led narrative 已检查；
- caveat repetition map 已执行；
- AI 风格风险没有被写成 AI 作者身份判定；
- “不是……而是……”“不仅……而且……”等高风险模板已做上下文判断；
- 没有仅凭关键词删除正常学术句；
- 所有 blocking issues 单独列出；
- `UNVERIFIED` 没有被包装成通过；
- 若已返修，重新审计新增主张、引用同步、construct status 和事实回归。

---

# 五十、最终原则

**无法验证优于猜测。**

**证据边界优于语言力度。**

**科学功能优于模板化修辞。**

**引用存在不等于引用正确。**

**句式常见不等于 AI。**

**“不是 X，而是 Y”本身不是问题；没有证据排除 X，却用该结构把 Y 写成更强结论，才是问题。**

**“不仅 X，而且 Y”本身不是问题；前半句是直接结果、后半句却偷偷升级成机制或普遍结论，才是问题。**

**同一个 caveat 写四遍，不会自动让论文更严谨；精确校准一次通常更强。**

**analysis 顺序不等于 scientific narrative 顺序。**

**一个 model parameter 不会因为进入 Discussion 就自动变成心理机制。**

**期刊风格不能突破 evidence ceiling。**

本 skill 的目标不是让论文“看起来不像 AI”，而是让它：

> **证据可核验、逻辑不跳跃、construct 身份不漂移、叙事由科学问题驱动、段落有明确功能、信息密度高、语言不靠模板化修辞制造重要感。**
