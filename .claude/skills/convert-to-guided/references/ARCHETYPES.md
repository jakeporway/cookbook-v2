# Archetypes

Classify by asking: **what does the reader have when the chat ends?**

| | Archetype | They end up with | Role line | §5 header | §9 verb |
|---|---|---|---|---|---|
| A | Build a local tool | A file on their computer they open again and again | setup assistant | WHAT TO BUILD | make |
| B | Configure a reusable assistant | A Project/GPT/Gem/Agent inside their AI product | setup assistant | WHAT TO SET UP | set up |
| C | Run the task now | A finished output — a table, a summary, a draft | research assistant | HOW TO DO THE WORK | do |
| D | Establish a recurring routine | A saved prompt plus a habit they repeat weekly | setup assistant | WHAT TO SET UP | set up |

Tie-breakers:

- Source page says "ask the AI to build you a single HTML page" → **A**, even if
  most of the page is about the chat conversation.
- Source page says "create a Project / GPT / Gem" or "upload your documents" → **B**.
- Source page's payoff is a table, a document, or an answer produced once → **C**.
- Source page's payoff is "every Monday" / "every meeting" / "every quarter" → **D**.
- A recipe that is C once and D thereafter is **D**: the routine is the harder
  thing to set up, and the first run happens inside it.

## Corpus classification

All 47 recipes, as settled during the conversion. These were verified against the
source pages, not guessed, so treat them as the record rather than a starting
guess. Titles mislead here more than you would expect: a recipe about photos or
receipts sounds like a tool and is usually a one-off job, while several
plain-sounding ones quietly ask for an HTML file.

- **A** (12) — private-transcriber, redaction-pass, paper-form, photo-prep,
  spreadsheet-viewer, spreadsheet-editor, caption-burner, interactive-report,
  certificates-from-a-list, dedupe-three-lists, quote-card-press, training-kit
- **B** (8) — handbook-answerer, ask-maria, house-style, personal-voice,
  story-bank, dread-document-expert, funders-eyes, intake-normalizer
- **C** (21) — district-lookup, 990-lookup, survey-themes, contract-read,
  receipt-shoebox, signin-sheets, whiteboard, avatar-video, export-button,
  whos-missing, matching-gifts, volunteer-employers, rule-change, open-data,
  inherited-spreadsheet, plain-language, announcement-test, finance-explainer,
  drive-archaeologist, slide-deck, report-podcast
- **D** (6) — monday-morning, board-packet, meeting-follow-through, preflight,
  one-event-every-asset, annual-report-social

The fastest reliable check is a grep, because A is the one archetype the source
page states outright:

    grep -l -i "self-contained HTML\|single HTML file" site/recipe-<slug>.html

A hit means A, with one exception: `whos-missing` offers a local tool only as its
privacy alternative, so the built file belongs in §8 and the recipe stays C.

## What changes per archetype

**A — build a local tool.** §3 clause 3 carries the file-delivery branch: hand me
a downloadable file if the product can, otherwise one copyable block plus
click-by-click saving instructions (ask Mac or Windows when the clicks differ).
§5 specifies a single self-contained HTML file, states plainly whether internet is
needed, and requires the page to say on its face that nothing leaves the computer.
§6 covers saving, opening, and a first test on non-sensitive material.

**B — configure a reusable assistant.** §2 names the product-specific words for
the thing (Project, GPT, Gem, Agent) and says the assistant will pick the right
one. §3 clause 3 must include the plan check and the fallback for plans without
the feature: a saved starter message plus attaching the files to a fresh chat each
time. §5 includes the instruction text to paste into the new assistant, indented
and quoted, with slots. §6 covers testing against real questions, checking quotes
against the source document, sharing with colleagues, and the ownership rule —
whoever owns the source material owns updating this.

**C — run the task now.** §1 is "research assistant" and "run the following FOR
me". §3 clause 3 becomes a live-web-access check when the recipe needs current
facts: if the product can't search the web, stop and say so rather than answering
from memory. §5 is the method plus the accuracy rules: source link per row,
UNKNOWN rather than a guess, no inference from adjacent data, and a
least-confident list after the output. §6 is fix-the-unknowns, spot-check-N, then
get-it-into-your-system.

**D — establish a recurring routine.** §2 describes the weekly or per-event
rhythm, not just the artifact. §5 has the assistant produce the reusable prompt or
checklist the reader saves, written so it works with next week's inputs and not
only this week's. §6 covers running it once together on this week's real material,
then where to save it and what triggers running it again. §7 usually carries the
staleness warning: a routine nobody updates goes quietly wrong.
