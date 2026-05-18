# XGame Project Status

**last_updated**: 2026-05-19  
**last_change_ref**: `ai-shared/skills/ux-collect/SKILL.md` / `AI-workflow-discussion-log.md` layout 家族页录入 workflow 固化完成

---

## Current Phase

Phase 1 - 核心流验证推进中

---

## Current Todo

- 验证真实策划文档的端到端 IA 输出
- 确认 `ux-collect` -> `ia-generate` -> Figma 的衔接路径
- 保留 Phase 2 / Phase 3 议题，等 Phase 1 验证完成后再推进

---

## Blockers

- Phase 1 端到端验证尚未完成

---

## Next Step

- 运行一个真实策划需求，通过 `ia-generate` 产出 IA 文档并人工复核
- 验证 `ia-generate` 已按 `organism_components -> molecular_components -> atom fallback` 顺序输出组件清单
- 用 Claude / Codex 各做一次共享入口读取，确认不再依赖旧正文

---

## Notes

- 当前共享知识源已显式区分原子层、分子层与组织层，`organism_components` 与 `molecular_components` 已成为高阶组件显式入口
- 本轮已完成组织层/分子层优先实例化规则落地，并已获人类批准同步写入项目日志
- `ia-generate` 已补充高阶组件优先消费策略：先读 `organism_components`，再读 `molecular_components`，原分类仅作原子兜底
- 已完成一次新的 `ux-collect` 实采：Figma「英雄卡牌」(`1928:3412`) 已补录到 `knowledge/common/`
- 本次新增武将头像、武将列表卡、武将大卡、战法卡、HUD头像、群头像等分子组件条目，且已补齐 `componentKey`
- 已继续完成 Figma「英雄卡牌」分子层第 1/2 批补录：`5480:6611` 与 `6453:23911` 已写入 `knowledge/common/`
- 本次补录扩展了道具格、武将信息、身份、特技、状态标签、排名徽章、地图标题、勾选行、趋势标签、体力标签等分子组件
- 已完成 Figma「组件 模板 Copy」(`jB3vJujGbA7pKX9rNIlJUt`) 的 token/style 首次实采，新增 `tokens-decision.md` 与 `tokens-data.json`
- 已完成 Figma「组件 模板 Copy」(`1928:3750`) 的沙盘部队组织层补录，知识库新增 `organism_components` 并将消费优先级扩展为 organism > molecule > atom-fallback
- 已补强 `ux-collect/SKILL.md`：采集 `component-spec.json` 时需先判断组织层/分子层/原子层归属，完整业务块优先录入 `organism_components`
- 已继续完成 Figma「组件 模板 Copy」组织层补录第 1~3 批：`1928:3790`、`1928:3851`、`5883:5226` 中真实可实例化组件已写入 `organism_components`
- 本次补录新增城池名牌、营帐、三档地图标签、排行榜前三块、排名条目、表头/条目结构件，以及主页 HUD 顶部栏、任务/招募/回城/右下按钮组等组织层组件
- 本轮继续执行“只录入真实 COMPONENT / COMPONENT_SET 且必须带真实 componentKey”的严格规则，场景 frame 与示例板不入库
- 已继续完成 Figma「组件 模板 Copy」组织层补录第 4~5 批：弹窗结构、地图 tips、聊天对话、信息栏系统、面板与阵营列表等真实组织层组件已写入 `organism_components`
- 本轮也明确跳过了无真实顶层组件的示例板页面，例如 `5922:5533`，以避免把 frame 或实例误记为可发布组件
- 已新增 `decision-source/knowledge/common/layout-decision.md`，收录界面 layout 分类逻辑：主界面 / 通用界面 / 弹窗 / 特殊界面，以及通用界面与弹窗的二级分类规则
- 已补齐 `ux-collect` 文件分类约定：按 `tokens / component / layout / flow` 四类落知识文件
- 已新增 `decision-source/knowledge/common/layout-spec.json` 作为 layout 结构化数据入口
- 已新增 `decision-source/knowledge/common/flow-decision.md` 作为 flow 规则入口
- 已明确 layout 采集口径：layout 可来自 frame 或 component，允许结合用户语义提示，并需在 `layout-spec.json` 中记录整页 UI 区块的位置、尺寸与适配信息
- 已完成 Figma「组件 模板 Copy」`中小弹窗`(`4832:3245`) 家族补录：剩余中小弹窗变体已同时写入 `layout-*` 与 `component-*`
- 本次补录新增详情查看、等级说明、举报反馈、规则阅读、左右联动选择、左图右内容、上下双区块说明、资源不足、挂机奖励、晋升说明、纯文本自适应、资源转换、道具使用、大输入留言与窄版长列表等中小弹窗模板
- 已将右侧问题记录按横向对应关系并入中小弹窗家族规则，包括白色输入区位置检查、滑条与按钮间距统一、获取途径 list 高度 58 检查点
- 已完成 Figma「组件 模板 Copy」`中弹窗`(`4884:1889`) 家族补录：中弹窗空白模板与整页真实中弹窗变体已同时写入 `layout-*` 与 `component-*`
- 本次补录新增搜索列表、审批列表、双栏阅读、协议阅读、左主视觉右详情、左列表右预览、奖励排行清单、页签概览、全宽单主体内容、对象培养与上下复合情报等中弹窗模板
- 已将中弹窗右侧问题记录并入家族规则，包括战法详情名字框需要加长，以及大文本框内部文字与边框间距为左右20、上下32
- 已完成 Figma「组件 模板 Copy」`大弹窗`(`4970:4432`) 家族补录：大弹窗空白模板、组件集及真实可实例化变体已同时写入 `layout-*` 与 `component-*`
- 本次补录新增左 tab + 中央大列表/空状态、左 tab + 中央单列/宫格选择区 + 右侧说明栏等大弹窗模板
- 已将大弹窗右侧问题记录并入家族规则：武将信息横向间距与中弹窗 `UIGridLandDefenderInfo` 不一致，后续应作为对齐检查项
- 已完成 Figma「组件 模板 Copy」`满屏浮窗`(`4009:327`) 补录：攻占成功/失败全屏结果层已写入 `layout-*`，真实 `名次` 组件集已写入 `component-*`
- 本次补录明确了“满屏浮窗”应以 layout 采集为主，不应把整页 frame 误记为普通弹窗组件
- 已将本轮 layout 录入 workflow 正式写回共享规则：包括右侧注释按横向与 `y` 轴邻近映射、空白模板先行、`component_set` 变体需单独补 `componentKey`、满屏覆盖层采用 `layout-first`
- repository encoding baseline verified: 25 target text files are strict UTF-8 and all target files now carry UTF-8 BOM by policy
- repository encoding policy is documented in `ai-shared/docs/encoding-governance.md` and enforced for common text types via `.editorconfig` and `.gitattributes`
- read-only encoding audit entry point is `tools/encoding-audit.ps1`; in Windows PowerShell 5.1, inspect text with explicit UTF-8 reads
- shared workflow entry documents now explicitly require future text files to follow UTF-8 with BOM + LF and route encoding checks through `tools/encoding-audit.ps1`
- 历史背景与结构变更过程见 `AI-workflow-discussion-log.md`
