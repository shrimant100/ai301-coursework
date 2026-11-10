# Unit 8 steps 1–3 (2026-11-09)

## 1. Materials

Cloned `ai301-unit8-starter` → `CodePath\ai301-unit8-starter`.

## 2. Install

```powershell
mkdir $env:USERPROFILE\.claude\pr-monitor
copy ai301-unit8-starter\skill\* $env:USERPROFILE\.claude\pr-monitor\
copy playbook-template.md → playbook.md (first time only)
```

Installed: `monitor.py`, `move-forms.md`, `playbook-template.md`, `playbook.md`, `INSTALL.md`.

## 3. `--state` (from Nest clone, branch `fix/5259-repositories-sitemap-lastmod`)

- **PR:** https://github.com/OWASP/Nest/pull/5818
- **State:** CLOSED (not merged)
- **Review:** REVIEW_REQUIRED; mergeable MERGEABLE, merge state BLOCKED
- **Checks:** 1 failing, 3 passing, 2 skipped
- **Playbook:** not ready — fill response rules, staleness thresholds, nudge etiquette, walk-away criteria before a full run

`gh repo set-default OWASP/Nest` may warn inside the fork clone (“does not correspond to any git remotes”); run from another directory or rely on `gh` auth — monitor still resolved the PR by branch.

## Step 5 full run (2026-11-09)

On Windows, set `$env:PYTHONUTF8=1` before `monitor.py` (unicode in prompt).

- **Move:** No-send — wait (7-day issue threshold not met)
- **Draft:** `~/.claude/pr-monitor/drafted-move.md` — wait on #5259; bot closed PR (unassigned, unsigned commit / no `Signed-off-by`); fix mechanics on branch before reopen
- **Do not post** the draft as-is (step 6)
