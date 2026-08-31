# Evidence-Constrained Repair

## 1. Claim 分类和强度上限

先把主张分为：本研究直接结果、外部文献背景、结果解释、拟议机制、假设、证据缺口。解释、机制、假设和证据缺口不得被改写成直接结果。

不得进行以下升级：

- correlation → causation；
- association → mechanism；
- exploratory → confirmatory；
- consistency → proof；
- subgroup/context → population/universal；
- non-significance → evidence of absence；
- model-derived construct → directly measured psychological process；
- one study → field consensus。

原稿强于证据时，降低主张而不是寻找模糊相关引用抬高证据。

## 2. Citation repair

对每个引用问题：

1. 定位 atomic claim 和 citation；
2. 核对参考文献身份和正文显示；
3. 重新打开原始来源；
4. 比较样本、设计、变量、条件、方向、显著性、范围、因果和机制；
5. 决定 `KEEP`、`DELETE_CITATION`、`WEAKEN`、`NARROW_SCOPE`、`CHANGE_CAUSAL_TO_ASSOCIATIONAL`、`CHANGE_MECHANISM_TO_INTERPRETATION`、`DELETE_CLAIM`、`REPLACE_CITATION` 或 `ADD_VERIFIED_CITATION`；
6. 记录来源和真实 locator；
7. 同步参考文献表。

当主张缺少可靠支持时，依次考虑：删除错误引用；若是本研究结果则改为 present-study attribution；降低确定性；缩小范围；降因果或机制；删除非必要主张；最后才添加实际核验的新来源。

`UNVERIFIED` 不自动删除、不自动保留、不自动替换。若保守改写可消除对该来源的依赖，可以最小改写；否则交由作者决定。

对于 `UNCITED_CLAIM`，先区分本研究结果、外部事实、常规方法描述、解释、novelty 和 gap。只有外部主张且有实际核验来源时才添加引用。没有充分检索依据时，不使用 `first`、`no previous study` 或 `few studies`。

## 3. Reference identity

核对作者、年份、题名、期刊、DOI、a/b 后缀、citation key、正文引用和文末条目。修复一个引用时不能产生新的作者年份错配。

只获得摘要时，只支持摘要明确表达的内容，标记 `ABSTRACT_ONLY`。不要推断全文细节、亚组、图表、效应量、精确显著性或机制。

## 4. Source conflict

记录 manuscript 值、来源值、来源路径、冲突类型和置信度。唯一且明确的最终高优先级来源可以用于修复抄写错误；多个高优先级来源冲突时标记 `[SOURCE CONFLICT]`，不得自行选择。

## 5. 数字和统计

若最终统计输出清楚证明只是抄写错误，可以修复数值、方向、`p`、CI、效应量或 df，并检查摘要、Results、题注和 Discussion 的所有对应位置。

不得重新计算、选择更有利模型、改变阈值或多重比较方法。需要新分析时写 `[SUGGESTED ANALYSIS — NOT PERFORMED]`，说明科学目的和对核心结论的影响。

## 6. 方法

Methods 与已确认 protocol 或分析代码明确冲突时，可修正描述。实际执行不确定时标记 `[AUTHOR INPUT REQUIRED]`。不得补造随机化、盲法、排除、伦理、知情同意、预注册或样本量依据。

## 7. Reference synchronization

删除正文引用后，只有该文献在全文不再被引用时才删除文末条目。新增已核验引用必须同步进入参考文献表。内容层只保证条目一致性；EndNote 域和 OOXML 由 `geshi` 检查。
