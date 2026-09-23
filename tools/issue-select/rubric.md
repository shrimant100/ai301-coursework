# Rubric: is this a good first issue?

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| `repo-not-archived` | Repo facts line `archived:` | Pass if `archived: no`. Fail if `archived: yes`. | required |
| `repo-recent-activity` | Repo facts: `last push to any branch` date and/or dates on `last 5 default-branch commits` lines; compare to the bundle `captured:` date | Pass if **either** last push is within **120 days** of capture **or** the newest of the five listed default-branch commit dates is within **120 days** of capture. | required |
| `maintainer-reachable` | Repo facts block `maintainer first-response sample` and `last push to any branch` vs bundle `captured:` date | Pass if at least one sample line shows a numeric response time ending in `days` with value **<= 90**. **Also pass** if no sample line shows any numeric `days` value and `last push to any branch` is within **120 days** of capture (sparse sample but living repo). Otherwise fail. | required |
| `ai-not-outright-banned` | Repo facts `contribution policy` line (and text it quotes) | **Fail** if policy explicitly forbids AI-generated contributions outright (e.g. phrases like `do not accept AI-generated`, `does not accept AI-generated`, `we do not accept AI-generated code`). **Pass** if policy is silent, only sets disclosure/review conditions, or welcomes AI with responsibilities. `AGENTS.md`-style agent instructions alone are not a ban. | required |
| `no-open-claim` | Repo facts `this issue: assignees:` and `linked PRs:` | Pass if assignees are `none` **and** the linked-PR list contains **no** `(open)` PR. Fail if an assignee is named or any linked PR is open. (Path Review live mode: still fail on assignee/open linked PR; ignore classmates' claim **comments** per `scope.md`.) | required |
| `not-umbrella-scope` | Issue title and body | Fail if title contains `megaissue` (any case) **or** body contains `tracking issue` / `megaissue` **or** title+body together describe work across the **whole codebase** without naming a specific file or module (e.g. `to the codebase` plus `incremental` / `throughout` / `anywhere in the codebase`) **or** the body is mainly a list of **8+** other issue references (`#1234` bullets). Otherwise pass. | required |
| `bounded-deliverable` | Issue body (and title), labels line, opener association in issue header | Pass if the issue asks for one concrete change with enough detail to start (>= **80** characters in the body, or repro / acceptance criteria / named paths). **Also pass** if labels include `good first issue` (case-insensitive) and opener association is **OWNER**, **MEMBER**, or **COLLABORATOR** (short maintainer-filed GFIs are bounded). Fail if it is only a usage/support question with no code change requested. | required |
| `not-stale-abandoned-prs` | Repo facts `linked PRs:` and issue opened date in the issue header vs bundle `captured:` date | Fail if the issue opened **>= 730 days** before capture **and** the linked-PR line lists **2+** PRs marked `(closed)` **and** lists **no** `(open)` or `(merged)` PR (multiple abandoned attempts). Otherwise pass. | required |
| `not-drive-by-feature` | Issue header (opener association), labels line, Comments | Fail if opener association is `NONE` or contains `bot` **and** labels are `none` or empty **and** there is no comment from `OWNER`, `MEMBER`, or `COLLABORATOR`. Otherwise pass (includes maintainer-filed issues, labeled bugs/docs, and community issues with maintainer replies). | required |
| `good-first-issue-label` | Issue labels line | Pass if labels include `good first issue` or `Good first issue` (case-insensitive substring). | preferred |
| `repro-or-acceptance` | Issue body | Pass if body contains a `Reproduction`, `Steps to reproduce`, `Acceptance criteria`, or checklist section with at least two `- [ ]` items. | preferred |

## Verdict rule

**Accept** only if every **required** check passes.

**Reject** if any required check fails or is **unclear** (unclear counts as fail).

**Preferred** checks never change accept/reject; they only rank multiple accepted issues (more preferred passes = better fit).

When grading several live URLs, grade each independently, then rank accepted issues using preferred checks and the fit profile in `scope.md`.
