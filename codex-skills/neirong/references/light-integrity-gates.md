# Light Integrity Gate 详细检查项（Gates A–J）

凡 Neirong 生成、续写、重写、润色或修改学术文本，交付前执行 Light Integrity Gate。只检查本轮新增/修改内容、直接受影响的相邻论证；整章重写则检查整章。Gate 是「生成阶段预防」，不是「独立完整审计」。

## Gate A：研究事实回归

确认本轮没有无意改变：

- sample / population / condition / design / method / variable definition；
- numerical result / p value / CI / effect size；
- significant / non-significant direction；
- correction status / analysis identity；
- figure / table / model setting；
- author's finding。

若本轮修改 Methods，额外确认：每个新增方法事实都有 source-of-truth；没有用领域常规补缺失细节；ethics/consent/exclusion/randomization/preprocessing/parameters 没有被推测；source conflict 没有被模型自行裁决；方法重排没有删除 reproducibility-critical 信息。

若本轮修改 Results，额外确认：所有数字来自 final source-of-truth；N、方向、统计量、p、CI、effect size 未改变；correction status 未改变；exploratory 没变 confirmatory；null 没变 absence；没有新分析被偷偷执行；narrative reorder 没有改变 scientific priority 或 analysis identity。

冲突无法判断 → `[AUTHOR VERIFICATION REQUIRED]`；来源彼此冲突 → `[SOURCE CONFLICT]`。

## Gate B：Citation hallucination 快检

对本轮新增或改写的外部 claim：

1. citation 是否来自实际访问来源；
2. source 是否支持具体 claim；
3. 是否只主题相关；
4. 是否超出 source（causality / certainty / population / task / mechanism / effect direction）；
5. 是否出现需引用但无引用的重要外部 claim；
6. 摘要证据是否被扩写成全文结论；
7. 是否根据模型记忆补文献。

来源不能可靠核验 → `[UNVERIFIED CITATION]`，不得假装 verified。

## Gate C：Claim-strength drift

检查本轮是否发生：association → causation；possibility → certainty；interpretation → finding；model fit → mechanism；condition-specific → universal；one study → consensus；non-significant → absence；descriptive parameter → participant strategy；indirect construct → direct measure。发现就降低表述。

## Gate D：Measurement Comparability

若本轮新增跨条件解释，确认 metric definition / target / scale / preprocessing / aggregation / exclusion 是否可直接比较。若不完全可比，在 claim 中显式保留边界。

## Gate E：Construct Status

扫描核心 construct：Results 的 derived metric、Discussion 的 conceptual interpretation、Abstract 的 wording、Title/heading 是否逐级升级。若发生，恢复到 evidence ceiling。

## Gate F：AI-style / rhetorical scaffolding

检查本轮是否出现：多段重复「总结→拔高→限定」、repeated These findings suggest / Taken together / Overall / Importantly / Notably、不是 X 而是 Y、不仅 X 而且 Y、artificial three-part parallelism、每段机械总结、vague importance、abstract noun stacking、meta-discourse、reviewer-response voice、defensive-prose loop、repeated caveat。

如果删除某句不损失 scientific information，优先删除/merge。不得通过 random synonym replacement、故意语法错误、随机句长、口语化、删除所有 transitions 来「去 AI」。

## Gate G：Workflow Residue

扫描 confirmed / final output / manuscript revision / paper-style / project records / source-of-truth / audit / reviewer request / TODO / TBD / placeholder。若是工作流语言，改成科学事实或删除；若背后事实未确认，保留 verification marker，不得伪装。

## Gate H：Caveat repetition

建立轻量 caveat map。同一 limitation 已在本轮准确表达，后续不要换词重复。尤其检查 does not establish / cannot demonstrate / should not be interpreted / does not prove / consistent with but / may-might-could。宁可把主 claim 写到正确强度，也不要给过强 claim 加四层免责声明。

## Gate I：Paragraph function 与信息密度

检查每段 primary function 是否清楚；是否有两个连续段落做同一件事；是否只是重复 finding；是否 analysis-led；是否 rhetorical payload 高于 scientific payload；是否能在不损失 evidence 的情况下压缩。

## Gate J：Regression check

完成任何修正后再检查：删除 citation 是否产生 uncited claim；弱化句子是否改变作者真实结论；prose 压缩是否删掉必要 qualifier；是否引入新解释；citation/reference 是否错配；是否修一个 AI pattern 又生成另一个 generic summary；是否修改一处导致 Abstract/Discussion/Title 不一致。
