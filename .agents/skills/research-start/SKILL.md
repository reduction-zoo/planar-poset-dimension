---
name: research-start
description: Launch a new reduction research campaign from a short instruction — pick a question from the board records using whatever the user names, create the independent repository and commit it, then continue with research-session.
---

# Research start

Use this when the user asks to start, kick off or launch an AutoResearch campaign
without naming a question, for example "pick an unsolved Construction open question and start research"
or "start a campaign from an unsolved scheduling question".

Take the filter from the instruction, pick one record, and launch. Do not rank
candidates, score difficulty, or build any preference machinery: if the user wants
a particular question or a particular kind of question, they say so.

The board checkout is the only input: read `website/questions/*.json` and nothing
outside the checkout.

## Defaults

- **Filter**: whatever the user named, matched as free text over the record's own
  fields. With no filter: `category = Construction open` and no `solutions`.
- **Round budget**: 3, unless the instruction gives a number.
- **Destination**: `~/Codes/reduction-zoo/<slug>`, unless the instruction gives a
  root. Skip a slug whose directory already exists there.
- **Count**: one question.

## Launch

1. Say the chosen slug and path before creating anything, and confirm the path is
   neither the board checkout nor inside it.
2. `git init -b main`, then copy in the research skills and `research/`
   specifications, keeping relative paths intact. Set up only the active
   reviewer registration as described in the repository standard. Do not copy
   `harness/` or the board's
   `research/experience/entries/` collection.
3. Write the destination `README.md`, local `AGENTS.md`, `.gitignore`, and
   `campaigns/<slug>/question.md` from the fixed board record — its `references`
   carry over as the campaign's literature starting points — then `state.md` with
   the budget, pending capability probe, an empty round table with fixed columns,
   and the next action.
4. Make the initial commit before any test, construction search or proof attempt.

## Continue

- On the `research` preset, continue straight into
  [research-session](../research-session/SKILL.md): probe capabilities, complete
  Prepare, then start research round by round.
- Otherwise stop after the commit and print the one-line instruction for the
  campaign session: workspace = the new repository, preset `research`, message
  `Continue the <slug> campaign: read README.md, AGENTS.md and
  campaigns/<slug>/{question,state}.md, probe capabilities, complete Prepare,
  then start research round by round.`
  A session cannot change preset after it produces anything, and only this preset
  carries the registered reviewer.

## Report

The chosen slug, its path, the initial commit, the round budget, and the next
action. Nothing else.

## Guardrails

- The board record is the only input. Do not fetch or verify anything outside the
  checkout, and do not resolve a record's `references`.
- If nothing matches the filter, say so and offer the nearest matches.
- Never invent a question or a record field. One campaign per repository; a
  different question is a new campaign.
- Keep the board checkout read-only. Creating a remote, publishing, updating the
  board or sending anything upstream needs separate authorization.
