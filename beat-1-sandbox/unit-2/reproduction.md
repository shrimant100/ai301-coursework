# Unit 2 — Claim and Reproduce

Path: `beat-1-sandbox/unit-2/reproduction.md`

Record of your claim and reproduction on the issue you chose in Unit 1, and of the
evaluation runs that produced `eval-run.txt`. This file is graded at the path above; a copy
kept anywhere else in the repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the wrong
label is not graded.

---

## Your identity upstream

**GitHub username**

shrimant100

---

## Posted upstream

**Claim comment**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/62#issuecomment-5902882065

I'd like to investigate #62 as my AI301 Path Review contribution.

From reading the code, the Redis probe in `api/routes/health.py` builds its client with `settings.redis_host` and `settings.redis_port`, while `Settings` in `core/config.py` only defines `redis_url`. I expect `GET /health` to return 503 with `"redis": "unhealthy"` and a `redis_health_check_failed` log mentioning `AttributeError` for `redis_host`, even when Redis itself is reachable.

I have not run a local repro yet. Next I will clone my fork, start Redis with `docker compose`, call `GET /health`, and post my environment, exact commands, and the response and log lines I observe in a follow-up comment.

**Reproduction comment**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/62#issuecomment-5902972213

Reproduced on my fork `shrimant100/pathreview` at commit `755267d6` (local tree on branch `fix/43-clear-agent-session-state`; the Redis probe in `api/routes/health.py` at this commit still reads `settings.redis_host` / `settings.redis_port`).

**Environment:** Windows 10 (10.0.26200), Python 3.12.10 (`.venv`), FastAPI 0.139.2, redis-py 8.0.1, uvicorn 0.51.0, SQLAlchemy 2.0.51. Backing services via `docker compose up -d db redis` (`postgres:16-alpine` on host port 5433, `redis:7-alpine` on 6379). App run with `.venv/Scripts/python.exe -m uvicorn api.main:app --host 127.0.0.1 --port 8000`.

**Steps**

1. `docker compose up -d db redis`
2. Confirm Redis is reachable independently of the health route:

```
$ docker compose exec -T redis redis-cli ping
PONG
```

3. Confirm `Settings` exposes `redis_url` but not `redis_host`:

```
$ .venv/Scripts/python.exe -c "from core.config import settings; print('redis_url:', settings.redis_url); print('has redis_host:', hasattr(settings, 'redis_host')); settings.redis_host"
redis_url: redis://localhost:6379/0
has redis_host: False
AttributeError: 'Settings' object has no attribute 'redis_host'
```

4. Start the API and call the issue's trigger endpoint:

```
$ .venv/Scripts/python.exe -m uvicorn api.main:app --host 127.0.0.1 --port 8000
$ curl.exe -s -w "\nHTTP_STATUS:%{http_code}\n" http://127.0.0.1:8000/health
{"detail":{"status":"unhealthy","dependencies":{"postgres":"unhealthy","redis":"unhealthy","vector_db":"healthy"},"safety_events_last_hour":0,"timestamp":"2026-09-30T02:35:51.168286"}}
HTTP_STATUS:503
```

Server log for that request:

```
redis_health_check_failed error="'Settings' object has no attribute 'redis_host'" request_id=bbead8cd-d1e9-40cc-85f5-182130162c86
```

Control: Redis answers through the field that actually exists on `Settings`:

```
$ .venv/Scripts/python.exe -c "import redis; from core.config import settings; print(redis.Redis.from_url(settings.redis_url, decode_responses=True).ping())"
True
```

**Expected:** With Redis running and reachable, `GET /health` should report `"redis": "healthy"`.

**Actual:** HTTP 503 with `"redis": "unhealthy"` because `health_check()` accesses `settings.redis_host` before any Redis connection attempt; the broad `except Exception` logs `redis_health_check_failed` with the `AttributeError` above.

**Note:** The same response also shows `"postgres": "unhealthy"` with a separate SQLAlchemy 2.x raw-string error in the log. That is unrelated to #62 (same pattern as other repros on this issue); the Redis log line and the missing-attribute control run are the evidence for this bug.

## Eval iterations

Answer all four sections. Quote source text directly; paraphrase does not satisfy these
fields.

**Run history**

1. Calibration (`--include-calibration --only calib-02,calib-03`): both packages agree with gold (informal warm-up, not scored).
2. Smoke (`--limit 3`): **2/3** — disagreed on **pkg-03** (`policy-disclosure`).
3. First full run (20 packages): **18/20** — disagreed on **pkg-16** and **pkg-19**; category floor not met.
4. Targeted canaries after rubric edits (`--only pkg-01,pkg-03,pkg-16,pkg-19,pkg-20`): **5/5**.
5. Confirming full run with `--save-run` (committed as `eval-run.txt`): **20/20** PASS, category floor met.

**Package analysis**

**pkg-20** (scored, category `disclosure`). Gold label: **reject**. Rubric: **reject**. The bundle’s repro report passes the proof checks, but repo facts require disclosing all AI usage in issues/comments with tool and extent stated; neither the claim nor the repro comment discloses. My `policy-disclosure` check fails that gap on purpose so the eval set’s single-item disclosure category is not invisible.

**Check rationale**

From `tools/repro-check/rubric.md`, check **`policy-disclosure`**:

> Fail only when policy **explicitly requires disclosing AI/tool usage** in issues or comments and **neither** comment discloses — eval packages are graded as if the student used AI assistance and must meet that disclosure bar when the repo demands it.

I added the human-authorship vs disclosure-required split after **pkg-03** flipped to reject on the first smoke run: ripgrep’s policy asks for human-written comments, not an AI disclosure tag, so generic “treat every AI mention as require disclosure” was wrong-target for gold **accept** on **pkg-03** while still catching ghostty **pkg-20**.

**Trade-offs**

After tightening **`environment-sufficient`** for version skew, I re-ran **`--only pkg-01,pkg-03,pkg-16,pkg-19,pkg-20`**: **pkg-01** and **pkg-03** stayed **accept**, **pkg-16**/**pkg-19** moved to **reject** to match gold, and **pkg-20** stayed **reject** on disclosure — so the policy fix did not silently drop the disclosure floor before the confirming full run.

---

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/repro-check/`.
