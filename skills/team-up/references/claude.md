# Claude Code execution

Use Claude's available native Agent mechanism. Read the installed command/tool schema
rather than assuming a version's optional features. Existing product permissions and
project contracts continue to apply; do not accept startup/trust dialogs for the user.

- Explore: repository discovery. Reuse the built-in role; a consumer may override its model.
- General-purpose: bounded implementation or work that needs edits. Supply the task
  contract, working directory and report/reply route. No permanent implementer is needed.
- Reviewer: use the installed read-only reviewer in a new context. The caller supplies
  original requirements and the exact target, excluding previous reasoning and conclusions.
- Optional researcher: external evidence where source and reading limits matter.
- Optional inspector: status/evidence reconciliation at useful boundaries. It reads raw
  snapshots supplied by the conductor; it has no live shell/PR tool. Collect evidence with
  commands/time/revisions, and recheck critical live state immediately before acting.

A normal new subagent starts without conversation history; a conversation fork inherits
history and is unsuitable for an independent review. Do not resume an implementation
worker as the reviewer. Definitions omit model fields; omitting a field differs from
explicitly setting inherit. Follow the host resolution order and the common model
selection reference linked from SKILL.md rather than creating a second role preset here.

For separate sessions, use the host's session-message/wait mechanisms if available.
Verify the live identity and working directory before sending consequential follow-up.
Agree a report location and reply address rather than deriving identity from inherited
terminal environment variables. Tool submission success is not task completion.
No report file is needed for a short native subagent result when its returned evidence
is sufficient and recoverable; durable or separate-session work needs retained reports.

Without optional roles, use native general-purpose research or the conductor's own
status reconciliation with the same boundaries. Without any native delegation, perform
bounded direct work and report that independent review/delegation was unavailable.
Do not simulate a missing agent or silently broaden tool access.

Sources: https://code.claude.com/docs/en/sub-agents and
https://code.claude.com/docs/en/best-practices (checked 2026-11-17).
