# 1个文件，让AI从废话助手变成项目专家

你让 AI 帮你写 PRD，它回你"建议根据业务需求进行个性化推荐"。

废话。

问题不是 AI 不行，是它根本不知道你的项目是啥。

---

解法特别简单：在项目根目录放一个 CLAUDE.md 文件，把项目背景写进去。

就写三件事：
1/ 这个产品是干什么的，给谁用的
2/ 团队多少人，什么技术栈
3/ 文档放在哪，哪几个最重要

总共 50 行，10 分钟写完。

---

效果对比：

之前问"写推荐算法PRD"
→ "可采用协同过滤或深度学习"（你就 1 个算法，深度学习做梦呢）

放了 CLAUDE.md 后同样的问题
→ "基于内容标签+协同过滤，冷启动用宠物档案粗排，考虑到 DAU 12 万建议按城市分桶做 AB"

一个文件的区别。

---

模板和完整示例我放 GitHub 了，直接 copy 改改就能用：
github.com/hy459229090-lang/ai-pm-workflow

系列第 01 篇，不懂 CLAUDE.md 的可以翻完整教程。

---

#AI工作流 #产品经理 #CLAUDE教程 #AI办公 #效率工具 #Cursor #AI编程 #上下文工程

---

## 封面图

**提示词（中文）**：

> 信息卡片对比风格封面图，深灰色背景，画面分为左右两栏。左栏标题"没有 CLAUDE.md"，下方红色区域显示一段模糊的通用文字，打上红色叉号。右栏标题"有 CLAUDE.md"，下方绿色区域显示一段清晰的结构化文字，打上绿色对勾。底部大字"1个文件的区别"。整体风格简洁信息图，科技感。尺寸 3:4 竖版。

**英文提示词**：

> Info-card comparison cover, dark gray background, split into left and right columns. Left column titled "Without CLAUDE.md" with a red zone showing blurred generic text and a red X mark. Right column titled "With CLAUDE.md" with a green zone showing clear structured text and a green checkmark. Bottom large text "One file makes the difference". Clean infographic style, tech aesthetic. Aspect ratio 3:4 vertical.
