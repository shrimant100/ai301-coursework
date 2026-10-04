# Evidence guide: where proof lives in a plan package

## Repro evidence

**Where it lives.** Eval bundle: **Repro evidence** block (excerpt of the accepted reproduction). Live mode: the student's posted repro comment on the issue (week-2 proof).

**What good looks like.** Steps, control runs, timings, and expected/actual that pin **what failed** and often **which subsystem** is implicated. Plans must follow from this block, not from the issue alone. Compare plan diagnosis to controls (e.g. same command with a flag off passes) and to timings that exclude whole subsystems (e.g. slow with `--paging=never` implicates work outside the pager).

## Issue and thread

**Where it lives.** Eval bundle: **Issue** section and **Thread highlights**. Live mode: issue title/body and comment thread via `gh`.

**What good looks like.** Issue states user-visible symptom; thread may add maintainer direction (file/line, patch to test, engagement with an open PR, WAI). The plan should respect explicit code-level direction unless it explains why the approach differs.

## Plan body

**Where it lives.** Eval bundle: **Candidate plan** (Diagnosis, Scope, Changes, Test plan, or equivalent prose). Live mode: `plan.md` draft.

**What good looks like.** Names **where** to change and **what** to change, bounded out-of-scope lines, and a test plan that says what observable will differ after the fix (often re-running a repro step). Terse plans are fine if those elements are present.

## Plan comment

**Where it lives.** Eval bundle: **Candidate plan comment**. Live mode: draft plan comment text.

**What good looks like.** Names the concrete fix area or repro hook; avoids generic "I'll take this" without mechanism. When repo policy requires AI/tool disclosure in comments, say so once clearly.

## Repo facts

**Where it lives.** Eval bundle: **Repo facts** `contribution policy` line. Live mode: `CONTRIBUTING.md` / policy files on GitHub.

**What good looks like.** Distinguish **disclosure required** (name tool and extent) from **human-authored comments only** (specific voice, no disclosure tag required unless policy says so).
