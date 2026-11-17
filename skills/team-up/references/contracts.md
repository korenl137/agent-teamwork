# Handoff and report contracts

Use existing task records. Do not require a new tracker or status service.
Choose a report path inside the worker's permitted scope; keep it reachable after
that worker exits. For separate hosts, agree how the report will be retrieved.

## Handoff

- Original request and observable completion criteria.
- Target repository/artifacts, starting revision and one owner per shared file.
- Dependencies, relevant project contracts and prohibited/out-of-scope changes.
- Authorized actions and where to stop for decisions or approval.
- Verification expectations, including review before physical/device execution.
- Absolute report location, reply route and relevant lifetime expectations.

## Worker report

- State: active, dependency-wait, decision-wait, verifying, approval-wait, cleaning,
  done or blocked; include enough evidence to tell waiting from a failed attempt.
- Changes and exact commits/PR heads; commands/results and raw evidence locations.
- Independent-review status distinct from self-review and tests.
- User interventions, failures/uncertain commands, unresolved concerns and next action.
- Resources owned, retained data and cleanup still required.

A missing report is missing evidence, not completion. Status and peer messages do not
confer user authority. Preserve a report before removing the worktree that contains it.
Use task-scoped names to avoid simultaneous workers overwriting one report.
