# 十个世界：独立迁移、修订与验证

十套均已完成独立新内容生成、规则修订与复测，最终采用样本的身份、构成与工艺评审均通过。所有失败稿和原始评审保留。最终样本与规则见 [对照图库](index.html)。

## 问题与做法

验证的是：只给 DESIGN.md、另一件作品的内容及声明素材，能否生成属于同一世界的新作品。第二张拼图的两张 Hackathon 共用一套构造，其余各有系统；加上报告组和景观身份，共十套。没有把同一拼图或相同流派名当作同一世界。

先复刻了 28 件原生作品，再提取初稿。第十套此前单测部分通过，随后另外九套分别用全新上下文测试。修订时先改世界规则，再由没有前作的新上下文生成；每轮沿用同一简报。制作者没有参考图、旧作品、图形组件、绘制代码、其他评审或主 skill，只收到本案输入。素材是授权字体，含第十套使用的像素替代字库；字体嵌入工具没有几何或排版。

输入和制作者定稿分别冻结并记录 SHA。浏览器由主流程独立渲染，再检查实际字体、事实、对比度与边界。身份、构成、工艺分别审阅；v1/v2 对照采用匿名 P/Q。后续身份评审直接查看用户原始 JPG。初次 P/Q 的 reference.png 来自复刻组；它直接证明与复刻世界的亲缘，原始 JPG 复评补查了原参考。

## 各套结果

首轮列是最初独立身份评审；后续评审有不同判断，原始文件均保留。

| 世界 | 首轮初评 | 本轮修正的关键关系 | 最终采用 |
|---|---|---|---|
| [01 方砖报告](../systems/01-report-tiles/DESIGN.md) | 部分通过 | 短胖斜 X、多瓣放射块、圆角方叶；轻重字体和阅读配色 | v2：身份／构成／工艺通过 |
| [02 街区拼贴](../systems/02-streetwise-collage/DESIGN.md) | 部分通过 | 粗图案频率、交错密度与切分曲面；同量级粗细中文 | v3：三项通过；箭头数值澄清见下 |
| [03 切割字形](../systems/03-cut-glyph-exhibition/DESIGN.md) | 部分通过 | 连续大字场与分节拼接场；并列弯钩、带腰双碗与内孔 | v6：三项通过 |
| [04 俱乐部分区](../systems/04-club-partitions/DESIGN.md) | 部分通过 | 裁切圆弧、楔形、鼓包与黑缝；艺人名单及小字配色 | v2：三项通过 |
| [05 文化角色](../systems/05-culture-monsters/DESIGN.md) | 部分通过 | 不同身体轮廓、长触手、扁平黑嘴中的密排白点；下部模块延续 | v4：三项通过 |
| [06 开发者空间](../systems/06-hackathon-space/DESIGN.md) | 部分通过 | 电蓝网格、纸色窗口与真实投影块体共同组织信息 | v2：三项通过 |
| [07 字母版面](../systems/07-type-built-week/DESIGN.md) | 通过 | 几何按整字格重造笔画；必要圆盘达标配色与一致间距 | v3：三项通过 |
| [08 森林角色](../systems/08-forest-character/DESIGN.md) | 部分通过 | 三层扁身体、突出大白眼、棋盘、粉胶囊与黑地绿树 | v2：三项通过 |
| [09 等轴舞台](../systems/09-isometric-letter-stage/DESIGN.md) | 通过 | 面内排字、错位高窄体块、顶面文字与白色跨桥 | v4：三项通过 |
| [10 模块景观](../systems/10-molly-scenery/DESIGN.md) | 部分通过 | 两种花的内部构造、模块景观；普通竖版与窄条条件分开 | v2：三项通过 |

### 修订并非一次就成功

v2 十套均实际生成。身份复评指出 02、03、05、07 仍有问题；构成复评同时指出 07 的几何退成字腔小贴片。03 的后续结果又暴露左右场密度趋同、右侧构件简化为普通半圆与 U 环。补回并列弯钩与带孔双碗后，复评又定位到小群密度和中文／Latin／日期功能色彩的漂移；继续明确了这些关系。05 一度把面部约束收得过窄，删去了原组浅黑嘴中的密排白点；直接原图复评后补回。09 的早期盒面排字成立，但原图复评指出规则同心台阶与无字顶面削弱空间字场，随后修了体块和顶面规则。

02、04、07 的基线在不同评审轮中出现评分差异。没有重写旧评论，也没有拿初评与最后评审的通过数量作可靠性提升百分比。每一项采纳的问题都须能在像素定位，并允许新内容的摆放自由。

### 02 的数值澄清

v3 制作者指出箭头的臂厚、直角与外高不能同时满足原来的独立外宽 0.62u。最终 DESIGN 以几何关系推导宽度 `0.35u + 0.22u/√2`，与该制作者披露并已渲染的实际构造一致。独立读取 SVG 实测四支箭头，宽、高、夹角均吻合。[几何记录](evaluation/02-arrow-clarification.json)保留计算。此澄清后没有再启动新制作者，不能称为最终字节版本的全新生成；其余最终施工正文与对应冻结输入一致，Record 仅回写结果。

## 已落地到 Skill 的修改

- [SKILL 路由](../../../../SKILL.md)：参考复刻／提取单独进入；已经选定的复刻方向直接保留。
- [DESIGN 生成规则](../../../../references/design-md.md)：按共享构造分世界；写出轮廓、内部比例、负形、连接与字体角色；区分固有数量和实例重复数量；明确场形与格式条件。冻结输入，用独立新内容验证，记录失败后再改规则。
- [孟菲斯方言](../../../../references/themes/swiss/dialects/memphis.md)：保留工作色彩、构造词汇与文字参与；允许方砖、分区、字形场和投影组装。方砖满铺是其中一种手法。撤去全方言方格、固定色数、主题图标配额和单一轻重字体约束。四种手法保留为选择入口，专有形状留在各世界。
- [主题入口](../../../../references/themes/swiss/theme.md)、[README](../../../../README.md)同步；历史提取脚本默认保留已修订系统。

这些通用规则提炼自世界修订。没有声称最终 skill 从零自动重提了全部十份系统；另外做了一项固定原图的提取对照。

## 生成规则本身的对照

固定简报为 [memphis-extraction.md](../../../../tests/memphis-extraction.md)。旧版、无 skill、候选版三个新上下文读同一原始第三张 JPG、同一字体清单和同一简报，分别写 DESIGN。第一位匿名评审将候选版排第一，无 skill 第二，旧版第三，前两者差距小。随后澄清固有构造数量与可变的实例重复数量，再用最终精确版本交给另一位新制作者提取，第二位匿名评审将最终新版排第一，旧版与无 skill 并列第二。

最终新版较清楚地交接了局部构造、尺度与格式条件；仍有局部数值、层级和未来 CJK 字形需要实际应用检查。这项对照只有文字交接，没有让三个提取文件各自再生成新图，不能把排名描述成成品审美或平均可靠性的胜出。原始匿名评审、版本映射与 source SHA 均保留。

## 工艺与证据

最终逐例检查保留在 [technical-final.json](evaluation/technical-final.json)。十份简报累计 90 个固定字符串，全部保留，0 缺失、0 警告；固定文字以实际渲染读序衔接换行，未经衔接的 rawText 留在 audit。CDP 记录实际使用内嵌字体，无字体错误或回退。按大小字各自阈值检查文本与实际底色；必要图形另查，见第七套 [图形检查](evaluation/07-graphic-audit-v3.json)。

最终 SVG 为原生文字和矢量，无栅格图像或外链；PNG 与简报画幅一致。第七套 TAIPEI 的字体外接盒跨上缘，实际可见墨迹从 y=26 开始，完整可读。工艺评审另查看了文字间距、遮挡和裁切。

所有输入、规则和制作源文件的指纹校验见 [frozen-integrity.json](evaluation/frozen-integrity.json)。第十套 v2 的同名制作者 PNG 曾被独立渲染覆盖，原字节仍与清单一致，已保留为 maker-poster.png；render-provenance.json 记录路径，原清单不改。没有以新作覆盖基线。

58 个冻结清单的原始字节均已保留，0 校验错误；02 的最终数值澄清按上文单列。当前世界规则已静态检查；历史生成器实际执行后保留十份修订规则。最终仓库检查结果见 evaluation/release-check.txt。通用 host quick_validate 在旧版、当前版均拒绝已有顶层 version 字段；[原始错误](evaluation/host-validator.json)保留。仓库协议依赖该字段，本轮没有为迁就另一个检查器改动元数据格式。

## 阅读原始记录

- 初次评审：[identity-v1](evaluation/identity-v1.json)、[structure-v1](evaluation/structure-v1.json)、[craft-v1](evaluation/craft-v1.json)；第十套原单测在 [transfer-test](../transfer-test/RESULT.md)。
- P/Q 复评：[身份](evaluation/identity-final-blind.json)、[构成](evaluation/structure-final-blind.json)、[工艺](evaluation/craft-final-blind.json)、[解码](evaluation/visual-decoded.json)。
- 直接原图复评：[全十套身份](evaluation/source-identity-final.json)、[v3 构成](evaluation/structure-v3-final.json)、[v3 工艺](evaluation/craft-v3-final.json)。v3 构成评审另外读了通用 skill 说明，未读本案 DESIGN；其读取边界如实保留。
- 最新三套：[v4 身份](evaluation/identity-v4-final.json)、[v4 构成](evaluation/structure-v4-final.json)、[v4 工艺](evaluation/craft-v4-final.json)。
- 03 的 v5：[身份](evaluation/identity-v5-final.json)、[构成](evaluation/structure-v5-final.json)、[工艺](evaluation/craft-v5-final.json)。
- 03 的 v6：[身份](evaluation/identity-v6-final.json)、[构成](evaluation/structure-v6-final.json)、[工艺](evaluation/craft-v6-final.json)。v6 由 v5 同三位独立于制作者的评审复查，知道自己的前轮意见，不称全新盲评。
- 提取规则：[首次匿名评审](evaluation/extraction-blind/review.json)、[最终匿名评审](evaluation/extraction-final-blind/review.json)、[最终解码](evaluation/skill-final-comparison-decoded.json)。

## 证据边界

每套只用一份全新简报，修订间重复同一简报，没有重复抽样或穷尽格式与内容长度。原字库、原作者和全部微小文案未确认；复刻使用已授权替代字库。第十套像素字体是预先声明的生产资产，未来字形的改造程序尚未全面验证。本次使用当前宿主模型的独立上下文，未按旧测试文档指定的 Sonnet／Opus 组合运行，也未做跨模型检验。没有验证印刷、实体打样、PDF/X、PPTX 或其他软件兼容性。交付为离线 HTML、可编辑 SVG、PNG 与规则文本。
