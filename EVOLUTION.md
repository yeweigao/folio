# EVOLUTION · 变更登记

登记格式：`日期 · 类型(law|style|anti-pattern|surface|interpretation) · 对象 · 动作(收紧/豁免/具体化/新增/退役) · 理由`

铁律条文的变动 = MAJOR，必须同步改 `SKILL.md` 正文，不能只记在这里。

---

## 2026-10-25 · v0.1 立宪

- `2026-10-25 · law · 全部 · 新增` —— 从 `ppt-art-director`（引擎绑定的 PPT 艺术指导）改为 `folio`（引擎无关的设计审美契约）。理由：审美判断不该绑在某一条生成管线上；同一套哲学应能落到 deck / poster / web / canvas。
- `2026-10-25 · law · 铁律 · 具体化` —— 从"四层派生哲学 + 四槽 DNA"压成七条一行判词 + 一条自由条款。理由：厚诠释不进 agent 常驻上下文，等于没写（hallmark 39KB gates 的前车之鉴）。厚内容改住 `references/anti-patterns.md` 按需查。
- `2026-10-25 · law · 铁律 7 · 新增` —— 可读性不可谈判，且与审美冲突时审美让路。理由：可用性优先于品味是可验证的，不是偏好。
- `2026-10-25 · anti-pattern · 15 条 · 新增` —— 硬禁令单列成 A 类机械清单。理由：AI 不是不懂设计，是默认滑向安全而平庸的捷径；契约的作用是堵住捷径。
- `2026-10-25 · style · folio · 新增` —— 母体风格确立为瑞士国际主义底座（纸 / 墨 / 一个信号色；双声部；12 列硬网格）。理由：屋主既有样式总册的骨架本身就是 Swiss，其他主题应由它派生而非并列。
- `2026-10-25 · surface · deck · 具体化` —— 全部生成引擎事实（字重只认 bold/normal、字族可用性、中文字体栈首、容器高度 ×1.6、lint / VLM 门禁）收容进 `surfaces/deck.md`。理由：这是全仓库唯一允许出现引擎细节的地方，换引擎只改这一个文件。
- `2026-10-25 · surface · typography / design-constitution / builtin-integration / teaching-deck-system / vlm-review / modular-grid / design-philosophy / designs · 退役` —— 内容并入 `surfaces/deck.md`、`styles/folio.md`、`styles/_template.md`、`review.md`。理由：一个判断只应有一个出处。
- `2026-10-25 · interpretation · 三个旋钮（V/M/D） · 豁免` —— 不引入数值旋钮，改用设计读解里的气质形容词定性。理由：旋钮本身就是新形式主义，且不是屋主的语言。
- `2026-10-25 · interpretation · 示例工程 · 退役` —— `Up High - Grade 3 English/` 移出到 `folio-examples/`。理由：宣言仓库保持纯 md，二进制离场。
