# Decision Tool Builder

A skill for Claude. It changes a problem into a decision tool. The result is one HTML file. The user opens the file, writes in it, and saves it.

## What it does

1. Claude asks a few short questions to learn the problem.
2. Claude chooses a decision method that fits the problem.
3. Claude helps the user list options and criteria.
4. Claude builds one interactive HTML file.
5. The user writes in the file and saves the decision.

The HTML file has the problem, the context, the tool, and a form for the decision. It has a **Save** button. The button downloads a JSON file, saves in the browser, and shows a text summary to copy.

## The tools

The skill has 40 tools. Each tool is a preset in `skill/assets/presets.json`.

| Group | Tools |
|---|---|
| Structure a choice | weighted matrix, decision tree with expected value, pros and cons, force field, rubber band |
| Sort and prioritize | Eisenhower matrix, project portfolio, BCG box, hard choice model |
| Check time and feelings | 10/10/10 test, three-day trial, coin test, when to decide |
| Stress test a plan | pre-mortem, one-way or two-way door, stop rule, Rumsfeld matrix, bias check, Swiss cheese model |
| Understand the situation | Cynefin, SWOT, gap in the market |
| Goals and coaching | goal check (SMART, PURE, CLEAR), GROW, WRAP, regret minimization |
| Buying | buyer's decision model |
| Understand yourself | personal performance, flow, Johari window, Maslow check, making-of, double-loop learning, feedback box |
| Team and people | Hersey-Blanchard, six thinking hats, appreciative inquiry, team performance |
| Ideas | morphological box and SCAMPER |
| Fast rule | yes/no rule |

Claude chooses one main tool. Claude adds one stress test only if the decision is hard to undo. The skill never builds more than three tools.

## Quick start

### Use the skill in Claude

- **Claude app:** upload `dist/decision-tool-builder.skill` in the skills settings.
- **Claude Code:** copy the folder `skill/` to `~/.claude/skills/decision-tool-builder/`.

Then write a problem in the chat. Example: "I have two job offers and I must answer by Friday. Help me decide."

### Build a file without Claude

You need Python 3.8 or later. You do not need other packages.

```bash
python3 skill/scripts/build_tool.py skill/examples/launch-config.json my-tool.html
```

Open `my-tool.html` in a browser.

To see all tool ids, run:

```bash
python3 skill/scripts/build_tool.py --list
```

## Repo layout

```text
.
├── README.md             this file
├── USAGE.md              how to use and change the skill
├── LICENSE               MIT license
├── dist/
│   └── decision-tool-builder.skill   the packaged skill
└── skill/
    ├── SKILL.md          the instructions for Claude
    ├── references/       the guides that Claude reads
    ├── assets/           the HTML template and the presets
    ├── scripts/          the build script and the STE checker
    ├── examples/         two complete configs and the files that they build
    └── evals/            test prompts
```

## The look of the page

The page follows a whiteboard pattern. It has a dot-grid board, a fixed top bar, sticky notes, white cards with hard shadows, and a side drawer. The pattern comes from two example files that the author supplied. `skill/references/output-pattern.md` describes it.

## The language

All text that the skill writes for the user follows Simplified Technical English (STE). The sentences are short. Each word has one meaning. Many users are not native speakers of English, and this helps them.

- `skill/references/ste-writing.md` has the rules and the vocabulary.
- `skill/scripts/ste_check.py` checks the text of a config.
- The skill does not use the official word list of ASD-STE100. It does not claim full STE compliance.

For other languages, the user sets `meta.language` and translates the page text with the `ui` setting.

## Checks

Run these commands from the repo root:

```bash
python3 skill/scripts/ste_check.py --all
python3 skill/scripts/ste_check.py skill/examples/launch-config.json
python3 skill/scripts/build_tool.py skill/examples/weekly-config.json /tmp/test.html
```

Each STE check must show `0 hard finding(s)`.

## Limits

- The tools help the user think. They do not decide for the user.
- The tools are not professional advice. For health, law, or money, ask a qualified person.
- Expected value uses the guesses of the user. It does not predict the future.
- The skill does not build tools for a person in crisis. Claude replies with care instead.

## Credits and licenses

- The decision methods come from many sources. Most come from *The Decision Book* by Mikael Krogerus and Roman Tschäppeler. `skill/references/tool-catalog.md` names the others. Examples: Gary Klein (pre-mortem), Kurt Lewin (force field), Dave Snowden (Cynefin), Chip and Dan Heath (WRAP), John Whitmore (GROW).
- The skill states each method in its own words. It does not copy text from the sources.
- `skill/scripts/ste_lint.py` comes from the `asd-ste100` skill by Dustin Yuchen Teng. It uses the MIT license. The license text is in `skill/scripts/LICENSE-ste-lint`.
- ASD-STE100 is a standard of ASD. This project is not certified by ASD.
- This repo uses the MIT license. See `LICENSE`.
