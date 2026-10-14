# Evidence guide: where evidence lives in a PR package

## Plan fidelity (harness category: silent-drift)

**Where it lives.**

- **Eval bundle:** **Plan context** (in-scope, out-of-scope, files, deferrals) read against **Candidate PR** **Diff** (paths and hunks) and **Description** fidelity claims.
- **Live mode:** `plan.md` (Scope + **Deviations**) and `git diff main...HEAD` read against draft PR description (e.g. `pr_draft.md`).

**What good looks like.**

Every changed file and behavior fits the plan's in-scope targets, or an honest deferral/deviation in the plan **and** description explains a narrower diff (e.g. `%VAR%` expansion deferred while the caret fix ships). The description does not claim "exactly as planned" or "no changes beyond…" when the diff touches extra files or scoped-out behavior. Silent extra hunks (second file the plan never named) or missing promised deliverables with no deferral are fail.

## Test evidence (harness category: not-tested)

**Where it lives.**

- **Eval bundle:** **Candidate PR** **Test evidence** section vs **Plan context** test plan and the repro steps quoted in plan context.
- **Live mode:** `test_evidence.md` (or equivalent captured output) vs `plan.md` test plan and your week-2 repro steps.

**What good looks like.**

For each verification the plan **names in its test plan** (repro command, failure mode, observable), the evidence quotes a run showing **expected-after** or **before/after**, or the plan and PR description explicitly defer that verification with reason. Out-of-scope limits the plan already excludes (with deferral restated in the description) are not missing tests. Quoted suite or template checks count when tied to the fix. Vague "tests pass" / "verified locally", wrong-path demos (testing GET when the issue is POST), or only one of two named failure modes without deferring the other are fail.

## Diff quality (harness category: unreviewable)

**Where it lives.**

- **Eval bundle:** **Candidate PR** **Diff** and **Commits** list.
- **Live mode:** `git diff main...HEAD` and `git log main..HEAD --oneline`.

**What good looks like.**

A maintainer can see the fix in one read: no leftover debug `eprintln!`/`print`, no commented-out first attempts, no dead probe functions, no drive-by re-indent on unrelated files outside plan scope without a deviation note. Commits describe the fix, not only `wip`/`fmt`. Debris that buries the real hunk is fail even when the underlying fix is right.

## Standards and comms (harness category: standards-wall)

**Where it lives.**

- **Eval bundle:** **Repo facts** `pull requests` and **contribution policy** vs **Candidate PR** **Description** and **Diff** (changelog/whatsnew files when the template requires them).
- **Live mode:** PR template and `docs/CONTRIBUTING.md` (or repo equivalent) vs draft description; diff for required doc paths.

**What good looks like.**

Every **explicit** template requirement in repo facts is filled with real content (closes `#` when required, checklist items substantively answered, changelog/whatsnew present in diff for bugfixes when the template demands it). When policy requires AI/tool disclosure in PRs, the description states tool and extent once clearly (eval packages are treated as AI-assisted). Empty checkboxes, omitted whatsnew, or missing disclosure when required are fail. Repos with no stated PR requirements pass when nothing is explicitly required.

**Note:** Whether the description **overclaims** relative to the diff (plan fidelity) is graded under **Plan fidelity**, not here — except disclosure and template asks, which live here.
