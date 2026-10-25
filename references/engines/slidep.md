# slidep 适配器

> status: tested · 最后核对：2026-10-25 · macOS · slidep → OOXML → LibreOffice 渲染核对
> 这些是**实测事实**，不是文档承诺。引擎升级后按 §7 重测；失真的条目降为 `stale`。

## 1. 适用范围

- 产出 16:9 幻灯片，内部生成 OOXML，可导出 PPTX；渲染核对以 LibreOffice 为准。
- 适合：论证型 deck、教学课件、评审材料。不适合：需要复杂矢量插画或视频嵌入的页面。
- 照片与原生图表可用；复杂图形用 SVG 形状 + 独立文字层。

## 2. 画布与单位

- 画布 **1280×720**，单位 px；所有坐标按 `surfaces/deck.md` 的网格计算。
- 容器高度按 **fontSize × 1.6** 预留；引擎的 `lineHeight` 在包含检测里几乎不生效，按 1.15 算必报 child-containment。

## 3. 字体与字重

| 写法 | 实测结果 |
|---|---|
| `fontWeight: 'bold'` | 约 700 |
| `fontWeight: 'normal'` | 400 |
| `fontWeight: 'thick'` | **反而更细**（退回常规），禁用 |
| `fontWeight: 700 / 800 / 900` | **被静默忽略**，与 bold 等价，拿不到 Black 字面 |

**结论：要 Black 字面只能换字族，调数字无效。**

| 字族 | 调用 | 结果 |
|---|---|---|
| Helvetica Neue | `'Helvetica Neue'` + bold/normal | 可用 400 / 700；正文与标题默认 |
| Avenir Next Heavy | `'Avenir Next Heavy'` + normal | 可用 约 900；D 档巨字首选 |
| Avenir Next Condensed Heavy | 同上 | 可用 约 900，窄 12–15%；长标题用 |
| Arial Black | `'Arial Black'` + normal | 可用 900；兜底，不首选 |
| Helvetica Neue Condensed Black | 任何写法 | 不可用 静默回退常规 |
| Futura / DIN Condensed | 任何写法 | 不可用 回退 |
| Arial | — | 可用但不首选：Helvetica 的克隆，笔画更粗笨 |
| Inter | — | 只在声明为标签/数字角色时可用 |

**中文必须栈首**：`"Helvetica, Arial, 'PingFang SC', sans-serif"` → 中文走系统回退且 bold 失效；`"'Hiragino Sans GB', 'PingFang SC', sans-serif"` → bold 正常。
规则：含中文的文本，中文字体放栈首；中英混排最稳是拆成两个文本元素各控字重。`Hiragino Sans GB` bold 最壮、汉字方正，中文标题首选；`PingFang SC` 字面偏圆。

## 4. 布局与文本

- 文本溢出**不一定报错**；必须用真实字族测量换行，抽 3 页看渲染图。
- 包含检测按容器尺寸判定；给足 `fontSize × 1.6` 的高度，再留 4–8px 余量。
- 换字体 = 重排版面：字宽差 10–25%，换行点与卡片高度必须重新核过。
- 一个文本元素只控一种语言的字重；混排拆元素。
- 可读文字保持为文本对象，不转图。

## 5. 图像与图表

- 原生图表用于柱 / 折线 / 面积；`background` 设为页面底色，不放进卡片；`showLegend=false`（≤3 系列）；系列名与终值用独立文本直标 16–18px。
- 瀑布 / 气泡 / 哑铃 / 结构图用 SVG 形状，**所有文字是独立文本元素**，禁止整块含字 SVG。
- 图片按列宽裁切；真实素材优先，找不到就改用色块 / 几何构图，不生成假照片。
- 占位框无法改掉引擎默认的灰底虚线圆角——改用信号色块 + 测绘角标 + 说明文字，或直接升格为满版构图。

## 6. 导出与门禁

- 导出 PPTX 后必须实际打开：字体替换、换行、图表、图片位置逐页核对。
- **工程门禁**（语法、溢出、包含、画布、组件能力）无条件服从，是机器限制。
- **审美门禁**（"留白 / 失衡"启发式）不是法令；按 `../review.md` 的偏离协议处置，记录后放行。
- `ART-DIRECTOR.md`：命中预设且不允许另建 DESIGN.md 时，落六行风格增量单（外观取自 / 结构取自 / 网格 / 声部 / 影像 / 禁区）。

## 7. 已知损失与复测清单

**做不到 / 会静默失败：**

- 数字字重 800/900（只能用 Heavy 字族代替）。
- `'thick'`（更细）。
- Helvetica Neue Condensed Black / Futura / DIN Condensed（回退）。
- 装饰性字即图像时，SVG 内文字不可编辑 → 必须另建真实文本层。
- 复杂阴影 / 渐变 / 3D 不可靠，本身也在硬地板上。

**复测清单（升级后逐条）：**

- [ ] bold / normal / 数字字重 / thick 四写法
- [ ] 三款 Heavy 字族与三款已知失败字族
- [ ] 中文栈首 bold 是否生效
- [ ] 容器高度 1.6 倍规则是否仍成立
- [ ] 原生图表背景 / 图例 / 直标文本
- [ ] 导出 PPTX 的字体替换与换行
- [ ] 占位框渲染
