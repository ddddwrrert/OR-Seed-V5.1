# OR-Seed V5.1 · Seed Intelligence

工程沿用 Organon 的 DSH 插件和 task 副本。新增的 Python 源码集中在工程根目录的 seed_intelligence/，安装包包含同一份控制器。

[实际全部源码和测试目录](SOURCE_TREE.md)



- M0 校验原有 Seed 0–49、顺序、逐 Seed 通过状态和整数原始分。内部用于排名的符号沿用题目优化方向。最终导出报告完整原始算术平均。
- M1/M8 从历史对照核验开放特征，得分范围单独记录。有分值量纲差异本身不足以启动发现。
- M2 提供 S01–S15 独立模块。对应证据达到条件时才生成候选假设，另可注册开放假设。M3 依据实测结果选择策略，支持双向兼容且已验证的自动双策略组合，也支持显式配置 2–6 步有序工作流。
- M4 通过现有 Worker 派发可忽略的软指引。M5 按候选预算限额并保留原版自主探索。M6 记录实际收益。M7 按有效试验的改善情况、均值与连续失败更新状态。
- M9 复用完整评分、历史对照和 Worker 正在阅读的源码。新方向可超出 S01–S15。通用适配器识别数据能力。当前 M9 的自动触发依据是可复用的逐 Seed 对照，已有轨迹、算子收益、运行时间和代理分可生成证据摘要；字段缺失时自动跳过。
- 每个任务副本独立生成 run/seed_intelligence/seed_manifest.json。候选画像保存在 run/evals/，指引和发现分配写入 run/guidance/，策略与反馈历史写入 run/population.jsonl。运行其他题目时按需生成对应的记录。

安装、运行和正式成绩导出见上级目录的 OR-SEED-V5.1.md。默认设置在 configs/seed_intelligence.yaml，采用 YAML 兼容的 JSON 写法以使用 Python 标准库。task.json 的 guidance 可覆盖预算、收益阈值、M9 开关和假设列表。

逐项对照见 [源码核对](IMPLEMENTATION_AUDIT.md)。
