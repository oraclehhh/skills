# Report and Repair

## 1. 审计报告结构

使用以下结构，未执行的模块标记“不在本次范围”，不要伪造检查结果。

### Scope and evidence access

- 已审计文件和章节；
- 已访问全文、摘要和仅有元数据的来源数量；
- 未审计范围和材料限制。

### Executive summary

- audited atomic claims；
- 各引用判定数量；
- logic blocking/major/minor 数量；
- prose risk 数量；
- `UNVERIFIED` 和作者核验事项数量。

### Blocking issues

按位置逐项说明为什么阻断核心论证或投稿可信度。

### Claim-level citation audit

使用 citation reference 中的表格。

### Logic audit

使用 logic reference 中的表格。

### Prose risk audit

使用 prose reference 中的表格，并明确“不是 AI 作者身份判定”。

### Prioritized revision map

顺序为：事实与引用身份 → 主张—证据不符 → 逻辑和结论边界 → 跨章节一致性 → 文风压缩。

## 2. Audit Mode

只生成审计报告，不改正文。若能创建文件，默认输出 `manuscript_integrity_audit.md`；大稿件可拆分，但必须保留总摘要和 claim-level 表。

聊天中简要报告范围、blocking issues、`UNVERIFIED` 和文件路径，并明确“未修改论文正文”。

## 3. Evidence-Constrained Repair

只有用户明确授权修改时执行：

1. 把报告当作问题索引，不当作事实依据；
2. 对每个问题重新打开原始来源；
3. 优先删除错误归因、降低强度、缩小范围、把因果改为关联，或删除非必要且无法支持的主张；
4. 只有实际取得并核验新来源后才新增引用；
5. 保持作者事实、数据、统计、设计、结构和声音，采取最小必要改动；
6. 同步正文引用与参考文献表；
7. 输出新稿，不覆盖源文件；
8. 记录原句、修改后句、来源、locator、判定和理由；
9. 对修改稿执行引用、逻辑、文风和事实回归复检。

若处理 DOCX，内容返修后调用 `geshi` 检查 Word/EndNote/OOXML 格式完整性。

## 4. 返修输出

按任务规模输出：

- 修改后的新稿；
- `integrity_revision_log.md`；
- `integrity_unverified.md`；
- `author_review_required.md`；
- `integrity_reaudit.md`。

小范围文本返修可合并日志，但不得省略证据和未验证事项。

## 5. 回归复检

至少检查：

- 是否新增 unsupported claim 或 citation mismatch；
- 删除引用后是否留下无来源主张；
- 新增引用是否进入参考文献表；
- 压缩是否删除必要限定语；
- 标题、摘要、Results、Discussion 和 Conclusion 是否产生 strength drift；
- 作者研究事实、数字和条件标签是否被误改；
- `UNVERIFIED` 是否被错误标成已解决。

只有没有未处理的明确 `MISMATCH`、`FABRICATED_REFERENCE` 和新增事实回归，且剩余限制已透明列出时，才能声明返修完成。
