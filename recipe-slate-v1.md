# Recipe Slate — 24 one-shot-ish recipes across the climb *(rev 2)*

*Titles + blurbs, per Jake's call. Each recipe carries the first-class field —
**"Information you give it"** — always an artifact you already have, never a document you
must write. Baseline assumption: reader has Claude Pro/Max (or equivalent), so web search,
Projects, and Skills are fair game.*

**Rev 2 changes (Jake's calls):** Categories 1 and 2 collapsed into one ("Your data,
handled") — split back later if it strains. The redaction pass promoted to recipe #1: it's
the key that unlocks every amber recipe in the book. New category added: **Enrich my data**
(Jake's proposal), slotted into the freed position 2 — it earns its own rung because it
introduces a new capability (web search / going OUT to the world) and its own cliff
(confabulated data looks identical to found data).

*Selection bias, per Jake: day-to-day operational pain that IT should have fixed but never
did. Grant-proposal-writing is banned (one grant-adjacent critic survives, and it writes
nothing).*

**The climb, revised:**
1. **Your data, handled** (nibbles + sense-making, merged)
2. **Enrich my data** (new)
3. **Remix your content**
4. **Build an expert you can ask**
5. **Stand up a reusable skill**
6. **Connected workflows** (capstone)

---

## Category 1 — Your data, handled

### 1. The redaction pass *(the opener — leads the whole book)*
A local tool that strips names, emails, phone numbers, and addresses from any text you paste
in — so you can safely use *every other recipe in this book* on real material. Read this one
first; it's the key that turns amber recipes green.
- **Who:** program staff at a domestic-violence services org who want AI help with case
  notes but can never paste identifying info anywhere.
- **Information you give it:** a description of what counts as identifying in *your* context
  ("client names, school names, our internal ID format looks like CL-####").
- **Teaches:** knowing the privacy tier you're in — this tool *moves* work between tiers.
- **Privacy:** 🟢 all-green (that's its whole job).

### 2. Turn your spreadsheet into a dashboard *(built — the anchor)*
Hand Claude 2–3 fake rows of your messy spreadsheet; get back a single HTML file you
double-click. Drag your real CSV on and see totals, charts, and a searchable table — nothing
ever uploads.
- **Who:** ops/logistics person at City Harvest with a food-rescue log.
- **Information you give it:** 2–3 made-up sample rows showing your column names.
- **Teaches:** build with fake data, run on real.
- **Privacy:** 🟢 all-green.

### 3. The private transcriber *(built as mockup — confirmed sleeper)*
A page that turns a recorded meeting or interview into a transcript entirely on your own
computer. The audio never leaves your machine — usable even for sensitive client
conversations.
- **Who:** case manager who records intake conversations (with consent) and dreads typing
  them up.
- **Information you give it:** nothing sensitive at build time — the audio only ever touches
  your own browser.
- **Teaches:** the green end of the privacy scale, made visceral.
- **Privacy:** 🟢 all-green.

### 4. Certificates, name tags, and letters from a list
Paste your attendee/volunteer CSV columns, get a page that generates print-ready
certificates, name badges, or mail-merge letters for everyone on the list. The task that eats
an afternoon every event, gone.
- **Who:** volunteer coordinator at Catchafire running a recognition event for 80 volunteers.
- **Information you give it:** your column names + one example of the finished certificate
  you made by hand last year.
- **Teaches:** context transfer in miniature — the example carries the design, not a spec.
- **Privacy:** 🟢 green (names processed locally in the page).

### 5. Explain this spreadsheet I inherited
Your predecessor left a workbook with 11 tabs, colored cells, and formulas nobody understands
— and then left the org. Paste it in and get a plain-language map: what each tab is for, what
calculates what, and which cells are load-bearing.
- **Who:** new development associate who inherited "FY24 MASTER TRACKER v7 (USE THIS ONE)".
- **Information you give it:** the workbook itself (or a copy with dollar figures blanked —
  the *structure* is what needs explaining).
- **Teaches:** pointing at an artifact instead of describing it.
- **Privacy:** 🟡 amber, with a blank-the-values variant.

### 6. Find the same people across your three lists
Your event platform, your mailing list, and your donor CRM each have their own version of
everybody. Claude builds you a local matching tool: drop in the three exports, get one
deduplicated list plus a "these might be the same person — you decide" pile.
- **Who:** small-shop development director juggling Eventbrite, Mailchimp, and Little Green
  Light exports before a mailing.
- **Information you give it:** just the column headers of each export (the tool does the
  matching on your machine).
- **Teaches:** the fuzzy-match is a smart guess — the "you decide" pile is the
  human-in-the-loop.
- **Privacy:** 🟢 green (build-with-headers, run-locally).

### 7. Who's missing? (the three-list reconcile)
Registered vs. attended vs. completed-the-survey — who fell through which crack? Paste the
lists (or drop them on a built tool) and get the gaps, not a pivot-table lecture.
- **Who:** workforce-program coordinator at Merit America chasing completion data before a
  quarterly review.
- **Information you give it:** the lists themselves, or headers-only for the local-tool
  variant.
- **Teaches:** picking the right privacy tier for *this* data, this time.
- **Privacy:** 🟡 amber with a 🟢 escape hatch.

### 8. Three hundred survey answers, five themes
Your post-program survey has one open-ended question and 300 answers nobody has read. Paste
the column, get the recurring themes, how often each appears, and three verbatim quotes per
theme — with a warning to spot-check before quoting anyone to a funder.
- **Who:** program manager sitting on two years of unread feedback.
- **Information you give it:** the response column, after a pass through the redaction tool
  (#1) if answers name people.
- **Teaches:** knowing when to trust the output (spot-check quotes against the source).
- **Privacy:** 🟡 amber — pairs explicitly with #1.

---

## Category 2 — Enrich my data *(new)*

*The shape: "for each entity in my list, go get publicly available information and attach
it." The new capability is web search inside the chat — no Chrome extension needed for the
core recipes. The category's cliff (see below) is that made-up data looks exactly like found
data, so the citation rule is baked into every card.*

### 9. Which district is everyone in?
Paste your list of partner orgs or program sites with addresses; get back each one's city
council district — plus the councilmember's name and contact — with a source link on every
row, so you know exactly which elected to put each org in front of.
- **Who:** coalition manager at an advocacy org prepping for city budget season.
- **Information you give it:** your list with addresses. Org addresses are public — a rare
  "paste freely" case. ⚠️ Client *home* addresses are not: for those, the recipe's local-tool
  variant (Claude builds a lookup page using the free Census geocoder + public district
  boundaries) keeps them on your machine.
- **Capability:** chat + web search up to ~50 rows; built tool when it's hundreds or
  recurring.
- **Teaches:** the citation rule — no source link, no cell.
- **Privacy:** 🟢/🟡 depending on whose addresses.

### 10. Where do our volunteers work?
Before searching anything: their email domains already told you.
jane@salesforce.com is not a mystery. Claude sorts your volunteer list by employer from the
domain column alone, then web-searches only the ambiguous ones (gmail, edu, generic ISPs).
- **Who:** corporate-partnerships lead at Catchafire spotting employer clusters worth a
  sponsorship conversation.
- **Information you give it:** the email-domain column only — strip the names first (#1).
- **Capability:** chat alone for the domain pass; web search for the stragglers. ⚠️ The
  tempting shortcut — looking people up on LinkedIn — is the red zone: logged-in scraping
  violates ToS, and per-person profile browsing (even assisted by Claude in Chrome) should
  be a deliberate, disclosed choice, not a batch job.
- **Teaches:** the cheapest enrichment is data you already hold.
- **Privacy:** 🟡 amber, with the LinkedIn caution front and center.

### 11. Size up any nonprofit in 30 seconds
Paste a list of org names or EINs; get back each one's budget size, staff count, and program
focus from their public 990 filings — the triage that turns "60 potential partners" into
"the 15 worth calling first."
- **Who:** partnerships person mapping a coalition, or a development director checking
  whether a prospective funder actually gives at their size.
- **Information you give it:** just the org names (all public from here).
- **Capability:** chat + web search (990 data is free and public via ProPublica's Nonprofit
  Explorer); a built tool calling that API for big recurring lists.
- **Teaches:** when a structured public dataset exists, point at it — it beats searching.
- **Privacy:** 🟢 green (everything here is public record).

### 12. Does their employer match gifts?
Your donors' employers, checked against publicly posted corporate matching-gift programs —
with a link to each program page and a plain "unknown" where nothing was found. The free
version of a paywalled fundraising database.
- **Who:** annual-fund manager in December, sitting on employer data nobody ever used.
- **Information you give it:** the employer column only — no donor names needed.
- **Capability:** chat + web search, batched.
- **Teaches:** mark unknowns as unknown — a confabulated "yes, they match" costs you a
  donor's trust.
- **Privacy:** 🟢 green (company names only).

### The cliff for THIS category: found vs. made-up (and the lookup line)
Two cliffs, both taught in situ:
1. **Confabulation is invisible.** A hallucinated council district looks identical to a real
   one. Every enrichment card carries the same three-part rule: *require a source link per
   cell · unknowns stay blank · spot-check 5 random rows before you act on any of it.* This
   is "knowing when to trust the output" at its sharpest.
2. **The lookup line** (this category's version of the browser line): dozens of rows →
   chat with web search handles it. Hundreds, or every month → have Claude build a tool that
   calls the public dataset directly (Census geocoder, ProPublica API). Thousands, or
   business-critical → you've outgrown the recipe; that's a data service.
3. **Chrome is the exception, not the default.** Claude in Chrome earns its place only when
   the source requires a login or an interactive lookup form — and logged-in sources
   (LinkedIn, member portals) carry ToS and ethics weight that make them spicy-card
   territory, never the happy path.

---

## Category 3 — Remix your content

### 13. One event, every asset
You wrote the event description once. Get back the registration-page blurb, the Instagram
caption, the newsletter blip, the reminder email, and the day-of signage — all in your org's
actual voice, because you showed it your voice instead of describing it.
- **Who:** the communications person (who is also the program person, and the ops person) at
  a 6-staff arts org.
- **Information you give it:** the new event description + one past example of each channel
  you liked. Not a brand guide — real artifacts.
- **Teaches:** context transfer — examples beat adjectives; cap iteration at one pass.
- **Privacy:** 🟢 green (public-facing content anyway).

### 14. Your annual report is 40 social posts
The annual report you sweated over contains months of content: stat callouts, story excerpts,
milestone posts, quote graphics copy. Mine it once, schedule it all quarter. You're sitting
on more than you think.
- **Who:** same overloaded comms person, the week after the report ships.
- **Information you give it:** the finished report PDF + 3 past posts that performed well.
- **Teaches:** the remix matrix mindset — one source, many cells.
- **Privacy:** 🟢 green.

### 15. Say it so everyone can read it
Turn your program flyer or intake instructions into a 6th-grade reading level version, a
large-print version, and a first-draft Spanish version — with the reading level scored and a
firm note that a fluent human reviews any translation before it goes out.
- **Who:** benefits-navigation org whose intake letter currently reads like the regulation
  it summarizes.
- **Information you give it:** the current document + the plainest thing your org has ever
  published (that's the target register).
- **Teaches:** keeping a human in the loop — machine translation is a draft, not a
  deliverable.
- **Privacy:** 🟢 green.

---

## Category 4 — Build an expert you can ask

### 16. The dread-document expert *(the pattern to elevate)*
Load the Medicaid manual, the HUD handbook, or your state's childcare licensing regs into a
Project. Ask it questions all year; make it cite the page every time so you can verify
before you act.
- **Who:** compliance-adjacent program director who currently ctrl-F's a 400-page PDF weekly.
- **Information you give it:** the public document itself. No writing, no explaining how
  your org thinks.
- **Teaches:** baby RAG + never act on an uncited answer.
- **Privacy:** 🟢 green (the document is public).

### 17. The handbook answerer
Your employee handbook, your board bylaws, your fiscal policies — into one Project that
answers "do I get bereavement leave for a grandparent?" with the section quoted. HR stops
being the bottleneck for questions the documents already answer.
- **Who:** operations manager at a 40-person org who answers the same nine questions monthly.
- **Information you give it:** the PDFs you already have.
- **Teaches:** the difference between "the document says" and "the org decided" — the expert
  only knows the former.
- **Privacy:** 🟡 amber (internal docs in a Project).

### 18. The funder's eyes
Not a generic critic — a reviewer built from the funder's *actual published* guidelines,
scoring rubric, and past awarded abstracts. It reads your draft the way they will, before
they do. (The only grant-adjacent recipe in the book, and it writes nothing.)
- **Who:** ED at an advocacy shop about to submit to a foundation for the first time.
- **Information you give it:** the funder's public guidelines/rubric + your draft.
- **Teaches:** a critic is an expert with a job — only as sharp as the real document behind
  it.
- **Privacy:** 🟡 amber (your draft goes in).

### 19. Ask Maria (the institutional-memory bot)
Your longtime program coordinator is leaving. Before she goes, she picks 10–15 email threads
and Slack conversations where she's actually solving problems — plus her handoff doc — into
a Project. Her successor asks it "how did we handle the site-visit scheduling mess?" instead
of doing archaeology.
- **Who:** any org losing 12 years of tacit knowledge in two weeks' notice.
- **Information you give it:** real threads *she chooses* — consent and curation are steps
  in the recipe, not a footnote. She redacts, she selects; it's her voice being preserved.
- **Teaches:** context transfer at its purest — 10 real conversations beat a 3-page "how I
  work" essay she'd never write anyway.
- **Privacy:** 🟡 amber, consent step non-negotiable.

---

## Category 5 — Stand up a reusable skill

### 20. The house style, bottled
Five pieces your org is proudest of go into a Skill. Now everyone's drafts — the intern's,
the board chair's, the ED's — come out sounding like the same organization. Feed it a new
best example whenever one exists; it keeps getting more you.
- **Who:** comms lead tired of rewriting everyone's "please share this" paragraphs.
- **Information you give it:** your 5 best published pieces + 1 counter-example ("we never
  sound like this").
- **Teaches:** honing a living tool — positive *and* negative examples.
- **Privacy:** 🟢 green.

### 21. Every meeting, the same follow-through
A Skill that takes any meeting transcript or messy notes and produces your team's exact
format: decisions, owners, deadlines, parking lot — then a draft follow-up message. The
consistency is the point: follow-through stops depending on who took notes.
- **Who:** a program team whose action items currently live in four notebooks and one memory.
- **Information you give it:** 2 past sets of notes + the follow-up email your best
  note-taker sent afterward (the template, demonstrated not described).
- **Teaches:** turning one person's good habit into an org function.
- **Privacy:** 🟡 amber (internal meeting content).

### 22. The intake normalizer
Every partner sends you data in their own format — different columns, different date styles,
different everything. A Skill that takes whatever they send and returns it in your canonical
format, flagging what it couldn't map instead of guessing silently.
- **Who:** City Harvest-style ops team receiving monthly reports from 30 partner agencies.
- **Information you give it:** your canonical template + 3 real (or lightly fictionalized)
  examples of the weird formats partners actually send.
- **Teaches:** honing a living tool — every new weird format becomes a training example.
- **Privacy:** 🟡 amber, headers-only variant available.

---

## Category 6 — Connected workflows (capstone)

### 23. The Drive archaeologist
Point Claude at your shared drive and ask the questions everyone actually has: "Which of
these six 'FINAL' budgets is actually final?" "Where is the current logo?" "What did we
promise this funder last year?" Read-only, cite the file path, you open the file yourself.
- **Who:** literally every nonprofit with a shared drive older than two years.
- **Information you give it:** nothing — you *connect* Drive (permission moment, taught
  explicitly) and ask.
- **Teaches:** connectors need permission; read-only is a posture you choose.
- **Privacy:** 🔶 amber-red — first card where org data is reachable; teaches scoping the
  connection.

### 24. Monday morning, sorted
Claude reads your weekend inbox pileup and hands you a triage: what needs a reply from
*you*, what has a deadline hiding in it, what's FYI. It drafts replies for the routine ones —
drafts only, you send. Nothing leaves without your click.
- **Who:** the ED whose Monday starts with 94 unread and a 9 a.m. board call.
- **Information you give it:** inbox access (permission moment) + one sentence on what
  counts as urgent in your world.
- **Teaches:** "draft-only, I send" as the default architecture of every connected workflow.
- **Privacy:** 🔶 amber-red; empowering-with-guardrails tone.

---

## Rev 3 addendum — Category 3 expansion (2026-07-09, Jake's calls)

**The output-format decision heuristic (now in the category-3 intro):** pick the route by
where the deliverable lives. A *file people edit* (deck, doc) → have the AI emit the real
file (.pptx/.docx). *Used in a browser* → a clickable HTML page (nibble rules apply).
*A platform* (podcast feed, LMS) → the AI writes the content; a **companion tool** performs it.

**New class: "companion tool" recipes** — use one named outside tool alongside the chat.
Inclusion bar (Jake's): clear, easy, reliable — one connector click or one simple prompt in a
friendly tool; free or already owned; behaves the same every time. Marked on the homepage tag
and in the card's "What you use" cell. Video explicitly does NOT clear the bar yet — it gets
an honesty note on the homepage, not a recipe.

### 25. One story, a real deck
Your finished report + last year's deck as the design template → a real, editable .pptx.
An HTML slideshow is a dead end for a board deck; the real file is the recipe.
- **Information you give it:** the report + the deck your org already likes.
- **Teaches:** template-by-example; file vs. browser. **Privacy:** 🟡 amber (report passes through).

### 26. The quote-card press
The certificates pattern pointed at social: a local HTML generator page — type a quote or
stat, download a branded PNG. Brand carried by a screenshot + logo + one past post.
- **Teaches:** the generator pattern generalizes. **Privacy:** 🟢 green (runs locally).

### 27. Your annual report is a podcast *(companion tool: NotebookLM)*
Public annual report → NotebookLM Audio Overview → a two-host conversation supporters will
actually listen to. Public documents only; listen to every minute before it ships.
- **Teaches:** the AI performs, you approve — draft-only architecture in audio form.
- **Privacy:** 🟢 green (public material only, by rule).

### 28. The volunteer training kit
One training doc → facilitator guide + plain-language handout + local HTML practice quiz.
The quiz teaches the browser line in situ: practice yes, completion tracking = an LMS.
- **Teaches:** one source, many teaching formats; the browser line; source-of-truth stays
  in your doc. **Privacy:** 🟡 amber with an R-01 pointer.

## Findings log

**From rev 1 (still standing):**
1. **"Information you give it" wrote itself on every card** — on the best recipes it *is*
   the recipe (Ask Maria, the funder's eyes, house style). First-class placement next to the
   prompt block confirmed.
2. **The redaction tool is infrastructure, not just a recipe** → now recipe #1 and
   cross-linked from every amber card. *(Adopted.)*
3. **Consent surfaces at Ask Maria** — building an expert from a colleague's messages needs
   the colleague's participation baked into the steps. Meta-skill candidate or extension of
   human-in-the-loop.
4. **Category 6 can't be one-shot-ish and doesn't need to be** — its two slots are
   destinations the first 22 recipes earn trust toward.

**New in rev 2:**
5. **Categories 1+2 merged** ("Your data, handled") — the old distinction (headers vs.
   content) survives as the privacy posture on each card rather than a category boundary.
   Split back later if the merged category gets unwieldy past ~12 recipes.
6. **Enrichment is a real rung, not a verb-group.** It introduces a new capability (web
   search — information flowing *out to the world and back*, vs. category 1's
   nothing-leaves-your-machine) and a new cliff (confabulation + the lookup line). That
   asymmetry justifies the category slot.
7. **The email-domain trick (#10) suggests a pattern worth naming:** *check what your data
   already knows before you go looking.* Candidate teaching moment for the category intro.
