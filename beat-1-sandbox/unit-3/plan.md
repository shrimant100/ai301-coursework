# Plan: #62 — Redis health check uses missing `settings.redis_host`

## Reproduction evidence I am building on

From my Unit 2 repro on this issue (Redis reachable, health route still marks Redis unhealthy):

- `docker compose exec -T redis redis-cli ping` → `PONG`
- `settings.redis_url` is `redis://localhost:6379/0`; `settings.redis_host` raises `AttributeError: 'Settings' object has no attribute 'redis_host'`
- `GET /health` → HTTP 503 with `"redis": "unhealthy"`
- Server log: `redis_health_check_failed error="'Settings' object has no attribute 'redis_host'"`

That matches the issue: the probe never reaches Redis because it reads attributes `Settings` does not define.

## Diagnosis

In `api/routes/health.py`, the Redis branch builds `redis.Redis(host=settings.redis_host, port=settings.redis_port, ...)`. `Settings` in `core/config.py` defines only `redis_url` (from `REDIS_URL` / `.env`). Accessing `redis_host` raises `AttributeError` inside the `try` block; the broad `except Exception` logs `redis_health_check_failed` and marks Redis unhealthy even when Redis is up (as shown by `PONG` and `Redis.from_url(settings.redis_url).ping()` in the repro).

## Scope

**In scope:** `api/routes/health.py` — construct the Redis client from `settings.redis_url` (same pattern as elsewhere in the codebase that connects via URL).

**Out of scope:** Adding `redis_host` / `redis_port` fields to `Settings`; fixing the separate Postgres probe failure (`SELECT 1` / SQLAlchemy 2.x, issue #61); vector DB or other routes.

## Approach

1. Replace the `host=` / `port=` constructor with `redis.Redis.from_url(settings.redis_url, decode_responses=True)` (or equivalent `from_url` call with the same decode behavior).
2. Keep the existing `ping()` and success/failure logging; only change how the client is created.
3. Add a focused unit test under `tests/unit/` that exercises the Redis branch with a patched client or settings so a reachable URL reports `"redis": "healthy"` when other dependencies are mocked or isolated — without requiring a live Redis in CI if mocks suffice.

## Test plan

1. **Re-run Unit 2 repro** on the branch: `docker compose up -d redis`, start the app, `GET /health`. With Redis up, expect `"redis": "healthy"` and no `redis_host` `AttributeError` in logs. (Overall status may still be 503 if Postgres probe fails separately; I will quote the Redis dependency field and the Redis log line as the pass/fail signal for this fix.)
2. **Automated:** new unit test for the health route's Redis path — mock `redis.Redis.from_url` to return a client whose `ping()` succeeds and assert the response marks Redis healthy (and that `from_url` was called with `settings.redis_url`).

## Deviations

No change to the approach: Redis client uses `Redis.from_url(settings.redis_url)` as planned. Removed the mypy `attr-defined` suppression for `api.routes.health` because #62 is fixed (per CONTRIBUTING).
