# OWASP/Nest — CONTRIBUTING.md notes (issue #5259)

- **Stack:** Django backend + Next.js frontend; **Docker required**; Windows contributors expected to use **WSL** (not PowerShell) for `make run` / `make check` / `make test`.
- **Before PR:** ask maintainers to **assign** the issue; run **`make check-test`** locally; address CodeRabbit/SonarQube comments; draft PR → ready for review.
- **AI:** no ban on AI-assisted work in CONTRIBUTING for issue comments; PR template may ask about AI (disclose in draft).
- **Tests:** backend coverage thresholds in `pyproject.toml`; add tests for new/changed backend code (`static_test.py` path fits issue).
