# Elicitation guide

Use this guide to learn the problem and to get the tool inputs from the user. Read it at Step 1. Read section 5 again at Step 3.

## Contents

1. Problem statement and decision question
2. The context checklist
3. Questions for each kind of decision
4. How to ask
5. Widen the options
6. Criteria and values
7. Where each answer goes in the config
8. Common situations

## 1. Problem statement and decision question

A **problem statement** says what is wrong or what happens. A **decision question** says what the user must choose and by when. The tool needs both.

| Problem statement (the user says) | Decision question (you write) |
|---|---|
| "I hate my job." | "Do I look for a new job this year, change my role here, or stay and change how I work?" |
| "We are late on everything." | "Which three tasks do we do first this week? Which tasks do we remove or give to others?" |
| "My boss offered me a move to Singapore." | "Do I accept the move to Singapore before 15 November?" |
| "Which vendor?" | "Which of the three vendors do we sign with by the end of the quarter?" |

A good decision question has three parts. It names the choice. It has a time limit. It allows more than yes or no when possible. If the user gives only a problem, write the decision question. Then ask: "Is this the choice that you must make?"

## 2. The context checklist

Get these items. The items marked **(gate)** are necessary before you choose a tool. Do not ask for all items at one time.

| Item | Question | Config field |
|---|---|---|
| Problem and background (gate) | "What is happening?" | `problem.statement`, `problem.background` |
| Decision question (gate) | "What must you decide?" | `problem.decisionQuestion` |
| Kind of decision (gate) | Learn it from the message. See `tool-selection.md`. | tool choice |
| Reversibility (gate) | "If it goes wrong, can you return? How hard is it?" | `problem.reversibility` |
| Stakes (gate) | "How big is this: small, medium, or life-changing?" | `problem.stakes` |
| Deadline (gate) | "When must you decide?" | `problem.deadline` |
| Decision owner | "Who decides? Do other people have a say?" | `problem.owner` |
| People affected | "Who feels the result?" | `context` |
| Limits | "Which limits do not change: budget, time, rules?" | `context` |
| What the user tried | "What did you try or remove?" | `context` |
| Options | "Which options do you see now?" | tool `data` |
| What matters | "What matters most in this choice?" | criteria in `data` |
| Known and unknown | "What do you know? What do you not know yet?" | tool choice, `assumptions` |
| First preference | "Which way do you lean now?" | scorecard `data.gut` |
| Worry | "What worries you most?" | pre-mortem, `context` |

## 3. Questions for each kind of decision

Ask only for the items that you do not have.

**Choose between options.** Which options does the user have? What does each option cost? What matters most: price, time, quality, risk, or people? Is there a limit that the user cannot cross?

**Go or no-go.** What is the plan in one sentence? What is the best case? What is the worst case? What does the user lose if the user waits one month?

**Prioritize tasks or projects.** List all items, also small items. Which item has a hard deadline? Which item hurts most if the user skips it?

**Risky bet with numbers.** What can happen after each option? What is the chance of each result? A rough guess is enough. What is the payoff or cost of each result?

**Change (job, move, relationship, study).** What pulls the user? What holds the user? Which items are facts? Which items are fears? What does the user do if the user is sure that it works?

**Goal or plan.** What result does the user want at the end? Which part does the user control? By when? Who must agree?

**Team or people.** Which people take part? What is the task? How skilled and how motivated is each person for this task? Is the team new or old? Where does the discussion stop?

**Ideas.** What is the goal? What did the user try? Which parts can change? Who are the competitors? Who solved a similar problem?

**Mistake.** What happened? What did the user expect? Which people and which things took part? What does the user do in a different way next time?

**Understand myself.** When does the user feel most alive at work or in life? When does the user feel tired or empty? What do other people say about the user? What does the user really want? What does the user only think that the user must want?

## 4. How to ask

1. Read the whole message first. Take every fact from it.
2. Give a short reason when you ask. Example: "Can you undo this later? This tells me how much effort the decision needs."
3. Give your best guess for the user to react to. Example: "I think the real choice is A or B, with a hard limit of 1,200 USD. Is this what you mean?"
4. Use the `ask_user_input_v0` function for short answers, if it is available. Examples: kind, stakes, reversibility, deadline. Keep each option short.
5. Ask 3 questions or fewer in one message. Fewer is better.
6. If the user shows stress, go slowly. Say one sentence that shows you understand. Then ask one gentle question. The tool can wait.
7. If the user pastes a long document, take the facts from it. Show 3 to 5 lines that say what you understood. Ask the user to check the lines.
8. If the user gives little information and says "just build it", build the tool. Label each assumption. Do not stop the work for questions.

## 5. Widen the options

Narrow thinking is the most common trap. Do these steps before you fix the options in the tool.

1. **Two options.** Ask: "Can you do both? Is there a middle way?" (the AND option)
2. **Vanishing options.** Ask one time: "If none of these options were possible, what would you do?"
3. **Small test.** Ask: "Can you try a small version first? Examples: a trial, a pilot, one week, a call with a person who did it."
4. **Do nothing.** Add "stay as it is" or "wait" as a real option. The user then sees the true cost of it.
5. **Other people.** Ask: "Who had a similar choice? What did this person do?"
6. **Remove the weakest.** More than 5 options cause overload. Help the user keep the best 3 to 5.

Mark each option that you add with "(suggested)". The user then knows which options are the options of the user.

## 6. Criteria and values

For a scoring tool, the criteria come from the values of the user. They do not come from what is easy to measure.

- Ask: "In one year, what makes you glad that you chose well?" Change each answer to a criterion.
- Use 4 to 6 criteria. Join criteria that are almost the same. Remove criteria that do not change the decision.
- The user must be able to score each criterion from 1 (poor) to 5 (excellent).
- For cost and risk, write the name so that 5 is good. Write "Low cost" and not "Cost". Write "Low risk" and not "Risk".
- The user sets the weights. If the user asks you for weights, set them. Then write this in `assumptions`: "The weights are my first guess. Please change them."

## 7. Where each answer goes in the config

| What you learned | Config field |
|---|---|
| The words of the user about the situation | `problem.statement` (2 or 3 short sentences) |
| The choice and the time limit | `problem.decisionQuestion` |
| Deadline, owner, stakes, reversibility, background | `problem.deadline`, `owner`, `stakes`, `reversibility`, `background` |
| Budget, rules, people affected, what the user tried | `context` (a list of label and value pairs) |
| Each guess that you made | `assumptions` (a list of short sentences) |
| The reason for the tool | `toolSelection.why`, `toolSelection.alsoConsider` |
| Options, criteria, items, numbers | `data` of each tool (see `html-config.md`) |
| A good end for the work | `finalStep.prompt` (optional) |

## 8. Common situations

**The user has a feeling but no options.** Use `grow` or `wrap`. Widen the options first. Do not use a scoring tool with one option.

**The user decided and wants approval.** Be kind and be honest. A pre-mortem of the choice is a fair test. It checks the plan and does not argue with the person.

**Two people, one decision.** Tell each person to score alone first. Then compare the differences. A difference often shows a hidden value.

**Another person makes the decision.** Help the user prepare. Use a pros and cons list for the case that the user presents. Or use a `rumsfeld` map of the risks that the user raises.

**The user wants certainty.** Say with care that the tools help the user think. They do not predict the future. Use `decide_when` and `stop_rule` to manage the wait and the exit.
