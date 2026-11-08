## Environment

- **OS:** Windows 11 (build 26200)
- **Repo:** `shrimant100/Nest` at commit `9cfebd7` (shallow clone of `main`, 2026-11-08)
- **Tooling:** Docker Desktop **24.0.6** installed; daemon was **stopped** during this repro (full `make backend-test-unit` deferred until WSL + Docker are up per `CONTRIBUTING.md`)
- **Python:** 3.12 (Windows store) for the helper script below only

## Steps to reproduce

1. Clone the fork and inspect `StaticSitemap.lastmod()` mapping vs `STATIC_ROUTES`:

   ```powershell
   git clone https://github.com/shrimant100/Nest.git
   cd Nest
   git rev-parse HEAD
   ```

2. Run the route-map repro helper (reads the real files under `backend/src/apps/sitemap/views/`):

   ```powershell
   python beat-1-sandbox\unit-6\repro_static_route_check.py
   ```

   (Run from `ai301-coursework` with sibling clone `..\Nest`.)

3. **Expected (issue):** `/repositories` should use `Repository.objects.aggregate(Max("updated_at"))` like `/projects` and `/chapters`.

4. **Actual (observed):** `/repositories` is the only static route not present in `path_to_model`, so `lastmod()` takes the `datetime.now(UTC)` branch — same failure mode as `/unknown-path` in `test_lastmod_unmapped_path_returns_current_time`.

## Quoted output

```text
STATIC_ROUTES (8): /chapters, /committees, /contribute, /members, /organizations, /projects, /repositories, /snapshots
path_to_model keys (7): /chapters, /committees, /contribute, /members, /organizations, /projects, /snapshots
unmapped static routes: ['/repositories']

Simulated StaticSitemap.lastmod branch (missing key => datetime.now fallback):
  /repositories: datetime.now(UTC) => 2026-11-08T23:29:36.894485+00:00
  /projects: would call model.objects.aggregate(Max('updated_at'))
  /chapters: would call model.objects.aggregate(Max('updated_at'))
```

## Next step (not posted upstream)

Once Docker Desktop is running in WSL, I will regenerate the static sitemap and compare `<lastmod>` for `/repositories` vs `/chapters` as in the issue thread before opening a PR.

(Draft written with AI assistance; I ran the commands and verified the quoted output locally.)
