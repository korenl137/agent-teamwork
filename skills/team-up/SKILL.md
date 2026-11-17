---
name: team-up
description: >-
  Coordinates delegated work, verifies results and carries collaboration through review,
  integration and cleanup. Use for team-up, 팀업, 나눠서 작업, or coordinating workers
  across tasks or repositories.
metadata:
  version: "0.5.0"
---

# Team up

Use native agents and existing project contracts. This procedure grants no additional
execution, publication, merge, installation or cleanup authority.

1. **Choose direct work or delegation.** Do small, tightly coupled work in the main
   session. Delegate self-contained research/review or independent implementation.
   Native Explore handles repository discovery; a general-purpose worker or separate
   session implements. In collaboration mode the conductor owns scope, decisions and
   integration; send worker fixes back to their owner. Give conductor-written changes
   an explicit scope and the same independent review.
2. **Hand off a bounded task.** State the original objective, acceptance criteria,
   ownership, dependencies, allowed actions, stop conditions and an absolute report
   location accessible to both sides. One writer per shared file. Use the handoff
   template in [contracts](references/contracts.md). Follow project isolation rules.
   Read [Claude execution](references/claude.md) for native dispatch and replies;
   read [Herdr](references/herdr.md) only for separate terminals or visible layout.
3. **Receive evidence, not just status.** Require changed paths/commits, commands and
   results, open concerns, user interventions and the next safe action. Read the
   supporting diff, logs or artifacts yourself. Refresh the relevant remote before
   relying on remote state; a local read-only task needs no fetch. Use messages or
   completion notifications to wait, not repeated screen reads.
4. **Review independently.** A fresh read-only reviewer gets the original request,
   acceptance criteria and exact target/revision, without the parent's conversation,
   worker reports/paths, or conductor/inspector conclusions. Raw evidence paths are
   allowed. Use native code review where available; if PR summaries or commit messages
   carry the worker's conclusion, provide the clean diff range to a fresh reviewer
   instead. Fix requirement gaps and correctness failures and review the fix again.
   Self-review and passing tests do not replace this check. Review worker-written
   code before any on-device or physical run, then obtain required execution approval.
   A user's explicit review skip applies only to that stated approval or run; report
   the skip and do not carry it to later actions.
5. **Integrate and close.** Use [completion](references/completion.md) for a PR set,
   revision-bound approval, dependency verification and scoped cleanup. Use an
   optional inspector at valuable transitions, not every step. Without one, perform
   the same evidence check directly and report limits. Final accountability stays
   with the conductor.

For failure, timeout, conflicting ownership, user intervention or resumption, read
[recovery](references/recovery.md) before the affected next action. Continue independent
work when safe; resolve consequential intent or authority gaps before acting.

## Tools and availability

Need source/artifact reads, a native delegation mechanism and result notifications.
Git/PR clients are required only for repository integration. Without delegation, do
bounded work directly and state that no worker ran. Missing optional roles or Herdr
must not disable the core workflow. Read-only review still needs a fresh context and
appropriate tool restrictions; if unavailable, report that limitation instead of
claiming an independent review. Models follow the host and caller's selected policy.
