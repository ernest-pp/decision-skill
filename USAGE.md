# Usage guide

This guide shows how to use the skill, how to change it, and how to fix common problems.

## Contents

1. Use the skill in a chat
2. Use the HTML file
3. Build a file with a config
4. Write a config
5. Change the language of the page
6. Add or change a tool
7. Check the text
8. Common problems

## 1. Use the skill in a chat

1. Install the skill (see `README.md`).
2. Write your problem in the chat. You can write a short message.
3. Answer the short questions of Claude. If you do not want to answer, write "just go". Claude then writes its guesses in the file as assumptions.
4. Claude gives you an HTML file.

Example messages:

- "I have two job offers. I must answer by Friday. Help me decide."
- "I have 40 tasks this week. Where do I start?"
- "We can release the app in two countries now or in one country later. Help me compare."

Claude does not tell you what to decide. Ask for an opinion after you use the tool. Claude then gives it and says that it is only an opinion.

## 2. Use the HTML file

Open the file in a browser. The file has these parts, from top to bottom:

1. The title, the deadline, the stakes, and the owner.
2. The decision question on a yellow sticky note.
3. The situation, the assumptions to check, and the reason for the tool.
4. The tool. Some files have a second tool as a stress test.
5. The form "Your decision".
6. Notes.

The top bar has jump chips for each part. It also has three buttons:

| Button | What it does |
|---|---|
| Save my decision | Downloads a JSON file. Saves in the browser. Opens a drawer with a text summary. |
| Load saved file | Loads a JSON file that you saved before. |
| Print or save as PDF | Opens the print window. |

If your browser blocks the download, use the **Copy text** button in the drawer. Keep the text in a safe place.

Each tool has a "Read this as text" section. It shows your answers as a plain list.

## 3. Build a file with a config

You need Python 3.8 or later.

```bash
python3 skill/scripts/build_tool.py config.json output.html
```

The script merges the presets, checks the config, and writes the file. It prints `ERROR` lines for problems that stop the build. It prints `WARNING` lines for problems that you can ignore if you are sure.

## 4. Write a config

Start from an example:

- `skill/examples/launch-config.json`: a risky bet with numbers.
- `skill/examples/weekly-config.json`: a list of tasks.

The config has these main parts:

| Part | Content |
|---|---|
| `meta` | The title, the language, and the short title |
| `problem` | The statement, the decision question, the deadline, the stakes, and the reversibility |
| `context` | Facts as label and value pairs |
| `assumptions` | Your guesses, as short sentences |
| `toolSelection` | The tool and the reason for it |
| `tools` | One to three tools. Each tool names a preset and has its data |

The full format is in `skill/references/html-config.md`.

## 5. Change the language of the page

1. Set `meta.language`, for example `"th"`.
2. Add a `ui` object. Each key replaces one fixed word on the page. Section 9 of `html-config.md` has an example.
3. Translate the text in the tool entries (`title`, `intro`, `how`, `steps`, `readout`).

The STE check skips configs that are not in English.

## 6. Add or change a tool

All presets are in `skill/assets/presets.json`. A preset names a renderer. The renderers are:

| Renderer | Use |
|---|---|
| `scorecard` | A table that scores options against weighted criteria |
| `quadrant` | Four boxes. The user places items in the boxes |
| `forces` | Two columns with strength scores |
| `lists` | Boxes of lists |
| `tree` | Options with chances and payoffs |
| `horizons` | Ratings of options at points in time |
| `flow` | A chart of questions with answers |
| `guided` | Questions, scales, checkboxes, and rules |

To add a tool:

1. Copy a preset that has the same renderer.
2. Change the text. Write it in STE.
3. Add an entry for the tool in `skill/references/tool-catalog.md`.
4. Add the tool to the routing table in `skill/references/tool-selection.md`.
5. Run the checks in `README.md`.

Do not change the layout for one tool. Read `skill/references/output-pattern.md` before you change the template.

## 7. Check the text

```bash
python3 skill/scripts/ste_check.py config.json     # one config
python3 skill/scripts/ste_check.py --presets        # the presets
python3 skill/scripts/ste_check.py --template       # the text of the page
python3 skill/scripts/ste_check.py --all            # presets and template
python3 skill/scripts/ste_lint.py skill/SKILL.md    # a Markdown file
```

Fix each `HARD` finding. A `note` is advice. Do not remove a fact to make a sentence short.

## 8. Common problems

| Problem | Action |
|---|---|
| `Preset 'x' does not exist` | Run `build_tool.py --list`. Check the spelling. |
| `chances add to N, not 100` | Change the percents of that option so that they total 100. |
| `points to missing node` | Change a `next` value in the flow. |
| `has placeholder text ('Replace')` | Write new questions for `yes_no_rule`. |
| The Save button does not download a file | Your browser blocked it. Use the Copy text button. |
| The fonts look different | The page loads Google Fonts. Without a network, the page uses fallback fonts. |
| The page does not show my saved work | Use **Load saved file** and choose the JSON file. |
