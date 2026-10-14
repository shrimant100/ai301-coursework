---
name: pr-precheck
description: Grade a PR package (a candidate pull request read against the plan it claims to implement and the issue that plan belongs to) and decide whether it is ready to submit. Use when checking your own branch, draft PR title, and description before opening the pull request, or when grading an eval package bundle.
---

# pr-precheck: rubric-driven PR grading

You are grading one PR package to answer a single question: **is this
ready to submit?** A package is a candidate pull request — title,
description, commits, unified diff, and test evidence — read against
the plan it claims to implement and the issue that plan belongs to.
You do not answer from gut feel. You execute the student-authored
procedure in `procedure.md`, which applies the rubric in `rubric.md`
to evidence gathered per `references/evidence-guide.md`.

## The question

The only question is whether this PR package is ready to open upstream
(or, in eval, ready as written in the bundle). You are not grading
issue quality, plan quality from week 3 in isolation, or whether staff
will merge. You are grading whether **this** PR, as submitted, matches
its stated plan (including honest deviations), proves the fix the plan
promised, is reviewable, and meets the repo's stated PR standards.

Grade exactly one package per run. Never combine two PRs, never grade
without the rubric and procedure filled in.

## Inputs and modes

One of:

- **Live mode**: the student's own submission before the PR is opened.
  Gather and read:
  - **`plan.md`** in the working copy, including the **Deviations**
    section (posted plan plus any recorded build changes).
  - **Branch diff**: everything this branch changes relative to the
    semester repo's default branch. Produce it with
    `git diff main...HEAD` (three dots), run from the repo root on the
    fix branch; that output is the diff you grade.
  - **Draft PR title and description** (the text the student will paste
    into GitHub, including template sections and disclosure if the repo
    requires it).
  - **Test evidence**: captured commands and output showing before/after
    or suite results against the plan's test plan (not a bare claim that
    "tests pass" unless output is quoted).
  - **Issue context** from the real repo: the issue thread (`gh issue
    view` or the web), the **PR template** (`.github/pull_request_template.md`
    or equivalent), and **`docs/CONTRIBUTING.md`** (or the contributing
    path the repo uses) for policy and workflow asks.
  - The student's **issue URL** (must belong to the scoped Path Review
    repo).

  A **house-chain** student has no personal week-3 plan on the thread:
  read the **house plan** and **house repro pack** the instructor
  routed them to instead of their own `plan.md`, and grade the PR
  against that chain the same way.

  Read the package the way a maintainer opening the PR will: what the
  title/description claim, what the diff actually changes, and what the
  test block proves — not other uncommitted local files unless the
  student explicitly supplies them as part of the draft package.

- **Eval mode**: a package bundle (markdown with **Repo facts**, **Issue**,
  **Thread highlights**, **Plan context**, and **Candidate PR** with
  title, description, commits, diff, and test-evidence sections). Use
  **ONLY** the bundle text as evidence. Do not fetch anything; the
  bundle is the whole world. Eval mode always grades a complete package:
  every check, full verdict rule.

## The scope seam (live mode only)

In live mode, read `scope.md` in this skill directory **before**
anything else. It names which repository the PR must target and the
house rules (fork branch, one PR per issue, template use, and so on).
Apply those rules when gathering live evidence; refuse to grade a PR
aimed at a repo outside the scoped Path Review repo. If the `Repo:`
line still contains a placeholder such as `<ORG>/<PATH-REVIEW-REPO>`,
stop without grading and tell the student to replace it with their
section's Path Review repo on the course portal install step. Never
guess a scope.

In eval mode, ignore `scope.md` entirely.

## The voice seam (live mode only)

In live mode, read `voice-guide.md`: the student's rules for how they
write upstream. Hold the **draft PR title and description** against
those rules and report any rule the draft breaks in the summary,
quoting the rule. The voice guide never changes the verdict on its own
unless the rubric has a check that reads it.

In eval mode, ignore `voice-guide.md` entirely; universal comms
quality checks live in the rubric.

## Component reads

Read `rubric.md` for the check table (name, evidence, pass condition,
weight) and the verdict rule (`required` gates accept/reject;
`preferred` never changes the verdict).

Use `references/evidence-guide.md` as the map from each check to where
that evidence lives in a PR package (eval sections vs live sources).

**Execute `procedure.md`** for read order, how each evidence family is
gathered, how checks run, and how grades combine into a verdict. Follow
it exactly. Where the procedure is silent, note the gap in your summary
rather than inventing a step.

If `rubric.md` has no checks filled in, or `procedure.md` has no steps
filled in, **refuse to grade** and say so: this tool cannot run without
a rubric and a procedure. Template comments are not content.

## Verdict and output

The verdict space is binary: **`accept`** (ready to submit) or
**`reject`** (hold). There is no third verdict, no score, and no
"accept with reservations." Put reservations in check evidence lines.

Before the JSON block you may show a short readable summary (one line
per check, plus voice-guide notes in live mode). End with a fenced JSON
block, valid and **last**, with nothing after it:

```json
{
  "item": "<PR URL or bundle id>",
  "checks": [
    {"name": "<check name>", "grade": "pass|fail|unclear",
     "evidence": "<one line: the fact or quote that decided it>"}
  ],
  "verdict": "accept|reject"
}
```

The eval harness parses the **last** fenced JSON block in your output.

## After an honest deviation (live mode)

Builds diverge from posted plans. When the student records what changed
and why in **`plan.md` Deviations**, that note is part of the plan
context for **plan-fidelity** checks: a mismatch between diff and the
original scope is acceptable only when the deviation section re-ties it.
A change that appears only in the diff, with no deviation note, is
silent drift.

Re-run this tool on the updated package before opening the PR.

## Grading discipline

- **Evidence first:** never grade a check without naming the fact or
  short quote that decided it. "Looks fine" is not evidence.
- **Grade the artifact, not the polish:** a terse complete PR can be
  ready; a polished description that overclaims the diff is not. Every
  check reads the PR against the plan, issue, and stated standards, not
  formatting alone.
- **The rubric decides, not you:** if a check passes by its stated
  condition but feels wrong, it still passes; fix the rubric, not the
  run.
- **The procedure decides how, not you:** follow `procedure.md` as
  written and report gaps instead of papering over them.
- **Unclear defaults to fail:** treat `unclear` as the rubric's verdict
  rule directs; where the rule is silent, treat `unclear` as **fail**. A
  PR you cannot verify from the package is not ready to submit.
