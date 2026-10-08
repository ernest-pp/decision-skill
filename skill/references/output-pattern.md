# Output pattern: the whiteboard page

Every tool file has one visual pattern. It comes from two examples that the user gave: `MFG_CRMP_User_Flow_v1.html` (flow charts on a page) and `MFG_CRMP_User_Story_Whiteboard_v4.html` (a board of cards with filters and a drawer). The template `assets/decision-tool-template.html` draws all of it. Read this file when you must explain the page, change a preset, or check that a change keeps the pattern.

## What the page looks like

1. **Board.** The background is pale blue-grey with a dot grid (28 px). The text is dark ink (`#1f2933`). Secondary text is grey.
2. **Fonts.** Body text: IBM Plex Sans Thai. Headings and labels: Mali (a hand-written face). Both load from Google Fonts. The page has safe fallback fonts. Thai and English both work.
3. **Top bar (fixed).** The bar is white with a 2 px ink line below it. First row: the short title, the decision status, and the buttons Save, Load, and Print. Second row: jump chips with a color square. There is one chip for each section. They work like the filter chips in the examples.
4. **Hero.** A large hand-font title, one short paragraph, and small boxes with a hard shadow. The boxes show the deadline, the stakes, the reversibility, and the owner.
5. **Sticky note.** The decision question is on a yellow sticky note with tape. The note has a small tilt. Each tool title is on a sticky note in its own color.
6. **Panels.** A panel is white with a 1.5 px ink border and a 4 px hard shadow. There is no blur. The panels are: The situation, Assumptions to check (with a dashed "to check" tag), Why this tool, and Notes.
7. **Cards.** A card is white with an ink border and a hard shadow in the color of the tool. It has a 7 px colored bar on the left edge. The card holds the tool, the numbered "How to use it" list, the "Think it through" steps, and the "How to read the result" note.
8. **Colors.** The sticky colors do not change: yellow `#f6d36b`, green `#9fd8ab`, blue `#bcd7fb`, purple `#cdbdf0`, pink `#f2989f`, teal `#9ee0e0`, orange `#ffc999`. Tool 1 is yellow. Tool 2 is blue. Tool 3 is green. The decision section is orange.
9. **Flow tools.** The page draws a flow tool like the user-flow example. It has a dark Start pill, yellow hexagon questions, arrows with the chosen answer as a small label, and a green End box. A legend shows the three shapes.
10. **Read as text.** Each tool has a "Read this as text" section. It shows the current state as a plain list. It helps screen readers, printing, and copying.
11. **Drawer.** When the user presses Save, a drawer opens on the right. It has a text summary and a Copy button. Esc or the Close button closes it. The focus returns to the Save button.
12. **Quality.** The focus ring is blue and visible. The tap targets are large. The page respects reduced motion. The print styles hide the bar and the drawer. On a phone, the page has one column (below 640 px).

## Rules for a change

- Keep the vocabulary: board, sticky note, paper card, hard shadow, colored edge bar, hand-font headings, and ink borders. Use a radius of 3 px or less.
- Do not add gradients, soft shadows, round cards, or new accent colors. Use the sticky colors.
- Do not make a layout for one tool. A new tool uses an existing renderer: `scorecard`, `quadrant`, `forces`, `lists`, `tree`, `horizons`, `flow`, or `guided`.
- Make each control available by keyboard. Give each control a name for screen readers.
- Keep the file self-contained. Do not load scripts from other sites. The page loads only the Google Fonts stylesheet from outside.
- Save must work in three ways. It downloads a file. It saves in the browser. It shows the text summary.
