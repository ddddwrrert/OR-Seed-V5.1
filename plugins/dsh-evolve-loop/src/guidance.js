import { spawn } from 'node:child_process'
import { existsSync } from 'node:fs'
import { fileURLToPath } from 'node:url'

const source = new URL('../../../seed_intelligence/controller.py', import.meta.url)
const installed = new URL('./seed_intelligence/controller.py', import.meta.url)
const controller = fileURLToPath(existsSync(installed) ? installed : source)

function invoke(request, signal) {
  return new Promise((resolve, reject) => {
    const child = spawn(process.env.OR_SEED_PYTHON ?? 'python', ['-B', controller], {
      signal, stdio: ['pipe', 'pipe', 'pipe'], windowsHide: true,
    })
    let output = ''
    let error = ''
    child.stdout.setEncoding('utf8').on('data', chunk => { output += chunk })
    child.stderr.setEncoding('utf8').on('data', chunk => { error += chunk })
    child.once('error', reject)
    child.stdin.on('error', reject)
    child.once('close', code => {
      if (code !== 0) {
        reject(new Error(`OR-Seed controller exited with code ${code}: ${error.trim()}`))
        return
      }
      try {
        resolve(JSON.parse(output))
      } catch (failure) {
        reject(failure)
      }
    })
    child.stdin.end(JSON.stringify(request))
  })
}

export async function guidanceFor(files, rows, parent, budget, config = {}, signal) {
  if (!Number.isFinite(parent.fitness) || budget.used % 2 !== 1 || budget.remaining < 2 ||
      config?.maxCandidates === 0) return
  const spent = (await files.list('guidance')).length
  if (spent >= Math.floor(budget.max / 2)) return
  const ids = new Set([parent.id, parent.parent, ...rows.slice(-10)
    .filter(row => row.parent === parent.id && Number.isFinite(row.fitness)).map(row => row.id)])
  ids.delete(undefined)
  ids.delete(null)
  const evaluations = Object.fromEntries(await Promise.all([...ids].map(async id => {
    if (!/^c\d{6,}$/.test(id)) return [id, null]
    const raw = await files.read(`evals/${id}.json`)
    try {
      return [id, raw === undefined ? null : JSON.parse(raw)]
    } catch {
      return [id, null]
    }
  })))
  const decision = await invoke({ action: 'plan', rows, parent, budget, spent, config, evaluations }, signal)
  if (!decision) return

  const instructions = []
  if (decision.id) {
    instructions.push(
      'Optional hypothesis. You may ignore it and choose any better direction.',
      decision.direction,
      `Supporting evidence: ${decision.evidence}`,
      `Counterevidence: ${decision.counterevidence}`,
      'The prediction is an improved complete 50-seed mean. Consider what would falsify it.',
    )
    if (decision.feature) {
      instructions.push(`Observed feature: ${decision.feature.name} (${decision.feature.observedDelta} mean points). ${decision.feature.observation}`)
    }
  }
  if (decision.inspect) {
    instructions.push(
      'Optional bottleneck discovery during this candidate. Keep choosing and implementing one complete solution.',
      'Use existing source inspection and recorded contrasts. Do not run extra probes or edit extra files.',
      'If you see a promising one-candidate change, report one OR_SEED_HYPOTHESIS JSON line with id, direction, evidence, counterevidence, reference, expectedGain (whole-panel mean points), cost, and optional feature {name, observation, seeds}. Any mechanism can be proposed.',
      ...decision.references.map(({ reference, profile }) =>
        `Reference ${reference}: recoverable mean at most ${profile.recoverableMean}; seed regressions: ${JSON.stringify(profile.regressions)}.`),
    )
  }
  await files.write(`guidance/${budget.used}.json`, JSON.stringify({ ...decision, parent: parent.id }))
  return { ...decision, instruction: instructions.join('\n') }
}

export async function assessGuidance(guidance, report, parent, fitness, config, signal) {
  if (!guidance) return {}
  return invoke({ action: 'review', guidance, report: report ?? null, parent, fitness, config: config ?? {} }, signal)
}

export async function discoveryFor(guidance, report, parent, config, fitness) {
  const result = await assessGuidance(guidance, report, { id: parent }, fitness, config)
  return result.discovery ?? undefined
}

export function observationFor(guidance, baseline, fitness, observation) {
  const delta = fitness === null ? null : fitness - baseline
  return {
    id: guidance.id, direction: guidance.direction, evidence: guidance.evidence,
    counterevidence: guidance.counterevidence, priorState: guidance.state,
    priorReliability: guidance.reliability, delta,
    ...(guidance.reference ? {
      reference: guidance.reference, expectedGain: guidance.expectedGain,
      cost: guidance.cost, feature: guidance.feature,
    } : {}),
    outcome: delta === null ? 'invalid' : delta > 0 ? 'improved' : 'no-improvement',
    candidateCost: 1,
    ...observation,
  }
}

export function workerHypothesis(text) {
  const line = typeof text === 'string'
    ? text.split('\n').find(line => line.startsWith('OR_SEED_HYPOTHESIS '))
    : undefined
  if (!line || line.length > 6200) return undefined
  try {
    const item = JSON.parse(line.slice('OR_SEED_HYPOTHESIS '.length))
    const keys = ['id', 'direction', 'evidence', 'counterevidence']
    if (item && keys.every(key =>
      typeof item[key] === 'string' && item[key].trim() && item[key].length <= 1500)) {
      return Object.fromEntries([...keys, 'feature', 'reference', 'expectedGain', 'cost']
        .filter(key => Object.hasOwn(item, key)).map(key => [key, item[key]]))
    }
  } catch {
    // The optional worker report does not affect candidate evaluation.
  }
  return undefined
}

