# 排印系统 —— 一种画布、两种观看距离 + 一个字重映射 W(S)

来源：ppt-master-themes `framework/TYPE_SYSTEM.md`。排印是三件事：**阶梯**（角色差多少）、**W(S)**（每个角色多重）、**密度**（这个字号装多少字）。定了一个，另外两个不能临时改。

本文件只管 **16:9 的一册 deck**。A4 讲义、印刷品、阅读稿不在本 skill 范围内——那是另一种介质，有另一套规格，混进来只会稀释判断。

## 1. 一套阶梯，两种观看距离

| 角色 | px | 行高 | 用途 |
|---|---|---|---|
| D · 展示 | 60–140 | 1.0–1.12 | 封面主张、章节巨字、核心大数字 |
| T · 页标题 | 44–60 | 1.12–1.18 | 每页 Action Title |
| L · 导语 | 22–28 | 1.38–1.45 | 导语、提要、pull quote |
| B · 正文 | 18–22 | 1.48–1.55 | 论证正文、表格正文 |
| Bs · 紧凑正文 | 16–18 | 1.42–1.48 | 三栏卡片、侧栏、账本单元格 |
| C · 注释 | 13–16 | 1.35–1.4 | kicker、图表标题、直标 |
| A · 参考 | 12–13 | 1.35 | 轴刻度、负责人、来源、页码（**底线 12px**） |

上表是**桌面型**（自己在电脑上看、会后翻阅）。**投影型（观众 ≥3m，教室/会场）**整档上调：

| D | T | L | B | Bs | C | A |
|---|---|---|---|---|---|---|
| 96–160 | 48–64 | 32–36 | 26–32 | 22–26 | 18–22 | 16–18 |

判据只有一条：**最后一排能不能看清正文**。线上分享、录播取中间值 B 22–26。一册只选一种距离，不能这页桌面字号、下页投影字号。

**硬线**：导语必须比正文大 ≥5–6px（视线不许跳过导语）；正文行宽 45–68 字符、左对齐不两端对齐；可读文字 ≥12px——这是唯一不可谈判的排印底线。

**标题不是正文的放大版**：T 与 D 同框时级比 D/T 不要超过 4×。一旦 D ≥ 96，**T 必须 ≥56（投影 ≥60）**；44–48 只在没有巨字的页成立。取了下限又同框巨字，标题会被读成图注——这是"标题不够大"的结构性原因，不是审美偏好。

## 2. 字重：先看引擎事实，再谈 W(S)

### 2.1 引擎只认两个值 —— 重靠字族，不靠数字

实测（slidep → OOXML → LibreOffice 渲染核对）：

| 写法 | 实际效果 |
|---|---|
| `fontWeight: 'bold'` | 粗体，约 700。Helvetica/Arial 的 Bold 字面偏细，48px 下只算"半粗" |
| `fontWeight: 'normal'` | 常规 400 |
| `fontWeight: 'thick'` | **反而更细**（实测退回常规），是陷阱值，禁止使用 |
| `fontWeight: 700 / 800 / 900`（数字） | **被静默忽略**，走默认分支，与 bold 等价，拿不到 Black 字面 |

结论：**要"粗壮"只有一个办法——换带 Black/Heavy 字面的字族**，调数字无效。

**系统字体实测可用性**（macOS，slidep → LibreOffice 核对；写错名字会静默回退成常规，最坑）：

| 字体 | 调用写法 | 结果 | 用途 |
|---|---|---|---|
| Helvetica Neue | `'Helvetica Neue'` + `'bold'` | ✅ 真瑞士骨架，700 | 正文、标题 |
| Helvetica Neue | `'Helvetica Neue'` + `'normal'` | ✅ 400（Medium 也可作标题） | 正文、强标题 |
| Helvetica Neue Condensed Black | 任何写法 | ❌ **回退成常规**，拿不到 | — |
| Avenir Next Heavy | `'Avenir Next Heavy'` + `'normal'` | ✅ ~900，人文几何 | **D 档默认**（单字数字、封面、金句） |
| Avenir Next Condensed Heavy | `'Avenir Next Condensed Heavy'` + `'normal'` | ✅ ~900 且窄 | 长标题、窄栏、需要省 15% 宽度时 |
| Avenir Next Condensed | `'Avenir Next Condensed'` + `'bold'` | ✅ 窄粗 | 长标题 |
| Futura Condensed ExtraBold | 任何写法 | ❌ 回退 | — |
| DIN Condensed Bold | 任何写法 | ❌ 回退 | — |
| Arial Black | `'Arial Black'` + `'normal'` | ✅ 900，但气质偏美式 | 兜底，不首选 |
| Gill Sans / Optima / Baskerville | 家族名 + bold | ✅ | 英式/古典方言，非 Swiss |

**选型原则**：瑞士骨架用 **Helvetica Neue**（这是这套哲学的默认字形，不是 Arial）；需要 900 重量时，只有 Avenir Next 系能拿到，**默认用非窄的 Avenir Next Heavy**——Condensed 会把单字数字和大字压瘦、失去分量，只在长标题或窄栏里才用。**不要写 Arial**——它是 Helvetica 的克隆，字形细节（R 的腿、t 的顶、数字 1）都更粗糙，放在瑞士语境里就是"像但不是"。

### 2.1b 正文家族 + 显示家族（允许的唯一双家族）

引擎拿不到 Helvetica Neue 的 Black，所以显示层需要一个搭档。编辑设计的标准做法是 **text face + display face**：

```
正文家族（T / L / B / C / A）：'Helvetica Neue', Helvetica, sans-serif       —— 400 / 700
显示家族（仅 D ≥96）：          'Avenir Next Heavy', 'Avenir Next', sans-serif —— normal
中文（栈首）：                  'Hiragino Sans GB', 'PingFang SC', sans-serif  —— bold / normal
```

规矩：**显示家族只在 D 档出现**，一页最多一处；T 及以下一律回正文家族。混用超过这两层就是没系统。

### 2.1c 字宽实测（换字体 = 重排版面）

同一句 `Higher Order`（12 字符）实测宽度：Helvetica Neue Bold 64px ≈ 380px；Avenir Next Heavy 56px ≈ 390px；Avenir Next Condensed Heavy 60px ≈ 342px；Arial Black 56px ≈ 389px。**窄体能省 12–15% 宽度**，长标题优先它。

### 2.2 中文字体必须排在栈首，否则粗体直接丢

中文"不够粗"很少是缺字体，多半是**字体栈顺序**：

- `"Helvetica, Arial, 'PingFang SC', sans-serif"` → 中文走系统 CJK 回退而非栈内苹方，**bold 不生效**（实测渲染成常规）。
- `"'PingFang SC', sans-serif"` / `"'Hiragino Sans GB', sans-serif"` → bold 正常生效。

规则：**含中文的 Text，中文字体放栈首**；纯西文才用 `Arial, Helvetica` 起头。中英混排最稳的做法是拆成两个 Text，各控字重与字体。

macOS 实测可用：`PingFang SC`（bold 可用，字面偏圆）、`Hiragino Sans GB`（bold 最壮、汉字方正，最接近 Swiss grotesque，**中文标题首选**）。`Heiti SC` 本机缺失，写了会回退成细字，不用。

### 2.3 三套 W(S) 预设

一册 deck 只允许一个 `字号 → 字重` 映射。

### A · 重压型（默认）

| D | T | L | B | C | A |
|---|---|---|---|---|---|
| 900（Avenir Next 显示家族） | 700 / 900（显示家族） | 400–500 | 400 | 600–700 | 400–600 |

T 取 700 还是 900，看同页有没有巨字：**有 D 就上 900**，否则 700 足够，免得每页都在喊。

层级靠字重 + 紧行距；适合决策文档。代价：每页超过 2 处重压开始喊叫。**D 的 900 必须由 Avenir Next Heavy / Condensed Heavy 实现**（Helvetica Neue 的 Black 字面引擎拿不到），写 `fontWeight: 800` 同样无效。

### B · 反压型（画册 / 封面主导）

D 900（Avenir Next Heavy，≥76px，投影 ≥100）· T 400–500 · L 400 · B 400 · C 600–700（唯一加重区）· A 400。硬条件：字距 -0.5%~-2.5%、行距 1.0–1.08、对比 ≥7:1、低 dpi 先实测。小字用细体才是真错误。

### C · 均质型

全册 400 或 700，层级只靠字号比 ≥1.6× 与留白。要 900 就全册 900，不许混档。

## 3. 密度耦合

| 页型 | 正文预算 | 视觉锚点 |
|---|---|---|
| 论证页 | 300–450 字（B 18–19，单栏 30–42 汉字/行） | 1 个大数字或大图 |
| 数据页 | ≤120 字 + 图 | 主图 ≥50% 内容区 |
| 封面 / 收束 | ≤40 字 | 主张本身 |
| 账本 / 表格页 | 每行 ≤14 字 | 数字列 |

字号变大，字数必须跟着减；"字大且塞满"就是挤。

## 4. 双声部（可选，定了不能换）

衬线承担主张（标题、导语、论述、大数字、引语）；无衬线承担证据（kicker、图表、表格、日期、页脚）。角色不互换；连续段落不用无衬线；表格不用衬线；正文不用 Bold。

**默认全无衬线**：包级默认是 grotesque（Helvetica / Arial / Inter）一套，层级靠字号与字重；衬线双声部是编辑方言（boardroom）的可选项，不是包级默认。

字体栈（**顺序即功能，见 §2.2**）：
- 西文骨架：`'Helvetica Neue', Helvetica, sans-serif`（T/L/B/C/A，400 与 700）
- 西文显示（仅 D ≥96）：`'Avenir Next Heavy', 'Avenir Next', sans-serif`（900，配 `'normal'`）
- 中文（**必须栈首**）：`'Hiragino Sans GB', 'PingFang SC', sans-serif`
- 衬线（仅编辑方言，非默认）：`Georgia, 'Times New Roman', 'Songti SC', serif`

**不用 Arial**：它是 Helvetica 的克隆，笔画与字宽都更粗笨；瑞士语境里"像但不正"。Arial 只作最后一档回退，且要在 DESIGN.md 说明为什么回退。

**先量后画**：Helvetica Neue、Avenir Next、Condensed 三者字宽差 10–25%（窄体最窄），换行点完全不同；中文回退后字宽再变一次。所有标题换行与卡片高度必须在渲染里核过，不靠估算。**标题换字体 = 重排版面**，不是换个名字。

## 5. 与内置参考表的关系

内置通用原则的字号表是参考推荐，不是法令；分支文件的 22px 下限只约束该分支。取 18–22 正文须在 DESIGN.md 声明"覆盖内置参考区间"，并保证对比度 ≥4.5:1、单页字号 ≤5 种。

## 6. 常见误判

| 现象 | 判断 |
|---|---|
| 封面 300 巨字 + 内页 700 标题 | 合法，同一 W(S) 的两个取值 |
| 标题 48px + bold，看着像图注 | 取了下限 + 只有 Bold 字面：升到 56–64，D 档换 Avenir Next Heavy |
| 写了 `fontWeight: 900` 却没变粗 | 数字被引擎忽略；必须换 Avenir Next Heavy 系字族 |
| 写了 `'Helvetica Neue Condensed Black'` | 回退成常规（实测）；改用 `'Avenir Next Heavy'` |
| 字体还是 Arial | Arial 是 Helvetica 的粗劣克隆；换 `'Helvetica Neue'`，Arial 只做最后回退 |
| 中文写了 bold 仍是细的 | 栈里中文字体不在首位，粗体丢失（§2.2） |
| 用了 `fontWeight: 'thick'` | 陷阱值，实测更细；删掉 |
| 同级标题同字号一粗一细，无页型理由 | 混用 |
| 反压型把 hero 加粗"更有力" | 违反声明 |
| 全册两套系统各占一半 | 无系统，返工 |
| 导语只比正文大 2px | 硬缺陷，重设阶梯 |
