---
tags:
  - index
---

# 工作区标准

> 本文定义 PMbranding 仓库中所有文件的命名、链接、标签规范。
> 适用于 Obsidian 图谱导航、内容生产、跨平台协作。

---

## 一、文件命名规范

### 文章文件

格式：`{两位数字}-{主题简称}.md`

| 篇号 | 主题 | 说明 |
|------|------|------|
| 00 | philosophy | 设计哲学 |
| 01 | claude-md | CLAUDE.md 文件 |
| 02 | workspace-map | 项目地图 |
| 03 | skills | Skill 原子化 |
| 04 | data-agent | 数据取数自动化 |
| 05 | agent-team | 多 Agent 协作 |
| 06 | evaluate | AI 产出评估 |
| 07 | review | Review 机制 |

- 源稿放在 `content/sources/`
- 平台适配版放在 `content/platforms/{wechat,xiaohongshu,zhihu}/`
- 平台版文件名**与源稿相同**（如 `04-data-agent.md`），但 full-length 版本可在文件名后加 `-full`（如 `04-data-agent-full.md`）

### 图片资源

格式：`{篇号}-{类型}.{ext}`

| 类型 | 目录 | 命名 |
|------|------|------|
| 公众号封面 | `assets/covers/` | `{篇号}-cover.{png/jpg}` |
| 小红书轮播 | `assets/carousels/{篇号}-{主题}/` | `{序号}-{类型}.png` |
| 历史/废弃 | `assets/archive/` | 按来源命名 |

### 工具脚本

放在 `tools/generators/`，命名用动词短语，如 `generate-cover.py`。

---

## 二、Obsidian 链接规范

### 基本规则

1. **使用 wikilink 格式**：`[[路径/文件名|显示文本]]`
2. **路径必须包含文件扩展名**：Obsidian 默认不显示扩展名，但为保证脚本可解析，建议在链接中写 `[[content/sources/00-philosophy|00 设计哲学]]`（省略 `.md`，Obsidian 自动识别）
3. **禁止使用相对路径**：所有链接使用相对于仓库根目录的路径

### 标准链接模板

每篇文章底部必须包含以下三个区块：

```markdown
---

## 系列导航

[[content/_index|总览]] · [[00-philosophy|00 设计哲学]] · [[01-claude-md|01 CLAUDE.md]] · ...（所有兄弟篇章，排除自身）

## 上下文链接

**上一篇**：[[XX-主题|第 XX 篇：标题]]   ← 仅源稿需要
**下一篇**：[[XX-主题|第 XX 篇：标题]]   ← 仅源稿需要

**平台版本**：[[content/platforms/wechat/XX-主题|微信公众号]] · [[content/platforms/xiaohongshu/XX-主题|小红书]] · [[content/platforms/zhihu/XX-主题|知乎]]   ← 仅源稿需要
```

### 平台版链接要求

平台适配版**必须**包含回链：

```markdown
---

**源稿**：[[content/sources/XX-主题|XX-主题（GitHub 完整版）]]
**其他平台**：[[content/platforms/wechat/XX-主题|微信公众号]] · ...（排除自身）
```

### 交叉引用

正文中引用其他文章时：
- 引用系列内文章：`[[content/sources/03-skills|第 03 篇：把重复工作变成一句话]]`
- 引用平台版：`[[content/platforms/xiaohongshu/03-skills|小红书版]]`
- 引用工具：`[[tools/generators/generate-cover.py|封面生成脚本]]`
- 引用案例：`[[case-study/maoqiu|毛球 App 案例]]`

---

## 三、标签体系

使用 Obsidian YAML frontmatter 定义标签。

### 文章文件标签

```yaml
---
tags:
  - source          # 源稿（仅 sources/ 下的文件）
  - platform/wechat    # 微信公众号版
  - platform/xhs       # 小红书版
  - platform/zhihu     # 知乎版
  - status/draft       # 草稿
  - status/review      # 待审核
  - status/published   # 已发布
  - status/archived    # 已归档
---
```

### 资源文件标签

在对应 markdown 引用或 MOC 中标注：
- `#asset/cover` — 封面图
- `#asset/carousel` — 轮播图
- `#asset/archive` — 废弃图

### 工具/案例标签

- `#tool/generator` — 生成脚本
- `#tool/template` — 模板文件
- `#case-study` — 案例研究

---

## 四、目录结构规则

### 内容生产流

```
content/sources/          ← 源稿（唯一的内容源头）
    ↓ 适配
content/platforms/wechat/     ← 微信公众号
content/platforms/xiaohongshu/ ← 小红书
content/platforms/zhihu/      ← 知乎
    ↓ 发布
publish/                  ← 已发布产物（只读归档）
```

**原则**：
- 源稿是**唯一的内容真实来源**（single source of truth）
- 平台版从源稿派生，不独立创作
- `publish/` 是发布后归档，**不是**创作目录

### 禁止行为

- 在根目录、`publish/` 或其他位置创建新的文章文件
- 在文章同级目录、根目录放置图片
- 直接修改 `publish/` 下的内容
- 在 `node_modules/` 或 `.obsidian/` 下创建业务文件

---

## 五、Obsidian 图谱配置

### 颜色分组（在 graph.json 中设置）

| 颜色 | 匹配规则 | 用途 |
|------|---------|------|
| 蓝色 (#4a90d9) | `path: content/sources/` | 源稿 |
| 灰色 (#888888) | `path: content/platforms/` | 平台版本 |
| 绿色 (#50b97a) | `path: tools/` | 工具与脚本 |
| 橙色 (#f5a623) | `path: case-study/` | 案例研究 |
| 紫色 (#9b59b6) | `name: _index` 或 `name: README` | 索引页 |

### 显示设置

- 显示孤立节点（showOrphans: true）— 便于发现漏链文件
- 隐藏箭头（showArrow: false）— 保持简洁
- 折叠力导向（collapse-forces: true）— 防止节点过度分散

---

## 六、质量检查清单

每次提交内容前检查：

- [ ] 所有 wikilink 指向存在的文件（无断链）
- [ ] 每篇源稿有"上一篇/下一篇"链接（首篇和末篇除外）
- [ ] 每篇源稿有"平台版本"链接
- [ ] 每个平台版有回链源稿的链接
- [ ] `content/_index.md` 包含所有已创作的源稿
- [ ] 图片放置在正确的 `assets/` 子目录下
- [ ] 没有文件在错误的位置（根目录、`publish/` 等）
