---
name: research-session
description: Start or resume a reduction research campaign with a round budget, executable tests, and independent review.
---

# Research Session

Investigate one fixed reduction in a persistent harness session, through a
reviewed paper or evidence-backed stop. Stage changes need no new session or
permission; continue within the authorized scope and round budget.

## Establish the campaign

For a new campaign, follow the [repository standard](../../../research/repository.md#start-before-prepare):
create the independent Git repository and initial question/state commit before
Prepare or any probe. Copy the research skills and `research/` specifications;
make the active reviewer registration available as described there. Keep
research artifacts out of the board.

Record a dated capability probe in `state.md`: Python, uv, available SAT/SMT/
CP-SAT solvers, Typst, Lean/Lake/Mathlib and the writing skill, with versions,
paths and status. Prepare selects the oracle solver and locks any Python binding.
Missing tools block only dependent stages; re-probe when the environment changes.

On resume, read the README, local instructions, fixed question, `state.md` and
latest review/evidence. Inspect Git status, last command outcome and capability
probe; continue the existing tests and round count.

Follow the [reduction contract](../../../research/reduction.md): legal F and
recovery G for every valid target output. A different theorem needs a new campaign.

## Work in the same conversation

Load a stage skill when its responsibility is needed:

| Responsibility | Skill and completion evidence |
|---|---|
| Testing foundation | [Prepare](../research-prepare/SKILL.md): independent oracles and at least 100 fixed random/edge cases; pass self-tests and commit before construction |
| Construction and proof | [Propose](../research-propose/SKILL.md): executable F and G, general proof and worst-case time/encoding bounds |
| Executable verification | [Verify](../research-verify/SKILL.md): solve actual target instances independently and test recovered source outputs, including alternate valid target outputs |
| Independent assessment | [Review](../research-review/SKILL.md): separate correctness, novelty and significance judgments |
| Manuscript | [Write](../research-write/SKILL.md): reviewed Typst paper, figures where explanatory, reproducible commands and inspected PDF |
| Formal proof, when requested | [Formalize](../research-formalize/SKILL.md): explicit Lean statements, certificate checks and scoped verification claims |

Commit Prepare, then begin round 001.

A failure returns to its responsible work. Separate candidate, oracle, proof
and execution defects; record the reproducer, expected/actual result and
affected claims. Repair and rerun relevant checks, reusing unaffected evidence.
Change oracle expectations only from fixed definitions, then rerun self-tests.

After changing F or G, rerun prepared checks and verification before review.
Proof changes need proof review; editorial changes need affected-page inspection.
Keep commands, inputs and revisions behind reused evidence. Bound instances or
search families, not wall time. A timeout or killed run is an execution failure,
not an oracle answer or exhausted search family; commit its partial state.

## Artifact ownership

The [repository standard](../../../research/repository.md#directory-ownership)
owns the directory layout and Git policy. Within `campaigns/<slug>/`:

- `question.md` fixes the target. `state.md` tracks the claim, probe, budget,
  checks, review, next action and one row per round: ID, attempted mechanism or
  literature scope, first check, outcome and evidence link.
- `work/` holds current cases, checkers, algorithm, proof and paper;
  `work/evidence/` holds checks outside a round.
- `rounds/NNN/round.md` records Plan / Evidence and diagnosis / Next action.
  Keep unique scripts, outputs and counterexamples there; link implementation
  commits instead of copying workspaces.
- `reviews/` holds independent reviews and checks; `formal/` holds formal
  sources and evidence.

Keep reusable findings in `research/experience/`. Read the board's local
`research/experience/entries/` in place; do not copy or treat it as evidence
([format](../../../research/experience/README.md#local-shared-collection)).
Link detailed evidence, preserve failures and counterexamples, and follow the
repository standard for reproducible bulk outputs.

## Research rounds and topic budget

Use the user's budget, or disclose a three-round default. A round is an
attempt at a construction, proof strategy or standalone literature search—not
a workflow stage. Before starting, record its scope and first discriminating
check. New mechanisms, strategies or expanded search families start new rounds;
failed and abandoned attempts count.

Prepare, Verify, Review, Write and Formalize add no round by themselves. Keep
their evidence in `work/`, `reviews/` or `formal/`. Repairs and supporting
lookups stay in the current attempt; interruption resumes its ID. A review
finding starts a new round only if it requires a new construction or proof
strategy.

At round closure, record evidence, actual instance/solver/recovery counts,
diagnosis, remaining obligations, next action and experience extraction;
update `state.md` and commit.
Reconcile used rounds with numbered attempt records and report distinct
mechanisms separately. Do not invent or retrospectively merge rounds; label
reconstructed records. At budget exhaustion, stop discovery but finish checks, review and
writing for a complete candidate. Further rounds need new allocation. Harness
continuation limits are separate from research rounds.

## Choose the next step

Choose the next action from the uncertainty: develop a claim, investigate,
change mechanism or stop. A round plan names the gap, mechanism, prior evidence,
first check and what its outcomes mean.
Parameter or seed changes are not new ideas; a known result is not discovery.
Supporting lookups stay in the current round; a standalone literature attempt
has a finite scope and counts. For literature, use Web/arXiv by default and
record primary sources, theorem locations, date and coverage limits.

## Learn from rounds

Use the [experience format](../../../research/experience/README.md). Search by
structure and assumptions before each attempt; record applicability or its
absence. At closure, separate observation, supported/suspected cause and
consequence. Bounded UNSAT excludes only its stated family; preserve
counterexamples as regressions. Record **Experience extraction:** links or
**none** with a reason; a new entry is not required for every round.

At campaign closeout, preserve contradictions and report distinct entries
created, updated and pending. Date retrospective extraction; entry use alone
does not establish improved discovery.

## Justify early exit

To stop for lack of progress with budget left, retain an actual attempt, its
failed assumption and what the evidence excludes. Try a different mechanism or
establish an obstruction; if none is testable, investigate adjacent literature.
One failed gadget is insufficient, and repeated trials must not pad rounds.

Stop earlier for user instruction, exhausted budget, an external blocker, a
complete result or decisive ineligibility. Distinguish incomplete from
unpromising work and investment decisions from impossibility proofs. Apply the
[screening criteria](../../../research/screening-method.md#exploratory-admission);
record partial results, remaining obligations and resumption evidence. Switch
topics only within authorized scope.

## Independent review

With F, G, proof and passing checks, spawn a fresh-context registered
[reviewer](../research-review/SKILL.md) ([harness contract](../../../harness/README.md)).
Provide the fixed question, artifact paths, new review directory and prior
findings without suggesting a verdict. Keep the candidate unchanged during
review. The reviewer writes independent checks, cannot edit the candidate or
spawn agents, and records which boundaries the harness enforced.

Resolve findings in the main conversation. Re-review repairs, reusing unaffected
evidence; material construction/proof changes require renewed review. An
advance review leads to writing. If review is unavailable, mark it pending;
self-review is not independent review.

## Recommend and report

Lead with the result, open proof obligations, main obstacle and next action.
Separate correctness, novelty and significance. Rate prospects within the
remaining budget as low/medium/high/unknown with evidence, label this
uncalibrated, and retain earlier assessments.

At handoff, give repository path/commit, rounds used/remaining, distinct
mechanisms, check scope, experience counts/links and next action. Avoid
test-pass percentages or unsupported success probabilities.

## Completion and interruption

Use `ready_for_expert_review` only with executable F/G, a general proof,
passing checks, an independent advance review and a compiled, visually inspected
Typst PDF. It is an agent assessment, not human certification; track formal and
other pending checks separately.

Use `stopped_without_discovery` for a supported stop. On interruption, commit
partial state and resume in the same campaign. Remote creation, publication,
board edits and integration need separate authorization.
