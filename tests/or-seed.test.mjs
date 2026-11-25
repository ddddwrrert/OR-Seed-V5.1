import assert from 'node:assert/strict'
import { execFile, execFileSync } from 'node:child_process'
import { mkdtemp, mkdir, readFile, rm, writeFile } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { fileURLToPath } from 'node:url'
import test from 'node:test'
import { Evolve } from '../plugins/dsh-evolve-loop/src/evolve.js'
import { discoveryFor, guidanceFor, observationFor, workerHypothesis } from '../plugins/dsh-evolve-loop/src/guidance.js'
import { filesOf } from '../plugins/dsh-evolve-loop/src/files.js'

const hypothesis = {
  id: 'new-mechanism', direction: 'Improve the fixture algorithm.',
  evidence: 'Observed repeated search work.', counterevidence: 'Reducing work can damage quality.',
}
const openReport = {
  ...hypothesis, reference: 'c000001', expectedGain: 2, cost: 'One candidate, bounded loop change',
  feature: { name: 'branch saturation', observation: 'Heavy inputs repeat a saturated branch.', seeds: [40, 41, 42] },
}
const config = { hypotheses: [hypothesis], maxCandidates: 3 }
const kit = fileURLToPath(new URL('../', import.meta.url))

async function temporary(t) {
  const directory = await mkdtemp(join(tmpdir(), 'or-seed-'))
  t.after(() => rm(directory, { recursive: true, force: true }))
  return directory
}

test('M7 uses alternatives, updates reliability and archives failures', async t => {
  const files = filesOf(await temporary(t))
  const budget = { used: 3, max: 12, remaining: 9 }
  const parent = { id: 'c000000', fitness: 100 }
  const first = await guidanceFor(files, [], parent, budget, config)
  assert.equal(first.state, 'proposed')
  assert.match(first.instruction, /may ignore/)
  assert.match(first.instruction, /Counterevidence/)
  assert.equal(await guidanceFor(files, [], parent, { ...budget, used: 4 }, config), undefined)
  const success = { guidance: observationFor(first, 100, 110) }
  const candidate = await guidanceFor(files, [success, success], parent, budget, config)
  assert.equal(candidate.state, 'validated')
  assert.equal(candidate.reliability, 0.75)
  const failure = { guidance: observationFor(first, 100, 90) }
  assert.equal(await guidanceFor(files, [failure, failure], parent, budget, config), undefined)
  const alternate = { ...hypothesis, id: 'alternate' }
  const next = await guidanceFor(files, [failure, failure], parent, budget,
    { ...config, hypotheses: [hypothesis, alternate] })
  assert.equal(next.id, 'alternate')
  assert.equal(observationFor(next, 100, null).outcome, 'invalid')
})

test('main loop, C++ compilation, 50-seed subprocess scoring, resume and final export', async t => {
  const task = await temporary(t)
  await mkdir(join(task, 'evaluator'))
  await writeFile(join(task, 'task.json'), JSON.stringify({
    program: 'solution.cpp', timeout: 60, max_retries: 0, or_seed_panel: true, guidance: { maxCandidates: 2, minExpectedGain: 1 },
  }))
  const program = offset => `#include <iostream>
int main() { int seed; std::cin >> seed; std::cout << (seed + ${offset} + (${offset} == 4 ? (seed < 25 ? -10 : 10) : 0)); }
`
  await writeFile(join(task, 'solution.cpp'), program(1))
  await writeFile(join(task, 'evaluator', 'evaluator.py'), `
import subprocess
from pathlib import Path
def evaluate(path):
    executable = str(Path(path).with_suffix('.exe'))
    subprocess.run(['g++', '-static', path, '-o', executable], check=True)
    scores = [int(subprocess.check_output([executable], input=str(seed).encode()))
              for seed in range(50)]
    rows = [dict(seed=i, score=score, accepted=True) for i, score in enumerate(scores)]
    if scores[0] == 20:
        rows[49]['seed'] = 48
    return dict(seed_scores=rows, score_direction=1, combined_score=99999)
`)
  const prompts = []
  const offsets = [4, 8, 20, 30, 6, 7]
  const evolve = new Evolve({
    get: () => ({
      resolveExecutable: async () => process.env.OR_SEED_PYTHON ?? 'python',
      spawn: ({ argv, cwd, env, signal }) => {
        const streams = {
          stdout: { readFrom: () => ({ text: '' }) },
          stderr: { readFrom: () => ({ text: '' }) },
        }
        const done = new Promise(resolve => {
          execFile(argv[0], argv.slice(1), { cwd, env: { ...process.env, ...env }, signal },
            (error, stdout, stderr) => {
              streams.stdout.readFrom = () => ({ text: stdout })
              streams.stderr.readFrom = () => ({ text: stderr })
              if (stderr) console.error(stderr)
              resolve({ exitCode: error ? 1 : 0 })
            })
        })
        return { done, collected: streams }
      },
    }),
    subagents: {
      getProvider: () => ({}),
      start: async (_, request) => {
        prompts.push(request.prompt[0].text)
        await writeFile(join(request.confine.root, 'solution.cpp'), program(offsets.shift()))
        const output = prompts.length === 2
          ? [{ type: 'text', text: 'OR_SEED_HYPOTHESIS ' + JSON.stringify(openReport) }] : []
        return { result: Promise.resolve({ output }), dispose() {} }
      },
    },
  })
  const exec = { agent: { session: { header: { cwd: task } } } }
  const restoreSelection = evolve.register('select', { select: () => 'c000000' })
  const first = await evolve.run({ maxBudget: 6, candidates: 2 }, exec)
  assert.equal(first.remaining, 4)
  const result = await evolve.run({ maxBudget: 6 }, exec)
  restoreSelection()
  assert.deepEqual(result, { best_id: 'c000004', best_fitness: 54.5, remaining: 0 })
  assert.deepEqual(prompts.map(prompt => prompt.includes('Optional hypothesis')), [false, false, false, true, false, false])
  assert.deepEqual(prompts.map(prompt => prompt.includes('Optional bottleneck discovery')), [false, true, false, false, false, false])
  const pop = (await readFile(join(task, 'run', 'population.jsonl'), 'utf8')).trim().split('\n').map(JSON.parse)
  assert.equal(pop[2].discovery.feature.name, 'branch saturation')
  assert.equal(pop[3].fitness, null)
  assert.equal(pop[3].survival, 'no')
  assert.equal(pop[4].guidance.outcome, 'improved')
  assert.equal(pop[4].guidance.delta, 29)
  const allocations = await readFile(join(task, 'run', 'evals', 'c000004.json'), 'utf8')
  assert.equal(JSON.parse(allocations).metrics.seed_scores.length, 50)
  const manifest = JSON.parse(await readFile(join(task, 'run', 'seed_intelligence', 'seed_manifest.json'), 'utf8'))
  assert.deepEqual(manifest.seeds, Array.from({ length: 50 }, (_, seed) => seed))
  assert.equal(manifest.aggregation, 'arithmetic_mean')
  assert.equal(pop[4].delta, 29)
  const report = execFileSync(process.env.OR_SEED_PYTHON ?? 'python',
    [join(kit, 'final_eval.py'), task], { encoding: 'utf8' })
  assert.match(report, /50-seed arithmetic mean: 54.5/)
  assert.match(await readFile(join(task, 'run', 'final-solution.cpp'), 'utf8'), /seed \+ 30/)
})



test('M9 checks whole-panel upside and M1 verifies open feature observations', async t => {
  const files = filesOf(await temporary(t))
  const panel = scores => ({
    fitness: 100,
    metrics: { score_direction: 1, seed_scores: scores.map((score, seed) => ({ seed, score, accepted: true })) },
  })
  await files.write('evals/c000000.json', JSON.stringify(panel(Array(50).fill(100))))
  await files.write('evals/c000001.json', JSON.stringify(panel(
    Array.from({ length: 50 }, (_, seed) => seed < 25 ? 90 : 110),
  )))
  const parent = { id: 'c000000', fitness: 100 }
  const historical = { id: 'c000001', parent: parent.id, fitness: 100 }
  const budget = { used: 3, max: 18, remaining: 15 }
  const rows = [historical]
  assert.equal(await guidanceFor(files, rows, parent, budget, { minExpectedGain: 5 }), undefined)
  const candidate = await guidanceFor(files, rows, parent, budget)
  assert.match(candidate.instruction, /recoverable mean at most 5/)
  const proposal = workerHypothesis('OR_SEED_HYPOTHESIS ' + JSON.stringify(openReport))
  assert.equal(await discoveryFor(candidate, { ...proposal, expectedGain: 6 }, parent.id, {}, 100), undefined)
  assert.equal(await discoveryFor(candidate, { ...proposal, feature: { ...proposal.feature, seeds: [0] } }, parent.id, {}, 100), undefined)
  assert.equal(await discoveryFor(candidate, proposal, parent.id, {}, null), undefined)
  const discovery = await discoveryFor(candidate, proposal, parent.id, {}, 100)
  assert.equal(discovery.feature.observedDelta, -10)
  const afterInspection = [...rows, { parent: parent.id, fitness: 100, discoveryAttempt: true, discovery }]
  assert.equal((await guidanceFor(files, afterInspection, parent, budget)).id, hypothesis.id)
  assert.equal(await guidanceFor(files, [{ ...historical, discoveryAttempt: true }], parent, budget), undefined)
  assert.equal(workerHypothesis('OR_SEED_HYPOTHESIS {}'), undefined)
})

