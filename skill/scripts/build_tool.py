#!/usr/bin/env python3
"""Build a decision-tool HTML file from a small config.

Usage:
  python build_tool.py --list                      # show all preset ids
  python build_tool.py config.json out.html        # build and validate

The config holds the problem, the context, and a list of tools. Each tool names
a preset (see assets/presets.json) and may override any preset field. The
script merges the presets, checks the result, and writes one self-contained
HTML file from assets/decision-tool-template.html.
"""
import argparse
import copy
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
TEMPLATE = ROOT / "assets" / "decision-tool-template.html"
PRESETS = ROOT / "assets" / "presets.json"
RENDERERS = {"scorecard", "quadrant", "forces", "lists", "tree", "horizons", "flow", "guided"}
QUAD_KEYS = {"tl", "tr", "bl", "br"}
MAX_TOOLS = 3


def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "-", (text or "decision").lower()).strip("-")
    return s[:48] or "decision"


def merge_tool(tool, presets, errors):
    """Preset first, then the tool's own fields on top. `data` merges by key."""
    name = tool.get("preset")
    base = {}
    if name:
        if name not in presets:
            errors.append(f"Preset '{name}' does not exist. Run with --list to see the ids.")
            return tool
        base = copy.deepcopy(presets[name])
    out = base
    for key, val in tool.items():
        if key == "data" and isinstance(val, dict) and isinstance(out.get("data"), dict):
            out["data"].update(val)
        else:
            out[key] = val
    if "renderer" not in out:
        errors.append(f"Tool '{name or out.get('title', '?')}' has no renderer. Write a preset or a renderer.")
    elif out["renderer"] not in RENDERERS:
        errors.append(f"Tool '{name}' uses renderer '{out['renderer']}'. This renderer does not exist.")
    return out


def check_tool(t, warnings, errors):
    label = t.get("preset") or t.get("title") or t.get("renderer")
    r = t.get("renderer")
    d = t.get("data") or {}
    if r == "scorecard":
        opts, crit = d.get("options", []), d.get("criteria", [])
        if len(opts) < 2:
            errors.append(f"[{label}] needs 2 options or more in data.options.")
        if len(crit) < 2:
            errors.append(f"[{label}] needs 2 criteria or more in data.criteria.")
        if len(opts) > 5:
            warnings.append(f"[{label}] has {len(opts)} options. More than 5 options can cause choice overload.")
        if len(crit) > 7:
            warnings.append(f"[{label}] has {len(crit)} criteria. Use 5 to 7 criteria.")
        for c in crit:
            if not 1 <= c.get("weight", 3) <= 5:
                errors.append(f"[{label}] criterion '{c.get('name')}' weight must be 1 to 5.")
    elif r == "quadrant":
        for k in ("axes", "quadrants"):
            if k not in t:
                errors.append(f"[{label}] is missing '{k}'.")
        for k in QUAD_KEYS:
            if k not in t.get("quadrants", {}):
                errors.append(f"[{label}] quadrants needs key '{k}'.")
        for it in d.get("items", []):
            if isinstance(it, dict) and it.get("q", "") not in QUAD_KEYS | {""}:
                errors.append(f"[{label}] item '{it.get('text')}' has bad quadrant '{it.get('q')}'.")
    elif r == "forces":
        if not (d.get("left") or d.get("right")):
            warnings.append(f"[{label}] has no starting items. The user writes them.")
    elif r == "lists":
        cols = t.get("columns", [])
        if not cols:
            errors.append(f"[{label}] needs 'columns'.")
        items = d.get("items", [])
        if items and len(items) != len(cols):
            errors.append(f"[{label}] data.items must have one list per column ({len(cols)}).")
    elif r == "tree":
        for o in d.get("options", []):
            ps = sum(x.get("p", 0) for x in o.get("outcomes", []))
            if o.get("outcomes") and round(ps) != 100:
                errors.append(f"[{label}] option '{o.get('name')}' chances add to {ps}, not 100.")
    elif r == "horizons":
        if not t.get("horizons"):
            errors.append(f"[{label}] needs 'horizons'.")
        if len(d.get("options", [])) < 2:
            warnings.append(f"[{label}] has fewer than 2 options in data.options.")
    elif r == "flow":
        nodes, start = d.get("nodes", {}), d.get("start")
        if start not in nodes:
            errors.append(f"[{label}] start node '{start}' does not exist.")
        reach, stack = set(), [start]
        while stack:
            n = stack.pop()
            if n in reach or n not in nodes:
                continue
            reach.add(n)
            for op in nodes[n].get("options", []):
                if op.get("next") not in nodes:
                    errors.append(f"[{label}] node '{n}' points to missing node '{op.get('next')}'.")
                stack.append(op.get("next"))
        for n, node in nodes.items():
            if "outcome" not in node and not node.get("options"):
                errors.append(f"[{label}] node '{n}' has neither options nor an outcome.")
            if n not in reach:
                warnings.append(f"[{label}] the user cannot reach node '{n}'.")
        if "Replace" in json.dumps(nodes):
            errors.append(f"[{label}] has placeholder text ('Replace'). Write real questions.")
    elif r == "guided":
        pass
    steps = t.get("steps", []) if r == "guided" else []
    for group in (steps, t.get("prompts", [])):
        ids = [s.get("id") for s in group]
        if len(ids) != len(set(ids)):
            errors.append(f"[{label}] has duplicate step ids.")
        for s in group:
            if s.get("type") == "choice" and not s.get("choices"):
                errors.append(f"[{label}] step '{s.get('id')}' is a choice with no choices.")
    for rule in t.get("rules", []) + t.get("promptRules", []):
        for c in rule.get("if", []):
            if c.get("id") not in [s.get("id") for s in steps + t.get("prompts", [])]:
                errors.append(f"[{label}] rule points to unknown step '{c.get('id')}'.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("config", nargs="?")
    ap.add_argument("out", nargs="?")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    presets = json.loads(PRESETS.read_text(encoding="utf-8"))

    if a.list:
        for pid, p in presets.items():
            print(f"{pid:24s} {p['renderer']:10s} {p['title']}")
        return 0
    if not a.config or not a.out:
        ap.error("give a config file and an output file, or use --list")

    cfg = json.loads(Path(a.config).read_text(encoding="utf-8"))
    errors, warnings = [], []
    meta = cfg.setdefault("meta", {})
    prob = cfg.setdefault("problem", {})
    if not meta.get("title"):
        errors.append("meta.title is required.")
    if not (prob.get("decisionQuestion") or prob.get("statement")):
        errors.append("problem.decisionQuestion (or problem.statement) is required.")
    meta.setdefault("id", slugify(meta.get("title")))
    meta.setdefault("created", datetime.date.today().isoformat())
    meta.setdefault("language", "en")
    tools = cfg.get("tools", [])
    if not tools:
        errors.append("Give at least one tool.")
    if len(tools) > MAX_TOOLS:
        warnings.append(f"{len(tools)} tools. More than {MAX_TOOLS} tools can overload the user. Use one main tool and one stress test.")
    cfg["tools"] = [merge_tool(t, presets, errors) for t in tools]
    for t in cfg["tools"]:
        if "renderer" in t:
            check_tool(t, warnings, errors)
    if not cfg.get("toolSelection", {}).get("why"):
        warnings.append("toolSelection.why is empty. Tell the user why you chose this tool.")

    if meta.get("language", "en").lower().startswith("en"):
        try:
            import ste_check  # same folder
            import io, contextlib
            out = []
            ste_check.walk(cfg, "", out)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                hard = ste_check.run(out, "config")
            if hard:
                warnings.append(f"STE check: {hard} hard finding(s). Run: python scripts/ste_check.py {a.config}")
        except Exception as exc:  # the check must never stop a build
            warnings.append(f"STE check did not run: {exc}")
    for w in warnings:
        print("WARNING:", w)
    if errors:
        for e in errors:
            print("ERROR:", e)
        return 1

    blob = json.dumps(cfg, ensure_ascii=False)
    blob = blob.replace("</", "<\\/").replace("<!--", "<\\!--").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    html = TEMPLATE.read_text(encoding="utf-8")
    pat = re.compile(r'(<script id="config" type="application/json">)(.*?)(</script>)', re.S)
    if not pat.search(html):
        print("ERROR: template has no config block.")
        return 1
    html = pat.sub(lambda m: m.group(1) + blob + m.group(3), html, count=1)
    title = meta["title"].replace("&", "&amp;").replace("<", "&lt;")
    html = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", html, count=1, flags=re.S)
    lang = re.sub(r"[^A-Za-z-]", "", str(meta.get("language", "en"))) or "en"
    html = html.replace('<html lang="en">', f'<html lang="{lang}">', 1)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"OK: wrote {out} ({out.stat().st_size // 1024} KB), {len(cfg['tools'])} tool(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
