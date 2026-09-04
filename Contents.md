
**如何给电子书做格式校准和加目录？**

https://github.com/oomol-lab/pdf-craft/blob/main/README_zh-CN.md

**如何做多智能体编排？langgraph**

https://github.com/langchain-ai/langgraph/blob/main/examples/chatbots/information-gather-prompting.ipynb

**如何使用loop来debug？**

https://x.com/EXM7777/status/2095572281804394895?s=20

请用一个有限循环完成这个任务：

目标：修复当前项目中的 Bug：*********

每一轮执行：
1. worker 修改代码
2. 运行相关测试、类型检查和 lint
3. 启动一个独立的只读 reviewer 检查改动
4. 如果测试失败或 reviewer 发现问题，把问题交回 worker 修复
5. 重新运行检查

通过标准：
- 相关测试全部通过
- 类型检查通过
- lint 通过
- reviewer 没有发现高严重度问题
- 没有删除或绕过测试

最多循环 3 轮。每轮报告检查结果。
达到标准后停止，不要继续无意义地修改。
它大致会变成：

```
修改代码
   ↓
运行测试
   ↓
独立审查
   ↓
合格？──是──> 输出结果
  │
  否
  ↓
继续修改
```

关键是你必须提前规定：

- 什么叫“合格”
- 谁负责检查
- 最多循环几次
- 每轮失败时返回什么信息

不要只写“不断优化直到满意”，否则代理可能反复修改、浪费 token，甚至把代码越改越复杂。

对代码来说，**测试结果比模型自己打分更可靠**。对文章、图片等内容，才比较适合用“评分达到 8/10 后通过”这种方式，但评分标准也要具体，例如事实准确性、结构、语法和是否有来源。

**如何减少token消耗？**
https://x.com/oliviscusAI/status/2095572963915333991?s=20
请按照以下 4 个步骤来防止 Fable 5.1 消耗你的每周积分： 1. 将“努力程度”设置得较低一些 2. 运行 /claude-api cost-optimize 命令，以找出最大的浪费情况。 3. 运行/claude-api prompt-audit 命令，以清除旧的垃圾数据。 4. 运行 /claude-api 命令，将该项目迁移到 claude-fable-5-1 版本，以更新旧的模型 ID。 您不再需要担心会浪费代币了。 [https://x.com/dr_cintas/stat/dr_cintas/status/2095216285114327412](https://x.com/dr_cintas/status/2095216285114327412)

**如何让codex调用子代理？**
https://x.com/AnatoliKopadze/status/2095573992140583363?s=20
明确告诉 Codex“拆成几个子代理、每个负责什么、是否等待全部完成、最后如何汇总”。提示词：

请使用并行子代理审查当前项目：
1. 一个代理检查安全问题
2. 一个代理检查测试缺口
3. 一个代理检查代码质量
等待所有代理完成后，按类别汇总结果。
每条结论都要给出文件路径、行号和理由。
这次只读，不要修改任何文件。

请审查当前分支与 main 的差异。
为以下每个方面启动一个子代理：
安全问题、Bug、竞态、测试不稳定、可维护性。
等待所有代理完成，再汇总，并标出严重程度。

**如何减少LLM的错误？**
https://x.com/akshay_pachaar/status/2095575252445405466?s=20
https://github.com/withmartian/routerbench
这篇论文的核心不是让某一个 LLM 突然变得更聪明，而是把多个模型和多次生成组合起来，减少系统整体错误。
主要方法：
1. 按问题路由到不同模型
   不同模型擅长的领域不同。先判断问题类型、难度和风险，再选择最合适的模型，而不是所有问题都交给同一个模型。
2. 多次生成，进行选择或投票
   对同一个问题生成多个答案，通过多数投票、一致性检查或独立评审模型选出更可靠的答案。论文中 10 次采样的理论上限可带来约 82.4% 的错误率下降，但成本也会明显增加。
3. 使用级联策略
   先用便宜、快速的小模型回答；如果出现低置信度、模型意见不一致或验证失败，再升级到更强的模型。
4. 增加外部验证
   不要只依赖模型自我判断：
   - 知识问题：RAG、搜索、引用来源
   - 数学问题：计算器或代码执行
   - 编程问题：运行测试
   - 数据库问题：SQL 执行和结果校验
   - 高风险问题：人工审核或强模型复核
5. 让输出可验证
   使用 JSON Schema、类型约束、规则检查、事实核验和业务逻辑校验，避免格式正确但内容错误。
6. 正确评估错误率
   论文特别指出：只挑多次生成中“最好”的结果，会夸大模型能力。评估时应使用独立测试集、多次重复实验，并对“最大值选择”带来的统计偏差进行修正。
一个实际可用的流程是：
用户问题
  -> 判断领域、难度和风险
  -> 选择一个或多个模型
  -> 生成答案
  -> 检索/工具/规则验证
  -> 不通过则重试或升级模型
  -> 输出答案和依据
需要注意：论文里的 oracle 路由知道每个模型对每道题是否正确，现实中无法直接获得，因此它更像是“可达到的上限”。真正部署时，重点应放在“路由器 + 多次采样 + 外部验证 + 失败升级”这四部分。

**减少token成本：**https://github.com/DietrichGebert/ponytail

**中转站是否掺水？**
https://x.com/Pluvio9yte/status/2052552998061297804?s=20
1. [http://hovy.ai](https://t.co/X0c0ooflnX) 在线监测，只需要把api和key填入即可，这里我测了一个X上一个中转站的1.5倍率分组，测试结果如图1所示。 可以看到是未达标准的，这种就是严重掺水的，就不建议使用。 此外，该网站上也有一些中转站的聚合榜单，实时标注了在线率，掺水率等，可以作为参考 
2. api-relay-audit 这是一个开源项目，评测维度更多一些。测试结果见图二。我使用体验下来，因为很多Claude Max满血分组是做了限制的，只允许在Claude Code客户端调用，所以有时候，测试仍然不全面，不过可以作为参考的维度。 开源地址： [https://github.com/toby-bridges/api-relay-audit](https://t.co/lAtPbdMo43) 
3. Skill 该Skill通过自省式分析检测当前 API 是否为真实 Claude 模型，或是否存在多层封装和提示词冲突。 使用教程：直接在Claude Code中发送提示词：使用skill进行自我检查即可 开源地址如下：[https://github.com/bi-boo/claude-model-fingerprint/blob/main/%E6%A8%A1%E5%9E%8B%E6%8C%87%E7%BA%B9%E6%A3%80%E6%B5%8B/SKILL.md](https://t.co/gew574AHVl)


AI观看视频并总结内容：解析病毒式视频的“前 3 秒钩子”、“镜头运镜”和“节奏”，然后将其转换为【结构化资产】。 接着，将所提炼出的让视频走红的框架再反馈给 AI，给出指令，例如“将这结构改写成宣传我们产品的剧本。” 只有在此时，曾经依赖个人“直觉”或“感觉”的视频制作才会演变成可重复的【工程（搭建流程）】。 当然，最终仍需要人类直觉，但随意猜测“这可能会走红”的时代已经结束。 用 AI 提取并再利用优秀结构。

https://x.com/cosmos_hzokujin/status/2073531186773909715

https://github.com/bradautomates/claude-video

连接X的MCP：docs.x.com/tools/mcp

https://mp.weixin.qq.com/s/C3IjvlViD8B1lzKTah_qGw

**Book-to-skill**：
https://github.com/virgiliojr94/book-to-skill
最适合使用 book-to-skill 的场景:
1. **高频查阅的经典技术书**：DDIA、Clean Code、Python 技术书籍等，编程时随时调取框架与方案；
2. **企业内部私有文档**：架构手册、运维规范、入职文档、产品说明（AI 训练库无相关内容，刚需）；
3. **新书 / 外文技术资料**：AI 原生训练数据未覆盖，避免 AI 编造内容；
4. **个人笔记 / 资料合集**：将 Markdown 笔记、零散文档整合为统一 Skill，统一管理。

**OpenAI Developers**：现在可以用一个提示，通过 Codex 的[@DigitalOcean](https://x.com/digitalocean)插件，启动一个持久的云开发环境。 它在你的 DigitalOcean 账户中运行，即使你离开也会继续工作。
https://x.com/OpenAIDevs/status/2070261549391024403?s=20

**EverOS**: 开源专业的一键备份codex、claude code 所有记忆的程序
https://x.com/LufzzLiz/status/2069769416930414980
[https://github.com/EverMind-AI/EverOS](https://www.google.com/url?q=https://github.com/EverMind-AI/EverOS&sa=D&source=editors&ust=1782005217718574&usg=AOvVaw0-7jNaalHxlIwjL5baaS-N)

Multica：开源托管代理平台。将编码代理变成真正的队友——分配任务、跟踪进度、复合技能。

https://github.com/multica-ai/multica/tree/main

**LLM-WIKI**：karpathy的个人知识库wiki化管理，不断填充user.md去养龙虾

卡兹克：

**skill creator**：可以评估skill
https://x.com/Khazix0918/status/2031579241062740206

推荐安装的几个skill：**Frontend Design Skills**（TOP1，AI做前端界面的品味问题），**Claude-mem**，**skill-creator**，**PUA**，**Web Access**，办公四件套（帮忙读取**docx、xlsx、pdf、pptx**）
https://x.com/Khazix0918/status/2038469585540944249?s=20

**AIHOT**：AI相关精选信息源
https://aihot.virxact.com/?category=paper&page=1

花叔：

**nuwa-skill**：蒸馏人物

**达尔文skill**：评分、自进化：https://github.com/alchaincyf/darwin-skill。

多agent协作：kimi是怎么做agent集群的？

**agent team：**

先安装环境变量：

{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}

例如，在tmux上给以下提示词：

Create a master reference guide for agent teams in a folder called docs. This will be used to help you build better and more effective agent teams in the future.
  https://code.claude.com/docs/en/agent-teams#enable-agent-teams.

存在了C:\Users\16494\docs\agent-teams-reference.md

目标：为一个名为“换乎 (huanhu)”的技能交换平台构建一个着陆页和后端 API。最终成果应该是一个可以正常运行的本地服务器，我可以在浏览器中打开它来查看着陆页，并附带一份总结文档，解释构建了哪些内容以及做出每项决策的原因。

使用 Sonnet 的分窗模式（Split Panes Mode）创建一个由 3 名成员组成、名为“huanhu”的agent team： 

前端开发（Frontend Dev）—— 利用前端设计技能为技能交换平台“换乎”构建一个着陆页。创建 src/index.html  文件，其中包含英雄区（强调技能交换、知识共享的概念）、功能网格（3个核心功能点，如“智能匹配”、“技能分类”、“安全社区”） 、热门交换类别/价格表格（3个服务层级或热门技能分类）以及一个联系/加入表单。同时创建 src/styles.css 文件，采用现代、清新的主题进行美化，使其看起来精致专业。完成后，向 QA 发送消息告知“前端开发完成”（frontend
  complete），并列出你所创建的文件。
  
  后端开发（Backend Dev）—— 为换乎平台构建一个简单的 Express.js API。运行 npm init -y 并安装 Express。创建 src/server.js 文件，包含以下端点：GET /api/features（返回 3 个平台核心功能）、GET /api/categories（返回 3个热门技能交换分类对象）、POST /api/contact（接收用户的姓名、邮箱、想交换的技能/消息并记录日志）。创建一个 README.md
  文件，说明如何运行服务器。完成后，向 QA 发送消息告知“后端构建完毕”（backend complete），并列出你所设置的端点。

  质量保证（QA）—— 在等待队友的同时，请在 tests/test-plan.md 中创建一个测试计划，概述你将针对前端和后端进行哪些检查。一旦收到前端开发人员和后端开发人员的消息，便需审阅他们的代码。检查：HTML 引用是否指向正确的 API 端点？服务器是否处理了所有路由？是否存在任何漏洞（Bugs）？将完整的测试报告撰写至 tests/report.md 中，并对每项检查的结果标明“通过/失败”（Pass/Fail）。完成之后，请向团队负责人（Team Lead）发送一份总结。

  最终交付成果： 一个运行中的服务器，地址为 http://localhost:3000，可显示“换乎”的着陆页。
  tests/report.md —— 带有通过/失败结果的 QA 测试报告。 docs/build-summary.md —— 一份总结所构建内容、关键决策及如何运行项目的文档


**loop engineering：**

Kyrie：用好 Loop 能让你事半功倍，六个实战场景教你驾驭循环工程：
https://x.com/KyrieCheungYep/status/2070333819249627273?s=20
```*
每个工作日早上 9 点：           # ① 心跳
  读 progress.md               # ⑥ 状态文件（记忆）
  找昨夜的 CI 失败 + 新 issue   # 要干的活
  对每一条：
    在独立 checkout 里起草修复   # ② Worktree
    用项目的 triage 技能         # ③ Skill
    让一个单独的 reviewer 打分    # ⑤ 子 agent（做/检分离）
    PASS：开 PR                  # ④ 连接器
    有风险：写进 progress.md 留给人
  更新 progress.md             # ⑥ 状态文件
```

① 会话内循环（盯着看，关掉会话就停），适合盯一个长任务直到完成：

```*
# Claude Code：每 5 分钟跑一次，会话开着才有效
/loop 5m 检查部署有没有跑完，跑完就告诉我结果

# OpenCode：自己用 shell 当心跳（opencode run 跑完一句就退出）
while true; do
  opencode run "检查部署是否完成，完成就回 DONE"
  sleep 300
done
```

② 跑到达标为止，让循环自己判断何时停止：

```*
# Claude Code：给一个它自己输出能证明的条件
/goal test/auth 下所有测试通过，且 npm run lint 干净。

# OpenCode：用 shell + 退出码，让命令来判停
for i in $(seq 1 8); do          # 一定要封顶，别无限跑
  opencode run "让 test/auth 的测试通过，并修掉 lint 报错。"
  if npm test -- test/auth && npm run lint; then
    echo "第 $i 次达标"; break
  fi
done
```

/goal 好用的地方在这里：每回合结束后，一个单独的小模型读一遍记录，判断“达标没有”。写代码的那个 agent 不给自己判分。它没有内置的“试 N 次就放弃”，要封顶就写进条件里，比如“跑满 20 回合就停”。

③ 无人值守定时，你睡觉它也跑：

```*
# 自己机器上用 cron：每个工作日 9 点
0 9 * * 1-5 cd /path/to/repo && claude -p "查 CI 看板，总结失败项" >> ~/cron.log 2>&1

# 同样一行，OpenCode 版
0 9 * * 1-5 cd /path/to/repo && opencode run "查 CI 看板，总结失败项" >> ~/cron.log 2>&1
```

想要笔记本关着也跑，就用云端 routine（在

[claude.ai/code/routines](https://claude.ai/code/routines)

建，跑在服务器上）或 GitHub Actions 的 schedule 触发。

④ 事件驱动，PR 打开、CI 挂了、消息到了就触发。比如一个 PR review 的 GitHub Action：

```yaml
on:
  pull_request:
    types: [opened, synchronize, reopened]
# 触发后让 agent review 这个 PR 的 diff
```

> 给循环两个刹车：一个成功条件，一个上限。成功条件说明这事什么时候算完成；上限说明最多跑几次、几分钟、多少钱。少了上限，预算会被一个达不到的目标慢慢烧掉。

第 2 步：把步骤写进一个 skill，让循环 prompt 保持一行

凡是你每次都要重新解释的东西，都该进 skill。这样定时任务的 prompt 可以缩成一句“跑 daily-triage 技能”，细节留在版本控制里，谁都能改。一个真实可用的 SKILL.md：

```markdown
---
name: daily-triage
description: 晨间维护：读进度文件，收集昨夜 CI 失败、新 issue、审计告警，
  起草安全修复（每个都由单独的 reviewer 检查），通过的开 PR，
  有风险的写进进度文件留给人。用于每日定时维护循环。
---
# 每日 triage（按顺序做，别跳过进度文件，它是你唯一的跨次记忆）

## 1. 先读记忆
- 打开 progress.md，读“进行中”和“需要人”两节。
- “已完成”里有的，不要重做。

## 2. 找活（按序，最多取 5 条）
1. 上次记录之后失败的 CI。
2. 带 bug、maintenance 标签的 open issue。
3. npm audit（或本项目审计命令）的新告警。

## 3. 逐条处理
- 开一个独立 checkout：git worktree，或新分支 claude/<短slug>。
- 起草解决“这一个”问题的最小改动，不要捆绑多个改动。
- 把 diff 交给 reviewer agent，拿到结论再继续。

## 4. 按结论决定
- PASS 且低风险（不动公开 API、无数据迁移、不删文件）：开 PR，标题 fix: <一行>，关联 issue。
- FAIL 或动到任何风险项：不开 PR，往 progress.md“需要人”追加一条，写清你试了什么、为什么停。

## 5. 最后更新记忆
- 完成项移到“已完成”并写上今天日期，保存 progress.md。

## 铁律
- 一次最多开 5 个 PR；绝不直接动 main，只用 claude/* 分支；拿不准就升级给人。
```


第 3 步：做/检分离，配一个 reviewer 子 agent

循环里很重要的一条：写活的 agent 不许给自己的活判分。模型给自己打分时经常太宽。配一个单独的、只读的、常用更便宜模型的 reviewer，它跑测试、对照规范，只回 PASS 或 FAIL：

```markdown
---
name: reviewer
description: 对照 spec 和测试结果检查 diff，回 PASS 或 FAIL 并给理由，不做任何改动。
tools: Read, Bash(npm test*), Bash(npm run lint*), Bash(git diff*)
model: claude-haiku-4-5
---
你是一个严格的只读 reviewer，从不改文件。
1. 自己跑测试和 linter，亲自读输出，别信“它说通过了”。
2. 对照 CLAUDE.md 里的项目约定和相关 spec 检查改动。
3. 找 bug、漏掉的边界情况、安全风险、对公开行为的改动。
然后只回其中一个：
- PASS：后跟一行你验证了什么。
- FAIL：后跟具体理由，一行一条。
“看起来没问题”不算 PASS。测试必须真的过，且改动只做了被要求的事。
```


> 子 agent 更费 token，每个都跑自己的模型和工具。把它花在值得第二意见的地方，比如任何会在你不盯着时提交东西的循环；只读的小杂活就别配了。

第 4 步：装上状态文件

模型每次跑完就忘，记忆必须放在模型之外、放在磁盘上。可以分两层：一层是规则文件（CLAUDE.md、AGENTS.md，记录稳定习惯，保持短，因为每次读都要花钱）；一层是进度文件，记“试了什么、过了什么、还开着什么”：

```markdown
<!-- progress.md：循环的跨次记忆 -->
## 已完成
- 2026-06-22：修了 test/auth 的 flaky 测试（token 刷新时重试）
## 进行中
- 依赖审计：7 个告警修了 3 个；lodash 升级遇到一个 API 变更
## 需要人
- 图像库 CVE-2026-xxxx：修复会改输出格式，升级给维护者
```

习惯就一条：每次跑，开头读它，结尾更新它。当循环反复犯同一个错，别急着写更玄的 prompt，把教训写进规则文件，让后面的每一次运行都能读到。

第 5 步：接上工具，让它能动手

只能读文件的循环只会“说”。连接器（基于 MCP）让它开 PR、更新工单、发 Slack、查库、调 staging API。一个系统只能说“这是修复方案”，另一个系统能在测试通过后开 PR、关联工单、发频道，差别就在这里。把你手动用的那些连接器，加进定时或云端 routine 的连接器清单即可。

把六件拼起来：一个真实早晨

你把上面这些设计一次。某个早晨醒来，记录可能是这样：

```*
[09:00] daily-triage 触发
  → 读 progress.md：1 项还在进行（lodash），无新标记
  → 发现：昨夜 2 个 CI 失败、1 个新 npm-audit 告警
  → CI 失败 #1（flaky auth 测试）：
        在 claude/fix-auth-retry 分支起草修复
        reviewer → PASS（测试绿；token 刷新重试；无 API 改动）→ 开 PR #142
  → CI 失败 #2（report.ts 类型错）：
        起草修复 → reviewer → PASS → 开 PR #143
  → 告警（图像库）：安全修复会改输出格式
        reviewer → FAIL（公开行为变更）→ 写进 progress.md“需要人”，不开 PR
  → 更新 progress.md，退出
[你，09:30] 两个待 review 的 PR，一个要拍板的事项。你一个字没敲。
```
这就是循环工程在干的事：找活、起草、检查，把安全的部分发出去，只把真正需要人的决定交到你手里。Claude Code 和 OpenCode 的差别，主要在心跳和运行位置；中间的 skill、状态文件、worktree、做/检分离、连接器，设计思路差不多。


## 

四、它能省下哪些重复劳动

骨架学会了，就可以把“晨间维护”这套东西搬到别的活上。别急着扩大范围，先问一句：产出能不能被命令、清单或另一个 agent 验收？

代码与工程类

可以交出去的活：每天扒 CI 失败、给 issue 分诊、修一类反复出现的 bug、跑依赖升级、做框架迁移、逐个 review PR。

做法基本沿用晨间维护循环。常见变体有几种：

- “跑到测试通过为止”：/goal test/auth 全过且 lint 干净，让小模型判停。
    
- 框架/API 迁移（清空队列模式）：找下一个还在用旧 API 的文件，迁到新写法，跑测试，停止条件是“没有文件再匹配旧写法”，封顶 200 次。
    
- 安全漏洞规模化：这类已有公开案例，比如某浏览器一个月提交 423 个安全修复。关键不只在模型能力，也在外层结构：先用一个简单的 LLM 评委给每个文件打分（出内存安全问题的可能性 × 从网页触发的难易度）排优先级；agent 可以连续尝试很多办法去触发一个 bug；验证再分两段，先触发真实崩溃，再让 verifier 确认报告合理。误报会少很多。同一结构也能用于性能优化、技术债。
    

内容流水线类

可以交出去的活：批量清洗文案、把粗想法变 hook、把一篇长内容拆成多平台版本、按缺口批量生成文章。

这里要把“完成态”写成数得出来的检查。比如：

```text
/goal 把 captions.txt 里每条改写到 150 字内、不带话题标签，全部改完为止，
      别动其他文件，最多 30 回合。      # 可验收：0 条超 150 字或含 #

/goal 把 ideas.txt 里 20 个粗想法各改成一个 10 词内的 hook，全做完为止。
                                       # 可验收：20 条全部改写完
```

更大的形态是多 agent 流水线：一个 agent 按内容缺口生成配图文章并排版，一个 agent 推送发布。但这里要清醒一点。模型越强，瓶颈越像指挥者的品味。循环会放大你写进 rubric、skill、验证步骤里的判断；判断糊了，它只是更快地生产一堆你不该发的东西。

信息监控与研究类

可以交出去的活：盯日志、盯服务健康、盯竞品定价页、盯 API changelog、盯一个领域的新闻、做一轮竞品调研。

按触发方式，可以分四种：

- 心跳：短间隔持续跑。每 5 分钟查 staging 错误日志，错误率超 1% 就开 issue。
    
- 定时：固定时间跑批。每工作日 10 点 review 所有超 3 天的 PR，逐个总结阻塞并 @ 作者。
    
- 钩子：事件触发跑一次。PR 推上来、CI 挂了、消息到了。
    
- 目标：迭代到达标才停，适合范围未知的任务。找出我们品类所有公开竞品，按这五个维度打分，起草定位简报。
    

还有一种办法，是把实时网页当心跳：监控一组 URL，内容一变就触发。定价页改了，启动竞品响应；changelog 更新了，触发文档重写；状态页出事，叫醒 on-call。个人场景里最轻的版本，就是晨间简报：每天早上读未读邮件，把最重要的 3 封各一行发我 Slack，别回任何东西。

文档生成类

可以交出去的活：把一摞 PDF 逐个写摘要、把零散数据整成结构化报告、按模板写提案/方案初稿、维护一份会过时的文档。

核心是“清空队列 + 反思、多 agent 检查”：

```text
/goal 给 reports 文件夹每个 PDF 写 5 行白话摘要到 summaries.md，
      每个都有为止，别改 PDF，最多 40 回合。  # 可验收：每个 PDF 都有对应摘要
```

按风险选循环模式：

- 反思 + schema 校验：起草结构化报告，对照 schema 补全缺字段，人最后过一遍。适合工地报告、表单类。
    
- 多 agent review + 人类闸门：A 起草，B 查规范、查合规、标出不该出现的敏感标识，人签字。适合诊疗方案、合规文档。
    
- 反思 + 清单校验：起草，对照方法论框架、字数格式和数据一致性检查，再标出需佐证的论断。适合提案。
    
- 带护栏的自治：逐条或逐批校验，只把没过自动检查的（通常 <5%）升级给人。适合数据批处理。
    

文档写手循环还能再套四层：① agent 干活（克隆仓库、读写文件、开 PR）；② 验证循环（一个 grader 跑检查，链接是否都通、CI 是否全绿、diff 是否只动了被要求的范围，不达标就带反馈打回）；③ 事件循环（某频道一来消息就触发）；④ 改进循环（拿运行记录喂分析 agent，自动改进 prompt 或工具配置）。

个人事务与办公

可以交出去的活：清理爆满收件箱、每月那份你一想到就头疼的报告、客服工单清理。

做法也不用复杂。用“目标 + 定时器”拼第一个自治 agent，不用写代码。建一个 routine：“每天早上读未读邮件，最重要的 3 封各一行发我 Slack，别回任何东西”，连上 Gmail/Slack，设每天 9 点。进阶时再加一个 skill，里面写你的处理方法；再加一个独立 checker，比如它判断某个被自动关闭的工单该留给人，就重新打开。

安全建议很简单：先只读。让它先“总结、汇报”跑几天，用大白话设死限制（“不许回复”“不许删除”），看着头几次跑，再让它动手。

商业与运营

替你处理：那些本来周期性做、其实该连续做的决策。定价每季度看一次竞品再调，HR 每年调研一次半年后才行动，产品每 sprint 按上月数据排一次优先级，这些都可以重新看。

做法是从“能力地图”升级成“循环地图”。对每项能力问：它是流程型（传统自动化）？工具辅助型（给人配更好工具）？还是目标驱动型（部署一个有边界、有升级触发、有人类监督的循环）？把“定价信号每天评估、实时建议”“持续追踪早期流失、在人递辞呈前标出干预点”这种位置识别出来。真正的价值，常常来自一个原本不存在的决策循环，或者把慢的季度循环改成更快的连续循环。

也要记得行业现实。Gartner 预测到 2027 年底，超过 40% 的 agentic AI 项目会被砍掉，原因是成本失控、价值不清、风控不足。很多问题都指向同一件事：把 agent 硬塞进碎片化流程，却没想清楚循环该装在哪、需要什么才能跑。

## 

  

## 

五、风险与边界

循环改变了工作方式，但没把你从工作里删掉。循环越强，下面三个问题越绕不开。

1. 让循环停下来很难。每个循环都得带硬刹车，三道闸尽量都要有：
    

- 迭代次数硬上限：跑不动的循环不能一直转；
    
- 无进展检测：最近几轮没有任何变化，就停；
    
- token、美元预算上限：账单失控前先停。
    

三者缺一，账单就容易失控。一个朴素的成本感：一拍（maker + checker）约读 4 万、写 6 千 token，按 Sonnet 4.6 价约 0.2 美元一拍；一天 5 拍、一月 20 天约 20 美元，便宜。同一循环改成全天每 5 分钟一拍，拍数上百倍，轻松破 1000 美元一月，却未必多产出价值。真正花钱的是频率。省钱三招：模型分级（强模型规划与检查、便宜模型干活，这是最大头的省）、prompt 和规则文件保持短、降低频率（每小时一次比每 5 分钟一次便宜约 12 倍）。

1. 验证还是你的活。无人值守地跑，也会无人值守地犯错。把做和检拆开，是为了让“做完了”有点分量；但“done”只是声明，还得看证据。读循环开的 diff，对它产出的代码负责。最诚实的 checker 是测试 runner 和 linter，命令没法说服自己“这活挺好”。
    
2. 理解会慢慢变薄。循环把你没写的代码更快送进仓库，“仓库里有什么”和“你真正理解什么”之间的缺口会变大（comprehension debt，理解债）。循环跑起来以后，人也容易照单全收（cognitive surrender，认知投降）。同样是设计循环，带着判断去做，它会帮你把熟悉的工作推进得更快；为了逃避思考去做，它会把你推到更陌生的地方。循环分不出这两种情况，人得自己分。
     

六、上手节奏：一阶一阶赚信任

不要追求一步到位，一步跳到“自动合并”。按成熟度阶梯，一次爬一格。当前这格产出的东西，已经是你本来也会手动接受的结果，再往上走。


![[Pasted image 20260627173411.png]]



放手前的最小安全清单有七样：成功条件、上限（次数、分钟、花费）、隔离分支或 worktree、只读的 checker、状态文件、人类闸门（风险或失败的活交给人，绝不直推 main）、日志或通知（夜里出事要看得见）。缺一样，循环就容易不安全、健忘，或者出了事没人知道。

一个好记的公式：

> AI 杠杆 = 你的技能 × 你的清晰度

> 清晰度：把“完成长什么样”定义清楚的能力。

> 技能：review 产出、改进循环的能力。

## 

  

每一年，工具都会吸收掉更多机械部分：编排、检查、调度。去年还要靠自己的 shell 脚本，今年变成内置的 /goal、routine、dynamic workflow。但工具吸收不掉两端的东西：意图（说清楚到结果可被验收）和担责（对发出去的东西负责）。这也是它叫“工程”的原因。

去搭你的循环，把那些重复、可验的活交出去。但要像一个打算继续当工程师的人那样去搭它。读循环写出来的东西，对质量负责，写好 skill，定义好停止条件。

循环可以让你在已经理解的工作上更快，也可以帮你逃开那些本该理解的部分。选哪条路，工具不会替你决定。

  

关于作者

Kyrie — 前国内大厂 R&D 工程师，现居曼谷，做中国科技企业出海 BD。持续分享出海一线真实记录、AI 在业务里的实战用法，偶尔也聊聊美股投资和国外生活。






https://mp.weixin.qq.com/s/kICrdEkPCYAiyOiwI-Gt1Q

https://x.com/addyosmani/status/2064127981161959567?s=20




**Deli-Auto-research：**

https://victorchen96.github.io/auto_research/framework.html

**Headroom**：压缩上下文，省token
https://github.com/chopratejas/headroom#get-started-60-seconds

怎么看github最新热点？①explore热门，②awesome，③hellogithub


![[Pasted image 20260620220822.png|282]]


AI提示词：李开复的提示词

![[Pasted image 20260621165043.png]]


**Agent-reach**：给你的 AI 代理“眼睛”，让它看到整個互联网。阅读与搜索 Twitter、Reddit、YouTube、GitHub、Bilibili、小红书——一个 CLI，零 API 费用。

https://github.com/Panniantong/Agent-Reach

**Superpowers**：给 Agent 装上一整套资深工程师的工作方法： 先拆需求，再写计划，按测试驱动开发，最后再派一个子 Agent 回头审查自己的代码。 这是目前最强的 Skill 之一，实至名归。

https://github.com/obra/superpowers


**Humanizer-zh**：专门去掉 AI 写作痕迹，比如滥用的破折号、空话套话、机械句式。 写文档、README、博客时，最后过一遍非常好用

https://github.com/op7418/Humanizer-zh


**vault-maintainer**：知识库维护员

维护 Obsidian vault 的规范性。比如：wikilink 是否规范 frontmatter 是否完整 文件名是否安全 路径是否混乱 笔记是否适合 Obsidian 读取 结构是否容易被 AI 调用。如果你有一个越来越大的知识库，这个 Skill 很有用。因为 Obsidian 用久了，最容易出现的问题不是“没资料”，而是：文件名乱。 标签乱。 双链乱。 属性乱。 同一主题重复写了好几篇。适合人群：Obsidian 重度用户 知识库玩家 AI Agent 用户 长期写笔记的人 用 Obsidian 管理项目的人


**obsidian-vault**：日常笔记读写必备

它更像 AI Agent 操作 Obsidian 的基础工具。主要能力是：读取笔记 搜索笔记 创建笔记 编辑笔记 追加内容 添加 wikilink。它适合日常笔记管理。比如你可以说：请在我的 Obsidian vault 里创建一篇新笔记。 标题：AI 内容工作流 内容包括： 1. 什么是 AI 内容工作流 2. 适合哪些人 3. 典型流程 4. 常用工具 5. 后续可补充的问题 请使用 Markdown 格式，并添加合适标签。

或者：请搜索我的 vault 里所有关于 Claude Code 的笔记， 帮我整理成一个目录索引。obsidian-vault 解决的是“AI 怎么安全读写我的笔记”。对小白来说，这是最应该优先理解的 Skill 之一。因为没有读写能力，后面很多高级玩法都跑不起来。

**qmd 语义搜索**：比关键词搜索更聪明

它解决的是一个很常见的问题：你明明记得自己写过某个内容，但搜关键词就是搜不到。比如你想找：“如何用 AI 做知识库”，但原文里写的是：“本地第二大脑搭建方法”，关键词不一样，传统搜索可能找不到。qmd 这类语义搜索更适合找“意思相近”的内容。它通常会结合：关键词搜索 语义检索 排序重排 本地知识库搜索，适合这些场景：找旧笔记 搜会议记录 搜研究资料 搜项目文档 搜学习笔记 搜写作素材

**clipper-template**：网页剪藏模板生成器

很多人搭知识库，第一步就是收藏网页。但网页剪藏很容易乱：标题不统一。 来源没记录。 摘要没写。 标签没加。 正文格式混乱。 以后根本不知道为什么收藏它。clipper-template 的价值是帮你把网页收藏变成统一模板。比如：请为网页剪藏生成一个 Obsidian 模板。 模板需要包含： 1. 标题 2. 原文链接 3. 作者/来源 4. 发布时间 5. 收藏时间 6. 核心摘要 7. 关键观点 8. 我的思考 9. 可延伸选题 10. 标签；这样你每次收藏网页，都不是简单丢进仓库，而是自动变成结构化资料。

**diary**：多项目日记系统

很多人写日记只写情绪。但如果你做项目、做内容、做学习计划，日记其实可以变成复盘系统。diary 适合做多项目日记。比如你可以分成：AI 工具学习日记 X 增长日记 独立开发日记 内容创作日记 健身复盘日记 读书日记；提示词：请帮我创建今天的项目日记。 项目：X 增长实战 日期：今天 内容结构： 1. 今天做了什么 2. 数据变化 3. 遇到的问题 4. 学到的经验 5. 明天要做什么 6. 可沉淀成知识库的内容。如果你想长期做个人 IP、内容号、独立项目，这个 Skill 很适合。

**obsidian-markdown**：让 AI 懂 Obsidian 的 Markdown 规则

Markdown 很多人都会。但 Obsidian 的 Markdown 有自己的特点。比如：wikilink 标签 callout embed frontmatter 属性 内部链接 双链网络；obsidian-markdown 的作用，就是让 AI 更懂 Obsidian 的写法。比如你可以要求：请把这篇普通 Markdown 笔记， 改成更适合 Obsidian 的格式。 要求： 1. 增加 YAML frontmatter 2. 增加 tags 3. 增加相关笔记 wikilink 4. 使用 callout 标注重点 5. 保持正文可读性。如果你希望 AI 帮你整理笔记，这个 Skill 很基础。


**obsidian-bases**：结构化数据库管理

Obsidian Bases 可以理解成一种结构化视图。它适合管理：项目库 书籍库 课程库 工具库 客户资料 文章选题 任务清单 研究资料。比如你有一个 AI 工具库，可以让 AI 帮你设计字段：请帮我为 AI 工具库设计一个 Obsidian Bases 结构。 字段包括： 1. 工具名称 2. 官网 3. 类型 4. 适合人群 5. 是否免费 6. 使用场景 7. 我的评分 8. 相关文章 9. 状态：待测试 / 已测试 / 推荐 / 不推荐。如果你做工具测评、项目管理、选题库，这个 Skill 很适合。

**json-canvas**：可视化白板 / 思维导图

Obsidian 的 Canvas 很适合做可视化关系图。比如：知识地图 产品流程图 文章结构图 项目规划图 学习路线图 选题关系图 人物关系图。json-canvas 可以帮 AI 创建和编辑 .canvas 文件。比如：请基于我的 10 篇 AI Agent 笔记， 生成一个 Obsidian Canvas 知识图谱。 要求： 1. 中心节点是 AI Agent 2. 周围分成：工具、工作流、案例、风险、学习路线 3. 每个节点链接到对应笔记 4. 节点之间标出关系。如果你做学习路线、课程设计、项目规划，这个 Skill 很实

**obsidian-cli**：命令行管理 vault。

最后一个是 obsidian-cli。它更适合进阶用户。可以用于：管理 vault 查找笔记 创建笔记 处理任务 维护属性 开发插件 调试主题 执行命令行操作。小白可以先不用急着上手，但要知道它的价值：当你的知识库越来越大，命令行管理会比手动点来点去更高效。比如：请通过 Obsidian CLI 帮我检查 vault 状态。 要求： 1. 列出最近 7 天修改过的笔记 2. 找出没有标签的笔记 3. 找出没有 frontmatter 的笔记 4. 生成一份维护报告 5. 不要直接修改文件。注意：命令行操作风险更高。 涉及删除、移动、覆盖，一定要先让 AI 给计划，再确认执行。


如果你刚开始，不建议一口气装 10 个。先从这 3 个开始：

1. obsidian-金库，解决日常读写问题。

2. obsidian-markdown，让 AI 写出符合 Obsidian 习惯的笔记。

3. defuddle 或 clipper-template如果你经常收藏网页，优先装网页清洗和剪藏模板。

等你知识库大了，再上：qmd 语义搜索 vault-maintainer obsidian-bases json-canvas obsidian-cli。Skill 不是越多越好，先解决读写、格式、剪藏这三个高频问题。

怎么安装？给一个最稳步骤

如果你用的是 kepano 的 Obsidian Skills，可以用官方推荐的方式安装。常见方式是：npx skills add [https://github.com/kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)

或者使用 Git SSH：npx skills add git@github.com:kepano/obsidian-skills.git

但要注意：不同 Skill 来源不同。 有些在 kepano 仓库。 有些在 NousResearch / Hermes Agent。 有些来自 OpenClaw 或其他生态。所以不要看到一个安装命令，就以为 10 个都来自同一个仓库。

更稳的做法是：

1. 先确认 Skill 来源
    
2. 看 README 和 SKILL.md
    
3. 看它会不会执行 shell 命令
    
4. 看它会不会改文件
    
5. 先在测试 vault 里试
    
6. 没问题再用到正式 vault
    

## 

这类 Skill 适合哪些人？

✅Obsidian 用户

已经在用 Obsidian，但笔记越来越乱。

✅ Claude Code / Codex / Cursor 用户

想让 Agent 不只是写代码，也能管理知识库。

✅ 自媒体创作者

需要管理选题、素材、网页剪藏、文章输出。

✅ 研究生 / 学生

需要整理论文、课程笔记、研究资料。

✅ 独立开发者

需要管理产品想法、技术文档、用户反馈、项目日志。

✅ 知识管理玩家

想把 Obsidian 变成 AI 可操作的第二大脑。

## 

必须注意的 5 个坑

坑一：不要直接在正式库里测试

先建一个测试 vault。

把几篇假笔记放进去，确认 Skill 行为正常再用到正式库。

坑二：不要让 AI 直接批量删除文件

删除、移动、重命名，一定要人工确认。

坑三：不要乱装来源不明的 Skill

Skill 本质上是在教 Agent 怎么做事。 如果来源不可信，可能带来数据和权限风险。

坑四：不要把敏感资料随便交给 Agent

公司文件、客户信息、合同、财务数据、个人隐私，先脱敏再处理。

坑五：不要迷信安装量

安装量高，只说明关注度高，不代表一定适合你。

## 

最后总结

这 10 个 Obsidian AI Skill，可以这样理解：

1. vault-maintainer：维护知识库规范
    
2. obsidian-vault：读写搜索笔记
    
3. qmd：语义搜索知识库
    
4. clipper-template：网页剪藏模板
    
5. diary：多项目日记系统
    
6. obsidian-markdown：Obsidian 标准 Markdown
    
7. obsidian-bases：结构化数据库
    
8. json-canvas：白板和思维导图
    
9. defuddle：网页内容提取去广告
    
10. obsidian-cli：命令行管理 vault
    

Obsidian 是知识库的地基，AI Skill 是让 Agent 正确施工的工具箱。




**斯坦福STORM系统**：由多角度构建的文章比以常规方式构建的文章更有条理，覆盖范围也更广，分别高出25%和10%。这就是整个突破。多角度提问可以捕捉单一提示研究从未看到的盲点。
https://x.com/heynavtoor/status/2067194761446920264
https://github.com/stanford-oval/storm

## 

提示1，多角度扫描

这是该方法的核心。把这段粘贴到 Claude 中。将第 1 行的主题替换为你要的主题。

```*
I need to research [YOUR TOPIC].
Simulate 5 different expert perspectives on this topic:
1. THE PRACTITIONER: works with this daily.
What do they know that academics miss?
What practical realities are usually ignored?
2. THE ACADEMIC: has studied this for years.
What does the peer reviewed evidence actually say?
Where does the evidence contradict popular belief?
3. THE SKEPTIC: thinks the mainstream view is wrong.
What is the strongest counterargument?
What evidence do proponents conveniently ignore?
4. THE ECONOMIST: follows the money.
Who profits from the current narrative?
What financial incentives shape the research?
5. THE HISTORIAN: has seen similar patterns before.
What historical parallels exist?
What can we learn from how those played out?
For each perspective give me:
- Their core position in 2 sentences
- The strongest evidence supporting their view
- The one thing they would tell me that no other perspective would
```

返回的是什么： 对同一主题的五种截然不同的解读。实践者看到学者所忽略的。怀疑者挑战实践者的假设。经济学家揭示学者忽视的激励。历史学家提供经济学家看不到的模式。

这只是60秒的工作，捕捉到一个提示永远找不到的内容。

## 

提示 2，矛盾地图

现在让 Claude 找出五个声音在哪里交锋。真正理解存在的地方就是在冲突处。

```*
Based on the 5 perspectives above, map the contradictions:
1. Where do two or more perspectives directly contradict
each other? List each conflict with the specific claims
that clash.
2. Which perspective has the strongest evidence?
Which has the weakest? Why?
3. What is the one question that, if answered, would
resolve the biggest contradiction?
4. What does EVERY perspective agree on?
(This is likely true. Even opponents confirm it.)
5. What topic did NONE of the perspectives address?
(This is the blind spot in the whole field.
Often the most valuable finding.)
```

返回的将是：专家意见分歧的地图及其原因。大多数人忽略这一步。这一步将表面的理解与真正的专业知识区分开来。

> 如果所有5个视角都同意，那可能就是真的。如果没有人讨论过某个话题，你就刚好找到了整个领域的空白。

## 

提示 3，综合（Synthesis）

现在让 Claude 把所有内容整合成一份研究简报。

```*
Synthesize everything from the 5 perspectives and the
contradiction map into a research briefing:
1. THE ONE PARAGRAPH SUMMARY: explain this topic as if
briefing a CEO who has 60 seconds and needs nuance,
not just the headline.
2. THE 5 KEY FINDINGS: most important things I now know,
ranked by reliability. For each, note which perspectives
support it and which challenge it.
3. THE HIDDEN CONNECTION: one non obvious link between
findings that only shows up when you look at all 5
perspectives together.
4. THE ACTIONABLE INSIGHT: based on all the evidence,
what should someone in [YOUR ROLE] actually DO
differently? Be specific.
5. THE FRONTIER QUESTION: the one question that, if
answered, would change everything about how we
understand this topic.
```

返回的是：一份连一个专家也写不出的简报。它考虑到所有角度，点出矛盾，评估可信度，并给出具体行动。这是一个博士生在48小时内能产出的东西。你只用了90秒就拿到了。

## 

提示 4，同行评审

STORM 有一个众所周知的弱点。斯坦福自己的研究人员也指出了它。该系统不会自我批评。 来源偏见 以及 事实错置 会偷偷混入。这个提示通过让 Claude 评估自己的工作来解决这个问题。

```*
Now peer review your own research briefing:
1. CONFIDENCE SCORES: rate each of the 5 key findings
on a 1 to 10 scale for reliability. Explain each score.
2. WEAKEST LINK: which claim are you least confident in?
What specific info would you need to verify it?
3. BIAS CHECK: which perspective might be overrepresented
in your synthesis? Did one voice dominate?
4. MISSING PERSPECTIVE: is there a 6th angle I should
have included that would change the conclusions?
5. OVERALL GRADE: if a Stanford professor reviewed this
briefing, what grade would they give and why?
What would they tell me to fix?
```

What comes back: → 回来的是你自己研究的诚实解读。强烈的主张、薄弱的主张、偏见、被遗漏的角度。真正的同行评审要几个月。你在 60 秒内已经完成了。

## 

5分钟工作流

第 1 分钟： 提示 1。你有 5 个专家观点。

第 2 至 3 分钟： 提示 2。你有一个矛盾地图。

第 3 至 4 分钟： 提示 3。你有一份研究简报。

第 5 分钟： 提示 4。你知道什么是可靠的，什么不是。

总时长：5分钟。输出：一个多角度简报，包含矛盾分析、综合、具体行动，以及可靠性评分。

一个博士生手工完成这件事需要40到60个小时。不是因为他们慢，而是因为从五个角度阅读、映射矛盾、综合并自我批评，实实在在是一个人脑需要花费的40小时工作。

## 

从今天开始的 7 种使用方法

1. 在撰写任何文章或报告之前。 运行这4个提示。你的作品将覆盖别人都没想到的角度。

2. 在做出重大商业决策之前。 获取全部5个视角。实操者告诉你现实中的可行之处。怀疑论者告诉你可能出错的地方。经济学家告诉你谁在获利。

3. 在面试前。 用5分钟从5个角度研究公司。实务者视角让你掌握内部用语；怀疑论者视角让你提出尖锐问题。你走进房间时比在场任何人都更加有备而来。

4. 投资之前。 牛市情景、熊市情景、历史对比、激励地图、学术证据。5分钟内。矛盾地图显示实际风险所在。

5. 在学习新技能之前。将领域从5个角度进行映射。实务者告诉你先学什么；学术界告诉你理论；怀疑论者告诉你哪些被夸大。你跳过噪音。

6. 在谈判前进行研究。从五个角度了解对方：他们的动机、弱点、历史行为。你带着结构性优势走进谈判。

7. 在任何演示文稿之前。 对你的议题运行 STORM。你的幻灯片将先回答观众提出的反对意见。你的问答将显得毫不费力。