# Procedure: how this skill grades a PR package

## Read order

1. Read **Issue** (user-visible symptom and expected behavior only; do not treat the issue body alone as proof the PR is correct).
2. Read **Plan context** fully: repro excerpt it builds on, in-scope and out-of-scope lines, intended files/approach, test plan (named steps and observables), and any stated deferrals or deviation notes.
3. Read **Repo facts**: the `pull requests` line (template/checklist asks) and **contribution policy** (including AI-use rules).
4. Read **Thread highlights** for maintainer direction (files, patches to test, engagement with open PRs, WAI).
5. Read **Candidate PR** in this order: **Title**, **Description**, **Commits**, **Diff** (every changed path and hunk), **Test evidence**.
6. In **live mode**, also read **`plan.md`** (including **Deviations**), the branch diff from `git diff main...HEAD`, draft PR text (e.g. `pr_draft.md`), and captured test output (e.g. `test_evidence.md`) when the student supplies them; treat those as the live equivalents of plan context and candidate PR sections.
7. Do not use knowledge outside the package (eval) or outside the gathered live inputs.

## Evidence gathering

For each rubric check, pull facts only from the sections the rubric and `references/evidence-guide.md` name. Prefer **side-by-side** comparisons:

- **plan-scope-honored:** List each changed file/path from the **Diff** and each in-scope / out-of-scope line from **Plan context** (live: `plan.md` scope + Deviations). Note extra files, new config/options, or refactors not in scope without a deviation/deferral in plan context **and** description when the diff omits a planned deliverable.
- **description-matches-diff:** Quote fidelity phrases from the **Description** ("exactly as planned", "no changes beyond", "docs now", "no functional changes outside…") and list diff paths/hunks that support or contradict them.
- **test-evidence-decisive:** List each **named verification** in the plan's test plan; for each, quote whether **Test evidence** shows before/after or expected-after for that step, defers it in plan + description, or is silent/vague/wrong-path.
- **diff-reviewable:** Scan the **Diff** and **Commits** for debug prints, commented-out attempts, dead helpers, `allow(dead_code)` probes, drive-by reformat hunks on out-of-plan files, and non-descriptive commit messages (`wip`, `fmt` only).
- **pr-template-standards:** Quote each **explicit required** item from repo facts' PR template line; check **Description** and **Diff** for closes `#`, checklist substance, changelog/whatsnew paths when required for bugfixes.
- **policy-disclosure:** Quote the AI/disclosure clause from repo facts policy; check **Description** for tool use and extent when required.
- **pr-title-specific:** Quote the **Title** and whether it names the fix area or symptom vs a generic label.

If a section a check needs is missing, record **missing section** for that check.

## Check execution

1. Execute checks in **rubric table order** (top to bottom).
2. Grade each check **pass**, **fail**, or **unclear** with one evidence line (fact or short quote).
3. Use **unclear** only when the package lacks the section the check requires or the text is too ambiguous to apply the pass condition.
4. Do not re-read the whole package between checks; use the facts already gathered.
5. **Preferred** checks use the same rules but never change the verdict.

## Verdict assembly

1. Apply the rubric **Verdict rule**: **accept** only if every **required** check is **pass**; any **fail** or **unclear** on a required check -> **reject**.
2. In the JSON output, include **every** check from the rubric with its grade and evidence line.
3. Set `"verdict"` to `"accept"` or `"reject"` only (no third value).
