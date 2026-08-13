# Guided prompt anatomy

Nine sections, fixed order, ALL-CAPS headers, blank line between sections.
Plain text only — no markdown, no bullets beyond `-`, no HTML entities.

**Hard line limit: 65 columns.** Aim for 64. This matches the `<pre>` width on
every cookbook card; a longer line wraps and the block stops looking authored.
Measure after stripping HTML tags.

Typical total length: 70–85 lines.

---

## §1 — Role and framing

Archetypes A, B, D:

```
You are my setup assistant. I work at a nonprofit. I am not
technical, and I don't want to become technical today. Your job
is to set the following up FOR me, asking me only questions a
non-technical person can answer.
```

Archetype C (the assistant does the work now rather than building something):

```
You are my research assistant. I work at a nonprofit. I am not
technical. Your job is to run the following FOR me, asking me
only questions a non-technical person can answer.
```

Append one clause naming the recipe's dominant risk when it has one, as
district-lookup does: `, and being strict about accuracy, because made-up data
looks exactly like found data.`

## §2 — WHAT WE'RE MAKING / WHAT WE'RE DOING

`WHAT WE'RE MAKING` for A, B, D. `WHAT WE'RE DOING` for C.

Three to six lines describing the end object in the reader's terms — what they
will have and what it does for them, never how it's built. Name the shape
concretely ("a single HTML file I can double-click", "one table", "a reusable
assistant"). For archetype B, list the product-specific names for the thing
(Project, GPT, Gem, Agent) and say the assistant will pick the right one.

## §3 — HOW TO WORK WITH ME

Seven required clauses. Use these sentences close to verbatim — only the
bracketed parts vary by recipe. Order them as below; the product-detection clause
may move to the top when the recipe's feasibility depends on the product.

1. **One at a time**
   ```
   - Ask me ONE question at a time and wait for my answer before
     asking the next. Tell me how many questions to expect.
   ```

2. **No technical questions** — with a *recipe-specific* example pair. This is the
   clause that carries the conversion's judgment; a generic pair is a defect.
   ```
   - Never ask me a technical question directly. Ask the everyday
     version and work out the technical answer yourself. For
     example: do NOT ask "<technical question>". Instead ask
     "<everyday question>" and figure out <the technical fact>
     from that. If you genuinely can't infer something, give me
     2-3 plain choices to pick from.
   ```

3. **Product and plan detection**
   ```
   - First, find out which AI product I'm talking to you in (for
     example ChatGPT, Claude, Microsoft Copilot, or Gemini) and
     whether I'm on a free or paid plan, then adapt everything
     that follows to what THIS product can actually do. If it
     can't do part of this, say so plainly now and offer the
     fallback, rather than letting me discover it halfway
     through.
   ```
   Archetype A extends this with the file-delivery branch: hand me a downloadable
   file if you can, otherwise one copyable block plus click-by-click saving
   instructions, asking Mac or Windows when the clicks differ.
   Archetype C replaces the file branch with a live-web-access check: if the
   product can't search the web, stop and say so rather than answering from
   memory.

4. **Don't assume my software**
   ```
   - Don't assume what software I use. Ask me what I use for
     <the relevant job> and adapt to that.
   ```

5. **Answer my questions**
   ```
   - If I ask you a question at any point, answer it in plain
     language, then pick up exactly where we left off.
   ```

6. **When reality diverges**
   ```
   - If an instruction doesn't match what I'm seeing, ask me to
     describe what's on my screen and work from that.
   ```

7. **One step at a time outside the chat**
   ```
   - When you give me instructions to do outside this chat, give
     ONE step at a time and check that it worked before the next.
   ```

## §4 — QUESTIONS YOU'LL NEED ANSWERED

Header verbatim:

```
QUESTIONS YOU'LL NEED ANSWERED (in your own words, one at a time)
```

Numbered, three to six items. More than six and the reader abandons the
interview; fold the rest into the assistant's inference.

Each item is the everyday question, not the technical slot. Every `[bracketed]`
token from the source prompt must be reachable from one of these.

Safety gates belong **inside** the relevant question, with the stop condition
stated, as district-lookup does with home addresses:

```
1. Whose addresses are on my list. If ANY are home addresses of
   clients, donors, or individual people, stop: tell me those
   must not be pasted into a chat, and offer the alternative at
   the end of this message.
```

Scale limits belong here too: what counts as too big, what to do instead.

## §5 — The technical spec

Header by archetype: `WHAT TO BUILD` (A), `WHAT TO SET UP` (B, D),
`HOW TO DO THE WORK` / `HOW TO DO THE LOOKUP` (C).

Always tagged `(this part is for you, not me)`.

This is where the source page's **Detailed** prompt variant goes — it is the
richest statement of the technical requirement. Rewrite it as a spec addressed to
the assistant, not as a prompt with blanks. Keep every hard requirement
(self-contained, no internet, source link per row, consistent placeholders) and
drop nothing on the grounds that it sounds technical: this section is the one
place technical language is correct.

For archetype B, include the instruction text the reader will paste into their
new assistant, indented two spaces and in quotes, with `[ORG]`-style slots the
assistant fills from the interview.

## §6 — AFTER ..., WALK ME THROUGH

Header names the moment: `AFTER YOU BUILD IT, WALK ME THROUGH`,
`AFTER IT'S SET UP, WALK ME THROUGH`, `AFTER THE TABLE, WALK ME THROUGH`.

Numbered, two to four items, carrying every `verification` step from the source
page, re-voiced as assistant-led. Always includes:

- a **safe first test** on made-up or non-sensitive material, before anything real;
- a **concrete check the reader performs** with a pass/fail rule ("five clean rows
  means you can trust the rest; one wrong row means we check them all");
- the **habit or handoff** that makes it stick.

## §7 — RULES

Every `.browserline` caution from the source page, re-voiced as an instruction
binding the assistant rather than advice to the reader. Two to four lines.

The last one is conventionally a reminder the assistant must deliver before
finishing — the thing the reader will otherwise forget ("private isn't the same
as permitted", "pattern matching is literal").

## §8 — Escape hatch (only when the source has one)

Header states the condition: `IF MY LIST HAS HOME ADDRESSES, OR HUNDREDS OF ROWS`.

Present only when the source page has a "when to stop using this recipe" line or
a local-tool alternative. Says what the assistant should do instead, and — if
that alternative is itself a build — tells it to switch into setup-assistant mode
and run the same interview pattern.

## §9 — Closing

Verbatim, with the verb matched to the archetype
(`do` for C, `make` for A, `set up` for B and D):

```
Start now by telling me, in two sentences, what we're going to
<do|make|set up> together, then ask your first question.
```
