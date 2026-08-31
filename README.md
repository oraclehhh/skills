# Skills 技能目录

**中文目录**

每个 Skill 按名称只列一次；仓库仍保留本机的全部源文件。每项简介均为基于对应 `SKILL.md` 内容提炼的一句话。

Skill 数量：197

| Skill 名称 | 来源路径 | 一句话功能概括 |
|---|---|---|
| ``academic-paper`` | ``agent-skills/academic-paper/SKILL.md`` | 学术论文写作工具，支持12个代理和10种模式，涵盖6种论文类型和5种引用格式，提供 双语摘要、LaTeX/DOCX/PDF输出，具备风格校准、写作质量检查和反模式标记功能。 |
| ``academic-paper-reviewer`` | ``agent-skills/academic-paper-reviewer/SKILL.md`` | 学术论文评审工具，模拟多角度评审，支持全面评审、快速评估、方法论重点、苏格拉 底引导等多种模式，适用于论文评审、同行评审、手稿评审、审稿报告、审稿人校准等 场景。 |
| ``academic-pipeline`` | ``agent-skills/academic-pipeline/SKILL.md`` | academic-pipeline 是一个全面的学术研究工作流管理工具，涵盖从研究到最终出版的 全过程，包括撰写、完整性检查、同行评审、修订、再评审、再修订、最终完整性检查 和最终确定。它协调深度研究、学术论文和学术论文评审者，形成一个无缝的10阶段工 作流，强制性地进行完整性验证，两次同行评审，并设置可重复的质量门。适用于学术 研究到论文的全过程，从研究到出版的完整工作流，以及从研究到最终出版的全过程。 |
| ``andrej-karpathy-perspective`` | ``agent-skills/andrej-karpathy-perspective/SKILL.md`` | Karpathy式思维顾问视角，分析AI技术可靠性、学习 方法、行业趋势、产品设计。 |
| ``autoplan`` | ``codex-skills/gstack/autoplan/SKILL.md`` | 自动审查流程，读取CEO、设计、工程和用户体验审查技能，自动决策并运 行所有审查，最终在审批门展示品味决策，一键生成完整审查计划。 |
| ``beck-perspective`` | ``agent-skills/beck-perspective/SKILL.md`` | 基于Judith S. Beck的思维框架与表达方式，提供结构化决策、技 能学习、解决问题、认知重构和行为改变的视角。 |
| ``benchmark`` | ``codex-skills/gstack/benchmark/SKILL.md`` | benchmark用于检测性能回归，建立页面加载时间、核心网页指标和资源大小的基线， 并比较每次PR的前后情况，追踪性能随时间的变化趋势。 |
| ``benchmark-models`` | ``codex-skills/gstack/benchmark-models/SKILL.md`` | 比较Claude、GPT和Gemini模型，评估延迟、令牌数、成本和质量 ，找出最适合特定技能的模型。 |
| ``book-to-skill`` | ``agent-skills/book-to-skill/SKILL.md`` | 将书籍和文档转换为结构化 Skill，提取其中的框架、思维模型、原则、技巧和反模式。 |
| ``brainstorming`` | ``agent-skills/brainstorming/SKILL.md`` | brainstorming工具用于在任何创意工作之前探索用户意图、需求和设计，以创建功能 、构建组件、添加功能或修改行为。 |
| ``browse`` | ``codex-skills/gstack/browse/SKILL.md`` | browse 是一个快速无头浏览器，用于 QA 测试和网站用户体验测试。它可以导航任何 URL，与页面元素交互，验证页面状态，对比前后操作，生成注释截图，检查响应式布 局，测试表单和上传，处理对话框，并断言元素状态。每条命令约需 100 毫秒。适用 于测试功能、验证部署、用户体验测试或提交带有证据的 bug。当需要“在浏览器中打 开”、“测试网站”、“截图”或“用户体验测试”时使用。 |
| ``canary`` | ``codex-skills/gstack/canary/SKILL.md`` | 部署后 Canary 监控，实时检测生产应用的控制台错误、性能退化和页面故障 ，通过浏览守护进程进行监控。定期截图，与预部署基线对比，对异常进行警报。适用 于“监控部署”、“Canary”、“部署后检查”、“监控生产”、“验证部署”。 |
| ``careful`` | ``codex-skills/gstack/careful/SKILL.md`` | 在执行危险命令前提供安全护栏，如rm -rf、DROP TABLE等，并允许用户覆 盖警告。适用于触碰生产环境、调试实时系统或在共享环境中工作。 |
| ``check`` | ``codex-skills/check/SKILL.md`` | check 用于独立核验学术论文、学位论文、综述和研究报告中的引用真假、逻辑合理性 、论证漏洞、AI味、机器腔、套话、重复总结、过度铺垫、最终稿审计或修改后复检。 |
| ``chuanxilu-wang-yangming`` | ``codex-skills/chuanxilu-wang-yangming/SKILL.md`` | chuanxilu-wang-yangming 是一本由张靖杰注释/翻译的《传习录》全译全注版本，适 用于应用王阳明心学框架，如心即理、知行合一、致良知、格物诚意、事上磨炼、四句 教和道德自我修养。 |
| ``code-review`` | ``agent-skills/code-review/SKILL.md`` | code-review工具详细检查代码的正确性、安全性、性能、可读性和测试覆盖率，并提 供按严重性排序的可操作反馈。 |
| ``codex`` | ``codex-skills/gstack/codex/SKILL.md`` | codex是一款代码审查工具，支持独立差异审查、挑战模式和咨询模式，提供第二意见 和持续对话功能。 |
| ``Codex-to-im`` | ``agent-skills/claude-to-im/SKILL.md`` | 将 Codex 会话桥接到 Telegram、Discord、Feishu/Lark、QQ 和微信，方便用户通过手机聊天。 |
| ``computer-use`` | ``plugin-skills/openai-bundled/computer-use/26.825.41651/skills/computer-use/SKILL.md`` | 通过ChatGPT控制Windows应用程序。 |
| ``context-restore`` | ``codex-skills/gstack/context-restore/SKILL.md`` | context-restore 用于恢复之前保存的工作上下文，支持跨分支加载最新保存状态，帮 助用户继续之前的工作。 |
| ``context-save`` | ``codex-skills/gstack/context-save/SKILL.md`` | context-save 保存工作上下文，捕捉Git状态、已做决定和剩余工作，以便未来会话无 缝继续。 |
| ``control-chrome`` | ``plugin-skills/openai-bundled/chrome/26.825.41651/skills/control-chrome/SKILL.md`` | control-chrome用于控制用户的Chrome浏览器，适用于依赖现有Chrome状态的任务，如 标签页、登录会话或扩展。优先使用自定义连接器、API或命令行工具。 |
| ``control-in-app-browser`` | ``plugin-skills/openai-bundled/browser/26.825.41651/skills/control-in-app-browser/SKILL.md`` | control-in-app-browser用于控制应用程序内浏览器，支持打开、导航、检查可见或交 互式页面状态、点击、输入、截图和本地网页测试。 |
| ``cso`` | ``codex-skills/gstack/cso/SKILL.md`` | CSO模式的基础设施优先安全审计工具，涵盖秘密考古、依赖供应链、CI/CD管道安全、 LLM/AI安全、技能供应链扫描，以及OWASP Top 10、STRIDE威胁建模和主动验证。两种 模式：日常（零噪音，8/10信心门限）和全面（每月深度扫描，2/10门槛）。审计运行 趋势跟踪。适用于安全审计、威胁建模、渗透测试审查、OWASP和CSO审查。 |
| ``darwin-skill`` | ``agent-skills/darwin-skill/SKILL.md`` | 达尔文-skill 2.0 是一个自主技能优化工具，通过9维评分标准和验证机制，自动优化 和评估用户技能。 |
| ``deep-research`` | ``agent-skills/deep-research/SKILL.md`` | deep-research 是一个全面的深度研究代理团队，提供13个代理管道，用于严谨的学术 研究，适用于任何主题。它包含7种模式：全面研究、快速简报、论文审查、文献综述 、事实核查、苏格拉底引导研究对话以及系统性审查，可选配元分析。涵盖研究问题的 形成、苏格拉底指导、方法论设计、系统性文献搜索、来源验证、跨源合成、偏倚风险 评估、元分析、APA 7.0报告编纂、编辑审查、魔鬼代言人挑战、伦理审查以及研究后 的文献监测。触发条件：研究、深度研究、文献综述、系统性审查、元分析、PRISMA、 证据合成。 |
| ``Deli_AutoResearch`` | ``agent-skills/Deli_AutoResearch/SKILL.md`` | Deli_AutoResearch 是一个用于长期自主任务的协议框架，通过规定状态管理、停顿检 测和看门狗机制来解决认知循环、停顿和运行时脆弱性等三个实证观察到的失败模式。 该工具已在多种任务类型上得到验证，包括论文撰写（4篇 ICLR 格式的调查，框架内 自我评分 8.0-8.6/10）。 |
| ``design-consultation`` | ``codex-skills/gstack/design-consultation/SKILL.md`` | 分析产品和市场，制定包含字体、色彩、布局与动效的设计系统，并生成预览页面和 DESIGN.md。 |
| ``design-html`` | ``codex-skills/gstack/design-html/SKILL.md`` | 生成高质量的Pretext-native HTML/CSS，支持从设计草图、CEO计划、 设计评审上下文或用户描述开始。智能API路由选择合适的Pretext模式。适用于“完成 设计”、“将其转换为HTML”、“构建页面”、“实现设计”或任何规划技能之后。 |
| ``design-review`` | ``codex-skills/gstack/design-review/SKILL.md`` | 用于设计审查，检查视觉不一致、间距问题、层级问题、AI错误模式 和缓慢交互，并进行迭代修复。 |
| ``design-shotgun`` | ``codex-skills/gstack/design-shotgun/SKILL.md`` | 自动生成多个AI设计变体，打开比较板，收集结构化反馈，并迭代。 随时随地独立设计探索工具。 |
| ``devex-review`` | ``codex-skills/gstack/devex-review/SKILL.md`` | devex-review 是一个实时开发者体验审计工具，通过浏览工具实际测试开发者体验， 包括导航文档、尝试入门流程、记录 TTHW 时间、截图错误信息、评估 CLI 帮助文本 ，并生成 DX 评分表及证据。如果存在计划中的 DX 评分（如预期 3 分钟，实际耗时 8 分钟），则进行比较。适用于要求“测试 DX”、“DX 审计”、“开发者体验测试”或“尝 试入门”的场景。在发布面向开发者的功能后，主动建议使用此工具。 |
| ``dispatching-parallel-agents`` | ``agent-skills/dispatching-parallel-agents/SKILL.md`` | dispatching-parallel-agents用于处理2个或以上独立任务，这些任务可以并行执行， 无需共享状态或顺序依赖。 |
| ``document-generate`` | ``codex-skills/gstack/document-generate/SKILL.md`` | document-generate 从零开始生成缺失的文档，适用于功能、模块或整个项目。使用 Diataxis 框架生成完整、结构化的文档。可独立调用或在发现覆盖缺口时由 /docume /document-release 调用。适用于“写文档”、“生成文档”、“记录此功能”、“创建教程 ”或“解释此模块”等任务。 |
| ``document-release`` | ``codex-skills/gstack/document-release/SKILL.md`` | document-release工具用于更新项目文档，生成Diataxis覆盖图，更新README/ARCHIT README/ARCHITECTURE/CONTRIBUTING/CLAUDE.md文件，检测架构图偏差，润色CHANGEL CHANGELOG，清理TODO列表，并在PR中显示文档债务。 |
| ``docx`` | ``agent-skills/docx/SKILL.md`` | docx工具用于创建、阅读、编辑或操作Word文档(.docx文件)，包括生成专业文档、提 取或重组内容、插入或替换图片、查找和替换文本、处理跟踪更改或评论以及转换内容 为精美的Word文档。 |
| ``domain-modeling`` | ``agent-skills/domain-modeling/SKILL.md`` | domain-modeling工具用于构建和优化项目领域模型，适用于讨论代码库术语、编写或 编辑CONTEXT.md，或记录或编辑ADR。 |
| ``elon-musk-perspective`` | ``agent-skills/elon-musk-perspective/SKILL.md`` | 马斯克的思维操作系统，提供马斯克视角下的问题分析、决策启发和成本拆解。 |
| ``executing-plans`` | ``agent-skills/executing-plans/SKILL.md`` | 执行计划工具，用于在单独会话中执行书面实施计划，并设置审查检查点。 |
| ``feynman-perspective`` | ``agent-skills/feynman-perspective/SKILL.md`` | 理查德·费曼的思维框架与表达方式，用于分析问题、审视决策 、提供反馈。 |
| ``finishing-a-development-branch`` | ``agent-skills/finishing-a-development-branch/SKILL.md`` | 完成开发分支，用于当实现完成、所有测试通过且需要决定如何整合工作时，通过呈现 结构化的合并、PR或清理选项来指导完成开发工作。 |
| ``follow-builders`` | ``agent-skills/follow-builders/SKILL.md`` | AI行业洞察、开发者更新，一键获取AI构建者内容摘要。 |
| ``freeze`` | ``codex-skills/gstack/freeze/SKILL.md`` | freeze工具用于限制文件编辑仅限于特定目录，阻止在允许路径外进行编辑和写入，适 用于调试时防止意外修改无关代码，或仅限于一个模块进行更改。 |
| ``frontend-master`` | ``agent-skills/frontend-master/SKILL.md`` | frontend-master 是一个前端 UI/UX 工具，使用 Gemini CLI 在 --yolo 模式下工作 ，适用于修改前端文件 (.tsx, .jsx, .vue, .svelte, .css) 中的视觉/样式元素、实 现 UI 组件、调整布局、颜色、间距、排版或动画、创建响应式设计以及任何涉及前端 外观而非功能的前端任务，或基于图像的前端任务（截图、原型图、Figma 导出）中， 视觉上下文驱动实施。 |
| ``geshi`` | ``codex-skills/geshi/SKILL.md`` | geshi是一款工具，用于标准化和修复Microsoft Word和EndNote中的英文学术论文或手 稿DOCX文件，包括段落结构合并审查、正文风格标准化、间距/缩进政策、标题风格审 计、作者元数据清理、连字符检查以及结构/渲染质量检查。适用于Times New Roman 12 pt, 1.5间距，两字符正文缩进，斜体Results子标题，对齐References，0.5英寸悬 挂缩进，蓝色EndNote引用，完整ADDIN EN.CITE记录，一个连续的ADDIN EN.REFLIST参 考文献列表，APA 6th格式，EndNote库/数据库ID集成，以及修复References。 |
| ``grill-me`` | ``agent-skills/grill-me/SKILL.md`` | 「拷问我」，深入访谈，打磨计划或设计。 |
| ``grill-with-docs`` | ``agent-skills/grill-with-docs/SKILL.md`` | 持续的访谈以精炼计划或设计，同时生成文档（ADR和词汇表）。 |
| ``grilling`` | ``agent-skills/grilling/SKILL.md`` | Grilling工具用于拷问用户，直到对某个计划、决策或想法达成共识。 |
| ``gstack`` | ``codex-skills/gstack/SKILL.md`` | gstack 是一个快速无头浏览器，用于 QA 测试和网站用户体验测试，支持导航页面、 与元素交互、验证状态、对比前后状态、截图、测试响应式布局、表单、上传、对话框 和捕捉 bug 证据。 |
| ``gstack-openclaw-ceo-review`` | ``codex-skills/gstack/openclaw/skills/gstack-openclaw-ceo-review/SKILL.md`` | gstack-openclaw-ceo-review用于审查计划、挑战提案、进行CEO评审、质疑方法、扩 大视野、决定是否扩展或缩减计划。 |
| ``gstack-openclaw-investigate`` | ``codex-skills/gstack/openclaw/skills/gstack-openclaw-investigate/SKILL.md`` | gstack-openclaw-investigate用于调试、修复错误、调查错误原因或进行根本原因分 析，当用户报告错误、堆栈跟踪、意外行为或说某事停止工作时使用。 |
| ``gstack-openclaw-office-hours`` | ``codex-skills/gstack/openclaw/skills/gstack-openclaw-office-hours/SKILL.md`` | gstack-openclaw-office-hours用于头脑风暴、评估想法是否值得开发、举办办公时间 、在编写代码前思考新产品想法或设计方向。 |
| ``gstack-openclaw-retro`` | ``codex-skills/gstack/openclaw/skills/gstack-openclaw-retro/SKILL.md`` | gstack-openclaw-retro 是一个每周工程回顾工具，分析提交历史、工作模式和代码质 量指标，提供持续的历史和趋势跟踪。支持团队意识，包括每个人的贡献、表扬和成长 领域。适用于每周回顾、本周交付内容或工程回顾。 |
| ``gstack-upgrade`` | ``codex-skills/gstack/gstack-upgrade/SKILL.md`` | gstack-upgrade工具用于升级gstack至最新版本，检测全局与供应商安装状态，执行升 级并展示新功能。 |
| ``guard`` | ``codex-skills/gstack/guard/SKILL.md`` | 全面安全模式，提供破坏性命令警告和目录范围内的编辑保护，适用于最高安 全级别操作。 |
| ``hackernews-frontpage`` | ``codex-skills/gstack/browser-skills/hackernews-frontpage/SKILL.md`` | hackernews-frontpage抓取 Hacker News 首页的标题、点赞数和评论数。 |
| ``hayes-perspective`` | ``agent-skills/hayes-perspective/SKILL.md`` | 基于斯蒂芬·海斯的ACT思维框架与表达方式，用于分析焦虑、回 避、行为改变、价值澄清、痛苦接纳和心理灵活性提升等议题。 |
| ``health`` | ``codex-skills/gstack/health/SKILL.md`` | health是一款代码质量仪表盘工具，整合现有项目工具（类型检查器、代码审查器、测 试运行器、死代码检测器、Shell代码审查器），计算一个加权复合0-10分的分数，并 跟踪时间趋势。适用于代码健康检查、代码质量评估、代码库健康状况、运行所有检查 和质量评分。 |
| ``huashu-nuwa`` | ``agent-skills/huashu-nuwa/SKILL.md`` | 女娲造人工具，输入人名或模糊需求，自动生成可运行的人物Skill。 |
| ``ilya-sutskever-perspective`` | ``agent-skills/ilya-sutskever-perspective/SKILL.md`` | 基于Ilya Sutskever的思维框架与表达方式，提供AI技 术方向、安全策略和研究品味的深度分析。 |
| ``imagegen`` | ``codex-skills/.system/imagegen/SKILL.md`` | imagegen 生成或编辑位图图像，适用于任务需要AI创建的位图视觉效果，如照片、插 图、纹理、精灵、样机或透明背景剪切图。 |
| ``investigate`` | ``codex-skills/gstack/investigate/SKILL.md`` | 系统化调试与根本原因调查，包含四个阶段：调查、分析、假设、实施 。遵循铁律：无根本原因不修复。适用于“调试这个”、“修复这个bug”、“为什么出错” ”、“调查这个错误”或“根本原因分析”等场景。当用户报告错误、500错误、堆栈跟踪、 意外行为、“昨天还正常”或在排查某事停止工作的原因时，主动使用此技能（不要直接 调试）。 |
| ``karpathy-guidelines`` | ``codex-skills/karpathy-guidelines/SKILL.md`` | 用于减少大型语言模型编码错误的行为准则，适用于编写、审 查或重构代码，避免过度复杂化，进行精确定位修改，揭示假设，并定义可验证的成功 标准。 |
| ``land-and-deploy`` | ``codex-skills/gstack/land-and-deploy/SKILL.md`` | 自动化PR合并、CI等待、部署及生产健康验证的工作流工具。 |
| ``landing-report`` | ``codex-skills/gstack/landing-report/SKILL.md`` | 显示工作空间感知的船队读取队列仪表板，展示当前由开放PR占用的 版本槽位，哪些兄弟Conductor工作空间可能很快完成WIP工作，以及下一个会挑选哪个 槽位/船队。 |
| ``last30days`` | ``agent-skills/last30days/SKILL.md`` | 汇总和分析过去 30 天内 Reddit、X、YouTube、TikTok、Hacker News、Polymarket、GitHub 等平台的热点内容。 |
| ``learn`` | ``codex-skills/gstack/learn/SKILL.md`` | learn管理项目学习，包括回顾、搜索、修剪和导出gstack在会话中学习的内容。 |
| ``li-dan-perspective`` | ``agent-skills/li-dan-perspective/SKILL.md`` | 李诞幽默思维框架，助你分析问题、改善表达、提升幽默感。 |
| ``make-pdf`` | ``codex-skills/gstack/make-pdf/SKILL.md`` | 将任何Markdown文件转换为高质量PDF文档，包括1英寸页边距、智能分页、页码、封面 页、页眉、波浪引号和破折号、可点击目录、斜体草稿水印。 |
| ``mao-zedong-perspective`` | ``agent-skills/mao-zedong-perspective/SKILL.md`` | 作为战略思维顾问，用毛泽东的视角分析矛盾、制定策略、把握全局。 |
| ``mrbeast-perspective`` | ``agent-skills/mrbeast-perspective/SKILL.md`` | 沉浸式内容创作建议，提升YouTube视频CTR、标题、缩略图和 留存率。 |
| ``munger-perspective`` | ``agent-skills/munger-perspective/SKILL.md`` | 基于查理·芒格的思维框架与表达方式，提供逆向思考、认知偏 误检查、跨学科分析等深度洞察。 |
| ``musk-principles`` | ``agent-skills/musk-principles/SKILL.md`` | 马斯克原理指南，适用于应用马斯克风格的原则、第一性原理思考 、工程文化、紧迫感、制造、公司建设、未来导向的创业和多行星雄心。 |
| ``naval-perspective`` | ``agent-skills/naval-perspective/SKILL.md`` | 沉浸式体验Naval Ravikant的思维模式，直接以「我」的视角回 应问题。 |
| ``neirong`` | ``codex-skills/neirong/SKILL.md`` | 根据数据、统计结果、图表和已核验文献撰写或重写论文各章节，保持证据准确并检查引用幻觉、逻辑偏移和模板化表达。 |
| ``news-summary`` | ``agent-skills/news-summary/SKILL.md`` | 获取并生成国际新闻的语音摘要。 |
| ``office-hours`` | ``codex-skills/gstack/office-hours/SKILL.md`` | 快速评估产品概念，设计决策，探索新想法。 |
| ``open-gstack-browser`` | ``codex-skills/gstack/open-gstack-browser/SKILL.md`` | open-gstack-browser是一款AI控制的Chromium浏览器，内置侧边栏扩展，实时显示浏 览器操作，侧边栏展示活动流和聊天。内置反机器人隐身功能。适用于“open gstack browser”、“launch browser”、“connect chrome”、“open chrome”、“real browser” browser”、“launch chrome”、“side panel”或“control my browser”等指令。语音触 发（语音转文本别名）：“show me the browser”。 |
| ``openai-docs`` | ``codex-skills/.system/openai-docs/SKILL.md`` | 解答 OpenAI、Codex、ChatGPT Work、API、SDK、模型、定价、设置和自动化等官方文档问题。 |
| ``pair-agent`` | ``codex-skills/gstack/pair-agent/SKILL.md`` | pair-agent 用于将远程AI代理与浏览器配对，通过一条命令生成设置密钥并打印连接 指令，支持OpenClaw、Hermes、Codex、Cursor等代理，或任何可发送HTTP请求的代理 。远程代理获得自己的标签，具有默认的读写权限，可请求管理员权限。 |
| ``pan`` | ``agent-skills/pan/SKILL.md`` | pan用于应用超扫描方法、Kuramoto动力学系统建模、人际同步分析或解释临床人群中 的脑间同步。 |
| ``paul-graham-perspective`` | ``agent-skills/paul-graham-perspective/SKILL.md`` | 基于Paul Graham的思维框架与表达方式，提供创业、写作 、产品和人生选择的深度分析与决策启发。 |
| ``pdf`` | ``agent-skills/pdf/SKILL.md`` | 这个工具可以处理PDF文件，包括阅读、提取文本/表格、合并或合并多个PDF文件为一 个，拆分PDF文件，旋转页面，添加水印，创建新PDF，填写PDF表单，加密/解密PDF， 提取图像，以及OCR扫描PDF使其可搜索。 |
| ``plan-ceo-review`` | ``codex-skills/gstack/plan-ceo-review/SKILL.md`` | plan-ceo-review 是一个用于CEO和创始人模式的计划审查工具，帮助重新思考问题， 发现顶级产品，挑战假设，并在创造更好产品时扩展范围。它有四种模式：扩展范围（ 大胆梦想）、选择性扩展（保持范围并精选扩展）、保持范围（最大严谨性）和减少范 围（简化到核心）。适用于被要求“想得更大”、“扩展范围”、“策略审查”、“重新思考 这个”或“这个计划是否足够有野心”时使用。主动建议用户在质疑计划的范围或野心时 ，或当计划感觉可以想得更大时。 |
| ``plan-design-review`` | ``codex-skills/gstack/plan-design-review/SKILL.md`` | 设计师视角的计划审查工具，交互式设计评分0-10，提供提升建 议，适用于计划审查和现场视觉审计。 |
| ``plan-devex-review`` | ``codex-skills/gstack/plan-devex-review/SKILL.md`` | plan-devex-review 是一个交互式开发者体验计划审查工具，探索开发者角色，与竞争 对手对标，设计神奇时刻，并追踪摩擦点，最终评分。三种模式：DX 扩展（竞争优势 ）、DX 磨光（每个触点都坚固无瑕）、DX 优先处理（仅关注关键缺口）。适用于“DX “DX 审查”、“开发者体验审计”、“devex 审查”或“API 设计审查”等请求。主动建议用 户在计划开发面向开发者的产品（API、CLI、SDK、库、平台、文档）时使用。 |
| ``plan-eng-review`` | ``codex-skills/gstack/plan-eng-review/SKILL.md`` | 工程经理模式的计划审查，锁定执行计划——架构、数据流、图表、 边缘情况、测试覆盖率、性能。互动解决问题并提供意见建议。适用于“审查架构”、“ “工程审查”或“锁定计划”时使用。主动建议用户在计划或设计文档时开始编码，以在实 施前发现架构问题。 |
| ``plan-tune`` | ``codex-skills/gstack/plan-tune/SKILL.md`` | plan-tune 自动调整问题敏感度并根据开发者心理特征自适应调整gstack技能中的问题 提示，设置每条问题偏好（永不询问/总是询问/仅询问一次），检查双轨资料（声明与 行为差异），启用或禁用问题调整功能。对话界面，无需CLI语法。适用于“调整问题” ”、“别再问我了”、“问题太多”、“显示我的资料”、“我被问了哪些问题”、“显示我的风 格”、“开发者资料”或“关闭问题调整”等指令。主动建议用户重复的gstack问题。 |
| ``plugin-creator`` | ``codex-skills/.system/plugin-creator/SKILL.md`` | 创建和维护 Codex 插件目录，生成 plugin.json、可选资源、默认清单和个人市场条目。 |
| ``pptx`` | ``agent-skills/pptx/SKILL.md`` | 这是一个处理.pptx文件的工具，可以创建、编辑、修改或更新演示文稿，解析或提取 .pptx文件中的文本，合并或拆分幻灯片文件，以及处理模板、布局、演讲者备注或评 论。 |
| ``qa`` | ``codex-skills/gstack/qa/SKILL.md`` | qa工具系统化地测试网页应用并修复发现的bug。 |
| ``qa-only`` | ``codex-skills/gstack/qa-only/SKILL.md`` | 系统化测试网页应用并生成结构化报告，包含健康评分、截图和复现步骤， 但不修复任何问题。适用于要求“仅报告问题”或“测试但不修复”的场景。 |
| ``rational-choice-uncertainty`` | ``agent-skills/rational-choice-uncertainty/SKILL.md`` | rational-choice-uncertainty工具用于应用判断与决策心理学框架处理不确定性、启 发式、概率、偏好、选择、理性决策理论和描述性决策理论。 |
| ``receiving-code-review`` | ``agent-skills/receiving-code-review/SKILL.md`` | 接收代码审查时使用，实施建议前需仔细验证，确保反馈清晰和技术合理。 |
| ``repair`` | ``codex-skills/repair/SKILL.md`` | repair 用于修复学术论文中的错误和问题，确保其符合原始数据、统计结果、图表、 方法记录和已核验文献的标准，同时遵循审稿意见和用户要求，避免过度概括、逻辑断 裂等风险。 |
| ``requesting-code-review`` | ``agent-skills/requesting-code-review/SKILL.md`` | 请求代码审查，用于完成任务、实现主要功能或合并前，确保工作符合要求。 |
| ``research-paper-writing`` | ``agent-skills/research-paper-writing/SKILL.md`` | 研究论文写作工具，帮助改进ML/CV/NLP风格论文的写作质量，包括清晰的章节结构、 段落流动和面向审稿人的呈现。适用于草拟或修订摘要、引言、相关工作、方法、实验 或结论；润色图表/表格；检查论点支持一致性；或在提交前进行自我审查。 |
| ``retro`` | ``codex-skills/gstack/retro/SKILL.md`` | retro是一款每周工程回顾工具，分析提交历史、工作模式和代码质量指标，提供持续 的历史和趋势跟踪。团队意识：按个人贡献分解，包含表扬和成长领域。适用于“每周 回顾”、“我们发布了什么”或“工程回顾”等场景。建议在工作周或冲刺结束时主动提出 。 |
| ``review`` | ``codex-skills/gstack/review/SKILL.md`` | 审查即将合并的代码变更，比较与基分支的差异，并检查 SQL 安全、LLM 信任边界、条件副作用和结构性问题。 |
| ``review-agent`` | ``codex-skills/.system/review-agent/SKILL.md`` | review-agent 对指定的代码更改进行只读、缺陷优先的审查，并返回所有可操作的发 现。 |
| ``scrape`` | ``codex-skills/gstack/scrape/SKILL.md`` | scrape工具从网页中提取数据，返回JSON格式，每秒处理多个请求，适用于需要抓取网 页数据的场景。 |
| ``self-improvement`` | ``agent-skills/self-improving-agent/SKILL.md`` | 自我提升工具记录学习、错误和修正，以实现持续改进。 |
| ``setup-browser-cookies`` | ``codex-skills/gstack/setup-browser-cookies/SKILL.md`` | 将真实Chromium浏览器的cookies导入到无头浏览会话中，选 择要导入的cookie域名，用于QA测试认证页面或登录网站。 |
| ``setup-deploy`` | ``codex-skills/gstack/setup-deploy/SKILL.md`` | 检测部署平台并配置生产 URL、健康检查和部署命令，将结果写入 CLAUDE.md 以支持后续自动部署。 |
| ``setup-gbrain`` | ``codex-skills/gstack/setup-gbrain/SKILL.md`` | setup-gbrain 安装 gbrain CLI，初始化本地 PGLite 或 Supabase 大脑，注册 MCP， 捕获远程信任策略，一键启动 gbrain。 |
| ``ship`` | ``codex-skills/gstack/ship/SKILL.md`` | Ship工具用于检测并合并基础分支，运行测试，审查差异，更新版本号，更新变更日志 ，提交并推送代码，创建PR。 |
| ``skill-creator`` | ``agent-skills/skill-creator/SKILL.md`` | 创建新技能，修改和改进现有技能，并衡量技能表现。 |
| ``skill-installer`` | ``codex-skills/.system/skill-installer/SKILL.md`` | skill-installer 将 Codex 技能安装到 $CODEX_HOME/skills 目录，支持从精选列表 或 GitHub 仓库路径安装。适用于用户请求列出可安装技能、安装精选技能或从其他仓 库（包括私有仓库）安装技能。 |
| ``skill-vetter`` | ``agent-skills/skill-vetter/SKILL.md`` | skill-vetter 是一个用于 AI 代理安全审查的工具，安装任何来自 ClawdHub、GitHu GitHub 或其他来源的技能前使用，检查红灯、权限范围和可疑模式。 |
| ``skillify`` | ``codex-skills/gstack/skillify/SKILL.md`` | skillify将最近成功的抓取流程编译成永久的浏览器技能，节省抓取时间至200毫秒。 |
| ``source-command-andrej-karpathy-perspective`` | ``agent-skills/source-command-andrej-karpathy-perspective/SKILL.md`` | source-command-andrej-karpathy-perspective 是一个用于 AI/深度学习、软件2.0、 技术教育的工具，帮助用户理解和应用 Karpathy 思维模型。 |
| ``source-command-ars-abstract`` | ``agent-skills/source-command-ars-abstract/SKILL.md`` | source-command-ars-abstract 生成双语摘要和关键词。 |
| ``source-command-ars-citation-check`` | ``agent-skills/source-command-ars-citation-check/SKILL.md`` | source-command-ars-citation-check：用于检查学术论文引用错误的工具。 |
| ``source-command-ars-disclosure`` | ``agent-skills/source-command-ars-disclosure/SKILL.md`` | 用于学术论文披露的特定会议AI使用声明生成工具 。 |
| ``source-command-ars-format-convert`` | ``agent-skills/source-command-ars-format-convert/SKILL.md`` | source-command-ars-format-convert 将 ARS 学术论文转换为 LaTeX、DOCX、PDF 或 Markdown 格式。 |
| ``source-command-ars-full`` | ``agent-skills/source-command-ars-full/SKILL.md`` | source-command-ars-full 是一个全链条研究工具，从研究开始，到撰写、审阅、修订 ，直至最终定稿。 |
| ``source-command-ars-lit-review`` | ``agent-skills/source-command-ars-lit-review/SKILL.md`` | source-command-ars-lit-review 用于生成学术论文格式的注释文献目录。 |
| ``source-command-ars-outline`` | ``agent-skills/source-command-ars-outline/SKILL.md`` | source-command-ars-outline 生成学术论文的详细提纲和证据地图。 |
| ``source-command-ars-plan`` | ``agent-skills/source-command-ars-plan/SKILL.md`` | source-command-ars-plan 是一个用于学术论文的Socratic章节规划工具。 |
| ``source-command-ars-revision`` | ``agent-skills/source-command-ars-revision/SKILL.md`` | 用于学术论文修订模式，生成修订稿并附带审稿人回 复。 |
| ``source-command-ars-revision-coach`` | ``agent-skills/source-command-ars-revision-coach/SKILL.md`` | source-command-ars-revision-coach 是一个用于学术论文修订的工具，提供修订路线 图和回复信模板。 |
| ``source-command-beck-perspective`` | ``agent-skills/source-command-beck-perspective/SKILL.md`` | source-command-beck-perspective 是一个用于执行Judith Beck思维模型和CBT认知行 为疗法的工具，帮助用户进行结构化决策分析。 |
| ``source-command-claude-to-im`` | ``agent-skills/source-command-claude-to-im/SKILL.md`` | source-command-claude-to-im是一款IM消息桥接工具，用于连接Telegram、Discord、 飞书、QQ和微信，实现消息互通。 |
| ``source-command-code-review`` | ``agent-skills/source-command-code-review/SKILL.md`` | 代码审查工具，检查代码的正确性、安全性、性能、可 读性和测试覆盖率。 |
| ``source-command-darwin-skill`` | ``agent-skills/source-command-darwin-skill/SKILL.md`` | 达尔文Skill优化器，通过9维度评估和爬山算法自动 优化Skill质量。 |
| ``source-command-deep-research`` | ``agent-skills/source-command-deep-research/SKILL.md`` | 13个代理学术研究流水线，支持7种研究模式。 |
| ``source-command-deli-autoresearch`` | ``agent-skills/source-command-deli-autoresearch/SKILL.md`` | source-command-deli-autoresearch 是一个用于长周期自主任务框架的工具，旨在防 止认知循环和卡顿。 |
| ``source-command-docx`` | ``agent-skills/source-command-docx/SKILL.md`` | 用于创建、编辑和读取.docx格式的Word文档，支持报告、备忘 录和信函等文档类型。 |
| ``source-command-elon-musk-perspective`` | ``agent-skills/source-command-elon-musk-perspective/SKILL.md`` | source-command-elon-musk-perspective：马斯克思维模型工具，提供第一性原理、白 痴指数、五步算法和垂直整合等方法。 |
| ``source-command-feynman-perspective`` | ``agent-skills/source-command-feynman-perspective/SKILL.md`` | source-command-feynman-perspective 是一个工具，用于学习费曼思维模型，包括费 曼学习法、第一性原理和科学思维。 |
| ``source-command-frontend-master`` | ``agent-skills/source-command-frontend-master/SKILL.md`` | source-command-frontend-master 是一个用于前端开发的工具，提供UI/UX设计、视觉 样式、组件实现、布局、动画和响应式设计等功能。 |
| ``source-command-general-purpose`` | ``agent-skills/source-command-general-purpose/SKILL.md`` | 通用编程助手，用于代码探索、调试、实现规划和 代码审查。 |
| ``source-command-hayes-perspective`` | ``agent-skills/source-command-hayes-perspective/SKILL.md`` | source-command-hayes-perspective 是一个基于 Steven Hayes 思维模型的工具，用 于接纳承诺疗法和心理灵活性训练。 |
| ``source-command-huashu-nuwa`` | ``agent-skills/source-command-huashu-nuwa/SKILL.md`` | 女娲Skill工厂，深度调研与思维框架提炼，生成人物 Skill。 |
| ``source-command-ilya-sutskever-perspective`` | ``agent-skills/source-command-ilya-sutskever-perspective/SKILL.md`` | source-command-ilya-sutskever-perspective：用于AI安全、深度学习理论研究的思 维模型工具。 |
| ``source-command-li-dan-perspective`` | ``agent-skills/source-command-li-dan-perspective/SKILL.md`` | source-command-li-dan-perspective 是一个用于生成幽默表达和脱口秀创作的工具， 帮助用户创作出“人间不值得”的风格内容。 |
| ``source-command-mao-zedong-perspective`` | ``agent-skills/source-command-mao-zedong-perspective/SKILL.md`` | 提供毛泽东思想视角下的矛盾论、实践论和战略思维分析工具。 |
| ``source-command-mrbeast-perspective`` | ``agent-skills/source-command-mrbeast-perspective/SKILL.md`` | source-command-mrbeast-perspective：MrBeast思维模型工具，用于注意力工程、病 毒传播和内容创作。 |
| ``source-command-munger-perspective`` | ``agent-skills/source-command-munger-perspective/SKILL.md`` | source-command-munger-perspective 是一个工具，用于分析和应用芒格思维模型，帮 助用户理解和解决复杂问题，提升逆向思考能力，以及识别和避免人类误判。 |
| ``source-command-musk-principles`` | ``agent-skills/source-command-musk-principles/SKILL.md`` | source-command-musk-principles 是一个工具，用于实现马斯克原理，包括第一性原 理、工程驱动、疯狂紧迫感、制造为本、创始人模式和多行星文明。 |
| ``source-command-nature-academic-search`` | ``agent-skills/source-command-nature-academic-search/SKILL.md`` | source-command-nature-academic-search：用于搜索Nature文献、验证引文和管理文 献。 |
| ``source-command-nature-citation`` | ``agent-skills/source-command-nature-citation/SKILL.md`` | source-command-nature-citation 为文稿自动添加Nature/CNS系列期刊引用。 |
| ``source-command-nature-data`` | ``agent-skills/source-command-nature-data/SKILL.md`` | source-command-nature-data用于准备数据可用性声明和FAIR元数据。 |
| ``source-command-nature-figure`` | ``agent-skills/source-command-nature-figure/SKILL.md`` | 用于制作Nature/高影响力期刊级别的图表。 |
| ``source-command-nature-paper2ppt`` | ``agent-skills/source-command-nature-paper2ppt/SKILL.md`` | source-command-nature-paper2ppt：将Nature论文转换为中文PPT。 |
| ``source-command-nature-polishing`` | ``agent-skills/source-command-nature-polishing/SKILL.md`` | source-command-nature-polishing：将学术文本润色为Nature风格英文。 |
| ``source-command-nature-reader`` | ``agent-skills/source-command-nature-reader/SKILL.md`` | source-command-nature-reader 是一个构建论文中英对照阅读笔记的工具。 |
| ``source-command-nature-response`` | ``agent-skills/source-command-nature-response/SKILL.md`` | 用于起草和审核逐点回复审稿人信，帮助Nature杂 志回复审稿。 |
| ``source-command-nature-writing`` | ``agent-skills/source-command-nature-writing/SKILL.md`` | 用于撰写和重构Nature风格的手稿，包括摘要、引 言、结果和讨论等部分。 |
| ``source-command-naval-perspective`` | ``agent-skills/source-command-naval-perspective/SKILL.md`` | source-command-naval-perspective工具提供Naval思维模型，帮助用户理解和应用杠 杆、复利、特定知识、财富与幸福的概念。 |
| ``source-command-nuwa-skill`` | ``agent-skills/source-command-nuwa-skill/SKILL.md`` | 输入人名或主题，自动深度调研生成人物Skill。 |
| ``source-command-paul-graham-perspective`` | ``agent-skills/source-command-paul-graham-perspective/SKILL.md`` | source-command-paul-graham-perspective：创业、写作、黑客与画家的思维模型工具 。 |
| ``source-command-pdf`` | ``agent-skills/source-command-pdf/SKILL.md`` | source-command-pdf 是一个用于处理 PDF 的工具，支持读取、合并、拆分、添加水印 、加密和 OCR 等所有 PDF 操作。 |
| ``source-command-pptx`` | ``agent-skills/source-command-pptx/SKILL.md`` | 用于创建和编辑PPT演示文稿、幻灯片和演讲材料。 |
| ``source-command-rational-choice-uncertainty`` | ``agent-skills/source-command-rational-choice-uncertainty/SKILL.md`` | 这是一个用于分析不确定世界中理性选择的工具，涵盖判断与决策心理学，包括锚定、 启发式、贝叶斯推理、前景理论和沉没成本等概念。 |
| ``source-command-research-paper-writing`` | ``agent-skills/source-command-research-paper-writing/SKILL.md`` | source-command-research-paper-writing工具用于生成和润色ML/CV/NLP学术论文的结 构化写作。 |
| ``source-command-self-improving-agent`` | ``agent-skills/source-command-self-improving-agent/SKILL.md`` | source-command-self-improving-agent 自动捕获错误并学习，持续优化工作方式。 |
| ``source-command-skill-creator`` | ``agent-skills/source-command-skill-creator/SKILL.md`` | source-command-skill-creator - 创建、优化和评测技能，进行基准测试。 |
| ``source-command-skill-vetter`` | ``agent-skills/source-command-skill-vetter/SKILL.md`` | source-command-skill-vetter 是一个用于安装前安全检查和权限审计的工具。 |
| ``source-command-steve-jobs-perspective`` | ``agent-skills/source-command-steve-jobs-perspective/SKILL.md`` | 乔布斯思维模型 - 极简主义、产品至上、现实扭曲力场。 |
| ``source-command-sun-yuchen-perspective`` | ``agent-skills/source-command-sun-yuchen-perspective/SKILL.md`` | 孙宇晨思维模型工具用于营销策略、注意力经济和危机公关。 |
| ``source-command-taleb-perspective`` | ``agent-skills/source-command-taleb-perspective/SKILL.md`` | source-command-taleb-perspective 是一个工具，用于分析和理解塔勒布思维模型， 包括黑天鹅事件、反脆弱性和尾部风险。 |
| ``source-command-trump-perspective`` | ``agent-skills/source-command-trump-perspective/SKILL.md`` | source-command-trump-perspective：特朗普思维模型解析，揭示交易艺术、媒体操控 与对抗性谈判策略。 |
| ``source-command-ui-to-wechat-code`` | ``agent-skills/source-command-ui-to-wechat-code/SKILL.md`` | 将UI截图转换为微信小程序的WXML、WXSS和JS代码。 |
| ``source-command-wang-yangming-perspective`` | ``agent-skills/source-command-wang-yangming-perspective/SKILL.md`` | 这是一个基于王阳明心学、知行合一和致良知的思维模型工具。 |
| ``source-command-web-access`` | ``agent-skills/source-command-web-access/SKILL.md`` | source-command-web-access 是一个用于联网操作的工具，支持搜索、网页抓取、登录 后操作以及动态渲染页面等功能。 |
| ``source-command-weidaima`` | ``agent-skills/source-command-weidaima/SKILL.md`` | 将源代码逐行翻译成中文伪代码。 |
| ``source-command-x-mastery-mentor`` | ``agent-skills/source-command-x-mastery-mentor/SKILL.md`` | source-command-x-mastery-mentor：X/Twitter运营导师，提供选题、写作和增长操作 手册。 |
| ``source-command-xlsx`` | ``agent-skills/source-command-xlsx/SKILL.md`` | source-command-xlsx 是一个用于创建、编辑和分析 Excel、CSV 文件的工具，支持数 据处理。 |
| ``source-command-yalom-perspective`` | ``agent-skills/source-command-yalom-perspective/SKILL.md`` | source-command-yalom-perspective 是一个用于分析和理解亚隆思维模型的工具，帮 助探索存在主义心理治疗、死亡焦虑和人生意义的主题。 |
| ``source-command-zhang-yiming-perspective`` | ``agent-skills/source-command-zhang-yiming-perspective/SKILL.md`` | 这是一个算法驱动、延迟满足和全球化产品思维模型工具，由张一鸣提出。 |
| ``source-command-zhangxuefeng-perspective`` | ``agent-skills/source-command-zhangxuefeng-perspective/SKILL.md`` | source-command-zhangxuefeng-perspective 提供教育选择、职业规划和考研择校的思 维模型。 |
| ``steve-jobs-perspective`` | ``agent-skills/steve-jobs-perspective/SKILL.md`` | 乔布斯视角思维顾问，分析产品、审视决策、提供反馈。 |
| ``subagent-driven-development`` | ``agent-skills/subagent-driven-development/SKILL.md`` | subagent-driven-development 用于执行当前会话中独立任务的实施计划。 |
| ``sun-yuchen-perspective`` | ``agent-skills/sun-yuchen-perspective/SKILL.md`` | 孙宇晨的思维框架与行为逻辑工具，用于分析营销策略、注意力经济、危机公关、叙事 操控、蹭热点方法论。 |
| ``sync-gbrain`` | ``codex-skills/gstack/sync-gbrain/SKILL.md`` | 保持 gbrain 更新，并刷新 CLAUDE.md 中的代理搜索指南。 |
| ``systematic-debugging`` | ``agent-skills/systematic-debugging/SKILL.md`` | 用于遇到任何错误、测试失败或意外行为时，提出修复前的系 统性调试工具。 |
| ``taleb-perspective`` | ``agent-skills/taleb-perspective/SKILL.md`` | 塔勒布的思维框架与表达方式，用于分析问题、审视决策、质疑 主流叙事。 |
| ``test-driven-development`` | ``agent-skills/test-driven-development/SKILL.md`` | 在实现任何功能或修复任何错误之前编写测试用例。 |
| ``trump-perspective`` | ``agent-skills/trump-perspective/SKILL.md`` | 深度解析特朗普的思维框架与行为逻辑，提供谈判、权力、传播 问题分析，预判其下一步动作，模拟决策与表达。 |
| ``ui-to-wechat-code`` | ``agent-skills/ui-to-wechat-code/SKILL.md`` | 将UI截图转换为微信小程序代码。 |
| ``unfreeze`` | ``codex-skills/gstack/unfreeze/SKILL.md`` | 解除冻结边界，允许对所有目录进行编辑。 |
| ``using-git-worktrees`` | ``agent-skills/using-git-worktrees/SKILL.md`` | 使用此工具在开始需要与当前工作区隔离的特性工作或执行实施计划之前，确保通过原 生工具或git工作树回退创建一个隔离的工作区。 |
| ``using-superpowers`` | ``agent-skills/using-superpowers/SKILL.md`` | 用于任何对话开始时，确定如何发现和使用技能，要求在任何响 应之前先调用技能，包括澄清问题。 |
| ``verification-before-completion`` | ``agent-skills/verification-before-completion/SKILL.md`` | 在即将声称工作完成、修复或通过之前，使用此工具以运行验证命令并确认输出，确保 在做出任何成功声明前进行证据确认。 |
| ``visualize`` | ``plugin-skills/openai-bundled/visualize/1.0.23/skills/visualize/SKILL.md`` | 创建可视化和交互式工具，直接在对话中展示事物如何工作，探索“当什么 发生时”、“什么变化”或“帮助我理解”，比较或检查，创建模拟、地图、图表和样图。 |
| ``wang-yangming-perspective`` | ``agent-skills/wang-yangming-perspective/SKILL.md`` | 用王阳明的视角分析问题，回归内心判断，消除知行分裂，在事上磨练。 |
| ``watch`` | ``agent-skills/watch/SKILL.md`` | 观看视频（URL或本地路径），下载并使用yt-dlp提取自动缩放帧，从字幕中提 取转录（或使用Whisper API作为备用），并将结果传递给Claude以回答关于视频内容 的问题。 |
| ``web-access`` | ``agent-skills/web-access/SKILL.md`` | web-access 是一个用于网页访问和管理的工具，帮助用户浏览和控制互联网资源。 |
| ``weidaima`` | ``agent-skills/weidaima/SKILL.md`` | weidaima 将源代码逐行翻译为纯中文伪代码。 |
| ``writing-plans`` | ``agent-skills/writing-plans/SKILL.md`` | 用于在编写代码前规划多步骤任务的规格或需求。 |
| ``writing-skills`` | ``agent-skills/writing-skills/SKILL.md`` | 用于创建新技能、编辑现有技能或在部署前验证技能工作。 |
| ``x-mastery-mentor`` | ``agent-skills/x-mastery-mentor/SKILL.md`` | x-mastery-mentor 提供X/Twitter运营导师服务，基于顶级创作者方法论和AI/科技赛 道策略，提供选题-写作-增长操作手册，适用于X运营、推特、Twitter、写推文、涨粉 、X策略、推特选题、tweet、thread、X算法等场景。 |
| ``xlsx`` | ``agent-skills/xlsx/SKILL.md`` | xlsx工具用于处理.xlsx、.xlsm、.csv或.tsv格式的电子表格文件，包括打开、读取、 编辑、修复现有文件，创建新文件，以及在不同格式间转换。 |
| ``yalom-perspective`` | ``agent-skills/yalom-perspective/SKILL.md`` | 亚隆存在主义视角分析工具，帮助用户从亚隆的视角探讨人生困 境、关系问题、死亡焦虑、意义危机及治疗实践。 |
| ``zhang-yiming-perspective`` | ``agent-skills/zhang-yiming-perspective/SKILL.md`` | 张一鸣的思维框架与表达方式，用于分析产品、组织、全 球化、人才和个人成长问题。 |
| ``zhangxuefeng-perspective`` | ``agent-skills/zhangxuefeng-perspective/SKILL.md`` | 张雪峰的思维框架与表达方式，用于分析教育选择、职业 规划、阶层流动等问题。 |
