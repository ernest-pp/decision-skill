#!/usr/bin/env python3
"""Check the text of a decision-tool config (or presets file) against the STE rules.

Usage:
  python ste_check.py config.json            # check a config
  python ste_check.py --presets              # check assets/presets.json
  python ste_check.py --template             # check the page text in the template
  python ste_check.py --all                  # presets + template

The script collects every sentence that the user can read. It sends them to
ste_lint.py (the linter of the asd-ste100 skill, MIT license). It prints each
finding with the field it came from. Exit code 1 means there is at least one
hard finding. Text in other languages is skipped when meta.language is not English.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import ste_lint  # noqa: E402

# keys whose values are code, ids, or data that the user enters. Do not check them.
SKIP_KEYS = {
    "id", "renderer", "preset", "op", "type", "next", "start", "q_key", "language", "created",
    "primary", "version", "app", "unit", "gut", "scores", "p", "payoff", "cost", "weight", "score",
    "min", "max", "value",
}
USER_DATA_PARENTS = {"data"}  # text the user supplies (options, items) is not checked


def walk(node, path, out, in_data=False):
    if isinstance(node, dict):
        for k, v in node.items():
            if k in SKIP_KEYS and not isinstance(v, (dict, list)):
                continue
            walk(v, f"{path}.{k}" if path else k, out, in_data or k in USER_DATA_PARENTS)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, f"{path}[{i}]", out, in_data)
    elif isinstance(node, str) and node.strip() and not in_data:
        out.append((path, node))


def sentences_of(text):
    """Make each string one linter line. Split long strings at sentence ends."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p]


def run(strings, label):
    findings, total = [], 0
    for path, text in strings:
        for s in sentences_of(text):
            if len(s.split()) < 2:
                continue
            f, w = ste_lint.lint(s, filename=path)
            total += w
            for item in f:
                item = dict(item)
                item["path"] = path
                item["text"] = s
                findings.append(item)
    hard = [f for f in findings if f["level"] == "advisory-free"]
    for f in findings:
        tag = "HARD" if f["level"] == "advisory-free" else "note"
        print(f"{tag} [{label}] {f['path']}: {f['rule']}: {f['message']}")
        print(f"       \"{f['text'][:160]}\"")
    print(f"{label}: {len(hard)} hard finding(s), {len(findings) - len(hard)} note(s), {total} words checked.")
    return len(hard)


def presets_strings():
    data = json.loads((ROOT / "assets" / "presets.json").read_text(encoding="utf-8"))
    out = []
    walk(data, "", out)
    return out


def template_strings():
    html = (ROOT / "assets" / "decision-tool-template.html").read_text(encoding="utf-8")
    m = re.search(r"var S = \{(.*?)\n  \};", html, re.S)
    out = []
    if m:
        for key, val in re.findall(r'(\w+):\s*"((?:[^"\\]|\\.)*)"', m.group(1)):
            if val in ("x", "rm"):
                continue
            out.append((f"S.{key}", val.replace("\\\"", '"')))
    return out


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    hard = 0
    if "--all" in argv:
        argv = ["--presets", "--template"]
    for a in argv:
        if a == "--presets":
            hard += run(presets_strings(), "presets")
        elif a == "--template":
            hard += run(template_strings(), "template")
        else:
            cfg = json.loads(Path(a).read_text(encoding="utf-8"))
            lang = str(cfg.get("meta", {}).get("language", "en")).lower()
            if not lang.startswith("en"):
                print(f"Skipped: language is '{lang}'. The STE check is for English.")
                continue
            out = []
            walk(cfg, "", out)
            hard += run(out, Path(a).name)
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
