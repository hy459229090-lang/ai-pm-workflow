
# 让 AI 当你的数据分析师 — 数据取数自动化实践

> 本文是我用 AI 解决数据问题一年多的实践沉淀。不是教程，是一个真实工作流从 0 到 1 的演化过程。

---

*本文是我用 AI 解决数据问题一年多的实践沉淀。不是教程，是一个真实工作流从 0 到 1 的演化过程。*

**文章约 5000 字，阅读时间 12 分钟。建议先收藏，用到的时候再翻出来看。**

---

## 01 为什么是数据取数？

过去这一年多，我一直在尝试用 AI 解决数据问题。

试过各种方案——从最早的"帮我看下这个表有什么数据"，到后来让 AI 直接生成 SQL、跑分析、出报表。

大部分尝试都失败了——要么 AI 理解不了业务口径，要么生成的东西没法直接用。

但有一个 Skill，我坚持用了一年多，而且用得越来越多：**数据取数自动化。**

一开始我只是想"省点事"——不用每次都跟 AI 描述表结构、字段含义、过滤条件。

但用了一年多后，我发现它带来的价值远超预期：

<div style="background:#f8f9fa;border-left:4px solid #07c160;padding:16px 20px;margin:20px 0;border-radius:0 4px 4px 0;">
<strong>验证数据</strong>：上线前看转化漏斗、功能渗透率、留存曲线
</div>

<div style="background:#f8f9fa;border-left:4px solid #07c160;padding:16px 20px;margin:20px 0;border-radius:0 4px 4px 0;">
<strong>收集数据</strong>：周报月报要的核心指标、老板突然问的"那个数据"
</div>

<div style="background:#f8f9fa;border-left:4px solid #07c160;padding:16px 20px;margin:20px 0;border-radius:0 4px 4px 0;">
<strong>产品分析</strong>：用户行为路径、功能使用情况、异常波动定位
</div>

<div style="background:#f8f9fa;border-left:4px solid #07c160;padding:16px 20px;margin:20px 0;border-radius:0 4px 4px 0;">
<strong>快速汇报</strong>：临时被叫去开会，5 分钟拉出关键数据
</div>

它不再是一个"取数工具"，而是一个 **全职数据分析师**。

说个真实的场景：

上周五下午 4 点，老板突然在群里问："最近新功能的渗透率怎么样？"

要是以前，我得：
1. 打开数据平台
2. 找对应的表
3. 写 SQL（还得回忆字段名）
4. 跑出来数据
5. 复制到 Excel 做图

一套下来最少 20 分钟，还得小心翼翼怕写错。

这次我直接在对话框输入：

`/data 新功能渗透率，按天看最近 7 天`

30 秒后，数据 + 趋势图已经发出来了。

老板回了一个"👍"。

这就是为什么我说它是一个**全职数据分析师**——随叫随到，还不会出错。

---

## 02 核心架构：数据知识库 + SQL 规则引擎

我的 `/data` Skill 不是简单的"SQL 生成器"。

它是一套完整的数据知识体系 + 分析能力：

<div style="background:#f6f8fa;border:1px solid #e1e4e8;border-radius:8px;padding:20px;margin:20px 0;">
<p style="margin:0 0 16px 0;font-weight:600;color:#1a1a1a;">用户问："过去 7 天的 DAU 怎么样？"</p>
<p style="margin:0 0 16px 0;font-weight:600;color:#666;">AI 内部执行：</p>
<p style="margin:8px 0;color:#555;"><span style="display:inline-block;width:24px;height:24px;background:#07c160;color:#fff;border-radius:50%;text-align:center;line-height:24px;font-size:12px;margin-right:8px;">1</span>识别指标：DAU = 日活跃用户数</p>
<p style="margin:8px 0;color:#555;"><span style="display:inline-block;width:24px;height:24px;background:#07c160;color:#fff;border-radius:50%;text-align:center;line-height:24px;font-size:12px;margin-right:8px;">2</span>查数据字典：用户行为日志在 t_event_log，user_id 标识用户</p>
<p style="margin:8px 0;color:#555;"><span style="display:inline-block;width:24px;height:24px;background:#07c160;color:#fff;border-radius:50%;text-align:center;line-height:24px;font-size:12px;margin-right:8px;">3</span>应用业务规则：排除测试账号、只算正式环境</p>
<p style="margin:8px 0;color:#555;"><span style="display:inline-block;width:24px;height:24px;background:#07c160;color:#fff;border-radius:50%;text-align:center;line-height:24px;font-size:12px;margin-right:8px;">4</span>生成 SQL → 执行 → 格式化输出</p>
<p style="margin:8px 0;color:#555;"><span style="display:inline-block;width:24px;height:24px;background:#07c160;color:#fff;border-radius:50%;text-align:center;line-height:24px;font-size:12px;margin-right:8px;">5</span>可选：生成趋势图、对比上周、计算环比</p>
</div>

**关键不是 AI 会写 SQL——是它理解你的业务数据。**

这个架构的核心是两个东西：

1. **数据字典**——让 AI 知道你的数据是什么
2. **SQL 规则**——让 AI 知道怎么写符合业务口径的 SQL

下面我分别讲。

---

## 03 数据字典：AI 分析师的大脑

### 我的数据字典长这样

**核心业务表 - t_user（用户表）**

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:14px;background:#fff;">
<thead>
<tr style="background:#f6f8fa;">
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">字段</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">含义</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">user_id</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">用户 ID</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">从 1000 开始，&lt;1000 是测试数据</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">username</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">用户名</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">-</td>
</tr>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">created_at</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">注册时间</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">-</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">last_login_time</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">最后登录时间</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">判断活跃用这个</td>
</tr>
</tbody>
</table>

**核心业务表 - t_event_log（行为日志表）**

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:14px;background:#fff;">
<thead>
<tr style="background:#f6f8fa;">
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">字段</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">含义</th>
<th style="border:1px solid #e1e4e8;padding:12px 10px;text-align:left;font-weight:600;">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">event_id</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">事件 ID</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">-</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">user_id</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">用户 ID</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">关联 t_user</td>
</tr>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">event_type</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">事件类型</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">login/purchase/share 等预定义枚举</td>
</tr>
<tr style="background:#fafbfc;">
<td style="border:1px solid #e1e4e8;padding:12px 10px;">event_time</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">事件时间</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">-</td>
</tr>
<tr>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">properties</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">事件属性</td>
<td style="border:1px solid #e1e4e8;padding:12px 10px;">JSON 格式</td>
</tr>
</tbody>
</table>

### 数据字典怎么来？

**不是手动写的——是 AI 自己分析的。**

我的做法：

<div style="display:flex;align-items:flex-start;margin:16px 0;">
<span style="display:inline-block;width:28px;height:28px;background:#07c160;color:#fff;border-radius:50%;text-align:center;line-height:28px;font-size:14px;margin-right:12px;flex-shrink:0;">1</span>
<div>让 AI 连接数据库，DESCRIBE 每张表</div>
</div>

<div style="display:flex;align-items:flex-start;margin:16px 0;">
<span style="display:inline-block;width:28px;height:28px;background:#07c160;color:#fff;border-radius:50%;text-align:center;line-height:28px;font-size:14px;margin-right:12px;flex-shrink:0;">2</span>
<div>采样前 100 行数据，让 AI 推断字段含义</div>
</div>

<div style="display:flex;align-items:flex-start;margin:16px 0;">
<span style="display:inline-block;width:28px;height:28px;background:#07c160;color:#fff;border-radius:50%;text-align:center;line-height:28px;font-size:14px;margin-right:12px;flex-shrink:0;">3</span>
<div>AI 生成初步字典，我 review 一遍</div>
</div>

<div style="display:flex;align-items:flex-start;margin:16px 0;">
<span style="display:inline-block;width:28px;height:28px;background:#07c160;color:#fff;border-radius:50%;text-align:center;line-height:28px;font-size:14px;margin-right:12px;flex-shrink:0;">4</span>
<div>业务口径补充（比如"user_id < 1000 是测试数据"这种规则）</div>
</div>

### 为什么这个方式有效？

传统做法是找 DBA 或数据团队写文档——但问题是：

- 文档更新跟不上表结构变化
- 业务含义只有建表的人懂
- 新人入职看文档像看天书

用 AI 分析的方式：

- **实时更新**：表结构变了，AI 重新分析就行
- **业务语义分离**：AI 负责推断字段类型和关系，人负责补充业务口径
- **新人友好**：可以问"这个字段什么意思"，AI 用自然语言解释

这里说一个踩坑经历：

最开始我自己写数据字典，花了一整天，写得密密麻麻。

结果两周后表结构变了，字典废了。

后来我想明白了——**这种重复劳动就该让 AI 干**。

我现在每加一张新表，就让 AI 自己分析生成字典，我只负责 review 和补充业务口径。

效率高多了。

---

## 04 SQL 规则：业务口径的沉淀

光有数据字典不够——**AI 写的 SQL 要符合业务口径。**

### 我的规则示例

**默认过滤规则**

- 排除测试数据：user_id >= 1000
- 只算正式环境：env = 'prod'
- 时间范围：默认近 7 天，除非用户指定

**指标定义**

- DAU：当天有登录行为的去重用户数（用 last_login_time 判断）
- 新增用户：created_at 在当天范围内的用户
- 留存：次日/7 日/30 日，用登录行为判断而非注册

**输出格式**

- Markdown 表格
- 按时间倒序
- 超过 100 行时只展示汇总

### 规则怎么来？

**跟 AI 对话对话出来的。**

最开始我没有规则，AI 生成的 SQL 经常不符合预期：

- 包含了测试数据 → 加规则 `user_id >= 1000`
- 时间范围不对 → 加规则"默认近 7 天"
- 输出太乱 → 加格式规范

每次发现问题，我就跟 AI 说"这样不对，应该是 XXX"，然后让它更新规则。

迭代了大概十几轮，现在稳定下来的规则覆盖了 90% 的场景。

说一个具体的例子：

有一次我要看留存，AI 生成的 SQL 是用 created_at 判断的。

我说不对，留存应该用登录行为判断，不是用注册时间。

AI 就记住了，现在它知道：
- 新增用户 = 看 created_at
- 活跃用户 = 看 last_login_time
- 留存 = 看登录行为

这种业务逻辑，不跟 AI 说，它永远不会懂。

---

## 05 当 AI 口径和业务口径不一致时

这是最大的坑。

### 问题

业务世界里有很多"中间表"——不是原始日志，是经过加工聚合的。

比如：
- 一张"每日活跃用户表"，已经聚合好了 DAU/MAU
- 一张"用户画像表"，打标了各种用户属性

这些表的口径是业务定义的，AI 直接看原始数据推导不出来。

### 解法：先解释逻辑，再执行

我现在的工作流：

<div style="background:#f6f8fa;border:1px solid #e1e4e8;border-radius:8px;padding:20px;margin:20px 0;">
<p style="margin:0 0 16px 0;font-weight:600;color:#1a1a1a;">复杂指标查询工作流</p>
<p style="margin:8px 0;color:#555;"><span style="display:inline-block;width:24px;height:24px;background:#07c160;color:#fff;border-radius:50%;text-align:center;line-height:24px;font-size:12px;margin-right:8px;">1</span>用户问一个复杂指标（比如"高价值用户留存率"）</p>
<p style="margin:8px 0;color:#555;"><span style="display:inline-block;width:24px;height:24px;background:#07c160;color:#fff;border-radius:50%;text-align:center;line-height:24px;font-size:12px;margin-right:8px;">2</span>AI 先输出它对指标的理解："我理解高价值用户是 XXX，留存率算法是 XXX，对吗？"</p>
<p style="margin:8px 0;color:#555;"><span style="display:inline-block;width:24px;height:24px;background:#07c160;color:#fff;border-radius:50%;text-align:center;line-height:24px;font-size:12px;margin-right:8px;">3</span>我确认/纠正</p>
<p style="margin:8px 0;color:#555;"><span style="display:inline-block;width:24px;height:24px;background:#07c160;color:#fff;border-radius:50%;text-align:center;line-height:24px;font-size:12px;margin-right:8px;">4</span>AI 生成 SQL 执行</p>
</div>

**多这一步，能避免 99% 的逻辑错误。**

而且这个对话过程本身也是知识沉淀——AI 记住这次校准，下次就懂了。

### 一个真实案例

有一次我问"复购率是多少"，AI 直接生成了 SQL。

结果跑出来的数据和我已知的对不上。

后来发现：我理解的"复购"是"同一用户下单≥2 次"，AI 理解的是"首次购买后再次购买的用户占比"。

两个定义都对，但算出来的数字差了一倍。

从那以后，我加了一条规则：**所有业务指标，第一次使用时必须先对齐定义。**

---

## 06 搞不定的场景

虽然我用了这么久，但 `/data` 不是万能的。

### 中间表没有权限

AI 只能访问它有权访问的表。如果核心数据在数仓、AI 只能连业务库，那就跨不过去。

**变通**：我手动导出中间表，丢给 AI 分析。

### 自己都不了解表的时候

有时候业务表是别人建的、文档缺失、连字段名都是拼音缩写。

这时候 AI 也懵——它只能基于已有信息推断。

**变通**：先让 AI 采样数据、推断含义，再找建表的人确认。这个过程本身也是在帮你理解数据。

### 极度复杂的连表

超过 5 张表 JOIN、嵌套多层子查询、各种 CASE WHEN——这种 SQL AI 能写，但执行效率可能不如手写优化的。

**变通**：让 AI 写基础版本，我手动优化。

---

## 07 人人都是数据科学家？

这是我写这篇最想讨论的。

### 我的观察

"人人都是数据科学家"这个口号喊了很多年，但一直没实现。

原因是 **工具门槛一直存在**——SQL 要学、数据模型要懂、可视化工具要熟练。

但 AI 把这个门槛抹平了。

现在的情况是：
- 你不用会写 SQL——用自然语言描述，AI 生成
- 你不用懂数据模型——数据字典 AI 维护
- 你不用学可视化——AI 直接输出图表

**唯一需要的能力是：知道要问什么问题。**

### 但这里有争议

有人会说："AI 生成的 SQL 你敢直接用吗？""口径不一致怎么办？""数据准确性谁负责？"

我的回答：

1. **不敢直接用→让 AI 先解释逻辑**（上面讲了）
2. **口径不一致→对话校准，AI 记住**（这也是知识沉淀）
3. **准确性→最终责任还是人**（AI 是工具，决策和验证还是你）

**"人人都是数据科学家"不是说不需要专家了——是说工具足够好用，让非专家也能做 80 分的数据分析。**

剩下的 20 分（复杂建模、数据治理、口径统一）还是需要专家，但日常分析需求 80% 都能自己搞定。

---

## 08 落地建议

如果你也想试试这个方案：

### 第一步：从一张表开始

不要一开始就想搞全量数据字典。

选你最常用的一张表（比如用户表、订单表），让 AI 分析结构、采样数据、生成初步字典。

### 第二步：定义 3-5 个核心指标

从你最常问的问题开始：
- DAU/MAU
- 新增用户
- 转化率
- 留存率

每个指标跟 AI 对齐定义，让它记住。

### 第三步：迭代规则

用几次后你会发现 AI 写的 SQL 有哪些问题。

每次发现问题，就加一条规则。迭代十几轮后，覆盖 90% 场景。

### 第四步：扩展数据源

一张表跑顺了，再慢慢加表。

优先加那些你经常 JOIN 的表（比如用户表→订单表→支付表）。

---

## 09 总结

这一年多的实践，我最大的收获不是"AI 能写 SQL"，而是：

**AI 可以成为你的数据知识库。**

它理解表结构、记得业务口径、知道哪些是测试数据、哪些指标怎么算。

你不需要记住所有表结构、所有字段含义、所有 SQL 语法。

你只需要知道 **要问什么问题**。

---

## 10 讨论

我很好奇你在用什么方式做数据分析？

- 还是手动写 SQL 吗？
- 有试过让 AI 生成吗？效果怎么样？
- 你觉得"人人都是数据科学家"是机会还是坑？

欢迎在评论区聊聊。

---

*上一篇：第 03 篇：把重复工作变成一句话 — Skill 与原子化能力*

*下一篇：第 05 篇：Agent Team — 当一个人搞不定的时候*

*作者：RicHe | 产品经理，专注 AI 产品设计*
