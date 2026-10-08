# Choose the right tool

Read this guide at Step 2. Choose one main tool. Add one stress test only if the decision is hard to undo. Explain the choice in one or two short sentences.

## Contents

1. Diagnose with six questions
2. Effort level
3. Routing table
4. Good pairings
5. When two tools fit
6. Worked examples
7. Mistakes to avoid

## 1. Diagnose with six questions

Learn the answers from the conversation. Ask a question only if the answer changes the tool.

1. **Kind.** What must the user decide? Choose one kind from this list:
   - choose between options, go or no-go, prioritize, risky bet
   - change, goal, understand myself, feedback
   - team or people, find ideas, learn from a mistake, when to decide or stop
2. **Reversibility.** Can the user undo the decision? The answer is easy, hard, or impossible. The `doors` tool helps with this question.
3. **Uncertainty.** Does the user know cause and effect? The `cynefin` tool helps with this question.
   - Clear or complicated: use analysis tools (matrix, tree, SWOT).
   - Complex: use small experiments. Use `trial_run`, `doors`, and `premortem` for each experiment.
   - Chaotic (a crisis now): act first. Do not build a heavy tool. Offer `eisenhower` to sort the work and `stop_rule` to set limits. Return to analysis when the situation is calm.
4. **State of the options.** The user has no options, two options, or many options.
   - No options: use `grow`, `wrap`, `morphological_box`, or `gap_in_market`.
   - Two options: use `pros_cons`, `force_field`, `rubber_band`, `ten_ten_ten`, or `trial_run`.
   - Three to five options: use `weighted_matrix`.
   - More than five options: reduce them first. Use a quick screen, for example `eisenhower`. Then score the finalists.
5. **People.** The user decides alone or with a team. Team tools: `six_hats`, `appreciative_inquiry`, `team_performance`, `hersey_blanchard`.
6. **Numbers.** Can the user estimate chances and payoffs? If yes, `decision_tree_ev` is possible. If no, do not use it. A tree with invented numbers gives false comfort.

## 2. Effort level

Use the `hard_choice` idea. Ask two questions. Can the user compare the options easily? How big are the consequences?

| | Small consequences | Big consequences |
|---|---|---|
| **Easy to compare** | **Easy choice.** Decide fast. Use a light tool or no tool. | **Big but clear.** The better option is clear. Check it one time and go. |
| **Hard to compare** | **Different options.** Follow the preference. A coin test (`unconscious_thinking`) is enough. | **Hard choice.** No answer is clearly right. Use a main tool and a stress test. Support the choice with strong personal reasons. |

Match the tool to the box. Too much process for a small choice wastes the time of the user. Too little process for a hard choice costs more.

## 3. Routing table

| Situation | Main tool (preset id) | Stress test |
|---|---|---|
| Choose between 3 to 5 options on several criteria | `weighted_matrix` | `premortem` or `ten_ten_ten` on the winner |
| Two options, with reasons for and against | `pros_cons` | `ten_ten_ten` |
| The user cannot choose and has strong feelings | `rubber_band` | `ten_ten_ten` or `regret_minimization` |
| The user wants a change, but obstacles exist | `force_field` | `premortem` |
| Risky bet, and the user can estimate the outcomes | `decision_tree_ev` | `premortem` |
| The user does not know if the decision is quick or slow | `doors` | the tool that the result names |
| The user does not know the kind of situation | `cynefin` | the tool that the result names |
| Quick yes or no by elimination | `yes_no_rule` (write new nodes) | `stop_rule` |
| Too many tasks, daily or weekly | `eisenhower` | none |
| Too many projects | `project_portfolio` | `eisenhower` for the next actions |
| Where to invest in products or units | `bcg_box` | `swot` for the question marks |
| Understand a business or venture first | `swot` | `rumsfeld` |
| Understand the risks and the gaps in knowledge | `rumsfeld` | `premortem` |
| Commit to a plan without failure | `premortem` | `stop_rule` |
| Set a quit rule before the start | `stop_rule` | `decide_when` |
| The user does not know when to decide | `decide_when` | `doors` |
| Buy a product or service | `buyers_model` | `weighted_matrix` |
| Two options feel equal | `trial_run` or `unconscious_thinking` | `ten_ten_ten` |
| Set a goal | `goal_check` | `grow` |
| Personal or coaching talk | `grow` | `regret_minimization` |
| Important personal decision, and no other tool fits | `wrap` | none (WRAP has a stress test in it) |
| The user worries about bias or a rushed decision | `bias_check` | `premortem` |
| Change a job | `personal_performance` | `regret_minimization`, `flow_model` |
| What makes the user happy at work | `flow_model` | `johari` |
| How other people see the user | `johari` | none |
| What the user needs and wants in life | `maslow_check` | `grow` |
| The user got feedback and does not know what to do | `feedback_box` | none |
| A mistake happened or can happen | `swiss_cheese` | `double_loop` |
| Learn from a past event or project | `making_of` | `double_loop` |
| How to lead one person | `hersey_blanchard` | none |
| A team discussion that does not progress | `six_hats` | `appreciative_inquiry` |
| A group does not work as a team | `team_performance` | `six_hats` |
| New ideas or a new product | `morphological_box` | `gap_in_market` |
| Is there room in the market | `gap_in_market` | `decision_tree_ev` |

## 4. Good pairings

A strong decision has one tool to structure the choice and one tool to stress test it. These are the best stress tests:

- `premortem`: finds the ways that the plan can fail. Use it for decisions that are hard to undo.
- `ten_ten_ten`: separates short-term feelings from long-term value. Use it for personal choices.
- `bias_check`: checks anchoring, confirmation, availability, and fast thinking.
- `doors`: checks if the user can make the decision smaller and reversible.

Do not add a stress test to a small decision that the user can undo.

## 5. When two tools fit

- Choose the tool whose inputs the user can give now. A tool that needs numbers that the user does not have stops the work.
- Choose the tool that shows the structure of the problem. `force_field` shows what blocks a change. `pros_cons` only counts reasons.
- If the user shows strong emotion, choose a quiet tool (`grow`, `rubber_band`, `ten_ten_ten`). Do not choose a numeric tool.
- If a team uses the file, choose a tool with a clear shared view (`weighted_matrix`, `eisenhower`, `swot`, `force_field`).
- Write the other tool in `toolSelection.alsoConsider`. Add one line that says when it is better.

## 6. Worked examples

Each example shows the diagnosis, the tool, and the text for `toolSelection.why`.

**Example 1. The user has two job offers.** The user says: "I have two job offers. One pays more. One has better people and more growth. I must answer by Friday."

- Kind: choose between options. The user cannot undo the choice easily. The user has two options and several criteria. The effort level is "hard choice".
- Main tool: `weighted_matrix`. Criteria: Pay, Growth, People, Work-life balance, Low risk.
- Stress test: `ten_ten_ten`.
- `why`: "Each offer is good in a different way. A scoring table shows both offers. The 10/10/10 test checks how each choice feels later."

**Example 2. The team wants to release a feature.** The user says: "We must decide. Do we release the feature to all users, or to 5% of users first?"

- Kind: go or no-go. The user can undo a small test. The user cannot easily undo a full release. Uncertainty: complex.
- Main tool: `doors`. It points to a pilot.
- Stress test: `premortem` of the pilot plan.
- `why`: "A small test lets you learn first. The pre-mortem finds what can go wrong in the test."

**Example 3. The user has 40 tasks.** The user says: "I have 40 tasks and the week is full."

- Kind: prioritize. The user can undo the choice. The effort level is small to medium.
- Main tool: `eisenhower`. No stress test.
- `why`: "You must sort the tasks. You do not need to score them."

**Example 4. The user thinks about a business.** The user says: "Do I start my own business?"

- Kind: change. The stakes are high. The options are not clear (start, wait, test on the side).
- Main tool: `wrap`. It widens the options first. Examples: a side project, a part-time start, a first customer.
- Stress test: `premortem` of the chosen path.
- `why`: "You have not listed your options yet. WRAP helps you find more options. The pre-mortem checks the best option."

**Example 5. A team argues in meetings.** The user says: "My team argues in meetings and we decide nothing."

- Kind: team. Main tool: `six_hats`. Other tool: `team_performance`, if trust or goals are the problem.
- `why`: "The six hats let everyone think in the same mode at the same time. People then stop talking at cross purposes."

## 7. Mistakes to avoid

- Do not build 3 or 4 tools to be thorough. This overloads the user.
- Do not use a numeric tool with invented numbers.
- Do not choose a tool because it looks advanced. The simplest tool that fits is the best tool.
- Do not skip the reversibility question. It saves the most effort.
- Do not put your opinion in the scores. The tool must have no opinions, except options that you label "(suggested)".
- Do not treat a crisis as a planning problem.
