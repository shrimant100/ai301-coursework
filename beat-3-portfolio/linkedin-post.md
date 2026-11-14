I contributed my first fix to a large open-source security project, OWASP Nest. I corrected how the public website’s sitemap reports when the repositories page was last updated—it had been using “right now” on every refresh instead of the real latest change in the database.

I traced the bug to a one-line mapping gap in the Python backend, added tests so every listed page routes through the right data model, and opened a pull request with a small, reviewable diff. The project’s automated checks closed the PR the same day because I was not yet assigned to the issue and my commit was not cryptographically signed—so the work is visible but not merged yet. That taught me that mature open-source repos care as much about contribution workflow as about the code itself: assignment, signatures, and signed-off-by lines are part of shipping.

I also built course tooling to choose issues, check my upstream tone, and gate my own PR drafts before I bother maintainers—skills I will reuse on the next ticket.

The full story, including before/after reproduction output and the exact bot feedback, is in my technical write-up in this repo’s portfolio folder for class.

https://github.com/OWASP/Nest/pull/5818

#opensource #python #firstcontribution