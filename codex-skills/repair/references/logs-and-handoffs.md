# Logs and Handoffs

## 1. Repair item 表

| ID | Priority | Location | Problem | Evidence | Authorized scope | Action | Acceptance criterion | Status |
|---|---|---|---|---|---|---|---|---|

## 2. Revision log

每处 substantive change 记录：

- Revision ID 和优先级；
- section/paragraph；
- 原句和原 citation；
- 修改后句子和 citation；
- 问题类型与修复动作；
- 科学理由；
- evidence source 与 locator；
- 修改前后 claim strength；
- 是否需要作者决定；
- re-audit 状态。

结构调整额外记录原位置、新位置、受影响图表、roadmap ID 和证据是否保留。图文调整额外记录原叙事角色、新角色、caption 影响和数据是否保持不变。

## 3. 默认输出

按适用范围创建：

- `<name>_repaired.docx` 或用户指定的新稿路径；
- `repair_revision_log.md`；
- `citation_revision_log.md`；
- `citation_unverified.md`；
- `author_review_required.md`；
- `architecture_revision_log.md`；
- `prose_revision_log.md`；
- `repair_handoff_to_check.md`。

只创建实际需要的日志，避免为小修改生成大量空文件。

## 4. Check handoff

`repair_handoff_to_check.md` 至少记录：

- 新稿和原稿路径；
- 使用的 repair modes、audit report 和 roadmap；
- 修改总数、引用删除/新增、主张弱化/缩小和结构变化；
- 剩余 `UNVERIFIED`、`SOURCE CONFLICT` 和 `[AUTHOR DECISION REQUIRED]`；
- 未执行的建议分析；
- 需要完整复检的范围；
- 所有变更文件。

在当前可用的 `check`（或注册名 `manuscript-integrity-check`）实际完成前，不写“all citations verified”或伪造 re-audit 文件。

## 5. Geshi handoff

内容复检通过且输出为 DOCX 时，记录：最终稿路径；引用、参考文献、图表、标题是否改变；分页是否可能变化；EndNote 域和 bibliography 是否可能受影响。然后执行 `geshi`，不要只生成交接文件就声称格式通过。

## 6. 最终汇总

简要报告修改数、引用增删、主张弱化/缩小、结构调整、剩余未验证项、作者决定项、内容复检状态、Geshi 状态、最终稿和日志路径。未实际完成的步骤明确写“未执行”或“等待”，不得写成通过。
