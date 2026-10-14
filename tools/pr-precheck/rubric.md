# Rubric: is this pull request ready to submit?

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| `plan-scope-honored` | **Plan context** in/out-of-scope lines and any stated deferrals vs **Candidate PR** unified diff (paths and hunks) | Pass if every changed file and functional change fits the plan's in-scope targets **or** is re-tied in an explicit deviation/deferral recorded in the plan context **and** restated in the PR description when the diff omits a planned deliverable. Fail if the diff adds behavior, files, config, or refactors the plan scoped out with no deviation note, or drops a planned in-scope deliverable with no paired deferral in plan context and description. | required |
| `description-matches-diff` | **Candidate PR** description vs unified diff | Pass if the description does not claim fidelity the diff contradicts (e.g. "implements the plan exactly", "no changes beyond…", "docs now document…", "no functional changes outside X") when extra files, features, or missing promised surfaces appear in the diff. Stating an honest deferral that matches the plan and the diff is pass. Fail on any such overclaim. | required |
| `test-evidence-decisive` | **Candidate PR** test-evidence section vs **Plan context** test plan and the repro steps the plan built on | Pass if the evidence quotes a run for the plan's **primary** repro (the failing step or symptom the fix targets) with before/after or expected-after, **and** each **other named** step in the test plan is either quoted, covered by quoted suite output the plan names (e.g. a spec file or `make` target), or briefly attested in one line when the plan expects no change (e.g. "control unchanged"). Out-of-scope limits the plan defers (plan + description) do not require their own test runs. Explicit deferral of a named step in plan + description is pass for that step. Fail if the primary repro is missing or vague, proof is only "tests pass" / "verified locally" with no quoted primary repro, exercises the wrong path/symptom, or a **named** non-deferred step has no quote, suite line, or attestation. | required |
| `diff-reviewable` | **Candidate PR** unified diff and commit list | Pass if the diff is reviewable as a bounded fix: no leftover debug prints or `eprintln!`/`console.log`-style probes, no commented-out first attempts or experiments kept in tree, no dead helper functions or `allow(dead_code)` probes, and no drive-by reformat/re-indent hunks on files outside the plan's scope without a deviation note. Fail if such debris buries the fix or unrelated churn dominates the patch. | required |
| `pr-template-standards` | **Repo facts** pull-request template asks vs **Candidate PR** description and diff | Pass if every checklist or section the repo facts **explicitly require** (e.g. closes `#` line, type-of-change checklist, changelog/whatsnew path for bugfixes, linked contributing rules) is filled with real content **and** any required changelog/doc file the template names appears in the diff when the PR is a bugfix. Fail if a stated required item is visibly empty, omitted, or checkbox-only while the template demands substance. If repo facts name no PR template requirements, pass. | required |
| `policy-disclosure` | **Repo facts** contribution policy (including AI-use rules) vs **Candidate PR** description | Pass if policy is silent on AI disclosure for PRs, allows assistive AI without a disclosure line, **or** the description discloses tool use and extent when policy requires stating AI/tool assistance. Fail when policy requires disclosure and the description omits it (eval packages are graded as AI-assisted). | required |
| `pr-title-specific` | **Candidate PR** title vs issue and plan | Pass if the title names the fix area or user-visible symptom (not generic "fix bug" / "updates"). Fail if it could describe any PR in the repo. | preferred |

## Verdict rule

**Accept** (ready to submit) only if every **required** check passes.

**Reject** (hold) if any required check fails or is **unclear**; **unclear counts as fail**.

**Preferred** checks never change accept/reject.
