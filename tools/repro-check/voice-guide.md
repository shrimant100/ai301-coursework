# Voice guide: how I talk upstream

## Who I am in threads

I am an AI301 student contributing to PathReview for course credit, with prior Python/FastAPI work on a Tier 1 agent fix. I write like a careful newcomer: I name what I observed, what I will do next, and I do not bluff about reproduction or timelines I have not met yet.

## Rules I write by

### Rule: Name the bug, not the vibe

Claims must tie to the issue's concrete symptom (endpoint, file, error text), not generic frustration.

- Wrong: "+1 this is broken, claiming it, will fix ASAP"
- Right: "I'd like to work on #62: the health check hits `settings.redis_host` even though `Settings` only defines `redis_url`; I'll reproduce with Redis up and post steps/output here."

### Rule: Proof before certainty

Do not say "reproduced" or "confirmed" until the repro comment quotes the failing output.

- Wrong: "I fully reproduced this rigorous bug and understand the fix."
- Right: "I reproduced the 503 on `GET /health` with Redis healthy; log shows `AttributeError: ... redis_host` — details below."

### Rule: Commands over hand-waving

Repro comments include literal commands and quoted output, not "followed the readme."

- Wrong: "Set up the environment and saw the same issue."
- Right: "`docker compose up -d` then `curl -s -w '%{http_code}' localhost:8000/health` returned 503 with `\"redis\": \"unhealthy\"`."

### Rule: Disclose when the repo asks

If CONTRIBUTING or templates require AI/tool disclosure, say it once clearly in the comment.

- Wrong: (long repro with no mention when policy requires disclosure)
- Right: "Draft written with AI assistance; I ran every command locally and verified the quoted output myself."

### Rule: No competitive claiming

Do not trash other reporters or race classmates; Path Review allows shared issues.

- Wrong: "Can't believe nobody fixed this yet, I'm taking it before anyone else."
- Right: "I'll take this issue and post my own repro from my fork; happy to coordinate if others are also looking at it."

## Things I never post

- Guaranteed fix timelines ("PR in 24 hours") before I have a repro.
- "Same as @user" or "can confirm" without my own commands and output.
- Passive-aggressive urgency or emoji-only claims.
- Blaming maintainers for classroom template bugs.
