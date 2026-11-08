# Search strategy: where your scout looks, and why

## Queries

<!-- Each line is a real gh invocation; comment names the fit-profile sentence. -->

# Python-primary repos with the standard newcomer label (search steering: Python + GFI).
gh search issues --label "good first issue" --language python --state open --limit 100 --json title,repository,labels,assignees,commentsCount,updatedAt,url

# Same pool, issues that say pytest/FastAPI/API in title or body (backend layers I named).
gh search issues "pytest OR fastapi OR api" --label "good first issue" --language python --state open --match title,body --limit 75 --json title,repository,labels,assignees,commentsCount,updatedAt,url

# Help-wanted on Python repos when GFI label is sparse (still bounded backend keyword).
gh search issues "bug" --label "help wanted" --language python --state open --match title --limit 50 --json title,repository,labels,assignees,commentsCount,updatedAt,url

## Ranking filters

Apply in order to the combined, de-duplicated result set (by issue URL):

1. **Drop** any result with a non-empty `assignees` list (claims count in the wild).
2. **Drop** any result whose `updatedAt` is older than **90 days** before the scan date.
3. **Prefer** issues whose `labels` include `good first issue` or `good-first-issue` (case-insensitive) over those that surfaced only via `help wanted`.
4. **Order** survivors by `updatedAt` descending (most recently touched first).
5. **Tie-break:** fewer `commentsCount` first (less thread noise for a first claim).
6. **Diversify:** when taking the top 5, include at most **1** issue per `repository.nameWithOwner` (skip later hits from a repo already in the list).
7. **Fit tie-break (title only):** among equal `updatedAt` / `commentsCount`, prefer titles that match `(?i)\b(api|pytest|fastapi|server|health)\b` over titles matching `(?i)\b(gui|frontend|qt)\b` (steers toward backend work in `scope.md` without opening issues).

## How many to grade

Grade the top **5** ranked results per scan.
