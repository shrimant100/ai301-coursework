# Rubric: is this plan ready to post and build from?

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| `diagnosis-grounded-in-repro` | Plan Diagnosis / Cause / Summary vs **Repro evidence** (steps, timings, control runs, expected/actual) | Pass if the plan's stated cause explains the failure the repro shows and is **not ruled out** by repro facts in the same bundle (e.g. a control run, a `--paging=never` timing, or a symptom flip that implicates a different subsystem). Fail if repro evidence pins one mechanism (highlighting cost, tokenizer ruled out by control, zeros gone before cast) while the plan blames another without addressing that contradiction. | required |
| `scope-bounded` | Plan Scope / Changes / "In scope" / "Out of scope" | Pass if the plan names **at least one concrete change target** (file, module, function, or doc surface) **and** at least one explicit **out-of-scope** boundary for this fix. Fail if there is no named target, or the fix is wrapped in a multi-front campaign (migrations, printer rewrites, new frameworks, "while we're here" refactors) beyond what the issue and repro require. | required |
| `test-plan-decisive` | Plan Test plan / Test section vs **Repro evidence** steps | Pass if the test plan states an **observable outcome** for the fix tied to the repro failure (same failing step, same symptom, or explicit before/after the repro quotes). Manual re-run of repro steps counts when it names the step and expected change. Fail if verification is only vague ("feel fast", "nothing else broken"), only "run the full test suite" with **no** fix-specific observable, or absent. | required |
| `implementation-not-vague` | Plan Changes / Diagnosis / Scope | Pass if the plan names **where** to change and **what kind of change** (not open-ended investigation only). Fail if the plan is explore-only ("poke around", "profile and optimize" with no chosen layer/files), or defers every decision ("upstream or vendored, whichever is easier") with no narrowed target. | required |
| `maintainer-direction-respected` | **Thread highlights** vs plan + **Candidate plan comment** | Pass if the thread contains **no** explicit maintainer fix direction (file, patch to test, prior PR to engage), **or** the plan/comment engages that direction (same area, tests the offered patch, acknowledges open PRs/WAI). Fail if a maintainer isolated a **code** culprit or posted a patch to test and the plan is **docs/workaround-only** without addressing that code path. | required |
| `policy-disclosure` | Repo facts **contribution policy** and **Candidate plan comment** | Pass if policy is silent on AI disclosure for comments, allows assistive AI without a disclosure line, requires human-authored comments and the comment is specific, **or** the comment includes disclosure when policy **requires** stating AI/tool use and extent. Fail when policy requires disclosure and the comment omits it (eval packages treated as AI-assisted). | required |
| `plan-comment-specific` | Candidate plan comment vs plan body | Pass if the comment names a **concrete mechanism, file, or repro step** from the plan (not generic enthusiasm). Fail if the comment could apply to any open issue. | preferred |

## Verdict rule

**Accept** (ready to post and build from) only if every **required** check passes.

**Reject** (hold) if any required check fails or is **unclear**; **unclear counts as fail**.

**Preferred** checks never change accept/reject.
