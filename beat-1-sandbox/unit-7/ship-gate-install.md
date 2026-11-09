# Unit 7 ship-gate install (2026-11-08)

- Materials: `ai301-unit7-starter` cloned under `CodePath`.
- Install: `python skill/install.py --repo c:\Users\shrim\IdeaProjects\CodePath\Nest`
- `~/.claude/ship-gate/` installed; `pr-precheck/scope.md` swapped to live (`scope.md.sandbox` kept).
- Nest clone: `ship-manifest.md`, `plan.md`, `test_evidence.md`, `pr_draft.md` on `.git/info/exclude`.
- Hook test (simulated `gh pr create --help`): **voice-guard STOP** + **ship-gate: STOP.** (exit 2 each).
- `settings.json` ship-gate hook uses `python` (Windows), not `python3`.

## Manifest (`Nest/ship-manifest.md`)

| Check | Command |
|---|---|
| Static analysis | `make check` |
| Checks + backend tests | `make check-test-backend` |
| Backend unit tests | `make backend-test-unit` |

Requires **Docker daemon running** + **bash** (Nest `Makefile` uses `SHELL := bash`). Prefer WSL per CONTRIBUTING before heavy check runs.
