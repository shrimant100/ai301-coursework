# repro-check (manual, 2026-11-08)

Graded `claim-draft.md` + `repro-draft.md` against live issue #5259 and `~/.claude/skills/repro-check/rubric.md`.

**Verdict: accept** (all required checks pass).

| Check | Result |
|-------|--------|
| environment-sufficient | pass — Windows 11, commit `9cfebd7`, Docker 24.0.6 named |
| steps-copy-pasteable | pass — `git rev-parse`, `python …/repro_static_route_check.py` |
| repro-has-artifacts | pass — quoted route map + simulated `lastmod` branch |
| trigger-faithful | pass — repro exercises the same `StaticSitemap.lastmod()` path the issue names (sitemap XML compare deferred honestly) |
| symptom-matches-issue | pass — `/repositories` uses `datetime.now(UTC)` fallback vs model aggregate on other routes |
| expected-and-actual-paired | pass |
| claim-honest-intent | pass (full package) |
| analysis-not-overclaim | pass — defers full XML sitemap until Docker/WSL |
| policy-disclosure | pass — AI disclosure present |

**Polish:** run `make backend-test-unit` in WSL once Docker Desktop is running to attach pytest output before the PR description.
