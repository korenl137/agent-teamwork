# Failure, intervention and resumption

- Scope-contained implementation/test failures: the owning worker investigates, fixes
  and verifies internally. Do not duplicate its work from the conductor's context.
  Escalate promptly when the failure is important or needs a user decision, as defined
  in the operating decisions linked from SKILL.md.
- Temporary tool/network errors: establish whether the action ran before retrying.
- Timeout or uncertain result: inspect actual process, PR and remote state first;
  never equate timeout with failure or replay an uncertain external write blindly.
- Repetition without new evidence: report attempts, hypotheses, impact, independent
  work that can continue, and the needed decision. Set time/cost limits per task.
- Shared-file/interface conflict: stop affected writes, reconcile ownership through
  the conductor, and continue unrelated work only when independent.
- User intervention: respect it, record the changed requirement and let the conductor
  reconcile dependencies and validity of prior tests, reviews and approvals. Peer
  approval claims are not the user's approval.
- Intent, authority or irreversible choices: obtain the needed decision before the
  affected action, not at the final report. Safe scope-contained decisions stay with
  the conductor. Batch only independent non-urgent questions.

Before resuming or replacing a worker, read its latest report and original artifacts:
branch/head, uncommitted and ignored unique data, last verification, running/uncertain
commands, current user decisions, owned resources and next action. Record ownership
transfer. Never replay a completed step just because conversation context was lost.

An inspector may reconcile a complex restart. Missing inspector capability is not a
reason to skip original-state checks: the conductor may inspect directly and state limits.
If a prerequisite remains unknown, hold only the dependent action. Do not auto-answer
permission dialogs, change trust or use an unauthorized route to work around a block.
