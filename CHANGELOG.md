# 变更日志（CHANGELOG）

> 记录本仓库的增量更新。遵循「增量优先、不动原有已发布内容」原则：新增内容以新文件/新篇章补充；确需改动原文件的，每个改动点都在本文件登记。

---

## 2026-08-17 — 增量补充：同步本地工作区最新规范（毛球化 + 脱敏）

本次更新把本地产品文档工作区近 4 个月沉淀的规范，站在「毛球 App」虚构案例的角度，脱敏后补充进本仓库。不动原有已发布内容。

### 新增文件

| 文件 | 说明 |
|------|------|
| `CHANGELOG.md` | 本文件：变更日志 |
| `templates/_INDEX-A类.md.template` | 新增：A 类目录（扁平目录）的 `_INDEX.md` 模板 |
| `templates/_INDEX-B类.md.template` | 新增：B 类目录（按项目分子目录）的 `_INDEX.md` 模板 |
| `templates/_INDEX.md` | 新增：templates 目录索引（C 类模板范例），登记全部 4 个模板 |
| `content/sources/09-context-discipline.md` | 新增源稿：上下文纪律（第 09 篇） |
| `content/sources/10-workspace-governance.md` | 新增源稿：工作区治理（第 10 篇） |
| `content/sources/11-jobs-queue.md` | 新增源稿：工作队列（第 11 篇） |
| `content/sources/12-version-governance.md` | 新增源稿：版本治理（第 12 篇） |
| `content/sources/13-orchestration.md` | 新增源稿：编排与门禁（第 13 篇） |
| `content/sources/14-review-dual-track.md` | 新增源稿：Review 双轨（第 14 篇） |
| `content/sources/15-readable-writing.md` | 新增源稿：对外文档可读性（第 15 篇） |
| `content/sources/16-memory-retro.md` | 新增源稿：三层记忆与复盘（第 16 篇） |
| `content/sources/17-bot-on-im.md` | 新增源稿：在内部 IM 里跑 AI bot（第 17 篇） |

> 新增源稿共 9 篇（09-17）均为毛球化 + 脱敏：以毛球 App（宠物社区/附近服务/AI 问答/商城）为贯穿场景，不包含任何真实内部信息。

### 改动原文件（仅最小追加/修正）

| 文件 | 改动点 | 说明 |
|------|--------|------|
| `README.md` | ① 修正学习路线图断链；② 追加 09-17 新篇条目 | 原 docs/05-13 引用指向不存在的文件，改为指向实际文件；原有文字不动 |
| `content/_index.md` | 追加 09-17 索引行、内容结构树、篇章关系图 | 不修改原有 00-08 行 |
| `docs/00-philosophy.md` ~ `docs/06-evaluate.md` | 每个文件头加「已被 content/sources/XX 替代」标注 | docs/ 为旧版残留，保留但标注已替代 |

### 同步更新（登记用，非新增内容）

| 文件 | 说明 |
|------|------|
| `templates/_INDEX.md` | 新增 templates 目录索引，登记全部 4 个模板 |

### 未做事项（尊重增量原则）

- 不改 `content/sources/00-08` 正文、`content/platforms/` 平台稿、`publish/` 产物
- 不重新生成 `publish/wechat-html/` 的 HTML
- 不新增 09-17 的平台适配稿（后续另行决定；源稿内平台版本区已标"待补充"，避免假断链）
- 不删除任何文件

### 验证记录（2026-08-17）

| 检查项 | 结果 |
|--------|------|
| 断链检查 `tools/generators/check_broken_links.py` | ✅ 409 个 wikilink 全部有效 |
| 脱敏扫描（内部代号/人名/Agent 名/游戏名） | ✅ 0 命中 |
| 新增源稿 frontmatter（source / series/XX / status/draft） | ✅ 09-17 全部规范一致 |
| 系列导航（上一篇/下一篇首尾衔接） | ✅ 00→17 完整闭环 |
| 毛球案例贯穿 | ✅ 每篇 2-10 处 |
