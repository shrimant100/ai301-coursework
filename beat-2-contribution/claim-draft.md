Hi — I'd like to work on this issue for an open-source contribution (AI301).

**What I understand:** `/repositories` is in `STATIC_ROUTES` but missing from `path_to_model` in `backend/src/apps/sitemap/views/static.py`, so `StaticSitemap.lastmod()` falls back to `datetime.now(UTC)` instead of the latest `Repository.updated_at`.

**First step (this week):** fork Nest, set up the backend per `CONTRIBUTING.md` (Docker/WSL), and run the existing sitemap/static tests so I can reproduce the wrong `<lastmod>` behavior before changing code.

**Plan:** add `"/repositories": Repository` (with the import) and extend `static_test.py` so every `STATIC_ROUTES` path maps to a model — matching the issue's regression ask.

**Report back:** I'll comment here with setup notes and either repro output or a draft PR link within ~2 weeks.

I see several earlier volunteers on this thread; if a maintainer already has someone assigned or an open PR in flight, I'll step back — otherwise could you assign #5259 to me (`shrimant100`)?

(Draft written with AI assistance; I will run the commands and verify behavior locally.)
