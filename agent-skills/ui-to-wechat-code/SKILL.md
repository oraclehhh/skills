---
name: ui-to-wechat-code
description: |
  截图转微信小程序代码。输入UI截图（ChatGPT/Figma/任何图片），
  先结构化重建布局（组件树、尺寸、颜色、间距、字体），
  再按微信小程序规范生成高保真WXML+WXSS+JS原生代码。
  内置验证循环：跑起→截图对比→指出差异→AI修→重复。
  触发词：「截图转小程序」「UI图转代码」「设计图生成小程序」「图片转微信小程序」
  「把这张UI做成小程序」「截图生成代码」
  也适合：需要从设计图快速出小程序前端页面的场景。
  不适合：逻辑交互复杂的页面（多角色权限、支付分账）——需要先生成骨架再补充业务逻辑。
type: pipeline
author: 阿虎
---

# UI截图 → 微信小程序代码

> pipeline: screenshot → structured reconstruction → WXML+WXSS+JS → visual verify → iterate

## 核心理念

截图转代码的保真度瓶颈不在「生码」，在**信息损失**。截图是把结构化UI信息压缩成像素矩阵，
模型要从像素猜尺寸、颜色、间距、字体——每一步都在猜。所以这个pipeline不做一次性生码，
而是分成两阶段：

1. **结构化重建（结构优先）**：让模型先读图，输出精确的UI结构化描述
2. **代码生成（规则约束）**：基于结构化描述，按照微信小程序规范生成代码

两阶段之间加一道人工确认，让模型「看到什么」先被你验证，再让它「写什么」。
这个顺序切换是保真度的关键——一次让模型同时做读图和写码，它会在细节上随机丢失。

---

## 执行流程

### Phase 0: 激活

收到触发词后，确认：

1. **输入形式**：一张或多张UI截图？（路径/粘贴/拖入）
2. **页面类型**：单页面？多页面？Tab页面？
3. **输出格式**：原生微信小程序代码？uni-app？Taro？
4. **已有项目**：是新建项目还是追加到现有项目代码中？
5. **需补充业务逻辑吗**：纯UI生成 vs 含交互逻辑

确认后进入Phase 1。

---

### Phase 1: 结构化重建

**目标**：从截图提取精确的UI结构化描述，不生成任何代码。

**输出格式**（要求AI输出以下结构）：

```markdown
## 页面概览
- 页面类型：[首页/列表页/详情页/个人中心/...]
- 整体布局：[上下结构/Tab结构/左中右/...]
- 设计风格：[圆角/直角/材质/拟物...]

## 组件树（自上而下）
1. 导航栏
   - 高度：约[？]rpx
   - 元素：返回按钮(左) / 标题(中) / 分享按钮(右)
   
2. 内容区
   - 上边距：[？]rpx
   - 子组件A：[描述]
   - 子组件B：[描述]

## 关键尺寸
- 页面总宽：750rpx（微信标准）
- 内容区左右边距：[？]rpx
- 卡片圆角：[？]rpx
- 组件间距：[？]rpx

## 色值表
- 主色：#??????
- 背景色：#??????
- 文字主色：#??????
- 文字次要：#??????
- 边框/分割线：#??????
- 按钮/CTA色：#??????

## 字体系统
- 标题字号/字重：[？]rpx / bold
- 正文字号：[？]rpx
- 辅助文字：[？]rpx

## 图标处理
- 图标列表：[描述哪些元素是图标]
- 处理方式：[用Unicode字符/用SVG/用图片]
```

**关键约束**：
- Phase 1 **禁止生成任何代码**——只输出结构化描述
- 所有尺寸用rpx单位（微信标准，设计稿px需要换算：1rpx = 设计稿px / 750 * 750）
- 颜色值精确到hex
- 不确定的值标注为「≈推测值」而非凭空编一个精确值

**人工确认点**：用户读完结构化描述，确认模型「看对了」再进入Phase 2。

---

### Phase 2: 代码生成

**条件**：Phase 1的结构化描述已获用户确认。

**生成规则**（编码到system prompt）：

#### 文件结构（单页面）
```
pages/[page-name]/
  ├── [page-name].wxml    # 模板
  ├── [page-name].wxss    # 样式
  ├── [page-name].js      # 逻辑
  └── [page-name].json    # 配置
```

#### WXML规则
- `<view>` 替代 `<div>`，所有块级元素用view
- `<text>` 替代 `<span>`，行内文字用text
- `<image>` 替代 `<img>`，必须指定mode属性（scaleToFill/aspectFit/aspectFill等）
- `<scroll-view>` 替代带滚动的div
- `<swiper>` / `<swiper-item>` 替代轮播图
- `<icon>` 替代简单图标（微信内置图标用type指定）
- 条件渲染用 `wx:if` / `wx:elif` / `wx:else`，不是v-if/ng-if
- 列表渲染用 `wx:for` + `wx:key`，不是v-for
- 事件绑定用 `bindtap` / `catchtap`，不是onClick

#### WXSS规则
- 所有尺寸用rpx，**不用px、rem、em**
- 使用flexbox布局，不用float
- 颜色变量用小程序不支持CSS custom properties（var()），直接用字面值
- 背景图用background-image + url()，图片放images目录
- 圆角用border-radius，微信支持
- 阴影用box-shadow，微信支持（但注意性能）

#### 字体规范
- 中文字体用：
  ```css
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "PingFang SC", "Microsoft YaHei", sans-serif;
  ```
- 字体大小范围：24rpx（辅助）~ 32rpx（正文）~ 40rpx（标题）

#### 交互状态
- 按钮需要处理：normal / pressed / disabled / loading
- 列表需要处理：loading / empty / error / loaded
- 图片需要处理：加载中占位 / 加载失败兜底
- 下拉刷新：用 `onPullDownRefresh` + `enablePullDownRefresh`

#### JS骨架
- Page({ data: { ... }, onLoad() {}, ... }) 结构
- data中声明所有模板变量及其默认值
- 事件处理函数放在Page参数第二层
- API调用统一用wx.request并暴露配置项

#### 如果是已有项目
- 读取项目中已有的 `app.json` / `app.wxss`，保持页面路由注册和全局样式一致性
- 匹配项目中已使用的组件库（WeUI / TDesign / Vant），优先复用
- 代码风格对齐项目已有文件（缩进、引号、分号规则）

---

### Phase 3: 验证循环

生成完代码后：

1. **先不修**：AI一次性输出全部文件（wxml+wxss+js+json）
2. **用户操作**：把文件放入微信开发者工具，跑起来，截图
3. **对比反馈**：用户把运行截图 + 原始UI截图一起发给AI，逐条指出差异
4. **定点修复**：AI针对差异逐条修正，不翻动已正确部分

**典型差异点**（AI常见凹陷区域）：
- 间距偏差 ±5rpx 以内可接受，超过需要修
- 颜色偏差：截图压缩导致的颜色偏移（特别在渐变区域）
- 字体回退：微信不支持某些字体时的fallback行为
- 圆角不匹配：小程序border-radius在某些机型上的渲染差异
- 图标缺失：截图中的图标需要手动找SVG或替代方案

**迭代终止条件**：用户对比截图确认无明显感官差异。

---

## 微信小程序编码速查表

| HTML | WXML | 说明 |
|------|------|------|
| `<div>` | `<view>` | 块级容器 |
| `<span>` | `<text>` | 行内文字（可选中） |
| `<img>` | `<image>` | 图片（需mode属性） |
| `<input>` | `<input>` | 输入框（类似） |
| `<button>` | `<button>` | 按钮（有微信内置样式） |
| `<ul>/<li>` | `<view wx:for>` | 列表渲染 |
| `<iframe>` | `<web-view>` | 内嵌网页 |
| `<canvas>` | `<canvas>` | 画布 |
| `<video>` | `<video>` | 视频 |
| `onClick` | `bindtap` | 点击事件 |
| `v-if` | `wx:if` | 条件渲染 |
| `v-for` | `wx:for` | 列表渲染 |
| `CSS变量` | **不支持** | 用字面值 |

| CSS | WXSS | 说明 |
|-----|------|------|
| `px` | `rpx` | 响应式单位，设计稿750px宽=750rpx |
| `rem` | **不用** | 小程序不支持 |
| `@media` | **不完全支持** | 用 `wx.getSystemInfo` + js判断 |
| `:hover` | `hover-class` | 点击态用class控制 |

---

## 与社区skill的衔接

这个skill专注于「截图→代码」生成阶段。生成后的测试和CI/CD可以衔接社区的已有skill：

- `npx skills add whinc/wechat-miniprogram-skills` — 安装后使用
  - `miniprogram-automation`：自动化测试（mock wx.request、截图回归）
  - `miniprogram-ci`：CI/CD发布（预览、上传、GitHub Actions）

建议工作流：用本skill生成 → 用miniprogram-automation写测试 → 用miniprogram-ci部署。

---

## 边界与局限

**这个skill不擅长**：
- 复杂交互动画（拖拽排序、手势识别、Canvas绘图）——需要人工介入
- 多页面路由设计和状态管理——只能生成单页面UI骨架
- 后端数据联调和API设计——纯前端UI生成
- 支付、登录、权限等微信原生能力集成——需要补充业务逻辑
- 已有项目的深度重构——适合增量添加页面，不适合大规模修改已有逻辑

**已知局限**：
- 截图中的图标无法自动还原，需要人工提供SVG/字体图标
- 截图质量影响还原度（低分辨率、JPEG压缩痕迹、文字模糊的截图效果差）
- 复杂布局（重叠、绝对定位、Grid）的识别准确率低于flexbox简单布局
