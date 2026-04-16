# 我让 AI 写 PRD 没 review，结果翻车了

> 三道检查点，AI 产出不失控

*本文是我用 AI 协作 1 年多，在"怎么 review AI 产出"这件事上的实战经验。不是教程，是踩坑后的复盘。*

**文章约 4500 字，阅读时间 9 分钟。建议先收藏，用 AI 写文档前翻出来看。**

---

## 一个差点翻车的故事

那次我让 AI 写了一份 PRD，然后直接丢给研发了。

没有 review。

原因很简单：之前的 PRD AI 都写得不错，我觉得"这次应该也没问题"。

结果呢？

研发做了一半来找我："这个权限逻辑有问题——管理员能删数据，普通用户也能？"

我打开 PRD 一看，AI 确实写了"用户可以对数据进行管理操作"——但它没区分角色。管理员和普通用户的权限边界完全是模糊的。

**问题不在 AI——在我没有设置检查点。**

从那天起，我建立了一套 Review 机制。

---

## 我以前的 Review 方式：要么全看，要么不看

最开始和 AI 协作，我在两个极端之间摇摆：

**极端 A：全看**

AI 写的每个字我都要过一遍。10 页的 PRD，我一字不改但读两小时。

累，而且效率极低。

**极端 B：不看**

"AI 写得挺好，直接用"。

直到上面那个翻车事件。

这两个都有问题：

- 全看 = AI 没帮我省时间，只是帮我省了打字
- 不看 = 垃圾直接流入下游，返工成本更高

**正确的方式是：只看关键节点，而且知道看什么。**

---

## 三道检查点

现在我有一套固定的检查点系统。

### 第 1 道：入口检查（AI 开始工作前）

这不是检查 AI 的产出，是检查**我给的信息够不够**。

<div style="background:#f6f8fa;border:1px solid #e1e4e8;border-radius:8px;padding:20px;margin:20px 0;">

**入口检查四项**：

1. **目标明确了吗？** — 要解决什么问题，一句话能说清
2. **背景给了吗？** — 用户场景、技术约束、历史决策
3. **格式指定了吗？** — 要表格/文档/代码，说清楚了
4. **边界定义了吗？** — 什么不在范围内，标注了

</div>

**这一步的目的**：避免 AI 跑偏。90% 的返工，问题出在这里。

实际案例：

**❌ 我给 AI 的指令**："写个用户增长方案"

**✅ 我给 AI 的指令**：

```
写一份用户增长方案，背景：
- 产品上线 3 个月，日活 5000
- 目标是 Q2 到 2 万
- 预算 10 万，主要是拉新，不含品牌投放
- 当前 70% 用户来自自然流量，渠道单一
- 参考竞品 A 的邀请裂变和竞品 B 的 KOC 投放

要求：
- 表格形式：策略/动作/时间/预算/预期效果/负责人
- 至少 3 个可执行的策略
- 每个策略有具体的 ROI 预估
```

同一个任务，两种指令。产出质量天差地别。

---

### 第 2 道：结构检查（AI 出初稿后）

**不看细节，只看骨架。**

快速扫一遍，检查三件事：

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:14px;background:#fff;">
<thead>
<tr style="background:#f6f8fa;">
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">检查项</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">说明</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">耗时</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">有没有遗漏核心场景？</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">边界 case、异常流程、角色区分</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">3 分钟</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">逻辑通不通？</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">前后矛盾、数据对不上</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">2 分钟</td>
</tr>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">格式对不对？</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">表格/标题/层级是否符合要求</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">1 分钟</td>
</tr>
</tbody>
</table>

**关键**：这一步不超过 5 分钟。

不是逐字读，是像看 PPT 一样快速扫。如果骨架有问题，直接打回——细节再好也没用。

**实际案例**：

AI 写的埋点方案，我扫了一眼就发现问题：

- 登录、注册、分享都有埋点
- 但"支付成功"这个核心事件漏了

骨架就不完整。打回。5 分钟发现一个会导致全链路数据缺失的问题。

---

### 第 3 道：细节抽查（结构通过后）

结构没问题了，才开始看细节。

但也不是全看——是**抽查**。

我的做法：

<div style="background:#f6f8fa;border:1px solid #e1e4e8;border-radius:8px;padding:20px;margin:20px 0;">

**抽查策略**：

1. **随机抽样 3-5 个关键点** — 比如 PRD 里随机挑 3 个功能点，看交互细节
2. **检查高风险区域** — 权限、金额、数据安全相关的逻辑
3. **对照真实场景走一遍** — "如果我是用户，从打开 App 到完成支付，流程对吗？"

</div>

这一步花 10-15 分钟，覆盖 80% 的风险。

---

## 不同类型产出的 Review 清单

### PRD 的检查清单

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:14px;background:#fff;">
<thead>
<tr style="background:#f6f8fa;">
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">必查项</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">常见遗漏</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">角色权限区分</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">管理员/普通用户/游客的边界</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">异常流程</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">断网、超时、失败重试</td>
</tr>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">数据边界</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">空数据、超长文本、极限值</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">前后端一致性</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">前端展示和后端逻辑对得上</td>
</tr>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">验收标准</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">每个需求有可验证的通过条件</td>
</tr>
</tbody>
</table>

### 埋点方案的检查清单

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:14px;background:#fff;">
<thead>
<tr style="background:#f6f8fa;">
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">必查项</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">常见遗漏</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">核心漏斗覆盖</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">注册/登录/下单/支付全链路</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">事件命名规范</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">统一前缀、动词+名词</td>
</tr>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">属性完整性</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">通用属性 + 事件特有属性</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">去重逻辑</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">同一动作多次触发怎么处理</td>
</tr>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">数据验证方式</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">怎么确认埋点生效</td>
</tr>
</tbody>
</table>

---

## 自动化 Review：让 AI 自己先审一遍

这是一个后来才想到的优化。

在人工 review 之前，我先让 AI 自己审一遍。

**具体做法**：

```
你是一个有 10 年经验的产品总监。
请审查这份 PRD，重点关注：
1. 有没有遗漏的异常场景？
2. 有没有逻辑矛盾？
3. 有哪些地方研发一定会来问你？

输出格式：问题编号 / 问题描述 / 严重程度 / 修改建议
```

AI 的自审能发现 60-70% 的问题。

剩下 30-40% 是 AI 发现不了的——因为它不知道你的业务细节、历史坑、团队习惯。

**所以自审不是替代人工，是让人工只看 AI 发现不了的问题。**

---

## 打回的规则

Review 不是只有"通过/不通过"两个选项。

我的打回分级：

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:14px;background:#fff;">
<thead>
<tr style="background:#f6f8fa;">
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">级别</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">条件</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">处理</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">小修</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">格式/措辞/个别遗漏</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">指出具体问题，AI 修改后直接通过</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">中修</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">结构缺陷/逻辑不通</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">打回重写，给出修改方向</td>
</tr>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">大修</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">方向性错误/完全跑偏</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">回到入口检查，重新对齐目标</td>
</tr>
</tbody>
</table>

**重要**：大修不是 AI 的错，通常是我入口检查没做好。

大修的时候我会先反思：是不是我给的信息不够？目标没说清？约束没讲？

---

## 我的 Review 时间分配

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:14px;background:#fff;">
<thead>
<tr style="background:#f6f8fa;">
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">阶段</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">时间占比</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">入口检查</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">20%</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">给 AI 的指令和信息</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">AI 自审</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">0%</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">AI 执行，我不看</td>
</tr>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">结构检查</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">10%</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">快速扫骨架</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">细节抽查</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">30%</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">抽查关键区域</td>
</tr>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">反馈沟通</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">40%</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">给 AI 修改意见、讨论疑问</td>
</tr>
</tbody>
</table>

**对比以前**：以前我 100% 的时间花在"读 AI 写的所有内容"上。现在我只花 40% 在细节上，40% 在反馈沟通上。

**效果**：总时间少了，质量反而高了。因为精力集中在真正能提升质量的地方。

---

## 核心洞察

这套机制的核心不是"怎么检查 AI 的产出"，而是：

**怎么让自己从"全量阅读者"变成"关键决策者"。**

AI 能写，但不能判断。
AI 能改，但不知道改得对不对。
AI 能审，但不知道你的业务细节。

**判断、裁决、业务理解——这是你必须守住的三件事。**

其他都可以交给 AI。

---

## 互动时间

来，说说你用 AI 踩过的坑：

- 你现在怎么 review AI 的产出？全看/抽查/不看？
- 有没有因为没 review 翻过车？什么场景？
- 你觉得"让 AI 自己先审一遍"靠谱吗？

评论区聊聊。

---

*上一篇：第 06 篇：AI 产出评估*

*下一篇：第 08 篇：待定*

*作者：RicHe | 产品经理，专注 AI 产品设计*
