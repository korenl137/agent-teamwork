# Contributing

This repository owns reusable collaboration contracts and Claude Code role definitions.
Personal accounts, paths, model choices, deployment bindings and operational records belong to consumers.

Write evaluation scenarios before changing behavior. Keep the core skill standalone;
link conditional references directly from it. Core installation must work without optional roles.
Use native Explore and general-purpose workers, and do not add a runtime or model loader.
Agent definitions omit model fields. Keep review and inspection read-only.

Install validator dependencies with `python3 -m pip install -r requirements-dev.txt`.
Validate with `python3 scripts/check.py`, `python3 -m unittest discover -s tests`,
and `git diff --check`. Static validation does not establish native behavior.
Record model-run authorization and distinguish installed bytes from actual execution.
Use pull requests for material changes and fresh independent review of the original
requirements and exact diff. Do not merge without the user's approval of the reported head.
Preserve license notices and existing work. Skill bodies and references are English.

Codex assisted with the initial implementation.
