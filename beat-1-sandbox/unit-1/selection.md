# Unit 1 — Issue Selection

Path: `beat-1-sandbox/unit-1/selection.md`

Record of the issue carried into Unit 2, and of the evaluation runs that produced
`eval-run.txt`. This file is graded at the path above; a copy kept anywhere else in
the repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the
wrong label is not graded.

---

## Selected issue

**Issue link**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/62

**Verdict output**

Grading all three issues from the scoped repo (`codepath/pathreview-ai301-fa26-s1`) against `rubric.md`, using only the live evidence gathered via `gh`.

**Repo-level required checks (identical for all three issues):**
- `repo-not-archived`: pass — `archived: no`
- `repo-recent-activity`: pass — last push 2026-09-16, capture 2026-09-23 (7 days, well under 120)
- `maintainer-reachable`: pass — no numeric response-time sample given, but last push is within 120 days of capture (sparse-sample fallback)
- `ai-not-outright-banned`: pass — CONTRIBUTING.md sets no outright AI ban

**Issue #62 — `redis_host`/Settings mismatch in health check**
| Check | Grade | Evidence |
|---|---|---|
| no-open-claim | pass | assignees: none; no open linked PRs |
| not-umbrella-scope | pass | single bounded bug in `api/routes/health.py` vs `core/config.py` |
| bounded-deliverable | pass | body has named files + Steps to reproduce for `GET /health` |
| not-stale-abandoned-prs | pass | no linked PRs at all |
| not-drive-by-feature | pass | opener is cohort-maintainer-filed; labels include bug/good-first-issue |
| good-first-issue-label (pref) | pass | label present |
| repro-or-acceptance (pref) | pass | explicit "Steps to reproduce" |

→ **accept**, 2/2 preferred.

**Issue #72 — `verify_password` raises `UnknownHashError`**
| Check | Grade | Evidence |
|---|---|---|
| no-open-claim | pass | assignees: none; no open linked PRs (classmate claim comments ignored per house rule) |
| not-umbrella-scope | pass | single fix in `core/security.py` |
| bounded-deliverable | pass | named file, xfail test H-05, 1-2hr estimate |
| not-stale-abandoned-prs | pass | no linked PRs |
| not-drive-by-feature | pass | maintainer-filed, bug/good-first-issue labels |
| good-first-issue-label (pref) | pass | label present |
| repro-or-acceptance (pref) | fail | no explicit Reproduction/Acceptance-criteria section noted in evidence, only a named xfail test |

→ **accept**, 1/2 preferred.

**Issue #57 — Tech detector counts vendored/build-output files**
| Check | Grade | Evidence |
|---|---|---|
| no-open-claim | pass | assignees: none; no open linked PRs |
| not-umbrella-scope | pass | single file `agent/tools/tech_detector.py` |
| bounded-deliverable | pass | repro snippet + named test names in body |
| not-stale-abandoned-prs | pass | no linked PRs |
| not-drive-by-feature | pass | maintainer-filed, bug/good-first-issue/agent labels |
| good-first-issue-label (pref) | pass | label present |
| repro-or-acceptance (pref) | pass | body includes a repro snippet |

→ **accept**, 2/2 preferred.

**Ranking (all three accepted):**
1. **#62** — ties on preferred checks (2/2) and best matches the fit profile: it's an API-layer bug directly involving Redis config (`redis_host` vs `redis_url`), continuing directly from the student's prior Tier-1 Redis session-state work in `agent/orchestrator.py`, with a clean repro path and one/two focused files.
2. **#57** — also 2/2 preferred, agent-layer (matches the preferred "agent" layer and prior agent-module experience), single file, repro snippet + named tests to extend.
3. **#72** — accepted but ranks last: only 1/2 preferred (no explicit repro/acceptance section in the evidence), and `core/security.py` sits outside the explicitly preferred agent/API/ingestion layers, though it's still a very tightly scoped fix.

```json
[
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/62",
    "checks": [
      {"name": "repo-not-archived", "grade": "pass", "evidence": "archived: no"},
      {"name": "repo-recent-activity", "grade": "pass", "evidence": "last push 2026-09-16 vs captured 2026-09-23 (7 days)"},
      {"name": "maintainer-reachable", "grade": "pass", "evidence": "no numeric sample, but last push within 120 days (sparse-sample fallback)"},
      {"name": "ai-not-outright-banned", "grade": "pass", "evidence": "CONTRIBUTING.md: no outright AI ban, standard fork/PR workflow"},
      {"name": "no-open-claim", "grade": "pass", "evidence": "assignees: none; no open linked PRs"},
      {"name": "not-umbrella-scope", "grade": "pass", "evidence": "bounded bug in api/routes/health.py vs core/config.py"},
      {"name": "bounded-deliverable", "grade": "pass", "evidence": "body includes Steps to reproduce for GET /health plus named files"},
      {"name": "not-stale-abandoned-prs", "grade": "pass", "evidence": "linked PRs: none"},
      {"name": "not-drive-by-feature", "grade": "pass", "evidence": "maintainer-filed cohort issue; labels bug/good first issue"},
      {"name": "good-first-issue-label", "grade": "pass", "evidence": "labels include good first issue"},
      {"name": "repro-or-acceptance", "grade": "pass", "evidence": "body has explicit Steps to reproduce"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/57",
    "checks": [
      {"name": "repo-not-archived", "grade": "pass", "evidence": "archived: no"},
      {"name": "repo-recent-activity", "grade": "pass", "evidence": "last push 2026-09-16 vs captured 2026-09-23 (7 days)"},
      {"name": "maintainer-reachable", "grade": "pass", "evidence": "no numeric sample, but last push within 120 days (sparse-sample fallback)"},
      {"name": "ai-not-outright-banned", "grade": "pass", "evidence": "CONTRIBUTING.md: no outright AI ban"},
      {"name": "no-open-claim", "grade": "pass", "evidence": "assignees: none; no open linked PRs"},
      {"name": "not-umbrella-scope", "grade": "pass", "evidence": "single file agent/tools/tech_detector.py"},
      {"name": "bounded-deliverable", "grade": "pass", "evidence": "body has repro snippet and named test names"},
      {"name": "not-stale-abandoned-prs", "grade": "pass", "evidence": "linked PRs: none"},
      {"name": "not-drive-by-feature", "grade": "pass", "evidence": "maintainer-filed; labels bug/good first issue/agent/tier-1"},
      {"name": "good-first-issue-label", "grade": "pass", "evidence": "labels include good first issue"},
      {"name": "repro-or-acceptance", "grade": "pass", "evidence": "body includes a repro snippet"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/72",
    "checks": [
      {"name": "repo-not-archived", "grade": "pass", "evidence": "archived: no"},
      {"name": "repo-recent-activity", "grade": "pass", "evidence": "last push 2026-09-16 vs captured 2026-09-23 (7 days)"},
      {"name": "maintainer-reachable", "grade": "pass", "evidence": "no numeric sample, but last push within 120 days (sparse-sample fallback)"},
      {"name": "ai-not-outright-banned", "grade": "pass", "evidence": "CONTRIBUTING.md: no outright AI ban"},
      {"name": "no-open-claim", "grade": "pass", "evidence": "assignees: none; no open linked PRs (classmate claim comments ignored per house rule)"},
      {"name": "not-umbrella-scope", "grade": "pass", "evidence": "single fix in core/security.py"},
      {"name": "bounded-deliverable", "grade": "pass", "evidence": "named file, xfail test H-05, 1-2 hour estimate"},
      {"name": "not-stale-abandoned-prs", "grade": "pass", "evidence": "linked PRs: none"},
      {"name": "not-drive-by-feature", "grade": "pass", "evidence": "maintainer-filed; labels bug/good first issue/api/tier-1"},
      {"name": "good-first-issue-label", "grade": "pass", "evidence": "labels include good first issue"},
      {"name": "repro-or-acceptance", "grade": "fail", "evidence": "no explicit Reproduction/Acceptance-criteria section noted, only a named xfail test"}
    ],
    "verdict": "accept"
  }
]
```

---

## Eval iterations

Quote source text directly in each field below. Paraphrase does not satisfy them.

**Run history**

1. Smoke run (`--limit 3`): **3/3** agreement.
2. First full run (20 issues): **17/20** — below the 18/20 bar; disagreements on issue-04, issue-14, issue-15.
3. Targeted re-run (`--only issue-04,issue-14,issue-15`) after rubric edits: **3/3**.
4. Confirming full run with `--save-run` (committed as `eval-run.txt`): **20/20** PASS, category floor met.

**Issue analysis**

**issue-15** (scored). Gold label: **reject**. Rubric (after adding `not-stale-abandoned-prs`): **reject**. The bundle shows the issue opened in 2021 with two linked PRs both `(closed)` and no open/merged PR, while the thread is years of claim/unassign cycles — a friendly label hiding a hard integration change. Gold and rubric agree the issue is not a realistic first contribution despite `good first issue`.

**Check rationale**

From `tools/issue-select/rubric.md`, check **`not-stale-abandoned-prs`**:

> Fail if the issue opened **>= 730 days** before capture **and** the linked-PR line lists **2+** PRs marked `(closed)` **and** lists **no** `(open)` or `(merged)` PR (multiple abandoned attempts). Otherwise pass.

I added this after the first full run wrongly **accepted** issue-15. The evidence guide’s “age and history” family says long-lived issues with abandoned PRs signal real difficulty; this check encodes that with countable thresholds on the repo-facts block instead of adjectives.

**Trade-offs**

The **`maintainer-reachable`** pass path that treats “no numeric response in the entire sample + last push within 120 days” as pass (added for issue-14) can accept repos where maintainers are active on code but silent on issues. I re-ran **`--only issue-07,issue-17`** on the confirming full run: both stayed **reject** because **`repo-recent-activity`** still fails on stale last-push dates, so dead-repo gold labels did not flip.

---

## Selection rationale

**Selection rationale**

1. **Fit and time:** Issue **#62** is tier-1 **api** work in `api/routes/health.py` and `core/config.py` — a bounded Redis configuration bug with explicit repro steps. It fits my Python/FastAPI background and the ~3–6 hours/week I have; the skill ranked it first for aligning with prior Redis-related Tier-1 work on the agent orchestrator.

2. **What the rubric gets right / what I weigh beyond it:** Required checks filtered liveness, policy, and scope; house rules correctly ignored classmates’ claim comments on #72 while still requiring no assignee/open linked PR. I also weighed the skill’s preferred-check tie-break (repro section present on #62 vs #72) and thread repro detail, which the rubric does not score as required.

3. **Claim difficulty:** Low–medium: clear `GET /health` repro, two focused modules, no design debate. Some classmates commented on related issues; per `scope.md` that does not block claiming — Unit 2 credit is on the PR I open.

---

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/issue-select/`.
