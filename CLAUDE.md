# AI-PM-Workflow 项目规则

> 所有 AI 在本项目中工作时必须遵守以下规则。

## 目录职责

```
ai-pm-workflow/
├── content/              # 文章内容的唯一来源
│   ├── _index.md         #   系列文档总览
│   ├── README.md         #   多平台发布指南
│   ├── CONTENT_STANDARD.md # 内容生产标准
│   ├── sources/          #   源稿（GitHub 完整版，所有平台版本的源头）
│   └── platforms/        #   各平台适配版
│       ├── wechat/       #     微信公众号
│       ├── xiaohongshu/  #     小红书
│       └── zhihu/        #     知乎
├── assets/               # 图片与静态资源（按用途分类）
│   ├── covers/           #   公众号封面图（每篇一张）
│   ├── carousels/        #   小红书轮播图（按篇章分子目录）
│   └── archive/          #   历史版本/废弃图片（不再使用）
├── tools/                # 脚本与模板
│   ├── generators/       #   图片/HTML 生成脚本（.py / .js）
│   ├── templates/        #   Canvas HTML 模板 + CLAUDE.md 等模板
│   └── examples/         #   示例文件（毛球 App 配置示例）
├── publish/              # 已发布的产物（只读归档，不要直接修改）
│   ├── wechat-html/      #   公众号可复制 HTML
│   └── README-canvas.md  #   Canvas 使用文档
├── case-study/           # 毛球 App 虚构案例设定
├── .claude/commands/     # Claude Code Skill 定义
├── .obsidian/            # Obsidian 配置（忽略）
└── node_modules/         # 依赖（忽略）
```

## 文件放置规则

### 文章相关
- **新文章** → 必须写到 `content/sources/`，按 `XX-主题.md` 命名
- **平台适配版** → 写到 `content/platforms/{wechat,xiaohongshu,zhihu}/`
- **禁止** 在根目录、`publish/` 或其他位置创建新的文章文件

### 图片相关
- **公众号封面** → `assets/covers/`，命名 `{篇号}-cover.{ext}`
- **小红书轮播** → `assets/carousels/{篇号}-{主题}/`，命名 `{序号}-{类型}.png`
- **历史/废弃图** → `assets/archive/`
- **禁止** 在文章同级目录、根目录放置图片

### 脚本/模板
- **生成脚本** → `tools/generators/`
- **HTML Canvas 模板** → `tools/templates/`
- **示例配置** → `tools/examples/`

### 发布产物
- **公众号 HTML** → `publish/wechat-html/`
- `publish/` 是发布后归档，**不是**创作目录，不要在这里新建文章

### 其他
- **临时文件**（测试图、中间产物等）→ 用完后删除，不要留在仓库中
- **配置文件** → 放到对应功能目录下，不要放根目录（根目录只保留 README、LICENSE、package.json、.gitignore）

## 内容创作规则

### 案例贯穿原则
**所有文章必须以「毛球 App」为贯穿案例**，每篇文章的举例、场景、数据都必须基于毛球的具体业务场景。
- ❌ 泛泛举例："比如某个产品"、"假设一个场景"
- ✅ 具体举例："毛球 App 的推荐 feed 改版"、"毛球的社区内容发布率从 3.2% 提到 5%"
- 案例设定详见 `case-study/README.md`（产品概述、用户角色、数据设定、表结构）
- 每篇文章开头必须用一个毛球的真实痛点/决策引入，不能直接讲方法论

## 工作流规则

1. **创作顺序**：先在 `content/sources/` 写源稿 → 再适配到各平台版本
2. **不修改已发布内容**：`publish/` 下的文件是已发布产物，如需更新应先确认
3. **不改 .obsidian/ 下的文件**：这是 Obsidian vault 配置
4. **不碰 node_modules/**
