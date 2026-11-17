"""Validate distributable skill/role metadata, references and evaluation inputs."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check(root):
    errors = []
    skill = root / "skills/team-up/SKILL.md"
    agents = list((root / "agents").rglob("*.md"))
    if not (root / "agents/reviewer.md").is_file():
        errors.append("missing core reviewer")
    for path in [skill, *agents]:
        if not path.is_file():
            errors.append(f"missing {path.relative_to(root)}")
            continue
        text = path.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        if len(parts) != 3 or parts[0].strip():
            errors.append(f"{path.relative_to(root)}: missing frontmatter")
            continue
        header = parts[1]
        for field in ("name", "description"):
            if not re.search(rf"^{field}:\s*\S", header, re.M):
                errors.append(f"{path.relative_to(root)}: missing {field}")
        if path in agents:
            if re.search(r"^model:", header, re.M):
                errors.append(f"{path.relative_to(root)}: public model override")
            tools = re.search(r"^tools:\s*(.*)$", header, re.M)
            allowed = {"Read", "Grep", "Glob", "WebSearch", "WebFetch"}
            if not tools or set(tools[1].split(", ")) - allowed:
                errors.append(f"{path.relative_to(root)}: role can execute or mutate")
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("#"):
                continue
            target_path = (path.parent / target.split("#", 1)[0]).resolve()
            if not target_path.is_relative_to(root.resolve()) or not target_path.exists():
                errors.append(f"{path.relative_to(root)}: invalid reference {target}")
    try:
        scenarios = json.loads((root / "evals/scenarios.json").read_text(encoding="utf-8"))
        if not isinstance(scenarios, list) or len(scenarios) < 3:
            errors.append("expected at least three evaluation scenarios")
        else:
            for index, case in enumerate(scenarios):
                if not isinstance(case, dict) or not case.get("query") or not case.get("expected_behavior"):
                    errors.append(f"scenario {index}: missing request/expectation")
    except (OSError, ValueError) as error:
        errors.append(f"invalid evaluations: {error}")
    return errors


if __name__ == "__main__":
    errors = check(ROOT)
    for error in errors:
        print(error)
    if not errors:
        print("Static contracts passed; no native/model execution claimed")
    raise SystemExit(bool(errors))
