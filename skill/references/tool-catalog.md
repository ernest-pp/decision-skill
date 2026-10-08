# Tool catalog

This file has one entry for each preset. Read only the entries for the tools that you chose. Each entry has these parts:

- **Use when:** the situation that the tool fits.
- **Elicit:** what to ask the user, and which `data` fields to write.
- **Read:** how to read the result with the user.
- **Careful:** limits and traps.
- **Source:** where the method comes from.

The preset has the title, the labels, the steps, and the "how to use it" text. You write only the data for the problem. Run `python scripts/build_tool.py --list` to see the ids.

## Contents

- Structure a choice: `weighted_matrix`, `decision_tree_ev`, `pros_cons`, `force_field`, `rubber_band`
- Sort and prioritize: `eisenhower`, `project_portfolio`, `bcg_box`, `hard_choice`
- Check time and feelings: `ten_ten_ten`, `trial_run`, `unconscious_thinking`, `decide_when`
- Stress test a plan: `premortem`, `doors`, `stop_rule`, `rumsfeld`, `bias_check`, `swiss_cheese`
- Understand the situation: `cynefin`, `swot`, `gap_in_market`
- Goals and coaching: `goal_check`, `grow`, `wrap`, `regret_minimization`
- Buying: `buyers_model`
- Understand yourself: `personal_performance`, `flow_model`, `johari`, `maslow_check`, `making_of`, `double_loop`, `feedback_box`
- Team and people: `hersey_blanchard`, `six_hats`, `appreciative_inquiry`, `team_performance`
- Ideas: `morphological_box`
- Fast rule: `yes_no_rule`
- Models in the book that are not presets

---

## Structure a choice

### weighted_matrix (scorecard)
**Use when:** The user has 3 to 5 options and several criteria. The user wants a fair and visible comparison. Other names: decision matrix, weighted scoring, Pugh matrix.
**Elicit:** Options in `data.options` (2 to 5). Criteria in `data.criteria`, a list of `{name, weight}` (4 to 7). Weights are 1 to 5. Leave the scores empty. Name cost and risk criteria so that 5 is good, for example "Low cost".
**Read:** The ranking is a guide. Check three things. Is it a close call? The tool says so. Does the winner change if all weights are equal? The tool says so. Does the result match the first preference of the user? The tool compares them. If the result does not match, a criterion is missing or a weight is wrong. Find which one.
**Careful:** More than 7 criteria make the weights weak. Equal weights mean that the user did not state a strategy. The most common error is a cost criterion that is not reversed.
**Source:** Standard multi-criteria decision analysis.

### decision_tree_ev (tree)
**Use when:** The results are uncertain. The user can estimate chances and payoffs. Money, hours, or points are all possible.
**Elicit:** `data.unit` (for example "USD"). `data.options`: each option has `{name, cost, outcomes:[{label, p, payoff}]}`. Chances (`p`) are in percent and total 100 for each option. Ask the user for the numbers. Never invent them. If the user has no numbers, use another tool.
**Read:** Compare the expected value (the average after cost) and the worst case. If the best average can lose money, ask if the user can afford one bad result. Test the result: change one chance by 10 points.
**Careful:** The user makes expected value from guesses. It helps thinking. It does not predict the future. Do not use it if the user cannot compare the results.
**Source:** Decision tree analysis with expected monetary value.

### pros_cons (forces)
**Use when:** The user has two options or one yes/no choice. The choice is small or medium. Each reason has a strength from 1 to 5.
**Elicit:** `data.left` (reasons for) and `data.right` (reasons against), as short strings or as `{text, score}`.
**Read:** Read the biggest item on each side and the totals. Ask a person who does not agree with the user to add one item to each side.
**Careful:** A list can have bias. A long list of weak reasons can hide one strong reason. The tool shows the biggest items for this reason.
**Source:** The classic pros and cons list, with strength scores.

### force_field (forces)
**Use when:** The user wants a change (a new process, a habit, a move). The user wants to know what helps and what blocks it.
**Elicit:** The change (write it in the decision question). `data.left` has the driving forces. `data.right` has the restraining forces. Scores are 1 to 5.
**Read:** The change happens only when the driving forces are stronger than the restraining forces. Lewin advised to reduce the restraining forces first. Use the two questions in the tool to plan how.
**Careful:** A change to one force can make new forces. Check again after the first action.
**Source:** Force field analysis by Kurt Lewin (1940s).

### rubber_band (forces)
**Use when:** The user cannot choose between two important and opposite options. Strong feelings are part of the problem.
**Elicit:** What pulls the user (`data.left`). What holds the user (`data.right`). Use short phrases.
**Read:** Ask which items on the holding side are facts and which items are fears. Ask: "Imagine that the rubber band breaks today. Which way do you move?" The answer often shows the preference.
**Careful:** Do not push the user to an answer. The tool helps the user see. It does not press.
**Source:** Rubber band model. From The Decision Book.

---

## Sort and prioritize

### eisenhower (quadrant)
**Use when:** The user has too many tasks. The user wants to sort them by importance and urgency.
**Elicit:** A list of tasks in `data.items`. You can place clear items with `q`. `tr` = urgent and important (do now). `tl` = important, not urgent (plan). `br` = urgent, not important (give to another person). `bl` = neither (later or remove).
**Read:** If the top-left box is empty, the user may work only on urgent tasks. Ask which top-left task goes in the calendar today.
**Careful:** "Important" means that the task serves the goals of the user. It does not mean that the task feels loud.
**Source:** Eisenhower matrix. From The Decision Book.

### project_portfolio (quadrant)
**Use when:** The user has many projects, at work and in private life. The user wants to keep, change, give away, or stop some projects.
**Elicit:** A list of projects in `data.items`. The user places each project by how much it helps the main goal and how much the user learns.
**Read:** Protect time for the very good projects. Ask which "stop" project can end this month.
**Careful:** The book also has a version with cost and time. The preset uses the version with goal and learning. For cost and time, replace `axes` and `quadrants`.
**Source:** Project portfolio matrix. From The Decision Book.

### bcg_box (quadrant)
**Use when:** The user decides where to invest in products, units, or markets.
**Elicit:** A list of products or units in `data.items`. The user places them by market growth and by relative market share.
**Read:** Stars: invest. Cash cows: keep them. Dogs: sell or close them, unless they have a value that is not financial. Question marks: a hard decision. Invest strongly or stop.
**Careful:** The user needs real market data to place items well. If the user has no data, use `swot` first.
**Source:** BCG growth-share matrix. From The Decision Book.

### hard_choice (quadrant)
**Use when:** The user wants to know how much effort a decision needs. Or the user has several decisions to compare. You can also use the idea in your diagnosis (see `tool-selection.md`).
**Elicit:** A list of decisions in `data.items`.
**Read:** Easy choice: decide fast. Different options: follow the preference. Big but clear: the choice is big but easy. Hard choice: use more tools and give personal reasons.
**Source:** Hard choice model. From The Decision Book.

---

## Check time and feelings

### ten_ten_ten (horizons)
**Use when:** A strong emotion today can change a choice. Use it most for personal choices.
**Elicit:** `data.options` (2 to 4). The time points do not change: 10 minutes, 10 months, 10 years.
**Read:** Good now and bad later: a trap. Bad now and good later: often worth it. Good at all three points: strong.
**Source:** 10-10-10 from Suzy Welch. Also in Decisive (Heath and Heath) and The Decision Book.

### trial_run (horizons)
**Use when:** Two options feel equal and the user can try each option for some days.
**Elicit:** Two options in `data.options`.
**Read:** Compare the trend over the three days. Ask which trial the user was sorry to stop.
**Source:** The Jesuit method of Ignatius of Loyola. Also in The Decision Book.

### unconscious_thinking (guided)
**Use when:** A complex choice has no clear answer after real thought. Or two options are close. It is also good for small choices.
**Elicit:** Nothing. You can change the coin labels in the step `coin` (`options`) to the two real options.
**Read:** The coin does not decide. The reaction of the user to the result decides.
**Careful:** Do not use a coin when the safety of another person depends on the result.
**Source:** Theory of unconscious thinking. From The Decision Book.

### decide_when (guided)
**Use when:** The user waits too long, or acts too early. The tool helps the user set a date for the decision.
**Elicit:** Nothing. The user answers the steps.
**Read:** The rules show this: if the consequences are small, decide now. If the stakes are high and the information is little, find the key facts and set a firm deadline.
**Careful:** If the user decides to decide later, the user must tell the people involved.
**Source:** Consequences model. From The Decision Book. The idea to decide with about 70% of the information, when the user can undo the choice, comes from Jeff Bezos.

---

## Stress test a plan

### premortem (guided)
**Use when:** The plan is almost ready and hard to undo. It is best as the second tool.
**Elicit:** Optional. Change the first step to name the plan, for example "It is one year after you accepted the move to Singapore..." (replace `steps`).
**Read:** The output is the three biggest reasons for failure and the warning signs. Ask which reason the user notices too late.
**Careful:** At least one reason must be a cause that the user or the team made.
**Source:** Pre-mortem by Gary Klein (Harvard Business Review, 2007).

### doors (flow)
**Use when:** The user does not know if the decision needs a slow or a fast process.
**Elicit:** Nothing. The user answers two questions. You can change the text of the question to name the real decision.
**Read:** Two-way door: decide fast and review. One-way door: go slowly. First try to change it to a two-way door. Use a pilot, a trial, a smaller first step, or an exit clause. Or split the test from the full commitment.
**Careful:** A two-way door for a rich team can be a one-way door for a poor team. Ask "for you".
**Source:** One-way and two-way doors. From the Amazon shareholder letters of Jeff Bezos (2015 and 2016).

### stop_rule (guided)
**Use when:** The user starts something that is hard to quit after the start. Examples: a climb, a project, a negotiation, a spending plan, a study.
**Elicit:** Optional. Write the goal. The user sets the limit that does not change (time, cost, or safety) and a flexible limit.
**Read:** A stop rule has no conditions. If the group reaches the limit, the group stops. Check that the user wrote the rule before the start. Check that no person can change it under pressure.
**Source:** Stop rule. From The Decision Book. The book gives the 1996 Mount Everest disaster as an example of a broken stop rule.

### rumsfeld (quadrant)
**Use when:** The user analyzes the risks and the gaps in knowledge of a plan.
**Elicit:** A list of facts, risks, and worries in `data.items`.
**Read:** Known knowns: keep the countermeasure. Known unknowns: make a plan and set a warning sign. Unknown knowns: test the feeling and find evidence. Unknown unknowns: ask people outside the group and keep a reserve.
**Source:** Rumsfeld matrix. From The Decision Book.

### bias_check (guided)
**Use when:** The user can be anchored, can look only for support, can use one story, or can rush.
**Elicit:** Nothing. The user answers the steps.
**Read:** Each full box is a countermeasure that the user did. Each empty box is a task.
**Careful:** Knowing about a bias does not remove it. The countermeasure boxes do the work.
**Source:** Cognitive bias. From The Decision Book. The four biases are: anchor effect, confirmation error, availability error, and fast and slow error.

### swiss_cheese (guided)
**Use when:** The user studies how a mistake happened or can happen. It fits work on process, safety, and quality.
**Elicit:** Optional. Write the event in the first step.
**Read:** A mistake usually comes from many holes that line up. List the layers: people, technical, organization, outside. Close at least one hole in each layer that the user can change.
**Source:** Swiss cheese model. From The Decision Book.

---

## Understand the situation

### cynefin (flow)
**Use when:** The user does not know the kind of situation. Or the usual method fails again and again.
**Elicit:** Nothing. The user answers two questions.
**Read:** Clear: sense, categorize, respond (use best practice). Complicated: sense, analyze, respond (use experts and analysis). Complex: probe, sense, respond (run small experiments). Chaotic: act, sense, respond (stabilize first). Not sure: split the problem into parts and classify each part.
**Source:** Cynefin framework by Dave Snowden.

### swot (lists)
**Use when:** The user must understand a business, a team, a venture, or a personal situation before the decision.
**Elicit:** Items for four boxes. In `data.items`, write four lists in this order: Strengths, Opportunities, Weaknesses, Threats. Strengths and weaknesses are inside. Opportunities and threats are outside.
**Read:** The four questions change the lists to actions: use the strengths, reduce the weaknesses, take the opportunities, and protect against the threats.
**Careful:** A SWOT is a picture of one moment. It does not choose. Use it with a matrix or a force field.
**Source:** SWOT analysis. From The Decision Book.

### gap_in_market (guided)
**Use when:** The user checks if a business idea has room in the market.
**Elicit:** Nothing. The user answers the steps. Use `decision_tree_ev` also if the user has numbers.
**Read:** An empty area can mean that nobody wants the product. Always check the demand before the user trusts a gap.
**Source:** Gap-in-the-market model. From The Decision Book.

---

## Goals and coaching

### goal_check (guided)
**Use when:** The user sets a goal or checks a goal.
**Elicit:** Optional. Write the goal.
**Read:** The final goal is the result. The performance goal is what the user does and controls. The user ticks SMART, PURE, and CLEAR. The user rewrites the goal until all boxes are full.
**Careful:** Whitmore calls the third set CLEAR (Challenging, Legal, Environmentally sound, Agreed, Recorded). Some summaries of the book write CLEAN. Use CLEAR.
**Source:** John Whitmore, Coaching for Performance. Also in The Decision Book.

### grow (guided)
**Use when:** The user has a personal or work problem, or a coaching talk. Or the user has no options yet.
**Elicit:** Nothing. Ask the questions one at a time.
**Read:** If the commitment is low, make the step smaller until the user feels sure.
**Source:** GROW model (Goal, Reality, Options, Will) by Sir John Whitmore.

### wrap (guided)
**Use when:** The user has an important personal decision and no other tool fits. The tool widens the options, tests the assumptions, adds distance, and prepares for a mistake.
**Elicit:** Nothing. The steps are the tool.
**Read:** The tripwire at the end is the key output. It is a clear warning sign and a date.
**Source:** WRAP process by Chip and Dan Heath, from the book Decisive.

### regret_minimization (guided)
**Use when:** The user has a rare, big, personal choice (a move, a career change, a new start).
**Elicit:** Nothing.
**Read:** The rules compare the regret of not trying with the regret of failing. If failing hurts more, find a safer and smaller version.
**Careful:** Do not use it for small choices. Do not use it if the safety of other people depends on the result.
**Source:** Regret minimization framework by Jeff Bezos.

---

## Buying

### buyers_model (guided)
**Use when:** The user buys a car, a laptop, a vendor, or a service, and feels lost in the choices.
**Elicit:** Nothing. Use it with `weighted_matrix` when the user has finalists.
**Read:** Set research limits first. Rank 5 criteria and remove the last two. Do the 10/10/10 check. If two options are equal, let another person decide, flip a coin, or try each option for three days.
**Source:** Buyer's decision model. From The Decision Book.

---

## Understand yourself

### personal_performance (guided)
**Use when:** The user asks "do I change my job?" This version starts from the purpose of the work.
**Elicit:** Nothing. The user gives ratings from 1 to 10 for Have to, Able to, and Want to.
**Read:** Able but does not want: find a different role or meaning. Wants but is not able: learn skills. Low on both: think about a change. High on both: check the expectations.
**Careful:** The original model asks only what the person wants. The preset first asks about the purpose of the work. The choice then stays connected to the people and goals that the user serves.
**Source:** Personal performance model. From The Decision Book, with the change that the source deck describes.

### flow_model (quadrant)
**Use when:** The user wants to find what makes the user happy or tired at work.
**Elicit:** A list of activities.
**Read:** Flow needs strong focus, a task that the user chose, the right challenge, a clear goal, and quick feedback. Too much challenge causes burnout. Too little challenge causes boredom.
**Source:** Flow by Mihaly Csikszentmihalyi. Also in The Decision Book.

### johari (quadrant)
**Use when:** The user wants to know how other people see the user, before a choice about a role or career.
**Elicit:** Words that describe the user. Some words come from the user. Some words come from other people.
**Read:** The hidden and blind areas hold the surprises. Feedback can help and can hurt. Go slowly.
**Source:** Johari window. From The Decision Book.

### maslow_check (guided)
**Use when:** The user does not know the difference between what the user needs and what the user wants.
**Elicit:** Nothing. The user gives ratings from 1 to 5 for five levels.
**Read:** Basic needs come first. A choice that puts a lower need at risk for a higher want needs a second check.
**Source:** Hierarchy of needs by Abraham Maslow (1943). Also in The Decision Book.

### making_of (lists)
**Use when:** The user must understand a past project or period before the user plans the next one.
**Elicit:** Seven lists in `data.items`, in this order: goals, what the user learned, obstacles overcome, successes, obstacles not overcome, failures, people involved.
**Read:** The last question asks what to take into the future and what to leave behind.
**Source:** Making-of model. From The Decision Book.

### double_loop (guided)
**Use when:** The user wants to learn from a mistake at the level of beliefs, not only actions.
**Elicit:** Nothing.
**Read:** The single loop changes the action. The double loop questions the goal or belief behind the action.
**Source:** Double-loop learning. From The Decision Book.

### feedback_box (quadrant)
**Use when:** The user received feedback and must decide which feedback to follow.
**Elicit:** Each piece of feedback as one short line in `data.items`.
**Read:** Criticism: act first. Advice: think and choose. Suggestion: usually ignore it. Compliment: keep it.
**Source:** Feedback box. From The Decision Book.

---

## Team and people

### hersey_blanchard (flow)
**Use when:** A manager must choose how to lead one person on one task.
**Elicit:** Nothing. The manager chooses the description of readiness.
**Read:** New: instruct. Learning: coach. Skilled but not sure: support. Skilled and motivated: delegate.
**Source:** Hersey-Blanchard situational leadership. From The Decision Book.

### six_hats (guided)
**Use when:** A team discussion does not progress.
**Elicit:** Nothing. A moderator must make sure that everyone uses the same hat at the same time.
**Read:** Blue: process. White: facts. Red: feelings. Black: risks. Yellow: benefits. Green: ideas. Close with blue.
**Source:** Six thinking hats by Edward de Bono. Also in The Decision Book.

### appreciative_inquiry (guided)
**Use when:** A team must develop an early idea and not drop it.
**Elicit:** Nothing.
**Read:** Notice the usual reaction of the user: dictator, fault-finder, school teacher, or appreciative thinker. Then use Discovery, Dream, Design, Deploy.
**Source:** Appreciative inquiry 4-D model. From The Decision Book.

### team_performance (guided)
**Use when:** A group does not yet work as a team.
**Elicit:** Nothing. Each member rates alone, if possible. Then the group compares the differences.
**Read:** Fix the first stage that is weak: Orientation, Trust, Goals, Commitment, Implementation, High performance, Renewal.
**Source:** Drexler/Sibbet team performance model. From The Decision Book.

---

## Ideas

### morphological_box (lists)
**Use when:** The user looks for new ideas by a combination of parts.
**Elicit:** Replace `columns` with the real parts (for example Design, Engine, Style, Target group). Write the options for each part in `data.items`.
**Read:** The user combines one option from each part. Then the user extends the ideas with SCAMPER: substitute, combine, adapt, change, put to other use, eliminate, reverse.
**Source:** Morphological box and SCAMPER. From The Decision Book.

---

## Fast rule

### yes_no_rule (flow)
**Use when:** A short chain of yes/no questions can reach a decision by elimination.
**Elicit:** You must write new nodes. Write 3 to 5 short yes/no questions that remove options. Put the question that removes the most options first. Every path must end in an outcome. The build script stops if the placeholder text ("Replace") is in the nodes.
**Read:** Check that the user can answer each question with yes or no.
**Source:** The yes/no rule. From The Decision Book.

---

## Models in the book that are not presets

These models are mostly advice. They are not decision procedures. Mention the idea in your reply if it helps the user. If the user wants one as a tool, build it with a custom `guided` or `lists` config (see `html-config.md`).

- **Choice overload:** this idea is in your elicitation rules. Keep the options and criteria few.
- **Gift model:** a generous gift is better than a cheap gift. An experience is better than an object.
- **Thinking outside the box:** people often think better inside a given structure. This supports `morphological_box`.
- **Expectations model:** very high expectations lead to disappointment. If the user cannot meet the standards, ask: "What do I lose if I lower them?" This is part of `buyers_model`.
- **Energy model:** the time that the user spends on the past, the present, and the future. Use a custom `guided` with three number steps.
- **Cognitive dissonance model:** change the attitude or the behavior to reduce the gap. Use a custom `guided`.
- **Belbin team roles:** nine roles in three groups: action, communication, and knowledge. Use a custom `lists`.
- **Political compass, Sinus milieu, and Bourdieu models:** these are maps of groups. They are not decision tools.
- **Personal potential trap:** promise 80 and deliver 120. Use it as advice about expectations.
- **Johari and cognitive dissonance:** these models touch on how people see themselves. Keep the tone kind.
