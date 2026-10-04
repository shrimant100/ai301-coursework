# Unit 3 — Plan and Build

Path: `beat-1-sandbox/unit-3/plan-and-implement.md`

Record of your plan, the branch you built it on, and the evaluation runs that produced
`eval-run.txt`. This file is graded at the path above; a copy kept anywhere else in the
repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the wrong
label is not graded.

---

## Posted upstream

**GitHub username**

shrimant100

**Plan comment**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/62#issuecomment-5984477760

Plan for #62 (builds on my Unit 2 repro on this thread):

**Cause:** `health_check()` in `api/routes/health.py` constructs Redis with `settings.redis_host` / `settings.redis_port`, but `Settings` only defines `redis_url`, so the probe raises `AttributeError` before `ping()` and always reports `"redis": "unhealthy"`.

**Fix (bounded):** Build the client with `Redis.from_url(settings.redis_url, decode_responses=True)` in that route only; add a small unit test on the Redis branch; re-run my repro (`PONG` + `GET /health`) and expect `"redis": "healthy"` with no `redis_host` error in the log. Not tackling the separate Postgres/SQLAlchemy issue in the same 503 response.

Full plan with quoted repro evidence is in my next steps on the branch `fix/62-redis-health-redis-url`; PR to follow after tests pass locally.

---

## Your branch

**Branch**

fix/62-redis-health-redis-url

**Evidence**

**Before (main, broken probe):**

```
redis_health_check_failed error="'Settings' object has no attribute 'redis_host'"
HTTP 503
redis: unhealthy
```

**After (branch fix/62-redis-health-redis-url):**

```
pytest tests/unit/test_health.py -v
# test_redis_health_check_uses_redis_url PASSED

docker compose exec -T redis redis-cli ping
PONG

redis_health_check_passed
HTTP 503
dependencies: postgres=unhealthy, redis=healthy, vector_db=healthy
```

(Full commands in `step-11-evidence.md` in this folder.)

## Eval iterations

Answer all four sections. Quote source text directly; paraphrase does not satisfy these
fields.

**Run history**

1. Calibration (`--include-calibration --only calib-01,calib-03`): both packages agree with gold (warm-up, not scored).
2. Confirming full run with `--save-run` (committed as `eval-run.txt`): **20/20** PASS; category floor met (`clear-accept 7/7`, `scope-creep 4/4`, `thread-convention 2/2`, `unbuildable 3/3`, `wrong-cause 4/4`).

**Package analysis**

**pkg-06** (scored, category `scope-creep`). Gold label: **reject**. Rubric: **reject**. The repro pins an empty tar on `minikube image save` for preloaded containerd images, but the candidate plan turns that into a five-part pipeline rewrite (preload regeneration, containerd bump, unified image abstraction, error surfacing, CI matrix) across preload scripts, all three runtimes, and workflows. **`scope-bounded`** fails the “multi-front campaign beyond what the issue and repro require” condition, matching gold’s scope-creep label.

**Check rationale**

From `tools/plan-check/rubric.md`, check **`scope-bounded`**:

> Pass if the plan names **at least one concrete change target** (file, module, function, or doc surface) **and** at least one explicit **out-of-scope** boundary for this fix. Fail if there is no named target, or the fix is wrapped in a multi-front campaign (migrations, printer rewrites, new frameworks, "while we're here" refactors) beyond what the issue and repro require.

I kept this wording from the Unit 3 template and evidence guide so eval **`scope-creep`** packages (like **pkg-06**, **pkg-12**, **pkg-15**, **pkg-19**) reject on an observable list of fronts instead of a vague “too big” judgment.

**Trade-offs**

**`scope-bounded`** is strict about “while we’re here” refactors: a plan that names one file but also schedules unrelated runtime upgrades still fails, which is why **pkg-06** stays **reject**. I did not loosen it to “any named file passes,” because that would let **pkg-12**-style creep through; the confirming **20/20** full run is the check that the threshold still aligns with gold on the other scope-creep items.

---

Related paths: `plan.md` and `eval-run.txt` in this directory; your skill's files in
`tools/plan-check/`.
