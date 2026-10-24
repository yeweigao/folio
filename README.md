# ppt-art-director

**给 AI PPT 生成管线用的艺术指导 Skill —— 先判内容形态，再谈风格。**

An art-direction skill for AI presentation pipelines: route by content form first, style second.

---

## 它解决什么问题

市面上的 AI 做 PPT，通病是**先套模板再想内容**：拿到需求先选一个"商务蓝"皮肤，然后把文字往格子里填。结果是每一页都"好看"，合起来却答不上一个问题——**这一页到底在干什么？**

本 skill 把顺序倒回来：

```
内容契约（整册：场合/读者/距离/证据形态）
  → 方言（真实设计流派，可检索、有代表作）
    → 形态（逐页：这一页在干什么）
      → 版式
        → 语法润色（网格/字号/色/线宽）
```

三条硬规矩：

1. **形态路由先于版式**——每页动笔前先判形态（宣言/展品/论证/推进/对照/演练/并列/转场），再在形态允许的版式家族里润色；
2. **内容有否决权**——形态与方言打架时，先换方言，再改内容；绝不为了守住风格曲解用途；
3. **方言括号里必须是真实流派名**——`瑞士网格 × 公共信息（Otl Aicher · Munich 72）`，不是"高级商务感"这种自造词。

## 仓库结构

```
SKILL.md                          技能入口：工作流、风格路由、完成定义
references/
  form-routing.md                 形态路由：八种形态判据 + 版式家族 + 内容否决权
  design-constitution.md          设计宪法：风格身份证 + 页面映射表规范
  design-philosophy.md            设计哲学：四层派生（哲学/方言/形态/语法）
  typography.md                   排印系统：字号阶梯 W(S) + 字体声部
  data-graphics.md                图表纪律：Tufte 式证据呈现
  builtin-integration.md          与内置 PPT 引擎的边界与协作
  vlm-review.md                   交付前视觉复核协议
  teaching-deck-system.md         讲课 PPT 设计体系（K12 英语课件特化）
  designs/
    design-principle.boardroom.md   方言模块：董事会编辑风（Brockmann 海报系统）
    design-principle.aicher.md      方言模块：公共信息（Otl Aicher · Munich 72）
```

## 已验证场景

本包在两类真实交付上跑通：

- **小学三年级英语课件**（26 页课堂投影）：方言为瑞士网格 × 公共信息（Otl Aicher · Munich 72），三色纪律黑 / 白 / 柠檬黄；教学架构源自 Grammar Explorer 与 Think 两套教材的拆解——一页一大题、答案独立成页、斜体焦点词、示例题 00、每页主题色锚点；母题是页眉 12 格进度刻度尺，26/26 页覆盖。
- **董事会 / 战略评审 deck**：boardroom 方言，阅读型高密度 + 论证驱动的标题制度。

示例课件的教学内容含公开教材的改编练习，不随本仓库分发。

## 用法

这是给 AI 编码助手用的 Skill（Claude Code / CodeBuddy / WorkBuddy 等兼容 skill 格式的环境）。放置于技能的 references 目录后，当任务涉及"做 PPT / 幻灯片 / 演示文稿"且要求大师级视觉时触发。

它**不替代**任何 PPT 生成引擎，只负责判断：这一页该长什么样、为什么、以及什么时候不该这么画。

## 许可

MIT（见 `LICENSE`）。
