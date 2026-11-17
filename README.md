# agent-teamwork

Native-first collaboration contracts for coding agents: delegate bounded work, verify
original evidence, review independently, and finish integration and cleanup.

Claude Code is the first target. This repository adds operating contracts to native
agents; it does not supply an agent runtime, model router or automatic approval system.
Other hosts can reuse the contracts, but their execution compatibility is unverified.

## Choose the smallest setup

| Component | Installation | Purpose |
|---|---|---|
| team-up | Core skill | Delegation, acceptance, integration and completion |
| reviewer | Core read-only agent | Independent requirement/correctness review |
| researcher | Optional agent | External evidence with sources and reading limits |
| inspector | Optional agent | Reconcile claims with timestamped state evidence |
| Explore / general-purpose | Claude built-ins | Repository discovery / implementation |

The main session conducts collaboration. It may implement small single tasks directly;
in collaboration mode, worker fixes go back to their owner. Conductor integration edits
still receive independent review. There is no custom implementer or orchestrator.

## Install in Claude Code

Clone the repository to a location you control. In an existing `.claude` profile:

1. Install `skills/team-up/` as `skills/team-up` below the profile.
1. Install `agents/reviewer.md` as `agents/reviewer.md`.
1. Optionally install individual files from `agents/optional/` as agent files.
1. Start a fresh session, confirm discovery, and ask `Use team-up to coordinate this
   work` or `Have reviewer compare this exact target against this original request`.

Use copies or symlinks supported by your system. Create missing parent directories;
inspect existing destinations before installing and preserve conflicts. Do not replace
an entire agents folder: it may contain personal roles or an Explore override.
No personal global instructions, other skills, AEM or Herdr are required.

Definitions omit `model`; the host's model policy and per-invocation selection apply.
This differs from explicitly setting `inherit`. A strong conductor and task-appropriate
workers are useful starting points, not model/version requirements. Do not force all
workers to the same model solely because the conductor uses it.

## Update, uninstall and evidence

Pull reviewed source changes, then refresh copies or inspect linked content. Links expose
updates immediately. Before uninstalling, preserve active work and remove only the files
or links you installed. Removing a catalog declaration alone does not remove installation.

The [scenarios](evals/scenarios.json) are expected behavior, not executed model results.
Install development checks with `python3 -m pip install -r requirements-dev.txt`
(PyYAML is only needed by the validator, not the skill or roles).
Run `python3 scripts/check.py` and `python3 -m unittest discover -s tests` for static
contracts. Native discovery, actual independent review and sustained collaboration are
separate checks; record host, model, revision, inputs and observed output. Installation
or static success alone does not establish behavior. See [contributing](CONTRIBUTING.md).

Initial material was extracted from korenl137/agent-loadout's authored team-up and role
contracts. MIT, copyright Yun Ji; Codex assisted with implementation.
