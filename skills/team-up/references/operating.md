# Execution, reporting and review decisions

## Subagent or separate session

Do small, tightly coupled work directly. For bounded delegation whose evidence can
return within the current task, default to a native subagent, including implementation
and review. Repository/worktree isolation is a separate decision: a subagent can use
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
