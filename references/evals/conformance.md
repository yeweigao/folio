# 合规检查（conformance）—— 仓库自身的机器检查

> 这是 L0。命令在仓库根目录运行；任何一项失败，不进入成品评测。
> 本文件只检查**可机械判定**的事实，不评价美。

## 1. 文件与格式

- [ ] 除 `LICENSE`、`.gitignore` 外，所有交付文件为 `.md`；无图片、字体、PDF、压缩包、示例工程。
- [ ] 无 `.DS_Store`、`.cache`、临时导出目录。
- [ ] `SKILL.md` 有严格 YAML frontmatter：`name` / `description` / `license` / `version`；`version` 与 README 版本路径的当前版本一致；1.0 发布时为 `1.0.0`，1.x 补丁按 `1.x.y` 递增。
- [ ] 所有方言文件头部有 `status: stable | experimental`；没有第三种状态。
- [ ] 所有 Markdown 相对链接可解析；锚点指向存在的标题。

```bash
# 非 md 文件（应只剩 LICENSE / .gitignore）
find . -path ./.git -prune -o -type f ! -name '*.md' -print

# 死链：按源文件所在目录解析每个相对 .md 链接
find . -name '*.md' -not -path './.git/*' -print0 | while IFS= read -r -d '' f; do
  d=$(dirname "$f")
  rg -o --no-filename '\]\(([^)#]+\.md)' -r '$1' "$f" 2>/dev/null |
    while IFS= read -r l; do [ -e "$d/$l" ] || echo "MISSING: $f -> $l"; done
done
```

## 2. 结构计数（改动后必须仍成立）

| 对象 | 数量 | 出处 |
|---|---|---|
| 铁律 | 7 | `SKILL.md §1` |
| 硬地板 | 16 | `SKILL.md §2` |
| 方言 | 10 | `references/styles/` + `SKILL.md §4` |
| 破格 | 14 | `references/variations.md` + `SKILL.md §5` |
| 形态 | 8 | `references/form-routing.md` |
| 表面 | 5 | `references/surfaces/` |
| 评测命题 | 12 | `references/evals/briefs.md` |
| 引擎适配器 | 3 | `references/engines/`（含 generic；验收单不计入） |
| 红队攻击 | 12 | `references/red-team.md` |

```bash
ls references/styles/*.md | grep -v _template | wc -l   # 10
rg -c '^\| [0-9]+ \|' references/variations.md          # 14
awk '/^## §2/{f=1} /^## §3/{f=0} f&&/^[0-9]+\./{n++} END{print n}' SKILL.md  # 16
awk '/^## 4\. 十二类攻击/{f=1} /^## 5\. 修复动作库/{f=0} f&&/^\| A[0-9][0-9] \|/{n++} END{print n}' references/red-team.md  # 12
```

## 3. 数字一致性

以下值只能有一种写法；改动必须同步全部出处。

| 量 | 规范值 | 主要出处 |
|---|---|---|
| deck 画布 | 1280×720；边距 70；12×73 + 11×24 = 1140 | `surfaces/deck.md`、`craft/grid.md`、`styles/folio.md` |
| deck 基线 | 8px；正文 18–22px；投影 26–32px | 同上 |
| web | 1440 视口内容 1296（12×86 + 11×24）；≥1600 视口封顶 1440（12×98 + 11×24）；断点 390/768/1024/1440；正文 16–20px | `surfaces/web.md`、`craft/grid.md` |
| A4 手册 | 210×297；边距上18/下21/内21/外15；版心 174×258；12×9 + 11×6；基线 21pt；正文 10.5pt | `surfaces/handbook.md`、`craft/grid.md`、`canon.md` |
| A5 手册 | 148×210；边距 15/18/18/13；版心 117×177；6×14.5 + 5×6；正文 9.5pt | `surfaces/handbook.md` |
| A2 海报 | 420×594；边距 28；12×23 + 11×8 = 364 | `surfaces/poster.md` |
| A3 海报 | 297×420；边距 20；12×15.92 + 11×6 = 257 | `surfaces/poster.md` |
| A4 海报 | 210×297；边距 15；6×25 + 5×6 = 180 | `surfaces/poster.md` |
| canvas | 8pt 空间网格；帧距 80/160/240；正文 14–16px | `surfaces/canvas.md` |
| 对比度 | ≥4.5:1 | `SKILL.md §2.16`、`craft/color.md` |
| 可读文字 | ≥12px（投影 ≥16px；deck 阅读型正文 ≥18px、投影正文 ≥26px） | `SKILL.md §2.16`、`surfaces/deck.md` |

**复算规则**：列宽 × 列数 + 槽宽 ×（列数−1）+ 左右边距 = 画布宽。任何一行加不上，就是数字错了。

**工艺常量**（改动必须同步 craft 与 surface）：

| 量 | 规范值 | 出处 |
|---|---|---|
| 排印阶梯 | 12 / 14 / 16 / 20 / 24 / 32 / 46 / 64 / 112 | `craft/typography.md`、`styles/folio.md` |
| 投影标签 | 18–22px | `craft/typography.md`、`surfaces/deck.md` |
| A4 展示上限 | 84pt | `craft/typography.md`、`surfaces/handbook.md` |
| A2 正文 / 主标题 | 36pt / 120–300pt | `craft/typography.md`、`surfaces/poster.md` |
| 信号面积 | 常规 ≤10%；主张 ≤20% | `craft/color.md` |
| scrim | ≤0.55（压白后白字 4.7:1） | `craft/imagery.md` |
| 图注 | 12–14px / 8.5–9.5pt | `craft/imagery.md` |
| illustrative 标记 | 不低于同表面图注下限（屏幕 12px；印刷 8.5pt；A2 14pt） | `engines/acceptance.md §2 #9` |
| 数据类别 | ≤5 | `craft/data.md` |
| 图表线 / 刻度 | 网格线 ≤5；轴刻度 3–5 | `craft/data.md` |
| 动效 | 100–400ms；stagger 20–40ms | `craft/motion.md` |

## 4. 引擎事实隔离

- [ ] `fontWeight`、`lineHeight`、`showLegend`、具体字族可用性、导出命令等**引擎事实**只出现在 `references/engines/`。
- [ ] `styles/`、`craft/`、`surfaces/` 只描述"要什么"，不描述"用哪个开关"。
- [ ] 允许出现引擎**名称**（说明适用范围），不允许出现引擎**命令/陷阱/API**。
- [ ] `slidep.md` 的每条能力有 `tested` 或 `unverified`；`ardot.md` 标 `unverified`。

```bash
# 引擎命令/陷阱不应出现在 engines 之外
rg -n 'fontWeight|showLegend|LibreOffice|OOXML|child-containment' --glob '!**/engines/**'
```

## 5. 语言与禁令

- [ ] 全文无 emoji、装饰性符号、颜文字；`✓/✗` 仅作为功能性教学标记（§2.4 例外），不靠红绿，不用作导航或状态装饰。
- [ ] 禁用词只作为**禁令示例**出现，不作为正面用词：
      `elevate / seamless / unleash / 赋能 / 一站式 / 引领未来`。
- [ ] 不出现"高级感 / 氛围感 / 呼吸感"作为**结论**；只能作为待翻译的客户原话，并给出具体做法。
- [ ] 每条禁令都有可指认的对象与替代（`anti-patterns.md`）。
- [ ] 中英文混排：中文用全角标点；英文正文不用装饰性长破折号（`AP-014`）。

```bash
rg -n '[\x{1F300}-\x{1FAFF}\x{2600}-\x{27BF}]' --glob '*.md' | rg -v '✓|✗'   # 应为空；✓/✗ 是 §2.4 允许的教学标记
rg -n 'elevate|seamless|unleash|赋能|一站式|引领未来' --glob '*.md'  # 只应出现在禁令行
```

## 6. 一致性抽查（人工，5 分钟）

1. 随机打开 3 个方言文件：`status`、四槽、七条互动表是否齐全？
2. 随机打开 3 条破格：是否有"打破 / 何时 / 怎么做 / 代价 / 仍然成立"？
3. 随机打开 3 个表面：网格数字能否复算？最小字号是否一致？
4. `README.md` 的文件地图是否与真实目录一致？有没有指向已删除文件的链接？
5. `SKILL.md` 行数是否 ≤130？新增内容是否挤掉了本应常驻的判词？
6. 抽查一次交付：对照 brief 逐字核对标题、日期、地点；通过结论是否来自独立复审？
7. 若有红队记录：实测与纸面是否分开？高危攻击是否都有封堵或具名残余登记？
8. `RELEASE.md §5` 的审计命令是否还能跑出注释里的数字？

## 7. 发布门禁

- [ ] §1–§6 全绿。
- [ ] `git status` 中只有预期的 `.md` 改动；无二进制、无密钥、无示例工程。
- [ ] `EVOLUTION.md` 有本次版本的登记（日期 / 类型 / 对象 / 动作 / 理由）。
- [ ] 版本号、README、SKILL frontmatter 三处一致；`RELEASE.md` 存在，且版本史、证据索引、未验证项三节齐全。
- [ ] 已知未验证项（Ardot 适配器、实验表面）在 README 或适配器中明确标注，不藏在正文里。
- [ ] 交付回执使用 `engines/acceptance.md` 的 12 项表单，并写明 §8 的表面追加项；硬地板项或追加硬项未验时结果为 `unverified`，不得写 `pass`。
- [ ] “实际打开的证据”能指认文件、页数 / 宽度 / 设备；缩略图与预览不算证据。
- [ ] 至少一份真实评分记录（`evals/run-*.md`），含独立复审分数、失败项与由此产生的契约修正；只有自评的记录不算。
- [ ] 若本版触发红队：高危攻击没有未登记的；残余风险表有等级、承担者与下次复查版本。
