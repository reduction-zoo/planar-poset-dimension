# {Source problem} → {Target problem}

**Status:** `{campaign status}` · **Research model:** `{model/version}` · **Submitted:** {YYYY-MM-DD}

{State the exact result and its scope in one paragraph. Say what every valid target output recovers, including NO-SOLUTION only where the fixed contract requires it.}

## Construction

{Explain the core construction and recovery idea in a short paragraph. Name the key invariant rather than retelling the research history.}

## Evidence

- **Mathematical correctness and recovery: {proof and review status}.** {State what the general proof covers, what the independent reviewer concluded, and what remains unaccepted.} ([evidence](campaigns/{slug}/reviews/{review}/review.md))
- **Construction and recovery complexity: {scope of bounds}.** {State the proved runtime and encoding-size bounds and any limits.} ([evidence](campaigns/{slug}/work/proof.md))
- **Executable verification: {finite-check status}.** {Give actual instance and recovery counts, the scope of the checks, and why they do not replace the proof.} ([evidence](campaigns/{slug}/work/verification.md))
- **Formal certification and maintainer acceptance: {status}.** {State what was and was not performed or accepted.} ([evidence](campaigns/{slug}/state.md))

## Reproduce

Run from the repository root:

```sh
uv sync --locked
uv run --locked python campaigns/{slug}/work/check.py --candidate campaigns/{slug}/work/algorithm.py
uv run --locked python campaigns/{slug}/work/verify.py --candidate campaigns/{slug}/work/algorithm.py
```

{Explain what these commands check and which general claim rests on the written proof.}

## Artifacts

- [Fixed question](campaigns/{slug}/question.md)
- [Campaign state](campaigns/{slug}/state.md)
- [Manuscript](campaigns/{slug}/work/manuscript.pdf)
- [Construction and recovery](campaigns/{slug}/work/algorithm.py)
- [General proof](campaigns/{slug}/work/proof.md)
- [Independent review](campaigns/{slug}/reviews/{review}/review.md)
- [Verification evidence](campaigns/{slug}/work/verification.md)
