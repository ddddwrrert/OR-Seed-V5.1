/**
 * Default search loop provider: coordinates baseline evaluation, iterative variation,
 * scoring, recording, and survival. Returns { best_id, best_fitness, remaining }.
 *
 * @module dsh-evolve-loop/providers/loop
 */

import { readFile } from 'node:fs/promises'
import { join } from 'node:path'
import { assessGuidance, guidanceFor, observationFor } from '../guidance.js'
import { defaultInstruction } from './mutate.js'
import { alive, merit } from '../population.js'

export const name = 'evolve-loop'

/**
 * Execute the evolutionary search loop.
 * @param {object} args - loop arguments (maxBudget, maxPopulation, k, candidates).
 * @param {object} evolve - the evolve service.
 * @returns {Promise<{ best_id: string, best_fitness: number, remaining: number }>}
 */
export async function run(args, evolve) {
  const { maxPopulation, candidates } = await evolve.context()
  const population = evolve.population()
  const runState = evolve.currentRun()

  const settings = runState.task
    ? JSON.parse(await readFile(join(runState.task, 'task.json'), 'utf8')) : {}
  const panel = settings.or_seed_panel === true

  // 1. Initialize baseline c000000 if population is empty
  let rows = await population.rows()
  if (rows.length === 0) {
    const base = await evolve.copyTask()
    const baseFitness = await evolve.evaluate(base)
    await population.append({
      id: base.id,
      parent: null,
      fitness: baseFitness,
      ...(panel ? { panel: true } : {}),
      survival: 'yes',
    })
    rows = await population.rows()
  }

  if (panel && rows.some(row => row.panel !== true)) {
    throw new Error('Use a fresh task copy: existing population is outside the OR-Seed scoring protocol')
  }

  // 2. Search iterations
  const limit = candidates ?? Infinity
  let created = 0

  while ((await evolve.context()).budget.remaining > 0 && created < limit) {
    runState.signal.throwIfAborted()

    // Selection
    const parentId = await evolve.select(population)

    // Mutation & Allocation
    const parent = rows.find(row => row.id === parentId)
    let guidance
    if (panel && parent) {
      try {
        guidance = await guidanceFor(evolve.files, rows, parent, (await evolve.context()).budget,
          settings.guidance, runState.signal)
      } catch (error) {
        runState.signal.throwIfAborted()
        await evolve.files.write('guidance-error.json', JSON.stringify({ message: String(error) }))
      }
    }
    const options = { parent: parentId }
    if (guidance) {
      options.reportHypothesis = guidance.inspect
      options.instruction = defaultInstruction(parent.fitness) + '\n\n' + guidance.instruction
    }
    const candidate = await evolve.mutate(options)
    created += 1

    // Evaluation
    const fitness = await evolve.evaluate(candidate)

    let feedback
    if (guidance) {
      try {
        feedback = await assessGuidance(guidance, candidate.discovery, parent, fitness,
          settings.guidance, runState.signal)
      } catch (error) {
        runState.signal.throwIfAborted()
        await evolve.files.write('guidance-error.json', JSON.stringify({ message: String(error) }))
      }
    }
    const delta = Number.isFinite(fitness) && Number.isFinite(parent?.fitness) ? fitness - parent.fitness : null

    // Recording
    await population.append({
      id: candidate.id,
      parent: parentId,
      fitness,
      ...(panel ? { panel: true, delta } : {}),
      survival: fitness === null ? 'no' : 'yes',
      ...(guidance?.inspect ? { discoveryAttempt: true, discovery: feedback?.discovery ?? undefined } : {}),
      ...(guidance?.id ? { guidance: observationFor(guidance, parent.fitness, fitness, feedback?.observation) } : {}),
    })

    // Survival culling
    rows = await population.rows()
    if (alive(rows).length >= maxPopulation) {
      await evolve.survive(population)
      rows = await population.rows()
    }
  }

  // 3. Determine best candidate overall (by merit: a failed evaluation never wins)
  rows = await population.rows()
  let best = rows[0]
  for (const row of rows) {
    if (row.fitness === null) continue
    if (best === undefined || best.fitness === null || (panel ? row.fitness > best.fitness : merit(row.fitness) > merit(best.fitness))) {
      best = row
    }
  }

  const budget = (await evolve.context()).budget
  return {
    best_id: best?.id ?? 'c000000',
    best_fitness: best === undefined ? 0 : best.fitness,
    remaining: budget.remaining,
  }
}

export default { name, run }
