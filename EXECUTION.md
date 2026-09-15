# 执行与验收协议

本目录的 `workflow.json` 是唯一执行版本来源；旧文件名中的 v1/v3 等只用于兼容引用。
规则顺序：本次用户明确要求 > 项目配置 > 对应任务类型标准 > 通用标准；不能把未验证事实升级为真实能力。README 和历史变更说明不另设执行规则。

## 启动与恢复

1. 建立独立任务目录，将本次输入和 `task-brief.md` 放入目录。确认任务模式、市场语言、原始关键词 Sheet、产品目标、实际交付物、结构/配图范围；已知项目配置直接继承，只有影响执行的缺项才询问。
2. 根据本次要求与项目配置生成 task-contract.json，包含 workflow.json 的 contract_fields。该文件由执行者整理，不要求用户手填；未明确的范围先做合理继承，只有关键缺项才询问。初始化自动将其纳入哈希记录，最终交付必须与其一致。
3. 阅读入口及 `workflow.json` 的 bootstrap_files，再运行初始化命令。程序读取文件并记录哈希；记录只证明加载，不证明模型理解。
4. 按当前阶段读取相关详细标准，不把无关产品和类型规则全部加载。先给出简短启动回执，无阻断项直接继续。
5. 每阶段生成实际产物与阶段检查报告，修复失败后再推进。发布检查前必须完成所有阶段。
6. 恢复任务时读取 workflow-state.json 并验证文件。已完成产物修改后，invalidate 该阶段及后续阶段，再重新核验。输入或工作流版本变动时新建任务目录，保留原记录；不能直接改哈希使旧检查通过。

运行器路径在本工作流入口中给出。以下以 `$RUNNER` 表示该脚本，`$ROOT` 表示含 workflow.json 的目录：

```bash
python "$RUNNER" --workflow-root "$ROOT" --run-dir ./runs/TASK-001 init --run-id TASK-001 --input task-brief.md --input keywords.xlsx
python "$RUNNER" --workflow-root "$ROOT" --run-dir ./runs/TASK-001 advance --stage research --report records/research-check.json
python "$RUNNER" --workflow-root "$ROOT" --run-dir ./runs/TASK-001 verify
python "$RUNNER" --workflow-root "$ROOT" --run-dir ./runs/TASK-001 invalidate --stage content
```

stage 名称及所需 check ID 以 workflow.json 为准，必须按顺序执行；以上 research 是示例，不能跳过更早的阶段。每个实际输入文件都要用 --input 登记。URL、页面抓取时间、用户范围要求记录于 task-brief.md，页面快照作为阶段证据保存。

阶段报告结构（示例，必须替换为该阶段真实检查）：

```json
{"run_id":"TASK-001","stage":"research","result":"pass","checks":[{"id":"serp-and-intent","result":"pass","reviewer_type":"ai","reviewed_by":"实际执行者","finding":"具体检查结论及适用边界","evidence":["research/serp.csv"]}]}
```

所有路径相对任务目录，证据必须存在且非空。所有状态由命令生成；不得手动编辑状态文件、预填 PASS、复制其他任务记录。运行器管理阶段依赖和文件失效，不代替 SERP 真实性、写作质量或审美判断。

## 检查与状态

- `SCHEMA VALID` 仅证明表结构完整，允许保存尚未解决的问题；不能作为交付通过。
- 最终发布检查必须验证当前状态、实际文件和最终渲染记录。必需项 Fail/Hold/未执行均阻断 Final。已排除的候选 Claim 可留在研究附录，但必须证明未进入生产文案；不能将整项内容标准标 Hold 后照常发布。
- AI 内容/视觉复核与真实人工批准分开记录：reviewer_type 为 ai 或 human，不得冒充人工。默认交付完整且已复核的内容包；human_approval_required 仅在本次要求或既有项目政策指定时启用，保持已有明确人工审批要求。
- 外部发布、上线或发送遵循本次授权范围，内容包检查通过不自动授权外部动作。
- 渲染缺失时保存真实已完成产物，标记 Content Complete — Render QA Blocked，不能标 Final。

## 项目配置

把固定语言、市场、产品和图片规格保存在项目配置中。模块数量、FAQ 数量、步骤数量、Sources 是否配图、关键词优先池和人工批准要求在 task-brief.md 冻结；本次要求可覆盖项目默认值。默认优先池只从同意图且适用的词选择，所有原始词仍须有处置结果。

## 更新兼容性

工作流名称和旧脚本入口保持可用。旧任务缺少新证据时不会自动升级为通过：新建任务、复用有效内容，并重新执行缺少的验证。Python 标准库脚本可以跨系统执行；文档生成/渲染能力仍需环境提供。

启动者使用 assets/task-contract.example.json（页面 Skill）或 templates/task-contract.example.json（文章工作流）整理本次范围。空的配图/模块数组是待填写值；必须根据实际页面和任务补全，不能直接作为完成记录。
