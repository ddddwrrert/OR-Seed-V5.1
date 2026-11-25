"""Final score of a finished ALE-Bench run: the private evaluation of its best candidate.

    <benchmark python> final_eval.py <task folder>

As with EvoX, the private evaluation (private_eval.py, next to this script, on the
hidden test cases) runs once the search is over, on the best candidate in
run/population.jsonl, chosen as the evolve loop chooses it. The search never sees these
scores. Our #EVOLVE_START/#EVOLVE_END lines are removed from the program first.
The output of private_eval.py is saved to run/final.txt.

Only ALE-Bench tasks have a separate final evaluation; for the others the
recorded fitness is the final score.
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

MARKERS = {b"#EVOLVE_START", b"#EVOLVE_END"}


def merit(fitness: float) -> float:
    """As the evolve loop ranks candidates (merit() in population.js): a failed evaluation (0)
    counts as 0, and a minimize task's scores, which its evaluator makes negative, as 1/|fitness|."""
    return fitness if fitness > 0 else -1 / fitness if fitness < 0 else 0.0


def export_panel(task, settings, rows):
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(Path(__file__).resolve().parent /
                          "plugins/dsh-evolve-loop/src/providers"))
    from run_evaluator import panel_score

    run = task / "run"
    ranked = []
    for row in rows:
        if row.get("panel") is not True or row["fitness"] is None:
            continue
        result = json.loads((run / "evals" / f"{row['id']}.json").read_text(encoding="utf-8"))
        metrics = result["metrics"]
        fitness = panel_score(metrics)
        if fitness is None or fitness != row["fitness"] or fitness != result["fitness"]:
            raise SystemExit(f'Invalid panel evidence for {row["id"]}')
        ranked.append((fitness, row["id"], metrics["score_direction"]))
    if not ranked:
        raise SystemExit("No candidate has a complete, accepted 50-seed evaluation.")
    fitness, candidate, direction = max(ranked, key=lambda row: row[0])
    program = run / "candidates" / candidate / settings["program"]
    code = b"\n".join(line for line in program.read_bytes().split(b"\n") if line.strip() not in MARKERS)
    (run / f"final-{program.name}").write_bytes(code)
    report = f"best candidate: {candidate}\n50-seed arithmetic mean: {fitness * direction}\n"
    (run / "final.txt").write_text(report, encoding="utf-8")
    print(report, end="")


def main() -> None:
    task = Path(sys.argv[1]).resolve()
    private_eval = Path(__file__).resolve().parent / "private_eval.py"
    settings = json.loads((task / "task.json").read_text(encoding="utf-8"))
    lines = (task / "run" / "population.jsonl").read_text(encoding="utf-8").splitlines()
    rows = [json.loads(line) for line in lines if line.strip()]
    if settings.get("or_seed_panel") is True:
        export_panel(task, settings, rows)
        return
    best = max(rows, key=lambda row: merit(row["fitness"]))
    program = task / "run" / "candidates" / best["id"] / settings["program"]
    code = b"\n".join(line for line in program.read_bytes().split(b"\n") if line.strip() not in MARKERS)

    with tempfile.TemporaryDirectory() as scratch:
        plain = Path(scratch) / program.name
        plain.write_bytes(code)
        completed = subprocess.run(
            [sys.executable, str(private_eval), "--program-path", str(plain), "--problem-id", task.name],
            cwd=private_eval.parent, stdout=subprocess.PIPE, text=True)

    report = f"best candidate: {best['id']} (fitness {best['fitness']})\n{completed.stdout}"
    (task / "run" / "final.txt").write_text(report, encoding="utf-8")
    print(report)
    sys.exit(completed.returncode)


if __name__ == "__main__":
    main()
