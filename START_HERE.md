# Article Review — 唯一启动入口

当前执行版本由 `workflow.json` 声明（3.8.0）；仓库名称中的 v3.1 保持兼容。

1. 读取 `EXECUTION.md` 与 `workflow.json` 列出的 bootstrap_files；README/CHANGELOG 用于说明，不是另一套执行入口。
2. 用户提供原文 DOCX 与关键词 XLSX。市场语言、产品目标和已明确的人工批准要求从项目配置继承；只有影响本次决策的缺项才询问。
3. 默认 Optimization Mode。只有明确要求重写才切换 Rewrite Mode；参考文章只能作为质量参照。
4. 用 `scripts/workflow_state.py` 初始化独立任务，记录实际加载文件和输入哈希。各阶段开始前读取对应模板，按 workflow.json 顺序生成产物、运行检查并推进状态。
5. 先做资产保留审计，再做 SERP/产品事实、结构、关键词、配图、编辑和最终文件核验。保持真实的 core-conversion 产品路线，不因升级删除有效转化资产。
6. 配图默认 NAMED_SECTIONS，按读者任务确定并写入契约。用户明确要求每个 H2 配图时才使用 ALL_H2，包括 Sources；不暗中减少已指定范围。
7. 最终验收运行 `python scripts/review_preflight.py RUN_DIR/manifest.json`。将输出保存于发布目录外，避免检查报告自身造成清单循环。manifest 的所有相对路径以 manifest 所在目录为基准。
8. 干净版与高亮版均要有各自的渲染报告，匹配最终 DOCX 哈希和实际页面图片哈希。AI 复核如实记录为 ai；人工批准仅在项目/本次要求指定时启用。

最简调用：`使用 SEO Article Review Workflow，对附件原文和关键词做完整优化，按项目默认值执行。`
启动回执只需列明实际版本、模式、输入 Sheet、产品目标、交付物和能力缺口；无阻断项直接继续。
