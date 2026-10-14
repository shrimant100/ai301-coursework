# Unit 4 — Test and Submit

Path: `beat-1-sandbox/unit-4/pull-request.md`

Record of the pull request you opened against the Path Review repo, and of the evaluation
runs that produced `eval-run.txt`. This file is graded at the path above; a copy kept
anywhere else in the repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the wrong
label is not graded.

---

## Your pull request

**Pull request**

https://github.com/codepath/pathreview-ai301-fa26-s1/pull/186

**Branch**

fix/62-redis-health-redis-url

## Eval iterations

Answer all four sections. Quote source text directly; paraphrase does not satisfy these
fields.

**Run history**

1. Smoke (`--limit 3`): **3/3** agree.
2. First confirming full run (`--save-run`): **19/20** — disagreed on **pkg-13** (`test-evidence-decisive`); category floor **6/7** on clear-accept.
3. Rubric clarification for primary repro + named steps/deferrals; canary `--only pkg-13,pkg-10,pkg-04`: **3/3**.
4. Final confirming full run (committed as `eval-run.txt`): **20/20** PASS; category floor met (`clear-accept 7/7`, `not-tested 4/4`, `silent-drift 4/4`, `standards-wall 2/2`, `unreviewable 3/3`).

**Package analysis**

**pkg-13** (scored, category `clear-accept`). Gold label: **accept**. Rubric: **accept** after rubric fix. Neovim URL fix with honest `%VAR%` deferral in plan and description; test evidence quotes primary repro before/after and names the functional spec pass — **`test-evidence-decisive`** passes without requiring a separate test run for the deferred out-of-scope limit.

**Check rationale**

From `tools/pr-precheck/rubric.md`, check **`test-evidence-decisive`**:

> Pass if the evidence quotes a run for the plan's **primary** repro (the failing step or symptom the fix targets) with before/after or expected-after, **and** each **other named** step in the test plan is either quoted, covered by quoted suite output the plan names (e.g. a spec file or `make` target), or briefly attested in one line when the plan expects no change (e.g. "control unchanged"). Out-of-scope limits the plan defers (plan + description) do not require their own test runs.

I added the primary-vs-named-step split after **pkg-13** flipped to reject on the first full run, so honest deferrals (like **pkg-16**) stay accept while **pkg-10**-style vague proof still fails.

**Trade-offs**

**`test-evidence-decisive`** allows a one-line control attestation when the primary repro is quoted; that is why **pkg-13** matches gold after the fix. I re-ran **`--only pkg-10,pkg-04`** so tightening did not let vague "verified locally" packages through before the **20/20** confirming run.

---

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/pr-precheck/`.
