---
name: team-up
description: >-
  Coordinates delegated work, verifies results and carries collaboration through review,
  integration and cleanup. Use for team-up, splitting work among workers, or coordinating workers
  across tasks or repositories.
metadata:
  version: "0.5.3"
---

# Team up

Use native agents and existing project contracts. This procedure grants no additional
execution, publication, merge, installation or cleanup authority. Before dispatching
work or changing its scope/risk, read [model selection](references/models.md).

1. **Choose direct work or delegation.** Do small, tightly coupled work directly.
   For bounded delegated work, default to a native subagent. Use a separate session
   for required independent environment/permissions, persistence/reconnection, or
   user-requested direct observation/intervention; size or a PR alone is not a reason.
   Read [operating decisions](references/operating.md) when choosing execution,
   reporting progress or deciding review scope. Native Explore handles discovery;
   general-purpose workers implement. The conductor owns scope, decisions and
   integration; send worker fixes back to their owner. Apply the same risk-based
   review criteria to conductor-written and worker-written changes.
2. **Hand off a bounded task.** State the original objective, acceptance criteria,
   ownership, dependencies, allowed actions, stop conditions and a recoverable reply
   route. Durable/separate-session work needs an absolute retained report location.
   One writer per shared file. Use the handoff
   template in [contracts](references/contracts.md). Follow project isolation rules.
   Read [Claude execution](references/claude.md) for native dispatch and replies;
   read [Herdr](references/herdr.md) only for separate terminals or visible layout.
3. **Receive evidence, not just status.** Require changed paths/commits, commands and
   results, open concerns, user interventions and the next safe action. Read the
   supporting diff, logs or artifacts yourself. Refresh the relevant remote before
   relying on remote state; a local read-only task needs no fetch. Use messages or
   completion notifications to wait, not repeated screen reads.
4. **Review proportionately.** Self-check low-impact, simple changes with suitable
   validation. Use independent review for meaningful behavior/design changes and
   security, permissions or governing shared guidance, and whenever project rules
   require it. Tests and self-review do not replace required independent review.
   A fresh read-only reviewer gets the original request, acceptance criteria and exact
   target/revision, without the parent's conversation, worker reports/paths or prior
   conclusions; raw evidence paths are allowed. Use native code review where available;
   if summaries expose worker conclusions, supply a clean diff range instead. Fix
   requirement/correctness failures, then recheck the affected scope and interactions;
   broaden only for new risk, scope changes or invalidated coverage. Review worker code
   before physical/device execution and obtain required execution approval. An explicit
   review skip applies only to the stated action; report it and never carry it forward.
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
