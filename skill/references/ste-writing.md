# Write in Simplified Technical English

Use this guide when you write text for the user. This includes chat replies, config text, notes, and example text. Read it one time at the start of a job.

## Contents

1. Why this skill uses STE
2. The rules
3. Vocabulary of this skill
4. Words and phrases to avoid
5. Examples
6. How to check your text
7. Other languages

## 1. Why this skill uses STE

STE is a controlled form of English. It has short sentences and plain words. Each word has one meaning. ASD-STE100 is the standard. Aircraft maintenance manuals use it. The readers of these manuals are often not native speakers.

The readers of this skill are the same kind of people. Many users are not native speakers. Some users are not technical. Other agents can also read the text. A short sentence with one meaning helps all of them.

This skill uses the structural rules of STE. It does not use the official word list of ASD. The skill does not claim full STE compliance. Use the `asd-ste100` skill when it is available.

Do not use STE for text where voice matters, for example a poem or an advertisement. Do not make the text so short that the meaning is lost.

## 2. The rules

| Rule | Do | Do not |
|---|---|---|
| One instruction in a sentence | "Open the file. Read line 3." | "Open the file and read line 3, then check it." |
| Sentence length | 20 words or fewer in an instruction. 25 words or fewer in a description. | A long sentence with many clauses. |
| Active voice | "The script builds the file." | "The file is built by the script." |
| Simple tenses | "The user chose an option." | "The user has chosen an option." |
| No semicolons | Write two sentences. | Use a semicolon. |
| No phrasal verbs | "Remove the item." | "Take out the item." |
| Verb, not noun | "Analyze the log." | "Do an analysis of the log." |
| Keep the article and the subject | "The tool shows the result." | "Shows result." |
| Noun clusters | 3 words or fewer. | 4 words or more in a row. |
| Keep the hedge | "The plan may fail." | "The plan fails." (if the source says "may") |
| Lists for steps | Use a numbered list for 3 steps or more. | Put 3 steps in one sentence. |
| One topic in a paragraph | 6 sentences or fewer. | A paragraph with 2 topics. |
| No marketing words | Say what the tool does. | "A powerful, seamless tool." |

Do not add a fact that the source does not state. Do not remove a condition to make a sentence short.

## 3. Vocabulary of this skill

Use one word for one meaning. Do not change words in the same file.

| Word | Meaning | Do not use |
|---|---|---|
| user | The person who asks you for help. | client, customer, person |
| tool | A decision tool. It has one method and one HTML file. | framework, model, instrument |
| preset | A tool definition in `presets.json`. | template (see below) |
| template | The HTML file that the script fills. | |
| config | The JSON file that you write for the script. | setup, settings file |
| option | A choice that the user can take. | alternative, choice |
| criterion, criteria | A factor to compare options. | factor, dimension |
| decision question | One sentence that states what the user must decide. | |
| stress test | A second tool that looks for weak points. | |
| check | Look at something to learn if it is right. | verify, confirm, validate |
| ask | Put a question to the user. | |
| choose | Take one thing from a group. | select, pick |
| build | Make the HTML file with the script. | generate, create, produce |
| write | Put text in a file or in a field. | fill in, enter |
| reversible | The user can undo the decision. | |
| stakes | What the user can lose or gain. | |

## 4. Words and phrases to avoid

| Avoid | Use |
|---|---|
| find out | learn, find |
| look for | find |
| look at | read, check |
| set up | prepare, make |
| fill in | write |
| carry on | continue |
| come back, go back | return |
| turn into | change to |
| cut down | reduce |
| hand off | give |
| write down | write |
| rule out | remove |
| in order to | to |
| make use of | use |
| a number of | some, 3 |
| is able to | can |
| perform an analysis of | analyze |
| provide assistance to | help |
| robust, seamless, powerful, easy | Remove the word. Give a fact. |

## 5. Examples

| Before | After |
|---|---|
| "It's important to note that you might want to think about whether this decision can potentially be reversed." | "Check if the user can undo the decision." |
| "Fill in the weights, then the scores, and look at the ranking to find out which option wins." | "1. Write the weights. 2. Write the scores. 3. Read the ranking." |
| "The tool has been built so that the choices of the user are saved." | "The tool saves the choices of the user." |
| "Pick up the key facts and sort out what is missing." | "Find the key facts. Find the facts that are missing." |
| "If the user is stressed, it may be a good idea to slow down." | "If the user is stressed, go slowly. Ask one gentle question." |

## 6. How to check your text

1. Write the config.
2. Run `python scripts/ste_check.py config.json`.
3. Read each finding. Fix the sentence. Do not remove a fact.
4. Run the command again until the output shows no findings.
5. Read the text one more time. Make sure that the meaning is the same.

The script uses `scripts/ste_lint.py`. This is the linter from the `asd-ste100` skill (MIT license). It does not check hedges. It cannot check the official word list.

To check a text file, run `python scripts/ste_lint.py file.md`.

This file shows bad text on purpose in the "avoid" and "before" columns. The linter flags that text. Ignore those findings.

## 7. Other languages

STE is for English. If the user writes in another language, write in that language. Use the same ideas: short sentences, one idea in each sentence, and one word for one meaning. Do not use idioms. Set `meta.language` and translate the page text with `ui`.
