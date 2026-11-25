import importlib.util
import json
from pathlib import Path
from types import ModuleType, SimpleNamespace
from unittest import TestCase, main
from unittest.mock import patch
import sys

KIT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PanelIntegration(TestCase):
    def test_all_delivered_ahc_adapters(self):
        runner = load("runner", KIT / "plugins/dsh-evolve-loop/src/providers/run_evaluator.py")
        result_types = ModuleType("ale_bench.result")
        accepted = SimpleNamespace(value="Accepted")
        result_types.CaseResult = result_types.Result = object
        result_types.JudgeResult = SimpleNamespace(ACCEPTED=accepted)
        session_module = ModuleType("ale_bench_eval.safe_ale_session")
        tasks = sorted((KIT / "tasks/ale_bench").glob("ahc*"))
        self.assertEqual(len(tasks), 10)
        for task in tasks:
            with self.subTest(task=task.name):
                self.assertIs(json.loads((task / "task.json").read_text())["or_seed_panel"], True)
                for goal, sign in (("maximize", 1), ("minimize", -1)):
                    batches, closed = [], []
                    results = [
                        SimpleNamespace(judge_result=accepted, absolute_score=seed,
                                        execution_time=0.1, memory_usage=1024,
                                        error_str="", message="")
                        for seed in range(50)
                    ]

                    def generate(seeds):
                        batches.append(seeds)
                        return seeds

                    def evaluate(seeds, code, **kwargs):
                        self.assertEqual(seeds, list(range(50)))
                        self.assertEqual(kwargs["code_language"], "cpp20")
                        return SimpleNamespace(overall_judge_result=accepted,
                                               overall_absolute_score=9999,
                                               case_results=results)

                    def start(**kwargs):
                        self.assertEqual(kwargs["problem_id"], task.name)
                        return SimpleNamespace(
                            problem=SimpleNamespace(metadata=SimpleNamespace(score_type=goal)),
                            case_gen=generate, case_eval=evaluate, close=lambda: closed.append(True))

                    session_module.start_ale_bench_session = start
                    with patch.dict(sys.modules, {
                        result_types.__name__: result_types,
                        session_module.__name__: session_module,
                    }):
                        adapter = load(task.name, task / "evaluator/evaluator.py")
                        metrics = adapter.evaluate(task / "solution.cpp")
                    self.assertEqual(batches, [list(range(50))])
                    self.assertEqual(closed, [True])
                    self.assertEqual(runner.panel_score(metrics), sign * 24.5)
                    self.assertIsNone(runner.panel_score(dict(metrics, seed_scores=metrics["seed_scores"][:-1])))
                    metrics["seed_scores"][5]["accepted"] = False
                    self.assertIsNone(runner.panel_score(metrics))


if __name__ == "__main__":
    main()
