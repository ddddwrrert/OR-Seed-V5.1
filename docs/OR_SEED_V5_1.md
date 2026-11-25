# OR-Seed V5.1 · Seed Intelligence

工程沿用 Organon 的 DSH 插件和 task 副本。新增的 Python 源码集中在工程根目录的 seed_intelligence/，安装包包含同一份控制器。

```text
OR-Seed-V5.1/
├── seed_intelligence/
│   ├── __init__.py
│   ├── controller.py
│   ├── config.py
│   ├── contracts.py
│   ├── core/evaluation_contract.py
│   ├── profiler/seed_profiler.py
│   ├── strategies/strategy_registry.py
│   ├── composer/adaptive_composer.py
│   ├── evolution/mutation_plan.py
│   ├── budget/budget_guard.py
│   ├── feedback/evolution_feedback.py
│   ├── reliability/guidance_controller.py
│   ├── discovery/bottleneck_discovery.py
│   ├── adapters/generic_adapter.py
│   ├── storage/history.py
│   └── integration/
│       ├── organon_adapter.py
│       └── package_plugin.py
├── configs/seed_intelligence.yaml
├── tests/
│   ├── seed_intelligence/test_controller.py
│   ├── or-seed.test.mjs
│   └── test_ahc_panel.py
└── docs/
    ├── OR_SEED_V5_1.md
    ├── INTEGRATION.md
    └── ACCEPTANCE_REPORT.md
```

- M0 校验原有 Seed 0–49、顺序、逐 Seed 通过状态和整数原始分。内部用于排名的符号沿用题目优化方向。最终导出报告完整原始算术平均。
- M1/M8 从历史对照核验开放特征，得分范围单独记录。有分值量纲差异本身不足以启动发现。
- M2 提供 S01–S15 可选模板和开放假设注册。模板只有配置了当前任务的证据与反证才成为候选策略。M3 依据有效实验收益和可靠性选择策略，两条明确互相兼容且各自验证过的策略可作为独立组合验证。
- M4 通过现有 Worker 派发可忽略的软指引。M5 按候选预算限额并保留原版自主探索。M6 记录实际收益。M7 按有效试验的改善情况、均值与连续失败更新状态。
- M9 复用完整评分、历史对照和 Worker 正在阅读的源码。新方向可超出 S01–S15。通用适配器识别数据能力。当前 M9 的自动触发依据是可复用的逐 Seed 对照，轨迹与算子收益只登记可用性，尚无独立解析器。
- 每个任务副本独立生成 run/seed_intelligence/seed_manifest.json。候选画像保存在 run/evals/，指引和发现分配写入 run/guidance/，策略与反馈历史写入 run/population.jsonl。运行其他题目时按需生成对应的记录。

安装、运行和正式成绩导出见上级目录的 OR-SEED-V5.1.md。默认设置在 configs/seed_intelligence.yaml，采用 YAML 兼容的 JSON 写法以使用 Python 标准库。task.json 的 guidance 可覆盖预算、收益阈值、M9 开关和假设列表。
