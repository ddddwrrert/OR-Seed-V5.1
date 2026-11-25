# Organon 接入

```text
providers/loop.js
  → guidance.js（读取本任务已有评测）
  → seed_intelligence/controller.py / plan
  → M5 预算 → M1/M8 画像与 M9 发现 → M2/M3 → M7 → M4
  → evolve.mutate() / 原版 Worker
  → evolve.evaluate() → run_evaluator.py → M0
  → controller.py / review → M6 与 M9 假设审查
  → population.jsonl → 下一轮 M7
```

默认主循环保留对 select、mutate、evaluate 和 survive 的调用位置，运行器的策略注册与切换接口继续可用。完全替换默认循环的策略需要主动调用指导接入。寻不到合格指引或专项预算用尽时，沿用原始生成调用。正式评分合同同时由搜索和导出复用。

## 本次修改

- 新增 seed_intelligence/ 源码、configs/seed_intelligence.yaml、tests/seed_intelligence/test_controller.py 和 docs/ 下三份文档。
- 修改 plugins/dsh-evolve-loop/src/guidance.js、providers/loop.js、providers/evaluate.js、providers/run_evaluator.py，接入 Python 控制器、正式评分合同和任务级记录。
- 原有 seed-profile.js 与 bottleneck-discovery.js 的逻辑并入对应 Python 模块。
- 更新 tests/or-seed.test.mjs、OR-SEED-V5.1.md 和 dist/dsh-evolve-loop-0.1.0.tgz。

修改 Python 源码或默认配置后，在项目根目录重新构建安装包：

```bash
python -B seed_intelligence/integration/package_plugin.py
```
