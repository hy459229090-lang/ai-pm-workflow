# 我拉了个 AI 群，它们自己把活干了

> 14 个 AI Agent 协作，我是怎么设计的

---

*本文是我用 Agent Team 工作流实战 3 个月的实践沉淀。不是教程，是一个真实工作流从混乱到秩序的演化过程。*

**文章约 4500 字，阅读时间 10 分钟。建议先收藏，用到的时候再翻出来看。**

---

## 01 为什么需要 Agent Team

第 03 篇讲了 Skill——把重复操作封装成原子化能力。

第 04 篇讲了数据取数——让 AI 成为你的全职数据分析师。

但用了半年 Skill，我发现了一个新问题：

**有些任务，一个 AI 真的搞不定。**

不是它不够聪明，是任务本身就涉及多份产出、多个视角、多轮评审。

举个例子：

我要做一个新功能，需要：

<div style="background:#f8f9fa;border-left:4px solid #07c160;padding:16px 20px;margin:20px 0;border-radius:0 4px 4px 0;">
一份 PRD（产品需求文档）
</div>

<div style="background:#f8f9fa;border-left:4px solid #07c160;padding:16px 20px;margin:20px 0;border-radius:0 4px 4px 0;">
一份技术方案（后端 + 前端）
</div>

<div style="background:#f8f9fa;border-left:4px solid #07c160;padding:16px 20px;margin:20px 0;border-radius:0 4px 4px 0;">
一份埋点方案（数据追踪）
</div>

<div style="background:#f8f9fa;border-left:4px solid #07c160;padding:16px 20px;margin:20px 0;border-radius:0 4px 4px 0;">
一份测试用例（QA 视角）
</div>

这四份文档有依赖关系——技术方案要回应 PRD 里的约束，埋点方案要基于功能定义，测试用例要覆盖所有场景。

更关键的是，**我没法同时关注所有环节的细节**。

PRD 写得好不好、技术方案可行不可行、埋点有没有遗漏——我的精力和注意力覆盖不了。

这时候，一个 Skill 不够用了。我需要拉一个 **Agent Team**。

---

## 02 Agent Team 是什么

最初我理解的 Agent Team 是"多叫几个 AI 一起干活"。

这个理解是错的，或者说太浅了。

**Agent Team 真正的意义是一套协作机制。** 就像你带团队，不是把一群人拉进一个群，然后说"你们自己干"。

你需要：

- 明确分工（谁负责什么）
- 定义输入输出（交付标准是什么）
- 设置检查点（什么时候 review）
- 处理冲突（意见不一致听谁的）

Agent Team 也是一样的逻辑。

---

## 03 我的第一个 Agent Team：14 个 AI 的混乱与秩序

说一个真实的故事。

去年 11 月，我在做一个比较复杂的项目——一个 AI 驱动的产品分析工具。

任务拆解出来有：
- 产品分析（市场分析、竞品分析、用户画像）
- 需求定义（PRD、用户故事、验收标准）
- 技术方案（架构设计、API 定义、数据模型）
- 数据埋点（事件定义、属性规范、看板设计）
- 测试用例（功能测试、边界测试、异常场景）

我一个人肯定干不完——就算每个环节都用 Skill，也得花几周。

于是我拉了一个 Agent Team，最多时有 14 个 AI 同时在线。

### 第一版设计：完全分布式

我把 14 个 AI 拉进一个群（其实是多个对话线程），然后说：

"产品分析组先输出市场分析，然后需求组基于市场分析写 PRD，技术组基于 PRD 设计技术方案..."

结果是一片混乱：
- 产品分析组输出完了，需求组没注意到，还在等
- 技术组写的方案和 PRD 里的约束对不上
- 数据组和测试组发现需求有歧义，但不知道问谁
- 我每隔 5 分钟要切换一次对话，确认进度、解决冲突

**那一天真的累。14 个 AI 给我干活，我比我自己干还累。**

晚上 11 点，我盯着屏幕上乱七八糟的对话，意识到一个问题：

我不是在管团队，我是在当**人肉路由器**——每个信息都要经过我，每个冲突都要我来裁决。

这不可持续。

---

## 04 第二版设计：主从架构 + 评审机制

第二天我重新设计了架构。

### 核心改变

<div style="background:#f6f8fa;border:1px solid #e1e4e8;border-radius:8px;padding:20px;margin:20px 0;">
<p style="margin:0 0 16px 0;font-weight:600;color:#1a1a1a;">1. 设一个队长（Lead Agent）</p>
<p style="margin:8px 0;color:#555;font-size:14px;">负责统筹全局、分发任务、收集产出。我只跟队长对话，不跟组员直接对话。</p>
</div>

<div style="background:#f6f8fa;border:1px solid #e1e4e8;border-radius:8px;padding:20px;margin:20px 0;">
<p style="margin:0 0 16px 0;font-weight:600;color:#1a1a1a;">2. 定义清晰的输入输出</p>
<p style="margin:8px 0;color:#555;font-size:14px;">每个 Agent 只负责一个环节。输入是什么、输出是什么、质量标准是什么。</p>
</div>

<div style="background:#f6f8fa;border:1px solid #e1e4e8;border-radius:8px;padding:20px;margin:20px 0;">
<p style="margin:0 0 16px 0;font-weight:600;color:#1a1a1a;">3. 设置评审点</p>
<p style="margin:8px 0;color:#555;font-size:14px;">关键产出完成后，自动触发评审。评审不通过，打回重做。</p>
</div>

<div style="background:#f6f8fa;border:1px solid #e1e4e8;border-radius:8px;padding:20px;margin:20px 0;">
<p style="margin:0 0 16px 0;font-weight:600;color:#1a1a1a;">4. 冲突解决机制</p>
<p style="margin:8px 0;color:#555;font-size:14px;">技术组和产品组意见不一致？先各自陈述理由，然后由评审组裁决。</p>
</div>

### 效果立竿见影

那天之后，我只需要做三件事：
1. 跟队长说清楚要做什么
2. 等队长通知"初稿完成"
3. Review 关键节点，给出反馈

剩下的交给 Team。

---

## 05 什么时候需要拉 Agent Team

这可能是这篇最有价值的部分。

### 我的判断标准

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:14px;background:#fff;">
<thead>
<tr style="background:#f6f8fa;">
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">任务特征</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">用 Skill</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">拉 Team</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">产出数量</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">1 份</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">多份（≥3）</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">依赖关系</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">无/简单</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">复杂（A 依赖 B）</td>
</tr>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">视角需求</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">单一</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">多个（产品/技术/用户/商业）</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">你的精力</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">能覆盖全部细节</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">覆盖不了，需要分权</td>
</tr>
</tbody>
</table>

### 简单说

- **流程固定、一次出结果** → 用 Skill
- **多份产出、需要交叉审视、你 review 不过来** → 拉 Team
- **一次性的创造性工作** → 直接跟 AI 对话就行

这个边界说实话我也还在摸索。

有时候以为 Skill 够用，做到一半发现得拉 Team。也有觉得需要 Team 的，后来发现一个好的 Skill 就搞定了。

---

## 06 怎么写一个 Agent Team

以毛球 App 的"需求分析"Team 为例。

### 第 1 步：定义任务边界

这个 Team 要做什么：
- 输入：一个产品想法/需求
- 输出：PRD + 技术方案 + 埋点方案 + 测试用例

### 第 2 步：设计角色分工

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:14px;background:#fff;">
<thead>
<tr style="background:#f6f8fa;">
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">角色</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">职责</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">输入</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">输出</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">产品 Agent</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">写 PRD</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">产品想法</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">PRD 文档</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">技术 Agent</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">设计技术方案</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">PRD</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">技术方案</td>
</tr>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">数据 Agent</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">设计埋点方案</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">PRD + 技术方案</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">埋点文档</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">测试 Agent</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">写测试用例</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">PRD + 技术方案</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">测试用例</td>
</tr>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">评审 Agent</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">审查所有产出</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">所有文档</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">评审意见</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">队长 Agent</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">统筹分发</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">你的需求</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">最终交付物</td>
</tr>
</tbody>
</table>

### 第 3 步：定义协作流程

<div style="background:#f6f8fa;border:1px solid #e1e4e8;border-radius:8px;padding:20px;margin:20px 0;font-family:monospace;font-size:13px;line-height:1.8;">
你 → 队长 Agent：需求描述<br>
队长 → 产品 Agent：写 PRD<br>
产品 Agent → 评审 Agent：PRD 评审<br>
评审 Agent → 队长：评审通过/打回<br>
队长 → 技术 Agent + 数据 Agent + 测试 Agent：并行工作<br>
各 Agent → 队长：交付<br>
队长 → 你：最终交付物
</div>

### 第 4 步：定义质量标准

每个环节产出前，定义清楚：
- 必填字段有哪些
- 格式规范是什么
- 自检清单是什么

### 第 5 步：测试和迭代

用几次真实任务测试。你会发现：
- 哪些角色多余（可以合并）
- 哪些环节缺失（需要补充）
- 哪些标准不够细（需要完善）

我的经验是迭代 3-5 轮才稳定。

---

## 07 踩过的坑

### 坑 1：队长太忙，变成瓶颈

第一版设计里，队长要统筹全局、分发任务、收集产出、解决冲突——累死了。

**解法**：
- 队长只负责分发和收集，不负责审查
- 审查交给评审 Agent
- 冲突由评审组裁决，队长执行

### 坑 2：评审流于形式

评审 Agent 最开始只会说"看起来不错"——没有实际价值。

**解法**：
- 定义评审清单（必须检查的 10 个点）
- 评审意见必须包含"通过/打回" + 具体理由
- 打回次数多了，评审 Agent 会学习

### 坑 3：产出风格不一致

产品 Agent 写的 PRD 和技术 Agent 写的方案风格差异太大，阅读体验很差。

**解法**：
- 定义统一的写作风格指南
- 提供模板（但不规定内容）
- 队长最后统一格式

---

## 08 效果对比

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:14px;background:#fff;">
<thead>
<tr style="background:#f6f8fa;">
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">指标</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">我一个人干</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">用 Skill</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">拉 Agent Team</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">时间</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">3-5 天</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">1-2 天</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">2-4 小时</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">我的精力投入</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">100%</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">30%</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">10%</td>
</tr>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">产出质量</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">看状态</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">稳定</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">稳定且全面</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">覆盖视角</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">产品</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">产品 + 数据</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">产品 + 技术 + 数据 + 测试</td>
</tr>
</tbody>
</table>

---

## 09 核心洞察

这一年多折腾下来，我最大的收获：

**Skill 是给 AI 增加能力，Agent Team 是给自己减少负担。**

Skill 让你不用重复说同一句话。
Agent Team 让你不用同时关注所有细节。

但 Agent Team 不是银弹——它解决的是"多份产出、多视角、你 review 不过来"的问题。

如果只是一个简单任务，用 Skill 就够了，拉 Team 反而是浪费。

---

## 10 讨论

- 你在用 Agent Team 吗？是什么场景？
- 你觉得"管理 AI 比 AI 干活还累"吗？
- 你的 Agent Team 架构是什么样的？

欢迎在评论区聊聊。

---

*上一篇：第 04 篇：让 AI 当你的数据分析师*

*下一篇：第 06 篇：待定*

*作者：RicHe | 产品经理，专注 AI 产品设计*
