# Integration, approval and cleanup

Before seeking approval, inspect original evidence and required review results.
Distinguish direct checks from independent review and state any unreviewed scope.
For several PRs, prepare a compact table: task/repository, PR, exact head, summary,
self-checks, independent review, CI, dependency order and unverified/deferred items.
Keep details in the PR bodies. Do not create a dashboard just to show the set.

An optional inspector can compare ownership, heads and evidence before PR-set approval,
complex resumption or final completion. It does not redo code review or grant approval.
Provide original criteria and timestamped raw evidence, not only completion claims.
Resolve requirement/verification/authority violations before that stage. Missing required
proof is unknown, not passing. If inspection is unavailable, the conductor checks the
same evidence or uses another read-only checker and records the limit.

## Merge

- The user may approve the whole set or a subset. Merge only authorized PRs at their
  approved heads using the host's head-match mechanism where available.
- A changed head requires new approval. A changed base or dependency combination needs
  affected integration verification; do not treat earlier CI as proof of a new combination.
- Check actual current heads, approval and required CI immediately before action;
  an inspector snapshot is not an atomic lock. A declined approval is not cleanup permission.
- Respect repository merge policy. If a permission layer rejects the merge, report it;
  do not bypass the rejection through another route.

## Cleanup

After merge and preservation are verified, ask each worker to clean only resources
it owns under the applicable project authorization. Preserve unmerged/uncommitted work,
unique ignored data and reproducibility evidence. Verify transfer before removing originals.
Do not directly delete remote branches; follow repository automation and report leftovers.
Workers report cleanup evidence before ending their sessions. If they must remove their
working directory, first move to a safe directory. The conductor takes over absent workers
only after recovering evidence and confirming ownership/authority.

Finally verify merge destinations, residual changes, worktrees and worker state, including
the conductor's own resources. Report cleanup failure as remaining work. Never close another
user's terminal or treat an exit status alone as proof that all work and cleanup finished.
