# Step 11 evidence — #62 Redis health (for plan-and-implement.md → Evidence)

Paste the blocks below into **Evidence** on the coursework form (edit as needed if you re-run with Docker up).

## Before (main @ f89c06f — broken Redis probe)

Command (TestClient against app, same trigger as Unit 2 `GET /health`):

```
python -c "from fastapi.testclient import TestClient; from api.main import app; r = TestClient(app).get('/health'); print('HTTP', r.status_code); d = r.json()['detail']['dependencies']; print('redis:', d['redis'])"
```

Relevant log line:

```
redis_health_check_failed error="'Settings' object has no attribute 'redis_host'"
```

Output:

```
HTTP 503
redis: unhealthy
```

## After (branch `fix/62-redis-health-redis-url`)

**Automated (unit test):**

```
pytest tests/unit/test_health.py -v
```

```
tests/unit/test_health.py::test_redis_health_check_uses_redis_url PASSED
```

**Integration-style (`GET /health` with fix, Redis not running):** probe reaches the network layer instead of `AttributeError`:

```
redis_health_check_failed error='Error 10061 connecting to localhost:6379. ...'
HTTP 503
redis: unhealthy
```

**With Redis up** (re-run on branch `fix/62-redis-health-redis-url`):

```
docker compose exec -T redis redis-cli ping
PONG

python -c "from fastapi.testclient import TestClient; from api.main import app; r = TestClient(app).get('/health'); print('HTTP', r.status_code); print(r.json()['detail']['dependencies'])"
```

Log:

```
redis_health_check_passed
```

Output:

```
HTTP 503
{'postgres': 'unhealthy', 'redis': 'healthy', 'vector_db': 'healthy'}
```

Redis is **healthy** after the fix; HTTP 503 remains because of the separate Postgres/SQLAlchemy probe (#61), as noted in the plan.
