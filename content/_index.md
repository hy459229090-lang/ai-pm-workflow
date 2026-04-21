---
tags:
  - moc
  - index
---

# AI 产品经理工作流 — 系列文档总览

> 用上下文工程（Context Engineering）让 AI 从"通用助手"变成"你的项目专家"。

---

## 系列概览

| # | 源稿 | 主题 | 一句话 | 微信公众号 | 小红书 | 知乎 | 状态 |
|---|------|------|--------|-----------|--------|------|------|
| 00 | [[content/sources/00-philosophy\|00-philosophy]] | 设计哲学 | 为什么产品经理需要 AI 工作流——不是效率工具，是工作方式的变化 | [[content/platforms/wechat/00-philosophy\|wechat]] | [[content/platforms/xiaohongshu/00-philosophy\|xhs]] | [[content/platforms/zhihu/00-philosophy\|zhihu]] | 已发布 |
| 01 | [[content/sources/01-claude-md\|01-claude-md]] | CLAUDE.md | 用一个文件让 AI 秒懂你的项目背景，从通用助手变项目专家 | [[content/platforms/wechat/01-claude-md\|wechat]] | [[content/platforms/xiaohongshu/01-claude-md\|xhs]] | [[content/platforms/zhihu/01-claude-md\|zhihu]] | 已发布 |
| 02 | [[content/sources/02-workspace-map\|02-workspace-map]] | WORKSPACE_MAP | 让 AI 能自己找到任何文档，不用你每次指路 | [[content/platforms/wechat/02-workspace-map\|wechat]] | [[content/platforms/xiaohongshu/02-workspace-map\|xhs]] | [[content/platforms/zhihu/02-workspace-map\|zhihu]] | 已发布 |
| 03 | [[content/sources/03-skills\|03-skills]] | Skill 原子化 | 把重复工作变成一句话——给 AI 增加可复用的手段 | [[content/platforms/wechat/03-skills\|wechat]] | [[content/platforms/xiaohongshu/03-skills\|xhs]] | [[content/platforms/zhihu/03-skills\|zhihu]] | 已发布 |
| 04 | [[content/sources/04-data-agent\|04-data-agent]] | 数据取数自动化 | 让 AI 成为你的数据分析师，自然语言取数 | [[content/platforms/wechat/04-data-agent-full\|wechat-full]] | [[content/platforms/xiaohongshu/04-data-agent\|xhs]] | [[content/platforms/zhihu/04-data-agent\|zhihu]] | 已发布 |
| 05 | [[content/sources/05-agent-team\|05-agent-team]] | 多 Agent 协作 | 构建 14 个 Agent 协作系统，应对复杂任务 | [[content/platforms/wechat/05-agent-team-full\|wechat-full]] | [[content/platforms/xiaohongshu/05-agent-team\|xhs]] | [[content/platforms/zhihu/05-agent-team\|zhihu]] | 已发布 |
| 06 | [[content/sources/06-evaluate\|06-evaluate]] | AI 产出评估 | 建立评估体系，判断 AI 产出质量 | [[content/platforms/wechat/06-evaluate-full\|wechat-full]] | [[content/platforms/xiaohongshu/06-evaluate\|xhs]] | [[content/platforms/zhihu/06-evaluate\|zhihu]] | 已发布 |
| 07 | [[content/sources/07-review\|07-review]] | Review 机制 | 让 AI 产出不失控——三道人类关卡 | [[content/platforms/wechat/07-review-full\|wechat-full]] | [[content/platforms/xiaohongshu/07-review\|xhs]] | [[content/platforms/zhihu/07-review\|zhihu]] | 已发布 |
| 08 | [[content/sources/08-templates\|08-templates]] | 模板与规范 | 模板不是限制创造力，是让 AI 产出像自己写的 | [[content/platforms/wechat/08-templates-full\|wechat-full]] | [[content/platforms/xiaohongshu/08-templates\|xhs]] | [[content/platforms/zhihu/08-templates\|zhihu]] | 草稿 |

## 内容结构

```
content/
├── _index.md              ← 本文件（总览页 / MOC）
├── README.md              ← 多平台发布指南
├── CONTENT_STANDARD.md    ← 内容生产思考标准
├── WORKSPACE_STANDARD.md  ← 工作区规范（命名、链接、标签）
├── sources/               ← 源文档（GitHub 完整版，所有平台版本的源头）
│   ├── 00-philosophy.md
│   ├── 01-claude-md.md
│   ├── 02-workspace-map.md
│   ├── 03-skills.md
│   ├── 04-data-agent.md
│   ├── 05-agent-team.md
│   ├── 06-evaluate.md
│   ├── 07-review.md
│   └── 08-templates.md
└── platforms/             ← 各平台适配版
    ├── wechat/            ← 微信公众号（部分篇章有 -full 长版）
    ├── xiaohongshu/       ← 小红书
    └── zhihu/             ← 知乎
```

## 内容流转

```
[[content/sources/00-philosophy|源文档]] (GitHub 完整版)
  ├→ [[content/platforms/wechat/00-philosophy|微信公众号]]
  ├→ [[content/platforms/xiaohongshu/00-philosophy|小红书]]
  └→ [[content/platforms/zhihu/00-philosophy|知乎]]
```

## 推荐阅读顺序

**如果你是产品经理**：从 [[content/sources/00-philosophy|第 0 篇]] 开始按顺序读。

**如果你是研发工程师**：先读 [[content/sources/00-philosophy|第 0 篇]] 和 [[content/sources/01-claude-md|第 01 篇]] 理解上下文工程，然后跳到感兴趣的部分。

**如果你只是好奇**：读完 [[content/sources/00-philosophy|第 0 篇]] 就够了。

## 篇章关系图

```
00 设计哲学
  └→ 01 CLAUDE.md（让 AI 秒懂项目）
       └→ 02 WORKSPACE_MAP（让 AI 自己找文档）
            └→ 03 Skills（给 AI 可复用手段）
                 └→ 04 数据取数（自然语言取数）
                      └→ 05 Agent Team（多 Agent 协作）
                           └→ 06 产出评估（判断质量）
                                └→ 07 Review 机制（三道人类关卡）
                                     └→ 08 模板与规范（让产出一致）
```

## 相关资源

- [[content/CONTENT_STANDARD|内容生产思考标准]]
- [[content/WORKSPACE_STANDARD|工作区规范]]
- [[content/README|多平台发布指南]]
- [[tools/generators/|工具脚本]]
- [[case-study/|毛球 App 虚构案例]]
- [[assets/covers/|封面图资源]]
- [[assets/carousels/|小红书轮播图资源]]
