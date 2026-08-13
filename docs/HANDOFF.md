# HANDOFF — Cookbook v2 (session ending 2026-07-05)

*Read this + `Cookbook V2 - Light PRD.md` (the thesis and working style) + `recipe-slate-v1.md`
(the 24-recipe content source, rev 2) before doing anything. This doc is what changed since the
PRD was written and where to pick up.*

---

## Where the project stands

**The full v2 mockup exists and renders.** Homepage + 24 recipe cards, all in the settled
Decoded Futures card design, all links verified, screenshots in `screenshots/`
(`homepage-v2-full.jpeg`, `recipe-redaction-full.jpeg`). Serve with
`python3 -m http.server 8487` (registered port for this project) or just open `index.html`.

## Decisions made this session (Jake's calls — treat as settled unless he reopens)

1. **Categories 1+2 merged** into "Your data, handled." Old distinction (headers vs. content)
   survives as each card's privacy posture, not a category boundary. Split back if it strains.
2. **New category 2: "Enrich my data"** — for-each-entity public-web lookup (district lookup,
   volunteer employers, 990 sizing, matching gifts). Vanilla chat + web search is the default;
   built tool on a public API (Census geocoder, ProPublica) is the upgrade; Claude-in-Chrome is
   the login-walled exception and spicy territory. Category cliff: **confabulated data looks
   identical to found data** → citation rule on every card (source link per cell · unknowns
   blank · spot-check 5 rows) + "the lookup line" (dozens→chat, hundreds→tool, thousands→outgrown).
3. **"Information you give it"** (Jake renamed from "what you feed it" — feed sounds like a
   beast) is a first-class card element: a gold panel on every card, always an artifact the
   reader already has, never a document they must write. This is the context-shortcut thesis
   made visible ("10 Slack threads, not a 3-page persona doc").
4. **The redaction pass leads the book** (R-01, gold-highlighted "read me first" tile) — it's
   infrastructure: the key that turns amber recipes green. Amber cards cross-link it.
5. Baseline assumption: reader has **Claude Pro/Max** (or equivalent), so Projects/Skills are
   fair game in categories 4–5.
6. Banned: grant-proposal writing ("done to DEATH"). The only grant-adjacent recipe is R-18
   The Funder's Eyes, a critic that writes nothing. Selection bias for all recipes:
   day-to-day ops pain IT never fixed, not "classic nonprofit problems."

## File map

- `index.html` — homepage, rev-2 climb (6 categories, 24 recipes linked, legend + give-note).
- `card-styles.css` — shared card styles. New this session: `.give` (Information-you-give-it
  panel). `.browserline` doubles as every category's caution callout.
- `recipe-*.html` — 25 card pages (R-01…R-24; the spreadsheet dashboard is a linked pair
  R-02/R-02b with live demos in `prototypes/dashboard-nibble/`). 23 pages were drafted this
  session by parallel agents against a tight spec; 2 (viewer/editor) predate it and were
  updated (renumbered, `.give` added).
- `recipe-card-mockup.html`, `recipe-card-spicy.html` — ORIGINAL standalone mockups, kept as
  historical artifacts; not linked from the homepage, don't share the stylesheet. Ignore or trash.
- `recipe-slate-v1.md` — rev 2 of the slate: all 24 recipes with blurbs, grounding, info-you-
  give-it, meta-skill, privacy, plus a findings log (worth rereading — e.g. "check what your
  data already knows before you go looking" as a nameable pattern).
- `Cookbook V2 - Light PRD.md` — thesis, core filter, meta-skills, card anatomy, working style.
  NOT yet updated for the rev-2 category structure (§3 still shows the old six categories).

## What the next session should probably do (menu, not mandate)

1. **Jake's editorial pass over the 23 drafted cards.** They followed one spec but were written
   by parallel agents — expect unevenness in tone, prompt quality, and scan-strip judgment calls.
   Especially check: privacy-tier assignments, the invented "What you use" states, helper-chat
   realism. Fix wording before building anything on top.
2. **Update the PRD §3** to the rev-2 category structure + fold in the slate findings log.
3. **Standardize the scan-strip vocabulary.** The new pages invented states ("Chat + search",
   "A Project", "A Skill", "Chat + connector", "Living tool" variants). The icon-vocabulary
   legend sub-project (PRD §5) now has real states to standardize against.
4. **Prototype the next high-wattage nibbles** to reverse-engineer real recipes (the PRD's
   build-first method): the redaction pass and the private transcriber are the obvious two —
   both are "all-clear green" anchors and R-01 currently teaches a tool we haven't actually built.
5. **Open card threads still open** (PRD §5): finalize 4-tier privacy wording; decide in-page
   helper scope (the static fakes on the new cards are good test cases if it goes live);
   spicy-card tone check on R-23/R-24.
6. **Expand the org-grounding bank** (PRD §7) — arts, advocacy, direct-cash, healthcare,
   environmental orgs — before generating any more recipes.

## Red-team pass (2026-07-09) — what changed and what's queued

A persona red-team (nonprofit exec, low-to-medium technical) reviewed all 24 cards. Fixes
already applied across the cards: a standard "you don't need to understand every word"
`.prenote` above every prompt block; `.demo-note` labeling the fake helper chats as examples;
jargon glosses (EIN, 990-PF, Flesch-Kincaid, web-search toggle); governance lines (handbook
answerer HR disclaimer + owner, Ask Maria compliance skim + retention, Drive archaeologist
Workspace-admin step 0, disconnect-doesn't-erase notes on R-23/R-24); time-estimate honesty
where verification is the real cost (R-12, R-14, R-19); R-07's sensitivity checklist;
Project-vs-Skill standardized on Project in category 5. Homepage got a "Which AI does this
work with?" note.

**Queued tasks (Jake's calls, not yet done):**
1. **De-Claude-ify the whole book** — a dedicated pass replacing explicit Claude references
   with model-agnostic language (ChatGPT Projects/GPTs, Gemini Gems equivalences), per Jake:
   the cookbook should apply to any LLM. Keep one "tested with" note per card or centrally.
2. **R-00 "Is my AI set up right?" pre-flight card** — plan check, web-search toggle,
   training-data settings, where Projects live. Would absorb half the remaining HIGH findings.
3. **Shared "When it doesn't work" troubleshooting page** linked from every card (file won't
   open / browser security warning / message-too-long / silent drag-drop failure).
4. **"Getting your data out" appendix** — CSV export click-paths for LGL, Eventbrite,
   Mailchimp, Google Forms; unblocks five category-1 recipes.
5. **Recipe candidates from the red-team:** board memo / AI-policy starter; renewal-deadline
   extractor (award letters → calendar-importable deadline list); "handing the tool to a
   teammate" (Project sharing mechanics).
6. **Per-card privacy mini-legend** — cards get shared as bare links; the 4-level scale
   currently only exists on the homepage.

## Category-3 expansion (2026-07-09)

Category 3 grew from 3 to 7 recipes after an output-format landscape pass (see slate rev-3
addendum for the full logic): R-25 real .pptx deck, R-26 quote-card generator, R-27 report →
NotebookLM podcast, R-28 volunteer training kit. New concepts introduced:
- **"Where does the deliverable live?" heuristic** (file people edit / browser / platform) —
  now in the category-3 homepage intro; candidate for the meta-skills spine.
- **"Companion tool" recipe class** (Jake approved): one named outside tool, bar = clear/easy/
  reliable, one click or one simple prompt, free or already owned. R-27 is the first. Marked
  in the homepage legend, the recipe tag, and the card's "What you use" cell.
- **Video = honesty note, not a recipe** (homepage callout in category 3) until generation
  clears the companion bar.
- Numbering: new cards appended as R-25–R-28 to avoid renumbering 24 existing cards, so
  numbers no longer run in strict climb order past category 3. Reopen if it grates.

## Working style (from the PRD, still accurate)

Talk back before building; one open question at a time; Jake owns audience calls; apply the
core filter (beats-a-generic-prompt · specific nonprofit pain · not done-to-death) relentlessly;
build real artifacts and derive recipes from what shipping them taught. Everything is a strong
default to argue with, not a spec.
