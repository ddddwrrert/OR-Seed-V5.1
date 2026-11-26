# OR-Seed V5.1 源码文件清单

seed_intelligence/ 下共 144 个 Python 源文件。测试目录共 28 个 test_*.py 文件。

## core/ · 固定 50 Seed

- [__init__.py](../seed_intelligence/core/__init__.py)
- [evaluation_contract.py](../seed_intelligence/core/evaluation_contract.py)
- [evaluation_guard.py](../seed_intelligence/core/evaluation_guard.py)
- [fixed_50_evaluator.py](../seed_intelligence/core/fixed_50_evaluator.py)
- [score_registry.py](../seed_intelligence/core/score_registry.py)
- [seed_manifest.py](../seed_intelligence/core/seed_manifest.py)

## profiler/ · 开放画像

- [__init__.py](../seed_intelligence/profiler/__init__.py)
- [candidate_profiler.py](../seed_intelligence/profiler/candidate_profiler.py)
- [decision_impact.py](../seed_intelligence/profiler/decision_impact.py)
- [difficulty_analyzer.py](../seed_intelligence/profiler/difficulty_analyzer.py)
- [distribution_analyzer.py](../seed_intelligence/profiler/distribution_analyzer.py)
- [feature_registry.py](../seed_intelligence/profiler/feature_registry.py)
- [open_feature_discovery.py](../seed_intelligence/profiler/open_feature_discovery.py)
- [problem_profiler.py](../seed_intelligence/profiler/problem_profiler.py)
- [profile_updater.py](../seed_intelligence/profiler/profile_updater.py)
- [randomness_analyzer.py](../seed_intelligence/profiler/randomness_analyzer.py)
- [response_analyzer.py](../seed_intelligence/profiler/response_analyzer.py)
- [score_scale_analyzer.py](../seed_intelligence/profiler/score_scale_analyzer.py)
- [seed_profiler.py](../seed_intelligence/profiler/seed_profiler.py)
- [seed_semantics.py](../seed_intelligence/profiler/seed_semantics.py)
- [structure_analyzer.py](../seed_intelligence/profiler/structure_analyzer.py)

## strategies/ · 策略目录

- [__init__.py](../seed_intelligence/strategies/__init__.py)
- [builtin/__init__.py](../seed_intelligence/strategies/builtin/__init__.py)
- [builtin/s01_universal.py](../seed_intelligence/strategies/builtin/s01_universal.py)
- [builtin/s02_structure_aware.py](../seed_intelligence/strategies/builtin/s02_structure_aware.py)
- [builtin/s03_difficulty_adaptive.py](../seed_intelligence/strategies/builtin/s03_difficulty_adaptive.py)
- [builtin/s04_algorithm_instance.py](../seed_intelligence/strategies/builtin/s04_algorithm_instance.py)
- [builtin/s05_failure_driven.py](../seed_intelligence/strategies/builtin/s05_failure_driven.py)
- [builtin/s06_randomness_controlled.py](../seed_intelligence/strategies/builtin/s06_randomness_controlled.py)
- [builtin/s07_distribution_aware.py](../seed_intelligence/strategies/builtin/s07_distribution_aware.py)
- [builtin/s08_instance_relationship.py](../seed_intelligence/strategies/builtin/s08_instance_relationship.py)
- [builtin/s09_rare_case.py](../seed_intelligence/strategies/builtin/s09_rare_case.py)
- [builtin/s10_operator_complementarity.py](../seed_intelligence/strategies/builtin/s10_operator_complementarity.py)
- [builtin/s11_search_budget.py](../seed_intelligence/strategies/builtin/s11_search_budget.py)
- [builtin/s12_parameter_adaptive.py](../seed_intelligence/strategies/builtin/s12_parameter_adaptive.py)
- [builtin/s13_landscape_aware.py](../seed_intelligence/strategies/builtin/s13_landscape_aware.py)
- [builtin/s14_constraint_aware.py](../seed_intelligence/strategies/builtin/s14_constraint_aware.py)
- [builtin/s15_generalization_aware.py](../seed_intelligence/strategies/builtin/s15_generalization_aware.py)
- [dynamic/__init__.py](../seed_intelligence/strategies/dynamic/__init__.py)
- [dynamic/strategy_loader.py](../seed_intelligence/strategies/dynamic/strategy_loader.py)
- [dynamic/strategy_serializer.py](../seed_intelligence/strategies/dynamic/strategy_serializer.py)
- [strategy_contract.py](../seed_intelligence/strategies/strategy_contract.py)
- [strategy_generator.py](../seed_intelligence/strategies/strategy_generator.py)
- [strategy_history.py](../seed_intelligence/strategies/strategy_history.py)
- [strategy_matcher.py](../seed_intelligence/strategies/strategy_matcher.py)
- [strategy_registry.py](../seed_intelligence/strategies/strategy_registry.py)
- [strategy_validator.py](../seed_intelligence/strategies/strategy_validator.py)

## composer/ · 选路与工作流

- [__init__.py](../seed_intelligence/composer/__init__.py)
- [adaptive_composer.py](../seed_intelligence/composer/adaptive_composer.py)
- [adaptive_router.py](../seed_intelligence/composer/adaptive_router.py)
- [compatibility_checker.py](../seed_intelligence/composer/compatibility_checker.py)
- [necessity_gate.py](../seed_intelligence/composer/necessity_gate.py)
- [strategy_composer.py](../seed_intelligence/composer/strategy_composer.py)
- [strategy_scheduler.py](../seed_intelligence/composer/strategy_scheduler.py)
- [strategy_value_estimator.py](../seed_intelligence/composer/strategy_value_estimator.py)
- [workflow_executor.py](../seed_intelligence/composer/workflow_executor.py)

## evolution/ · 变异与软指引

- [__init__.py](../seed_intelligence/evolution/__init__.py)
- [candidate_analyzer.py](../seed_intelligence/evolution/candidate_analyzer.py)
- [exploration_dispatcher.py](../seed_intelligence/evolution/exploration_dispatcher.py)
- [mutation_history.py](../seed_intelligence/evolution/mutation_history.py)
- [mutation_plan.py](../seed_intelligence/evolution/mutation_plan.py)
- [original_exploration.py](../seed_intelligence/evolution/original_exploration.py)
- [seed_conditioned_mutation.py](../seed_intelligence/evolution/seed_conditioned_mutation.py)
- [soft_guidance.py](../seed_intelligence/evolution/soft_guidance.py)

## budget/ · 预算与回退

- [__init__.py](../seed_intelligence/budget/__init__.py)
- [budget_controller.py](../seed_intelligence/budget/budget_controller.py)
- [budget_guard.py](../seed_intelligence/budget/budget_guard.py)
- [cost_tracker.py](../seed_intelligence/budget/cost_tracker.py)
- [discovery_budget_guard.py](../seed_intelligence/budget/discovery_budget_guard.py)
- [early_stopping.py](../seed_intelligence/budget/early_stopping.py)
- [fallback_controller.py](../seed_intelligence/budget/fallback_controller.py)
- [marginal_value_estimator.py](../seed_intelligence/budget/marginal_value_estimator.py)
- [opportunity_cost.py](../seed_intelligence/budget/opportunity_cost.py)
- [search_budget_guard.py](../seed_intelligence/budget/search_budget_guard.py)

## feedback/ · 实测反馈

- [__init__.py](../seed_intelligence/feedback/__init__.py)
- [evolution_feedback.py](../seed_intelligence/feedback/evolution_feedback.py)
- [experiment_recorder.py](../seed_intelligence/feedback/experiment_recorder.py)
- [failure_memory.py](../seed_intelligence/feedback/failure_memory.py)
- [online_policy_updater.py](../seed_intelligence/feedback/online_policy_updater.py)
- [per_seed_delta.py](../seed_intelligence/feedback/per_seed_delta.py)
- [strategy_reward.py](../seed_intelligence/feedback/strategy_reward.py)

## reliability/ · M7

- [__init__.py](../seed_intelligence/reliability/__init__.py)
- [counter_evidence.py](../seed_intelligence/reliability/counter_evidence.py)
- [duplicate_hypothesis_detector.py](../seed_intelligence/reliability/duplicate_hypothesis_detector.py)
- [evidence_analyzer.py](../seed_intelligence/reliability/evidence_analyzer.py)
- [evidence_registry.py](../seed_intelligence/reliability/evidence_registry.py)
- [guidance_circuit_breaker.py](../seed_intelligence/reliability/guidance_circuit_breaker.py)
- [guidance_controller.py](../seed_intelligence/reliability/guidance_controller.py)
- [guidance_lifecycle.py](../seed_intelligence/reliability/guidance_lifecycle.py)
- [hypothesis_competition.py](../seed_intelligence/reliability/hypothesis_competition.py)
- [hypothesis_registry.py](../seed_intelligence/reliability/hypothesis_registry.py)
- [original_exploration_guard.py](../seed_intelligence/reliability/original_exploration_guard.py)
- [reliability_updater.py](../seed_intelligence/reliability/reliability_updater.py)

## discovery/ · M9

- [__init__.py](../seed_intelligence/discovery/__init__.py)
- [bottleneck_discovery.py](../seed_intelligence/discovery/bottleneck_discovery.py)
- [discovery_feedback.py](../seed_intelligence/discovery/discovery_feedback.py)
- [discovery_history.py](../seed_intelligence/discovery/discovery_history.py)
- [discovery_trigger.py](../seed_intelligence/discovery/discovery_trigger.py)
- [evidence_collector.py](../seed_intelligence/discovery/evidence_collector.py)
- [execution_analyzer.py](../seed_intelligence/discovery/execution_analyzer.py)
- [hypothesis_validator.py](../seed_intelligence/discovery/hypothesis_validator.py)
- [open_hypothesis_generator.py](../seed_intelligence/discovery/open_hypothesis_generator.py)
- [operator_gain_analyzer.py](../seed_intelligence/discovery/operator_gain_analyzer.py)
- [recorded_evidence.py](../seed_intelligence/discovery/recorded_evidence.py)
- [scoring_behavior_analyzer.py](../seed_intelligence/discovery/scoring_behavior_analyzer.py)
- [search_diagnostics.py](../seed_intelligence/discovery/search_diagnostics.py)
- [search_trace_analyzer.py](../seed_intelligence/discovery/search_trace_analyzer.py)
- [source_code_analyzer.py](../seed_intelligence/discovery/source_code_analyzer.py)
- [unknown_pattern_detector.py](../seed_intelligence/discovery/unknown_pattern_detector.py)

## adapters/ · 通用适配

- [__init__.py](../seed_intelligence/adapters/__init__.py)
- [base_adapter.py](../seed_intelligence/adapters/base_adapter.py)
- [baseline_reader.py](../seed_intelligence/adapters/baseline_reader.py)
- [capability_discovery.py](../seed_intelligence/adapters/capability_discovery.py)
- [generator_reader.py](../seed_intelligence/adapters/generator_reader.py)
- [generic_adapter.py](../seed_intelligence/adapters/generic_adapter.py)
- [instance_reader.py](../seed_intelligence/adapters/instance_reader.py)
- [problem_loader.py](../seed_intelligence/adapters/problem_loader.py)
- [reactive_adapter.py](../seed_intelligence/adapters/reactive_adapter.py)
- [scorer_reader.py](../seed_intelligence/adapters/scorer_reader.py)

## storage/ · 历史与证据

- [__init__.py](../seed_intelligence/storage/__init__.py)
- [budget_store.py](../seed_intelligence/storage/budget_store.py)
- [candidate_store.py](../seed_intelligence/storage/candidate_store.py)
- [evaluation_cache.py](../seed_intelligence/storage/evaluation_cache.py)
- [evidence_store.py](../seed_intelligence/storage/evidence_store.py)
- [experiment_store.py](../seed_intelligence/storage/experiment_store.py)
- [history.py](../seed_intelligence/storage/history.py)
- [hypothesis_store.py](../seed_intelligence/storage/hypothesis_store.py)
- [profile_store.py](../seed_intelligence/storage/profile_store.py)
- [strategy_store.py](../seed_intelligence/storage/strategy_store.py)

## integration/ · Organon 接入

- [__init__.py](../seed_intelligence/integration/__init__.py)
- [evaluation_hook.py](../seed_intelligence/integration/evaluation_hook.py)
- [feedback_hook.py](../seed_intelligence/integration/feedback_hook.py)
- [generation_hook.py](../seed_intelligence/integration/generation_hook.py)
- [initialization_hook.py](../seed_intelligence/integration/initialization_hook.py)
- [integration_guard.py](../seed_intelligence/integration/integration_guard.py)
- [organon_adapter.py](../seed_intelligence/integration/organon_adapter.py)
- [package_plugin.py](../seed_intelligence/integration/package_plugin.py)
- [selection_hook.py](../seed_intelligence/integration/selection_hook.py)
- [strategy_evolution_hook.py](../seed_intelligence/integration/strategy_evolution_hook.py)
- [survival_hook.py](../seed_intelligence/integration/survival_hook.py)

## 统一入口与测试

- [controller.py](../seed_intelligence/controller.py)
- [config.py](../seed_intelligence/config.py)
- [contracts.py](../seed_intelligence/contracts.py)

- [end_to_end/test_ahc001.py](../tests/seed_intelligence/end_to_end/test_ahc001.py)
- [end_to_end/test_full_evolution.py](../tests/seed_intelligence/end_to_end/test_full_evolution.py)
- [end_to_end/test_unseen_problem.py](../tests/seed_intelligence/end_to_end/test_unseen_problem.py)
- [integration/test_feedback_to_strategy.py](../tests/seed_intelligence/integration/test_feedback_to_strategy.py)
- [integration/test_guidance_to_mutation.py](../tests/seed_intelligence/integration/test_guidance_to_mutation.py)
- [integration/test_m1_m9_integration.py](../tests/seed_intelligence/integration/test_m1_m9_integration.py)
- [integration/test_m9_m7_integration.py](../tests/seed_intelligence/integration/test_m9_m7_integration.py)
- [integration/test_organon_main_loop.py](../tests/seed_intelligence/integration/test_organon_main_loop.py)
- [integration/test_original_exploration.py](../tests/seed_intelligence/integration/test_original_exploration.py)
- [scenarios/test_budget_exhaustion.py](../tests/seed_intelligence/scenarios/test_budget_exhaustion.py)
- [scenarios/test_heterogeneous_seeds.py](../tests/seed_intelligence/scenarios/test_heterogeneous_seeds.py)
- [scenarios/test_homogeneous_seeds.py](../tests/seed_intelligence/scenarios/test_homogeneous_seeds.py)
- [scenarios/test_original_fallback.py](../tests/seed_intelligence/scenarios/test_original_fallback.py)
- [scenarios/test_scale_not_difficulty.py](../tests/seed_intelligence/scenarios/test_scale_not_difficulty.py)
- [scenarios/test_unknown_bottleneck.py](../tests/seed_intelligence/scenarios/test_unknown_bottleneck.py)
- [scenarios/test_unknown_seed_pattern.py](../tests/seed_intelligence/scenarios/test_unknown_seed_pattern.py)
- [scenarios/test_wrong_guidance.py](../tests/seed_intelligence/scenarios/test_wrong_guidance.py)
- [test_controller.py](../tests/seed_intelligence/test_controller.py)
- [unit/test_bottleneck_discovery.py](../tests/seed_intelligence/unit/test_bottleneck_discovery.py)
- [unit/test_budget_guard.py](../tests/seed_intelligence/unit/test_budget_guard.py)
- [unit/test_counter_evidence.py](../tests/seed_intelligence/unit/test_counter_evidence.py)
- [unit/test_dynamic_strategy_registry.py](../tests/seed_intelligence/unit/test_dynamic_strategy_registry.py)
- [unit/test_fixed_50_contract.py](../tests/seed_intelligence/unit/test_fixed_50_contract.py)
- [unit/test_guidance_circuit_breaker.py](../tests/seed_intelligence/unit/test_guidance_circuit_breaker.py)
- [unit/test_guidance_reliability.py](../tests/seed_intelligence/unit/test_guidance_reliability.py)
- [unit/test_open_feature_discovery.py](../tests/seed_intelligence/unit/test_open_feature_discovery.py)
- [unit/test_seed_profiler.py](../tests/seed_intelligence/unit/test_seed_profiler.py)
- [unit/test_strategy_composer.py](../tests/seed_intelligence/unit/test_strategy_composer.py)
