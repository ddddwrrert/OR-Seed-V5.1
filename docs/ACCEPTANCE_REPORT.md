# 验收报告

在工程根目录可直接运行 `python -B verify.py`，也可逐项运行：

```bash
python -B -m unittest discover -s tests/seed_intelligence -v
python -B tests/test_ahc_panel.py
node --test tests/or-seed.test.mjs
```

| 验证 | 结果 | 覆盖 |
|---|---|---|
| Python 控制器 | 33 项通过，2 项跳过 | 固定面板、量纲与难度区分、15 个独立匹配器、开放策略注册、多阶段工作流、预算回退。跳过 AHC001 实题与重复 Node 包装入口 |
| Python 评测集成 | 1 项通过，含 10 道交付 AHC 题 | 逐个调用交付的评测入口，核对固定 50 Seed、最大化与最小化方向、异常面板拒绝。判题服务使用替身 |
| Node 集成及本地端到端 | 3 项通过 | M7 生命周期、M9 与 M1、默认 Organon 主循环、真实 C++ 编译和运行、在线收集假设、后续试验、续跑与导出。Worker 为确定性夹具 |
| 安装包 | 控制器冒烟通过 | 从重新打包的压缩档解包，经 JavaScript 桥实际启动其中的 Python 控制器 |
| Organon 原版 | 工作树无变更 | 原版仓库 Git 状态 |

## 尚待真实环境验收

本机 Docker Linux 引擎不可连接。真实 ALE-Bench 判题和在线模型联跑仍待验证。现有任务集未包含 AHC001，所以同质或量纲差异场景由确定性夹具覆盖。当前版本以任务副本内的 run/ 保存历史，跨题策略迁移尚未交付。既有轨迹与算子记录的读取及证据摘要已增加固定夹具测试。

