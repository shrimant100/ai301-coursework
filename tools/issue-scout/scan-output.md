## Scan read-out — 2026-11-06

**Funnel:** 3 strategy queries → q1 (GFI+python) returned 100, q2 (pytest/fastapi/api) returned **0**, q3 (help wanted+bug) returned 50 → 150 combined, 150 unique → dropped 21 assigned, 1 stale (>90d) → 128 survivors → ranked (GFI-first, updatedAt desc, fewer comments, 1-per-repo, fit tie-break) → **top 5 graded**. All five surfaced via **q1** and ranked on: carries `good first issue` label, most-recent `updatedAt`, 0 comments, and the 1-issue-per-repo diversity cap.

### Accepted (in fit order)

1. **`davidcasr/colombia-open#14`** — *add pytest tests for the atomic writer in `builders/formats.py`.* Bullseye for the fit profile: pure Python, pytest, one focused module, a named test template to copy, and verify commands. Preferred: GFI ✓, repro-or-acceptance ✗ (has "Cómo verificar" but no literal heading/checkbox).
2. **`btclib-org/btclib-wallet#705`** — *fix two silent-payment docstrings + pin a two-owner test.* Python, bounded, exact files+line ranges, a measured reproduction, and a "Done when" clause; the repo is explicitly LLM-based so AI work is welcome. Domain (silent payments) is subtle but scope is tight. Preferred: GFI ✓, repro-or-acceptance ✗ (same literalism gap).
3. **`alicangunduz/raggie#32`** — *configurable mock-LLM answer template.* Clean acceptance criteria + unit-test location, preferred 2/2 — but the code is **Go** (`mockllm.go`), so it ranks below the Python accepts per the fit profile.
4. **`tunguyen1993/kintsugi-harness#2`** — *passes every required check* (GFI label + OWNER opener trips the "Also pass" clause), **but it is a roadmap vote poll, not a code change.** Lowest fit; it's only here because the rubric accepts it as written.

### Rejected

- **`Scottcjn/rustchain-bounties#17182`** — sank on **`no-open-claim`**: two open linked PRs (`#17190`, `#17191`) are already active claims on this bounty.

```json
[
  {
    "item": "https://github.com/davidcasr/colombia-open/issues/14",
    "checks": [
      {"name": "repo-not-archived", "grade": "pass", "evidence": "repo archived: false"},
      {"name": "repo-recent-activity", "grade": "pass", "evidence": "pushed_at 2026-11-07, 0 days before scan"},
      {"name": "maintainer-reachable", "grade": "pass", "evidence": "no comment sample; last push within 120d (0d)"},
      {"name": "ai-not-outright-banned", "grade": "pass", "evidence": ".github/CONTRIBUTING.md 'Contribuir con agentes de IA' sets disclosure/understanding conditions, not a ban"},
      {"name": "no-open-claim", "grade": "pass", "evidence": "assignees none; no linked PRs"},
      {"name": "not-umbrella-scope", "grade": "pass", "evidence": "names src/builders/formats.py and tests/builders/test_formats.py"},
      {"name": "bounded-deliverable", "grade": "pass", "evidence": "1858-char body: named paths, 4 test cases, verify commands"},
      {"name": "not-stale-abandoned-prs", "grade": "pass", "evidence": "opened 2026-11-07 (<730d); no closed linked PRs"},
      {"name": "not-drive-by-feature", "grade": "pass", "evidence": "opener author_association OWNER"},
      {"name": "good-first-issue-label", "grade": "pass", "evidence": "labels include 'good first issue'"},
      {"name": "repro-or-acceptance", "grade": "fail", "evidence": "has 'Cómo verificar' but no Reproduction/Acceptance-criteria heading or - [ ] checklist"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/btclib-org/btclib-wallet/issues/705",
    "checks": [
      {"name": "repo-not-archived", "grade": "pass", "evidence": "repo archived: false"},
      {"name": "repo-recent-activity", "grade": "pass", "evidence": "pushed_at 2026-11-07, 0 days before scan"},
      {"name": "maintainer-reachable", "grade": "pass", "evidence": "no comment sample; last push within 120d (0d)"},
      {"name": "ai-not-outright-banned", "grade": "pass", "evidence": "CONTRIBUTING.md 'Development here is LLM-based... Humans are welcome'"},
      {"name": "no-open-claim", "grade": "pass", "evidence": "assignees none; no linked PRs"},
      {"name": "not-umbrella-scope", "grade": "pass", "evidence": "names src/btclib_wallet/silent_payments.py lines 765-771 and psbt/silent_payments.py lines 78-85"},
      {"name": "bounded-deliverable", "grade": "pass", "evidence": "1700-char body: named files/lines, measured repro, 'Done when' acceptance"},
      {"name": "not-stale-abandoned-prs", "grade": "pass", "evidence": "opened 2026-11-07 (<730d); no closed linked PRs"},
      {"name": "not-drive-by-feature", "grade": "pass", "evidence": "opener author_association MEMBER"},
      {"name": "good-first-issue-label", "grade": "pass", "evidence": "labels include 'good first issue'"},
      {"name": "repro-or-acceptance", "grade": "fail", "evidence": "'Done when:' + measured repro prose, but no literal heading or - [ ] checklist"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/alicangunduz/raggie/issues/32",
    "checks": [
      {"name": "repo-not-archived", "grade": "pass", "evidence": "repo archived: false"},
      {"name": "repo-recent-activity", "grade": "pass", "evidence": "pushed_at 2026-11-07, 0 days before scan"},
      {"name": "maintainer-reachable", "grade": "pass", "evidence": "no comment sample; last push within 120d (0d)"},
      {"name": "ai-not-outright-banned", "grade": "pass", "evidence": "CONTRIBUTING.md community-preview project, no AI ban; LLM refs are about the mock LLM"},
      {"name": "no-open-claim", "grade": "pass", "evidence": "assignees none; no linked PRs"},
      {"name": "not-umbrella-scope", "grade": "pass", "evidence": "names services/edge/internal/mockllm/mockllm.go (Answer)"},
      {"name": "bounded-deliverable", "grade": "pass", "evidence": "327-char body with explicit acceptance criteria + code pointers"},
      {"name": "not-stale-abandoned-prs", "grade": "pass", "evidence": "opened 2026-11-07 (<730d); no closed linked PRs"},
      {"name": "not-drive-by-feature", "grade": "pass", "evidence": "opener author_association OWNER"},
      {"name": "good-first-issue-label", "grade": "pass", "evidence": "labels include 'good first issue'"},
      {"name": "repro-or-acceptance", "grade": "pass", "evidence": "body has 'Acceptance criteria:' section"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/tunguyen1993/kintsugi-harness/issues/2",
    "checks": [
      {"name": "repo-not-archived", "grade": "pass", "evidence": "repo archived: false"},
      {"name": "repo-recent-activity", "grade": "pass", "evidence": "pushed_at 2026-11-07, 0 days before scan"},
      {"name": "maintainer-reachable", "grade": "pass", "evidence": "no comment sample; last push within 120d (0d)"},
      {"name": "ai-not-outright-banned", "grade": "pass", "evidence": "AGENTS.md agent instructions present, no ban in CONTRIBUTING.md"},
      {"name": "no-open-claim", "grade": "pass", "evidence": "assignees none; no linked PRs"},
      {"name": "not-umbrella-scope", "grade": "pass", "evidence": "no 'megaissue'/'tracking issue'; lists harness formats, not 8+ issue refs"},
      {"name": "bounded-deliverable", "grade": "pass", "evidence": "GFI label + opener OWNER triggers the 'Also pass' clause (body is a roadmap vote poll — see scan-notes)"},
      {"name": "not-stale-abandoned-prs", "grade": "pass", "evidence": "opened 2026-11-07 (<730d); no closed linked PRs"},
      {"name": "not-drive-by-feature", "grade": "pass", "evidence": "opener author_association OWNER"},
      {"name": "good-first-issue-label", "grade": "pass", "evidence": "labels include 'good first issue'"},
      {"name": "repro-or-acceptance", "grade": "pass", "evidence": "checklist with 5 '- [ ]' vote options (not true acceptance criteria — see scan-notes)"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/Scottcjn/rustchain-bounties/issues/17182",
    "checks": [
      {"name": "repo-not-archived", "grade": "pass", "evidence": "repo archived: false"},
      {"name": "repo-recent-activity", "grade": "pass", "evidence": "pushed_at 2026-11-07, 0 days before scan"},
      {"name": "maintainer-reachable", "grade": "pass", "evidence": "no comment sample; last push within 120d (0d)"},
      {"name": "ai-not-outright-banned", "grade": "pass", "evidence": "CONTRIBUTING.md bounty guide, no AI ban"},
      {"name": "no-open-claim", "grade": "fail", "evidence": "linked PRs #17190 and #17191 are both state=open (active claims)"},
      {"name": "not-umbrella-scope", "grade": "pass", "evidence": "docs-only fix naming WALLET_SETUP.md / INSTALL.md and installer paths"},
      {"name": "bounded-deliverable", "grade": "pass", "evidence": "3554-char body with deliverable + acceptance checklist"},
      {"name": "not-stale-abandoned-prs", "grade": "pass", "evidence": "opened 2026-11-07 (<730d); no closed linked PRs"},
      {"name": "not-drive-by-feature", "grade": "pass", "evidence": "opener author_association OWNER"},
      {"name": "good-first-issue-label", "grade": "pass", "evidence": "labels include 'good first issue'"},
      {"name": "repro-or-acceptance", "grade": "pass", "evidence": "body has 'Acceptance criteria' checklist with - [ ] items"}
    ],
    "verdict": "reject"
  }
]
```

---

## Direct grading — tracker picks (2026-11-08)

Graded with `issue-scout: grade` on the two issues claimed on the [AI301 Issue Selection](https://open-source-issue-tracker.onrender.com/) site (surfaced: **direct**).

### OWASP/Nest#5259 — **accept**

Bounded Python backend fix (`static.py` + tests). Rubric passes; thread is busy (~14 claim comments, several closed PRs) but no assignee and no **open** linked PR at grade time.

### apache/hamilton#74 — **reject**

**`no-open-claim` fail:** open PR [#1796](https://github.com/apache/hamilton/pull/1796) (`create-tests` for #74). Held on cohort tracker as backup; scout says do not take for OSS work while that PR is open.

```json
[
  {
    "item": "https://github.com/OWASP/Nest/issues/5259",
    "checks": [
      {"name": "repo-not-archived", "grade": "pass", "evidence": "archived: false"},
      {"name": "repo-recent-activity", "grade": "pass", "evidence": "last push 2026-11-08, same day as capture"},
      {"name": "maintainer-reachable", "grade": "pass", "evidence": "sparse-sample fallback: last push within 120 days (today)"},
      {"name": "ai-not-outright-banned", "grade": "pass", "evidence": "CONTRIBUTING.md silent on AI; no ban phrase"},
      {"name": "no-open-claim", "grade": "pass", "evidence": "assignees none; all cross-referenced PRs closed, none open"},
      {"name": "not-umbrella-scope", "grade": "pass", "evidence": "single file static.py, one dict entry"},
      {"name": "bounded-deliverable", "grade": "pass", "evidence": "repro + named path + good first issue label"},
      {"name": "not-stale-abandoned-prs", "grade": "pass", "evidence": "opened 2026-07-20, ~111 days < 730"},
      {"name": "not-drive-by-feature", "grade": "pass", "evidence": "labels present; opener CONTRIBUTOR"},
      {"name": "good-first-issue-label", "grade": "pass", "evidence": "labels: good first issue"},
      {"name": "repro-or-acceptance", "grade": "pass", "evidence": "body has To Reproduce section"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/apache/hamilton/issues/74",
    "checks": [
      {"name": "repo-not-archived", "grade": "pass", "evidence": "archived: false"},
      {"name": "repo-recent-activity", "grade": "pass", "evidence": "last push 2026-11-07"},
      {"name": "maintainer-reachable", "grade": "pass", "evidence": "last push within 120 days; skrawcz active in thread"},
      {"name": "ai-not-outright-banned", "grade": "pass", "evidence": "CONTRIBUTING.md silent on AI"},
      {"name": "no-open-claim", "grade": "fail", "evidence": "open PR #1796 'create-tests command (#74)' by Kulraj69, open since 2026-11-01"},
      {"name": "not-umbrella-scope", "grade": "pass", "evidence": "single bounded CLI feature"},
      {"name": "bounded-deliverable", "grade": "pass", "evidence": "detailed spec + good first issue label"},
      {"name": "not-stale-abandoned-prs", "grade": "pass", "evidence": "open PR #1796 present"},
      {"name": "not-drive-by-feature", "grade": "pass", "evidence": "labeled + maintainer comments"},
      {"name": "good-first-issue-label", "grade": "pass", "evidence": "labels: good first issue, help wanted"},
      {"name": "repro-or-acceptance", "grade": "fail", "evidence": "feature request, no repro/acceptance checklist"}
    ],
    "verdict": "reject"
  }
]
```
