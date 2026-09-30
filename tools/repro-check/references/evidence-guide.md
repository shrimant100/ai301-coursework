# Evidence guide: where proof lives in a reproduction package

## Environment

**Where it lives.** Eval bundle: the **Candidate repro report** (look for Environment / Setup / versions). Live mode: the student's **repro draft** (`repro.md` or pasted comment body). Issue context may state target versions to compare against.

**What good looks like.** A stranger could recreate the runtime: OS (and arch if relevant), tool or app version, install path or commit SHA, and any services that must be running (DB, Redis, Docker compose). If the issue names a version, the repro either matches it or explicitly says what differed and why the test still applies. When the issue or thread says the bug is confirmed on **latest/main/current**, compare the repro's primary tool version to **latest release** in repo facts and to versions cited in the issue/thread; a large gap without acknowledgment is not sufficient evidence about the filed bug.

## Steps

**Where it lives.** Eval bundle: **Candidate repro report** steps, execution, or preparation sections. Live mode: repro draft body. Issue context describes the trigger to match.

**What good looks like.** Steps start from a stated baseline ("repo cloned at SHA", "docker compose up", "venv activated") and include copy-paste commands or exact UI clicks through the trigger. "I ran the app" alone is not followable.

## Behavior shown

**Where it lives.** Eval bundle: quoted blocks in the **Candidate repro report**; issue **actual behavior** / stack trace in the Issue section. Live mode: repro draft quotes; live issue page for the reporter's described symptom.

**What good looks like.** Artifacts are read **against the issue**: same input/trigger as the issue, and quoted output shows the same failure mode (message, panic line, HTTP field values). A different error on a edited input is adjacent behavior, not proof of the filed bug.

## Honesty

**Where it lives.** Eval bundle: repro report **Analysis / Expected / Actual** and the **Candidate claim comment** if it asserts reproduction. Live mode: both drafts.

**What good looks like.** Conclusions stay within what artifacts show. "Cannot reproduce on main at SHA X after steps Y" with quoted output is a pass. "Confirms the bug" when artifacts show a different error is a fail.

## Comms

**Where it lives.** Eval bundle: **Candidate claim comment**, **Candidate repro report**, and repo facts **contribution policy** (and any quoted AI/disclosure rules). Live mode: claim/repro drafts; repo `CONTRIBUTING.md` or template on GitHub.

**What good looks like.** Claim comments name the specific failure and honest next steps (investigate, post repro soon). They avoid generic "+1 claiming", assign-me flattery, or guaranteed fix timelines without naming the concrete bug (symptom, file, endpoint, trigger). Read the repo-facts **contribution policy** line for two different AI rules: (1) **Disclosure required** — policy says to state the tool and extent of AI help in issues/comments; the draft must say so plainly. (2) **Human authorship only** — policy bans AI-generated maintainer comments but does not ask for a disclosure tag; specific, human-voiced claim and repro text satisfies that rule without an extra disclaimer.
