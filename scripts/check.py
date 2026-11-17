"""Validate distributable skill/role metadata, references and evaluation inputs."""
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


class UniqueKeyLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        self.flatten_mapping(node)
        keys = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                if key in keys:
                    raise yaml.constructor.ConstructorError(None, None, f"duplicate key: {key}", key_node.start_mark)
                keys.add(key)
            except TypeError as error:
                raise yaml.constructor.ConstructorError(None, None, "unhashable mapping key", key_node.start_mark) from error
        return super().construct_mapping(node, deep=deep)


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
        frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.S)
        if not frontmatter:
            errors.append(f"{path.relative_to(root)}: missing frontmatter")
            continue
        try:
            header = yaml.load(frontmatter[1], Loader=UniqueKeyLoader)
        except yaml.YAMLError as error:
            errors.append(f"{path.relative_to(root)}: invalid frontmatter: {error}")
            continue
        if not isinstance(header, dict):
            errors.append(f"{path.relative_to(root)}: frontmatter must be a mapping")
            continue
        for field in ("name", "description"):
            if not isinstance(header.get(field), str) or not header[field].strip():
                errors.append(f"{path.relative_to(root)}: missing {field}")
        if path in agents:
            if "model" in header:
                errors.append(f"{path.relative_to(root)}: public model override")
            tools = header.get("tools")
            if isinstance(tools, str):
                tools = [tool.strip() for tool in tools.split(",")]
            allowed = {"Read", "Grep", "Glob", "WebSearch", "WebFetch"}
            if not isinstance(tools, list) or not tools or not all(isinstance(tool, str) and tool in allowed for tool in tools):
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
