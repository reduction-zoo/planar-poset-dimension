# Research instructions

Read the [fixed question](campaigns/planar-poset-dimension/question.md), [prior state](campaigns/planar-poset-dimension/state.md) and [preparation notes](campaigns/planar-poset-dimension/work/preparation.md). The fixed [test corpus](campaigns/planar-poset-dimension/work/cases.json) and [verifier](campaigns/planar-poset-dimension/work/check.py) are the starting evidence; the preparation notes state their coverage and any pending checks.

Run `uv sync --locked`, then `uv run --locked python campaigns/planar-poset-dimension/work/check.py --self-test` before relying on that evidence. Follow the current user's AutoResearch pipeline. Preserve prior evidence, commit new work incrementally and make only evidence-backed claims.
