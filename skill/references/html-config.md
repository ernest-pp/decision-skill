# Config format for `build_tool.py`

You do not write HTML. You write one JSON config. The script merges the presets, checks the result, and builds the HTML file.

## Contents

1. Top-level fields
2. A tool entry and how presets merge
3. Data shapes for each renderer
4. Guided steps and rules
5. Custom tools (no preset)
6. A full example
7. Wording
8. Common build errors
9. Change the page language (`ui`)

## 1. Top-level fields

The page has one fixed **whiteboard pattern**. It comes from the MFG CRMP examples. You do not choose the layout. You write the content. The template draws it. `output-pattern.md` describes the page.

```json
{
  "meta": { "title": "Which laptop do I buy?", "id": "laptop-choice", "language": "en", "shortTitle": "Laptop choice" },
  "problem": {
    "statement": "My old laptop is slow. I need a new laptop for work and travel.",
    "decisionQuestion": "Which of these three laptops do I buy this month?",
    "deadline": "End of October",
    "owner": "Me",
    "stakes": "Medium",
    "reversibility": "Hard to undo after 14 days",
    "background": "Optional: one or two sentences."
  },
  "context": [ { "label": "Budget", "value": "Up to 1,200 USD" } ],
  "assumptions": ["You use the laptop mostly for office work and video calls."],
  "toolSelection": {
    "primary": "weighted_matrix",
    "why": "Short sentences. Say why this tool fits this problem.",
    "alsoConsider": [ { "name": "Pre-mortem", "why": "Use it on your top option before you pay." } ]
  },
  "tools": [ { "preset": "weighted_matrix", "data": { } }, { "preset": "premortem" } ],
  "finalStep": { "prompt": "Optional. The text above the decision form." },
  "notes": ["Optional. Short notes for the last box."],
  "ui": { "save": "Optional. Replace any button or label. See section 9." }
}
```

- `meta.title` and `problem.decisionQuestion` (or `problem.statement`) are necessary.
- `meta.language` sets the page language, for example `en` or `th`. The fonts include Thai. `meta.shortTitle` is the short name in the top bar.
- `meta.id` is optional. The script makes it from the title. The page uses it as the save key and as the name of the downloaded file.
- `notes` is an optional list for the last box. If you do not write it, the page shows one standard note. The note says that the tool helps the user think and does not decide for the user. For health, law, or money, add a note that says the tool is not professional advice.
- `ui` replaces the fixed text of the page. Use it when the user does not write in English (section 9).
- All other fields are optional. Write all that you know. The page hides empty fields.
- Write every guess in `assumptions`. Use short sentences.
- Use 1 to 3 tools. The script gives a warning for more than 3 tools.
- Write all text in STE. Read `ste-writing.md`.

## 2. A tool entry and how presets merge

A tool entry is an object. The key `preset` names a preset id from `assets/presets.json`. The script starts with the preset. Then it copies your fields on top.

- A field that you write replaces the preset field with the same name. Examples: `title`, `intro`, `how`, `steps`, `columns`, `quadrants`, `prompts`.
- The script merges `data` by key. Your `data.options` replaces `data.options` of the preset. Other `data` keys of the preset stay.

Fields that most tools accept:

| Field | Meaning |
|---|---|
| `title` | The heading of the tool section |
| `shortTitle` | The name in the jump chip |
| `source` | The small line that names the method |
| `intro` | One or two sentences before the tool |
| `how` | A list of short steps ("How to use it") |
| `readout` | A note after the tool ("How to read the result") |
| `prompts` | A list of guided steps under the tool ("Think it through") |
| `promptsTitle` | The heading for the prompts |
| `promptRules` | Rules for `prompts` (same format as `rules`) |
| `data` | The content for the problem. The shape depends on the renderer |

Run `python scripts/build_tool.py --list` to see the ids.

## 3. Data shapes for each renderer

### scorecard (`weighted_matrix`)

```json
"data": {
  "options": ["Laptop A", "Laptop B", "Laptop C"],
  "criteria": [ { "name": "Low price", "weight": 5 }, { "name": "Battery life", "weight": 4 } ],
  "gut": ""
}
```
Weights are 1 to 5. Do not write scores. The user writes the scores. Use 2 to 5 options and 4 to 7 criteria. Name cost and risk criteria so that 5 is good ("Low cost", "Low risk").

### quadrant (`eisenhower`, `bcg_box`, `project_portfolio`, `feedback_box`, `hard_choice`, `rumsfeld`, `johari`, `flow_model`)

```json
"data": { "items": ["Pay tax", { "text": "Plan next year", "q": "tl" }] }
```
`q` is optional. The values are `tl`, `tr`, `bl`, `br` (top-left, top-right, bottom-left, bottom-right). An item without `q` starts as "not placed yet". The preset has the meaning of each box (`quadrants` and `axes`). To change the labels, replace `axes` and `quadrants`:

```json
"axes": { "x": {"label": "Effort", "low": "small", "high": "large"}, "y": {"label": "Impact", "low": "small", "high": "large"} },
"quadrants": { "tl": {"name": "...", "when": "...", "action": "..."}, "tr": {...}, "bl": {...}, "br": {...} }
```
All four quadrant keys are necessary.

### forces (`pros_cons`, `force_field`, `rubber_band`)

```json
"data": {
  "left":  [ "Lower cost", { "text": "Faster", "score": 4 } ],
  "right": [ "Training is necessary" ]
}
```
An item is a string (score 3) or `{text, score}` with a score from 1 to 5. To change the words, replace `leftTitle`, `rightTitle`, `leftWins`, `rightWins`, `balanced`, or `tip`.

### lists (`swot`, `making_of`, `morphological_box`)

```json
"data": { "items": [ ["Strong team"], ["New market"], ["Little cash"], ["Rival cuts its price"] ] }
```
Write one list for each column. Use the same order as `columns` in the preset. To change the columns, replace `columns`: `[{ "name": "Design", "hint": "..." }, ...]`. Then `data.items` must have the same number of lists.

### tree (`decision_tree_ev`)

```json
"data": {
  "unit": "USD",
  "options": [
    { "name": "Launch now", "cost": 20000,
      "outcomes": [ { "label": "Sells well", "p": 40, "payoff": 90000 }, { "label": "Sells badly", "p": 60, "payoff": 10000 } ] },
    { "name": "Wait", "cost": 0, "outcomes": [ { "label": "Same as now", "p": 100, "payoff": 15000 } ] }
  ]
}
```
`p` is a percent. The chances of each option must total 100. The script checks this. Use only numbers that the user gave. If you have no numbers, do not write `options`. The user then writes them in the tool.

### horizons (`ten_ten_ten`, `trial_run`)

```json
"data": { "options": ["Take the job", "Stay"] }
```
The preset has the time points (`horizons`). To change them, replace `horizons`: `[{ "label": "After 1 month", "help": "..." }]`.

### flow (`doors`, `cynefin`, `hersey_blanchard`, `yes_no_rule`)

```json
"data": {
  "start": "q1",
  "nodes": {
    "q1": { "q": "Question text?", "help": "Optional help.", "options": [ { "label": "Yes", "next": "q2" }, { "label": "No", "next": "stop" } ] },
    "q2": { "q": "Next question?", "options": [ { "label": "Yes", "next": "go" }, { "label": "No", "next": "stop" } ] },
    "go":   { "outcome": { "title": "Go", "text": "Short advice.", "next": ["Optional next step."] } },
    "stop": { "outcome": { "title": "Stop", "text": "Short advice." } }
  }
}
```
Each `next` must name a node that exists. A node has `options` or `outcome`. The script checks for broken links and for nodes that the user cannot reach. `doors`, `cynefin`, and `hersey_blanchard` are complete. Only `yes_no_rule` needs new nodes from you.

### guided (all the step-by-step tools)

See section 4.

## 4. Guided steps and rules

`steps` is a list. Each step has these fields:

| Field | Meaning |
|---|---|
| `id` | A short and unique id |
| `q` | The question or the instruction |
| `help` | Optional small help text |
| `section` | Optional group heading. The page shows it when it changes |
| `type` | `text` (default), `number`, `scale`, `choice`, `check`, `checks`, `coin` |
| `min`, `max`, `low`, `high` | For `scale`. The default is 1 to 5. `low` and `high` name the ends |
| `choices` | For `choice`: a list of strings |
| `label` | For `check`: the text of the box |
| `items` | For `checks`: a list of texts for the boxes |
| `options` | For `coin`: two strings (heads and tails) |

`rules` show a short message when the answers match. Each rule has this form:

```json
{ "if": [ { "id": "conseq", "op": "gte", "value": 4 }, { "id": "info", "op": "lte", "value": 2 } ],
  "then": "The stakes are high and you have little information. Find the key facts. Set a deadline." }
```
All conditions in `if` must be true. `op` is one of `lt`, `lte`, `gt`, `gte`, `eq`, `neq`. For a `checks` step, the value is the number of full boxes. For a `choice` step, use `eq` or `neq` with the text of the choice. A rule does not show if the user did not answer the step.

## 5. Custom tools (no preset)

If no preset fits, write a `renderer` and the fields yourself:

```json
{ "renderer": "guided", "title": "Energy check", "intro": "...", "steps": [ { "id": "past", "q": "Percent of time that I think about the past", "type": "number" } ] }
```
The renderers are: `scorecard`, `quadrant`, `forces`, `lists`, `tree`, `horizons`, `flow`, `guided`. Use a preset when one exists. Use a custom tool only in a rare case.

## 6. A full example

The folder `examples/` has two complete configs and the files that they build:

- `examples/launch-config.json`: a risky bet with numbers. Tools: `decision_tree_ev` and `premortem`.
- `examples/weekly-config.json`: a list of tasks. Tool: `eisenhower`.

This is a shorter example for a hard personal choice:

```json
{
  "meta": { "title": "Singapore move: yes or no?" },
  "problem": {
    "statement": "My company offered me a two-year role in Singapore. My partner has a job here.",
    "decisionQuestion": "Do I accept the move to Singapore before 15 November?",
    "deadline": "15 November", "stakes": "High", "reversibility": "Hard to undo after we move"
  },
  "assumptions": ["Your partner can work remotely for part of the time. This is not confirmed."],
  "toolSelection": {
    "primary": "force_field",
    "why": "You want a change. This tool shows what pushes you toward it and what holds you back.",
    "alsoConsider": [ { "name": "Regret minimization", "why": "Use it if the scores do not give an answer." } ]
  },
  "tools": [
    { "preset": "force_field", "data": {
        "left": [ { "text": "Career step", "score": 5 }, { "text": "Life abroad", "score": 4 } ],
        "right": [ { "text": "Job of my partner", "score": 5 }, { "text": "Distance from family", "score": 3 } ] } },
    { "preset": "premortem" }
  ]
}
```

## 7. Wording

- Write in STE. Use short sentences. Do not use idioms or long words. Many readers are not native speakers.
- Use the words of the user for the problem. Write the statement in 2 or 3 short sentences.
- Use sentence case for titles. Say what a button or a step does. Do not write "Submit".
- Do not put your opinion in the scores or items. Label each suggestion, for example "Run a trial for one week (suggested)".
- Run `python scripts/ste_check.py config.json` before you build.

## 8. Common build errors

| Message | Action |
|---|---|
| `Unknown preset 'x'` | Run `--list`. Check the spelling. |
| `needs at least 2 options` | Write 2 or more names in `data.options`. |
| `chances add to N, not 100` | Change the percents for that option. |
| `points to missing node` | Change a `next` value in the flow. |
| `still has placeholder text ('Replace')` | You did not write new nodes for `yes_no_rule`. |
| `data.items must have one list per column` | Use the same number as `columns`. |
| `rule points to unknown step` | The rule `id` must match a step `id`. |

## 9. Change the page language (`ui`)

The page has a built-in list of fixed words in English. These are the buttons, labels, hints, and result messages. You can replace any word with `ui`. If the user writes in another language, translate at least the groups below. Do not change the placeholders in braces, for example `{name}`.

```json
"ui": {
  "save": "บันทึกการตัดสินใจ", "load": "เปิดไฟล์ที่บันทึก", "print": "พิมพ์หรือบันทึกเป็น PDF",
  "navProblem": "ปัญหา", "navDecision": "การตัดสินใจของฉัน",
  "situation": "สถานการณ์", "assumptions": "สมมติฐานที่ต้องตรวจสอบ", "why": "ทำไมเลือกเครื่องมือนี้",
  "how": "วิธีใช้", "readout": "วิธีอ่านผล", "think": "คิดให้ครบ",
  "finalTitle": "การตัดสินใจของคุณ", "statusNo": "ยังไม่ตัดสินใจ", "statusYes": "ตัดสินใจแล้ว",
  "chipNo": "การตัดสินใจ: ยังไม่ตัดสินใจ", "chipYes": "การตัดสินใจ: {choice}"
}
```

The main groups are:

- the page: `save`, `load`, `print`, `close`, `nav*`, `situation`, `assumptions`, `why`, `how`, `readout`, `think`, `asText`, `notes`
- the final form: `finalTitle`, `statusNo`, `statusYes`, `choice`, `reason`, `conf`, `step1`, `review`, `trip`
- the tools: `add`, `remove`, `crit`, `weight`, `rankTitle`, `closeCall`, `gutAgree`, `evTitle`, `back`, `again`, `suggests`, and more

The full list of keys is the `S` object at the top of `assets/decision-tool-template.html`. The preset text (titles, steps, advice) is in English. Replace it in the tool entry (`title`, `intro`, `how`, `steps`, `readout`) when you translate.
