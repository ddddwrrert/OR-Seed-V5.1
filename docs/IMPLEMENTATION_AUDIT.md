# OR-Seed V5.1 逐项源码核对

以附件中的功能为核对单位。目录中的建议文件名允许按照现有工程合并。下表每项注明实际实现及边界。

| 模块 | 实际运行路径与行为 | 当前覆盖范围 |
|---|---|---|
| M0 | Python 评测器 → core/evaluation_contract.py → 原候选记录、最终导出 | 原有 Seed 0–49，有序完整结果的原始算术平均。拒绝缺项、重复及未通过结果 |
| M1/M8 | controller → profiler/seed_profiler.py | 从两份完整面板比较逐 Seed 响应，记录得分范围，通过分组退化核验开放特征。已增加记录列、结构组、耗时难度和历史重复差异分析。缺少对应元数据时跳过 |
| M2 | controller → strategies/strategy_registry.py | S01–S15 各自定义证据匹配与变异方向，允许库外假设。匹配案例均由现有 Worker 实现一份完整候选 |
| M3 | controller → composer/adaptive_composer.py | 依历史可靠性与实测收益排序。验证后并配置双向兼容的两个策略可独立组合试验。显式工作流支持 2–6 个经验证且两两兼容的有序步骤，在同一候选内执行 |
| M4 | controller → evolution/mutation_plan.py → guidance.js → Organon Worker | 可选的修改方向和证据。无指引时保留原 Worker 调用 |
| M5 | guidance.js 和 budget/budget_guard.py → Organon 候选预算 | 限制专项候选数，交错保留原版尝试。无价值或用完后继续原始搜索 |
| M6 | controller.assess → feedback/evolution_feedback.py → population.jsonl | 按正式评分取向记录父子真实收益与失败。尚无跨题经验迁移 |
| M7 | composer → reliability/guidance_controller.py → 后续候选 | 有效实验更新可靠性，连续失败熔断，数学上的同一方向经大小写与空白归一后共用历史。复杂语义改写仍可能产生新方向 ID |
| M9 | discovery/bottleneck_discovery.py → recorded_evidence.py → Worker → M7 | 复用逐 Seed 得分和耗时，按需汇总已有正式评分轨迹、算子收益和代理分差异。只有已有记录才使用。Worker 阅读当前源码并提出库外方向。缺少成对正式评分时不会仅凭遥测启动 |
| 通用适配 | adapters/generic_adapter.py 和已有评测接口 | 已接入固定面板协议的题目按数据能力运行。新增题目需对应评测器。程序源码由现有 Worker 读取 |
| 存储 | storage/history.py 和 Organon 文件接口 | 每个任务副本独立保存 manifest、候选、评测、证据和实验历史。旧发现持续引用原证据。尚无全局共享策略数据库 |
| 集成 | providers/loop.js → guidance.js → controller.py | 默认主循环调用实际控制器。注册与切换搜索策略继续保留。完全替换默认循环时，自定义循环需要接入这些调用 |

## 实际修改与复验

- 完整新增文件见 [源码清单](SOURCE_TREE.md)。运行入口与端到端验收方式保持兼容。
- 修改 Python 控制器、发现审查、策略注册、历史读取、JavaScript 指引连接、10 道 AHC 适配器及测试。重建插件安装包。
- 项目根目录运行 `python -B verify.py`，依次执行控制器、10 题评分入口和真实 C++ 候选的本地端到端测试。需要 Python、Node 和支持静态链接的 g++。
- 正式环境在满足 Organon 依赖的 Linux 主机执行 `bash setup.sh`，按工程根目录 OR-SEED-V5.1.md 启动 Evolve Mode。可用 `python final_eval.py <任务目录>` 导出正式成绩。
- AHC001 未随当前工程交付。真实 Docker 判题与在线模型运行尚未在本机通过。
