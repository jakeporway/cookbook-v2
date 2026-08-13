---
name: convert-to-guided
description: Converts a Decoded Futures cookbook recipe page from step-by-step instructions plus a fill-in-the-blanks prompt into a "guided" page whose single pasteable prompt turns the reader's AI into a setup assistant that interviews them and does the work for them. Use when asked to make a recipe guided, convert a recipe to a guided recipe, produce a one-paste version of a recipe, or generate recipe-<slug>-guided.html in site/.
---

# Convert a recipe to a guided recipe

A **step recipe** (`site/recipe-<slug>.html`) makes the reader do the assembly: swap
the bracketed tokens, know what their AI product can do, remember to verify.

A **guided recipe** (`site/recipe-<slug>-guided.html`) is one block the reader pastes
whole. The AI then interviews them in everyday language, does the technical
assembly itself, and walks them through verifying the result.

Target reader: a nonprofit program manager or development director. Not technical,
not planning to become technical, on an unknown AI product and an unknown plan.

## Gold references

Four converted pages in `site/`. Read the one matching the archetype before composing:

| Archetype | Gold page |
|---|---|
| A — build a local tool | `recipe-private-transcriber-guided.html`, `recipe-redaction-pass-guided.html` |
| B — configure a reusable assistant | `recipe-handbook-answerer-guided.html` |
| C — run the task now | `recipe-district-lookup-guided.html`, `recipe-receipt-shoebox-guided.html` |
| D — establish a recurring routine | `recipe-monday-morning-guided.html`, `recipe-board-packet-guided.html` |

All 47 recipes are already converted. A new conversion means a new recipe page;
`references/ARCHETYPES.md` records what every existing one was classified as.

## Procedure

### 1. Resolve the target

`site/recipe-<slug>.html` must exist. If `site/recipe-<slug>-guided.html` already
exists, stop and ask before overwriting.

### 2. Read

The full source page, plus the gold page for its archetype
(`references/ARCHETYPES.md` for classification).

### 3. Inventory the mechanics

Write a YAML inventory to the scratchpad. Do not skip this and compose from
memory: the point is that every obligation the source page places on the reader
gets accounted for, and unaccounted-for obligations are the failure mode.

```yaml
slug:
archetype:            # A | B | C | D
end_object:           # one sentence: what the reader has when they're done
tokens:               # EVERY [bracketed] slot, in BOTH prompt variants
  - slot: "[New York City]"
    everyday_question: "What city or state is your list in?"
user_actions:         # every numbered step in the source
  - step: 1
    text: "Check whose addresses these are"
    kind: judgment    # judgment | mechanics | prompt | verification
assumptions:          # anything presupposing a product, OS, or SaaS
safety_gates:         # warning flags + every .browserline + any stop-condition
  - text: ...
    lands_in: rules   # rules | question | escape
technical_spec: |     # lifted from the Detailed <pre>, the richest source
yield: |              # carried through to the page unchanged
```

### 4. Compose the prompt

Follow `references/PROMPT-ANATOMY.md` exactly: nine sections, fixed order,
ALL-CAPS headers, every line wrapped at **≤64 columns**.

Coverage rules, checked against the inventory before moving on:

- every `tokens` entry appears in §4 as an everyday question — never by its
  technical name (see below);
- every `safety_gates` entry lands in §4 as an inline gate, in §7 RULES, or in §8;
- every `user_actions` entry tagged `verification` lands in §6;
- every `user_actions` entry tagged `mechanics` becomes something the assistant
  walks the reader through one step at a time, never a step the page assumes;
- every `assumptions` entry becomes a question, not an assumption.

### 5. Emit the page

Per `references/PAGE-DIFF.md`. Clone the source page and change only the listed
elements.

### 6. Validate

```
python3 .claude/skills/convert-to-guided/scripts/check_guided.py site/recipe-<slug>-guided.html
```

Fix and re-run until clean. Warnings are judgment calls; errors are not.

### 7. Cross-link

Add a mode link to the left `<span>` of the `.backlink` bar on both pages, so
neither is orphaned. No CSS change — the span already holds one link.

Guided page:

```html
<span><a href="index.html">← The Cookbook</a> · <a href="recipe-<slug>.html">Read the steps instead</a></span>
```

Step page:

```html
<span><a href="index.html">← The Cookbook</a> · <a href="recipe-<slug>-guided.html">Have AI walk you through it</a></span>
```

### 8. Report

Archetype chosen, the list of questions the assistant will ask the reader, and
anything from the source deliberately dropped.

## The everyday-translation rule

This is the judgment the whole conversion turns on. **Never ask for a technical
fact by its technical name.** Ask the everyday proxy and infer the technical
answer. When inference genuinely fails, offer two or three plain choices.

| Don't ask | Ask | Assistant infers |
|---|---|---|
| "Is it .m4a or .wav?" | "What do you record on: your phone, Zoom, a handheld recorder?" | audio format |
| "List your regex-able patterns" | "Do you use case numbers? What does one look like, with made-up digits?" | ID pattern |
| "What's your CSV delimiter?" | "What do you open your spreadsheet in?" | export shape |
| "Do you have API access?" | "When you need this data, where do you click to get it?" | export path |
| "What model tier are you on?" | "Which AI am I talking to you in, and are you on a free or paid plan?" | capability ceiling |
| "What's your document schema?" | "What are the headings in the document, top to bottom?" | structure |

Each guided prompt must carry **one recipe-specific** do-NOT-ask / ask-instead pair
inside §3, as the gold pages do. A generic pair is a sign the conversion was done
without reading the source.

## Non-negotiables

- **LLM-agnostic.** Never require a named product. Name products only inside an
  "for example ChatGPT, Claude, Microsoft Copilot, or Gemini" list. The assistant
  detects the product and plan first and says plainly when this one can't do it,
  with a fallback.
- **System-agnostic.** Never assume Google Workspace, Excel, a Mac, or any
  particular CRM. Ask what they use.
- **One question at a time**, with the count announced up front.
- **Nothing real enters the chat** on any recipe whose source page carries an amber
  or red flag. Made-up examples only, said out loud each time.
- **The reader stays the last check.** Guided means the assistant does the
  assembly, not that verification disappears. §6 always ends with the reader
  checking something concrete.
