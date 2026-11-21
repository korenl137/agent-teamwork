# Execution, reporting and review decisions

## Main loop or delegation

Work in the main loop by default. A single loop that keeps earlier results in one
context can connect them, while each delegation hands back a lossy summary and adds a
nested loop. Delegate a piece when it needs little from the rest of the work and can
return a compact result:

- Independent paths that run in parallel with fresh, disposable contexts.
- A broad sweep or long log whose detail would bloat the main context, or a loop that
  shows measurable degradation from its size.
- A loop that struggles to choose tools or holds conflicting instructions for a task.
- Independent verification, or a permission boundary the main loop should not hold.
- A context-free collection task that the consumer's cost policy routes to a cheaper
  worker; record cost as the reason.

Split by context, not by role: a worker per problem type passes information back and
forth and loses fidelity at each handoff. Delegate implementation only when the task,
its decisions and its acceptance checks can be stated in the handoff; otherwise keep it
in the main loop. Revisit an existing delegation pattern when its reason no longer holds.

## Subagent or separate session

For bounded delegation whose evidence can return within the current task, default to a
native subagent, including self-contained implementation and review. Repository/worktree isolation is a separate decision: a subagent can use
an isolated worktree; a new terminal does not itself isolate files or credentials.

Choose a separate session when it supplies a required capability:

- An independently configured environment or permission boundary that the available
  subagent cannot provide; use authorized host mechanisms, never copied credentials.
- Work that must persist across conductor exit or support later reconnection.
- Explicit user preference, including direct observation or intervention in a worker.

Task size, another repository, PR creation or an available terminal manager alone do
not require a separate session. Verify the host actually supports the needed lifetime,
permissions and interaction; report an unavailable requirement rather than simulate it.
Keep a durable handoff/report and verify session identity, working directory and return
route. Visibility does not imply persistence. Use the host-specific execution references
linked from SKILL.md only after deciding a separate session is needed.

## Report when it helps the user act

Resolve internal dependencies, ordinary recoverable worker/test failures and missing
worker evidence with the owners. Continue safe independent work. Do not ask the user
to validate an unfinished result or settle a question that further authorized work can
answer. An approval request needs a concrete, checked result and the required evidence;
explain any genuine user decision separately from approval of completed work.

Promptly report important failures, material errors in earlier user reports, and
material scope/cost changes or blocks requiring a user decision. Do not wait for all
workers or a complete diagnosis before correcting an important false claim or exposing
a serious failure. State known facts, impact, containment, remaining uncertainty and
what is needed from the user, if anything. Hold affected actions when required, while
continuing safe independent work. Reporting a failure is not automatically asking for
permission to perform an already authorized fix.

Give ordinary progress updates at meaningful results or transitions; honor any host or
user cadence without turning a progress update into a confirmation gate. Worker
completion alone is not an approval-ready milestone. Do not hide a material limitation
in the final report, or repeatedly relay every pending worker message to the user.

## Spend review effort where it changes confidence

Judge impact, complexity and uncertainty, not line count or who wrote the change.
Simple low-impact edits can use direct inspection and suitable checks. Meaningful
behavior/design changes and security, permission or governing shared-guidance changes
need independent review. Existing repository/user requirements remain binding; a tiny
policy edit may still be high risk. Cost alone does not waive required review.

Reuse review evidence for unchanged scope and revision. After a localized fix, recheck
the finding and affected interactions; use a fresh reviewer where independence is
required, without supplying the prior reviewer's conclusion as the answer. Broaden
review when scope grows, new risks emerge or prior coverage is unreliable. A prior
head's review never proves newly changed content was checked. Do not add duplicate
reviewers, optional inspectors or full repeated passes without a concrete question
they can resolve. Report checks, independent-review coverage and remaining limits
accurately; self-checking is not independent review. Required approval stays separate.
