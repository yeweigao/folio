# Folio · 设计审美契约

一份让 AI agent 按**你的审美**做设计的契约。不是风格教程，不是组件库，不是生成引擎。

- 适用表面：PPT / 幻灯片、海报、网页与落地页、画布设计稿、手册排版
- 适用 agent：Claude、Codex、DeepSeek，以及任何读 SKILL.md 的东西
- 不管的事：内容生产、数据编造、引擎命令、品牌资产管理

## 为什么这么短

参考 `karpathy-guidelines`（67 行、4 条原则、零 references）的做法：**契约必须常驻上下文、执行时零查找**，所以 `SKILL.md` 硬上限 100 行（当前 79 行），全是声明式判词与禁令，不解释为什么更好。

但视觉品味有两类型规则，只有一类能压进 100 行：

- **A 类·负向机械**（禁 emoji、禁紫蓝渐变、禁三张同构卡片、禁假数据）→ 一句一条，住 `SKILL.md`。
- **B 类·正向构造**（三色相取什么值、排印阶梯、网格数学、形态路由）→ 必须有数字，且必须能**整体替换** → 住 `references/`。

所以 `SKILL.md` 是**自足的**：一个 reference 都不读也能交出不像 AI 的稿子；`references/` 只是深水，按需加载。

## 文件地图

```
SKILL.md                     契约（≤100 行）：七铁律 + 硬禁令 + 起飞检查 + 路由表
references/
  styles/folio.md            ★ 母体风格：色彩 / 双声部 / 网格 / 母题 / 影像 / 禁忌
  styles/_template.md        派生新风格七步 + 项目 DESIGN.md 模板
  form-routing.md            八形态路由：先判这一页在干什么
  anti-patterns.md           每条禁令的为什么 + 替代程序
  review.md                  交付前复核：留白审判、四视角、偏离记录
  surfaces/deck.md           幻灯片：网格数学 + 引擎事实（唯一收容所）
  surfaces/README.md         新表面接入十步清单（poster / web / canvas 待补）
EVOLUTION.md                 变更登记
```

## 装法

把整个目录放到你的 skill 目录（如 `~/.workbuddy/skills/folio`、`.claude/skills/folio`、`.codex/skills/folio`）。
**frontmatter 是唯一的发现契约** —— 严格 YAML，触发词写全。改坏了不会报错，只会被静默丢弃。

## 怎么用（agent 的工作顺序）

1. 输出一行设计读解：`Reading this as: [形态], for [读者], with a [气质] vibe.`
2. 形态路由：逐页判八形态之一（`references/form-routing.md`）
3. 选风格：从 `references/styles/` 整套采纳，禁止混搭
4. 版式与数字：按 `references/surfaces/<表面>.md` 的网格与阶梯执行
5. 交付前过起飞检查（`SKILL.md §3`）+ 复核（`references/review.md`）

项目级 `DESIGN.md` 是本项目最高权威。优先级链：**用户指令 > 形态 > DESIGN.md > 风格文件 > 通用默认**。

## 加一套新风格

复制 `references/styles/_template.md`，七步走完，状态标 `experimental`；在真实项目最难的一页跑通后升 `stable`。
风格身份证括号位必须是**真实流派名**（可检索、有代表作、给系统不给皮肤），自造场景词不算。

## 已验证场景

- **小学三年级英语课件**（26 页课堂投影）：瑞士网格 × 公共信息（Otl Aicher · Munich 72），三色纪律黑 / 白 / 柠檬黄；教学叠加层（阶段词 kicker、✓/✗ 对照、示例题 00、斜体焦点词、每页信号色锚点 ≥1.5%）；母题是页眉 12 格进度刻度尺，26/26 页覆盖。
- **董事会 / 战略评审 deck**：boardroom 编辑风，阅读型高密度 + 论证驱动的标题制度。

示例工程不随本仓库分发（见 `folio-examples/`）。

## 分期

| 版本 | 内容 |
|---|---|
| v0.1（当前） | 契约 + folio 母体 + 形态路由 + 反模式 + 复核 + deck 表面 |
| v1.0 | poster / web / canvas 三个表面文件；每个表面一个 worked example |
| v2.0 | evals（briefs / rubric / 盲测）、frontmatter CI 校验、跨 agent 安装验证 |

## 许可

MIT（见 `LICENSE`）。
