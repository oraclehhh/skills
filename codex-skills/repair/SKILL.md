---
name: repair
description: 修复已经发现问题、已有审计报告、revision roadmap、审稿意见或用户明确要求改好的学术论文版本。按照原始数据、最终统计结果、图表、方法记录和已核验文献，对错误引用、引用幻觉、claim–evidence mismatch、数字或方向错误、因果与机制夸大、过度概括、逻辑断裂、章节结构、重复论证和模板化 AI 风格风险进行证据约束下的最小返修或经授权的深度 revision。用户提到“修复论文”“按检查报告修改”“根据审稿意见改稿”“citation repair”“降低过强结论”“修复AI味”“执行revision roadmap”时都应使用。不得覆盖原稿、伪造证据或执行未授权分析；修改后必须用 check（或已注册的 manuscript-integrity-check）重新审计，DOCX 再交给 geshi 格式后检。
---

# Repair

把本 skill 作为学术论文工作流中的返修执行层。目标是在不改变研究事实的前提下，把已识别问题修到现有证据允许的最强、最清楚、最可交付版本。

优先级为：

**事实正确 > 来源与主张匹配 > 推理有效 > 结论边界 > 结构清楚 > 语言精炼。**

## 与其他 skill 的分工

- `check`（某些环境注册为 `manuscript-integrity-check`）：定位引用、逻辑和文风问题；修改后执行新的完整复检。
- `neirong`：在需要重写 Abstract、Introduction、Discussion、假设、RQ 或段落论证时提供写作规则。
- `geshi`：在内容通过复检后检查 DOCX、Word、EndNote、OOXML、字体、颜色和分页。

不要复制这些 skill 的全部规则。需要相应能力时，通过当前 skill 注册表 / 路由定位并读取其当前 `SKILL.md`：

- `check`（某些环境注册为 `manuscript-integrity-check`）
- `neirong`
- `geshi`

推荐顺序：

`诊断/审计 → Repair → Check REAUDIT → DOCX 时 Geshi`

## 授权判断

以下请求已经授权在给定范围内直接修改：

- “修复/改好这篇论文”；
- “根据这份审计报告修改”；
- “执行 revision roadmap”；
- “根据 reviewer comments 改稿”；
- “检查并修复引用、逻辑或 AI 风格问题”。

若没有审计报告但用户明确要求修复，先使用当前可用的 `check` 或 `manuscript-integrity-check` 建立问题清单，再在同一任务中修复，不必为了形式重复征求许可。

下列高影响事项若用户尚未明确授权，必须标记 `[AUTHOR DECISION REQUIRED]` 并请求决定：

- 改变中心主张、研究问题、假设或总体结论方向；
- 删除核心结论、关键阴性结果或关键文献主张；
- 裁决相互冲突的高优先级事实来源；
- 大幅重排主图、改变研究 framing 或目标期刊定位；
- 执行新统计、新模型或其他未完成分析；
- 在多个竞争性解释之间替作者作高影响选择。

## 选择修复模式

按问题选择最小充分模式：

- `INTEGRITY_REPAIR`：错误数字、方向、方法描述、来源冲突、虚假或错配引用、unsupported core claim。
- `CITATION_REPAIR`：删除错误归因、缩小主张、补充已核验引用、同步参考文献。
- `CLAIM_RECALIBRATION`：把因果降为关联、机制降为解释、普遍结论缩小到研究样本或情境。
- `ARGUMENT_REPAIR`：修复前提缺失、设计—结论错配、分析层级混用、跨章节 claim-strength drift。
- `ARCHITECTURE_REPAIR`：按已授权 roadmap 调整章节、段落、图文叙事和材料位置。
- `PROSE_REPAIR`：删除重复、模板化总结、元话语、审稿回复残留、宣传性或低信息密度语言。
- `REVIEWER_RESPONSE_REPAIR`：逐条落实审稿意见，同时保持证据边界。
- `FULL_REPAIR`：按 P0 至 P3 完成全部适用修复、复检和格式交接。

只有用户明确指定 Nature 或其他目标期刊时，才应用对应期刊的深度 revision；期刊风格不能突破 evidence ceiling。

## 输入与事实来源

尽量读取：

- 原始 manuscript 和待修版本；
- 审计报告、revision roadmap、审稿意见和作者决定；
- 最终数据、统计输出、图表、方法、protocol、分析代码；
- 参考文献表、文献库和相关原始来源；
- 目标期刊与交付格式。

Manuscript 和审计报告都不是事实本身。默认参考层级为：最终数据/统计输出 → 已确认图表和分析代码 → protocol/Methods/实验记录 → 作者确认事实 → 已核验原始文献 → manuscript → 审计或审稿转述。

高优先级来源冲突时不要自行裁决，记录 `[SOURCE CONFLICT]`。材料不足时完成可安全完成的部分，并使用 `[UNVERIFIED]`、`[AUTHOR INPUT REQUIRED]` 或 `[SUGGESTED ANALYSIS — NOT PERFORMED]`。

## 修复顺序

严格按照以下优先级工作：

1. `P0 Integrity`：引用身份、数据、统计、方向、方法和核心事实。
2. `P1 Scientific argument`：主张—证据匹配、因果和机制边界、逻辑链、替代解释。
3. `P2 Structure`：章节、段落、图文顺序、重复和材料位置。
4. `P3 Language`：清晰度、简洁度、术语和模板化文风。

不要在 P0–P2 未稳定时先做大规模语言润色。

## 核心工作流

### 1. 建立 repair item list

把审计报告、roadmap 或本轮诊断拆成可执行项目。每项记录：位置、问题、证据、优先级、授权状态、拟采用动作和验收条件。

审计报告只是问题索引。每个 substantive repair 都要重新查看 manuscript、事实来源和原始文献，不能因为报告写了 `MISMATCH` 就直接改稿。

### 2. 保护事实和不方便的证据

未经明确依据和授权，不创建或改变样本、设计、变量、方法、模型、数字、统计、显著性、效应量、图表、伦理信息、预注册、假设状态或作者研究发现。

不得隐藏或改写成有利结果的 null findings、失败预测、矛盾证据、不确定性、边界条件、敏感性分析和关键局限。

### 3. 执行证据约束修复

涉及引用、数字、方法、统计、主张强度或来源冲突时，读取并执行 `references/evidence-repair.md`。优先最小动作：不改 → 删除错误引用 → 改动词或限定语 → 缩小范围 → 因果改关联 → 机制改解释 → 删除非必要 unsupported claim → 添加实际核验的替代引用 → 重写更大单元。

### 4. 修复逻辑、结构和文风

涉及论证链、章节、Results/Discussion、图文叙事、Nature revision 或 AI 风格风险时，读取并执行 `references/argument-and-prose-repair.md`。结构优化不得改变事实，去模板化不得删除必要限定语或引文。

### 5. 同步全文

任何数字、方向、条件标签、主张或引用变化，都要检查标题、摘要、正文、图表、题注、Discussion、Conclusion 和参考文献表中的对应位置。不要只修出现问题的单句。

### 6. 写入新稿并记录

不覆盖唯一原稿。DOCX 默认输出 `<original_name>_repaired.docx` 或用户指定的新路径。执行 `references/logs-and-handoffs.md`，记录所有 substantive changes；纯排版或无意义机械改动不要淹没日志。

### 7. Repair Integrity Gate

🔴 CHECKPOINT · 🛑 STOP：以下任一未满足即不得宣称修复完成。

确认：

- 研究事实、数字、方法、图表和假设状态未被无依据改变；
- 没有新增 unsupported claim、citation mismatch、因果/机制夸大或范围扩张；
- 引用与参考文献同步，无孤立条目、作者年份错配或虚构来源；
- 压缩和去模板化未删除必要证据、限定语、阴性结果或局限；
- 修改范围符合授权，所有 substantive changes 可追踪；
- 原稿未覆盖。

### 8. 强制内容复检

🔴 CHECKPOINT · 🛑 STOP：把修改稿当作新稿执行 `REAUDIT`。

加载当前可用的 `check`；若它未安装，则通过注册表定位 `manuscript-integrity-check`。把修改稿当作新稿执行 `REAUDIT`。不要只检查改动句，也不要因 Repair 自检通过就宣称引用或内容已经通过。

复检发现新的 `MISMATCH`、关键 `OVERSTATED`、错误引用、核心漏引、来源冲突、逻辑阻断或 claim-strength drift 时，返回修复步骤并再次复检，直到问题解决或透明标为作者决定/无法验证。

### 9. DOCX 格式后检

只有内容复检达到可交付状态后，才加载 `geshi`。对引用域、参考文献域、标题、统计格式、图表、分页和逐页渲染执行其最新 checklist。

## 禁止事项

- 不根据模型记忆、标题、搜索片段或 AI 摘要补文献。
- 不用主题相似的新文献为原本 unsupported 的句子“洗引用”。
- 不把摘要证据扩展为摘要未报告的机制、边界或精确统计。
- 不执行未授权分析并把建议写成已完成结果。
- 不随机换同义词、故意制造错误、机械改变句长或声称能规避 AI detector。
- 不为满足审稿人而突破真实证据。
- 不声称已通过 Check、Geshi、Word、EndNote 或逐页检查，除非实际完成。

## 完成条件

只有满足以下条件，Repair 层才完成：

- 所有授权项目已处理或明确标为无法处理；
- 每处 substantive repair 有可追溯证据和日志；
- 原稿安全保留；
- 没有已知新增事实错误、unsupported claim 或 citation laundering；
- `UNVERIFIED` 没被误报为 `VERIFIED`；
- 未授权分析没有执行；
- Repair Integrity Gate 已通过；
- 已生成复检交接并实际执行或明确等待 Check 复检；
- DOCX 在内容通过后实际执行或明确等待 `geshi`。

**Repair 完成不等于论文最终通过。最终内容状态由复检决定，最终文档状态由 Geshi 决定。**
