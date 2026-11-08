# Scope: where to look, and who is looking

<!--
This is the real-world scope. It replaces the sandbox scope.md in
your installed skill: the field is no longer the Path Review repo,
and the house rules do not travel. Like every scope file, this one is
the skill's field of view: the rubric (rubric.md) decides whether an
issue is GOOD; the scope decides which issues are candidates at all,
and the strategy (search-strategy.md) decides where the scout
actually walks. Live mode only: in eval mode the bundle is the whole
world and this file is ignored.
-->

## Where candidates come from

Any public repository. The sandbox is behind you; the field is now
all of GitHub, and your fit profile below is what keeps that
searchable. Start from repos in languages and tools you named there,
and let the profile steer where you search, not just how results are
ranked.

**Claims count again.** The Path Review house rule does not travel.
Out here a claim comment or an assignee is a stranger who got there
first, and you have no channel to coordinate with them. Read claim
signals exactly as the rubric's checks state them; do not carry the
classroom habit of claiming over someone.

**Claim upstream the moment you commit.** The rule cuts both ways:
the instant you decide to take an issue, say so on the issue itself
(a short comment: what you plan to do and roughly when). You are now
the claim signal someone else's skill will read. Deciding privately
and claiming later is how two strangers do the same work twice.

## Your fit profile

I am most comfortable in **Python backend** work (FastAPI, pytest, Docker,
SQLAlchemy/Redis-style service code) after a bounded PathReview fix on
health checks and agent session code. I want **good first issue** (or
similar newcomer-labeled) tasks with a clear repro, one or two focused
modules, and unit tests I can extend—not umbrella refactors,
frontend-heavy UI, or cross-cutting RAG/agent architecture work.

**Search steering (languages & areas):** Python repos; API routes,
health/ingestion/agent layers; CLI or library bugs with quoted stack
traces. I will run queries on **`language:Python`** plus **good first
issue** labels, and a second pass with **pytest / FastAPI / API** keywords
in title or body when I need narrower signal.

**Avoid:** issues already **assigned**, mega-issues and "refactor the
codebase" threads, stale repos with no maintainer response, drive-by
features with no repro, and non-Python-primary repos unless the issue body
is explicitly a small Python tooling fix.

Fit **ranks** rubric accepts and **steers** queries; it never overrides
a rubric reject or accept.
