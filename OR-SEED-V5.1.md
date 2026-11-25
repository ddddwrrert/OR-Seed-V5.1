# OR-Seed V5.1

[源码目录与模块说明](docs/OR_SEED_V5_1.md) · [调用链与修改清单](docs/INTEGRATION.md) · [验收报告](docs/ACCEPTANCE_REPORT.md)

本工程从本地 Organon 原版独立复制。原版 10 个 AHC 任务使用 Seed 0–49。请使用 V5.1 下的任务新副本启动搜索，旧版 run 记录缺少完整逐 Seed 证据。

## 安装与运行

在满足原版 README 中依赖条件的 Linux 环境执行以下命令。默认使用独立的 Harness 克隆和配置目录。发布包已包含本次修改。

```bash
bash setup.sh
cd ~/deepseek-harness-or-seed-v5.1
PATH="$HOME/.dsh-or-seed-v5.1/benchmarks/venv/bin:$PATH" DSH_HOME="$HOME/.dsh-or-seed-v5.1" pnpm dsh web
```

在 Evolve Mode 打开 V5.1 中某个 AHC 任务的独立副本。按原版方法调用 evolve_run，例如 max_budget=30，candidates=5。保留 evolve_define、evolve_activate 及原有搜索策略扩展接口。M7 由内置循环调度。完全替换内置循环的自定义策略须自行接入 M7。带 or_seed_panel 标识的任务由评分服务固定调用内置评测器。

在工程根目录运行 `python final_eval.py /path/to/task-copy`。正式分从已完成且全部通过的 Seed 0–49 原始分数计算算术平均，导出到 run/final.txt 和 run/final-solution.cpp。内部按题目优化方向比较均值。缺失、重复、失败或顺序异常的面板没有正式分。导出时不另跑私有面板。

## M1、M7 和 M9

- M9 从同一父方案近期的有效挑战者以及父方案自身的变异前版本中搜索可复用的完整逐 Seed 证据。只有同时出现互补收益和可挽回损失、且损失折算到完整面板后高于阈值，才会在已有候选的 Worker 指令中邀请做一次可选发现。Worker 可根据正在阅读的源码报告任意算法机制或题目特征。发现阶段复用既有候选记录与源码阅读。
- M1 按名称记录开放特征。Worker 指出一个 Seed 子群时，M1 核验子群编号与历史面板对应，并检查该组确实出现更大退化。算法级假设也可以直接引用同一份历史对照。子群差异用于筛选假设，正式评分仍用完整均值。
- M7 要求新发现引用同一父方案的有效对照，给出反证和单次尝试的成本说明，并将预期收益限制在观测到的可挽回上限内。实际验证由后续正常候选的完整 50 Seed 结果完成。试验记录包含真实收益、预测和参考候选。可信度根据有效试验的改善情况更新，同时记录平均实际收益。两次连续无收益或无效的方向停止分配。候选收益衡量收到建议后的结果，证据强度会受 Worker 自主选择影响。
- 可通过 task.json 的 guidance.hypotheses 显式提供任意数量的竞争假设。M9 可用 guidance.discovery=false 关闭。guidance.minExpectedGain 控制何时值得研究，单位为 50 Seed 均分，默认要求正收益。发现和指引共用 guidance.maxCandidates 上限，默认取总候选预算三分之一向下取整，上限是总预算的一半。每个父方案至多安排一次可选发现。发现未产出合格假设、方向归档或专项预算耗尽后，继续原始探索。
- run/guidance/ 保存候选专项分配，run/population.jsonl 保存开放特征和指引试验结果，run/evals/ 保存正式逐 Seed 证据。

## 验证

在工程根目录运行：

```bash
node --test tests/or-seed.test.mjs
python -B tests/test_ahc_panel.py
```

Node 测试覆盖 M7 更新和归档、M9 机会筛选和 M1 特征审查，以及带实际 C++ 编译、发现、指引验证、预算回退和导出的端到端流程。Python 集成测试用替身判题服务核对全部 10 个 AHC 入口。2026-11-25 本地复验，Node 3 项及 Python 1 项通过。需要 Node 22+、Python 和支持静态链接的 g++。必要时用 OR_SEED_PYTHON 指定 Python。测试使用确定性 Worker 和 C++ 评分夹具，可在没有模型账户或 Docker 的机器上验证候选分配、评测子进程和导出。真实 AHC 验证需要已配置的 Linux Docker 判题环境。

