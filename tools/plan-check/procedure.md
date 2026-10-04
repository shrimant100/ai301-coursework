# Procedure: how this skill grades a plan package

## Read order

1. Read **Issue** (symptom and expected behavior only; do not treat issue text as proof of root cause).
2. Read **Repro evidence** fully: environment, steps, control runs, expected vs actual, quoted timings or outputs. Note which subsystem or step the evidence pins down.
3. Read **Thread highlights** for maintainer-stated direction (files, patches to test, prior PRs, WAI).
4. Read **Candidate plan** in order: diagnosis/cause, scope, changes, test plan (any headings the bundle uses).
5. Read **Candidate plan comment** and **Repo facts** contribution policy line.
6. Do not use knowledge outside the bundle.

## Evidence gathering

For each rubric check, pull facts only from the sections the rubric and evidence guide name:

- **diagnosis-grounded-in-repro:** quote one repro timing/control/symptom and the plan's stated cause; note agreement or contradiction.
- **scope-bounded:** list in-scope targets and out-of-scope lines from the plan; count whether change is a single bounded fix vs a campaign.
- **test-plan-decisive:** quote the repro's failing step/symptom and what the test plan says will be observed after the fix.
- **implementation-not-vague:** quote the plan's named file/module and intended change, or absence.
- **maintainer-direction-respected:** quote any maintainer direction from thread highlights and whether the plan/comment engages it.
- **policy-disclosure:** quote the repo-facts policy clause and whether the comment discloses if required.
- **plan-comment-specific:** quote issue-specific anchors in the comment.

If a section the check needs is missing from the bundle, record **missing section** for that check.

## Check execution

1. Execute checks in rubric table order (top to bottom).
2. Grade each check **pass**, **fail**, or **unclear** with one line of evidence (fact or short quote).
3. **unclear** only when the bundle lacks the section the check requires or the plan text is too ambiguous to apply the pass condition.
4. Do not re-read the whole bundle between checks; use the facts already gathered.
5. Preferred checks use the same rules but never change the verdict.

## Verdict assembly

1. Apply the rubric **Verdict rule**: **accept** only if every **required** check is **pass**; any **fail** or **unclear** on a required check → **reject**.
2. In the JSON output, include every check from the rubric with its grade and evidence line.
3. Set `"verdict"` to `"accept"` or `"reject"` only (no third value).
