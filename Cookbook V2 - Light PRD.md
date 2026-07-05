# Decoded Futures Prompt Cookbook v2 — Working Report & Light PRD

*A working document for continuing the design and build. Decisions here are **held loosely** — we are iteratively building and exploring. Treat everything as a strong default to push on, not a spec to obey.*

---

## 0. How to use this document (note to the next agent)

You are picking up a collaborative design effort with Jake (co-founder / EiR at Decoded Futures). The work so far has produced: a clear thesis, a category structure, two fully-built recipe-card mockups, and a deep pass on the first recipe category. Your job is to continue generating and pressure-testing recipes category-by-category, and eventually help build out cards and supporting structure.

**Working style that has been productive:**
- Talk back before building. Jake wants a thinking partner who reflects structure back, names tradeoffs, and surfaces the load-bearing decision — not an order-taker.
- One genuinely open question at a time, deferred to his judgment on audience calls (he knows the nonprofit frontline reader better than you do).
- Apply the core filter relentlessly (see §2). Most generic ideas die on it.
- Build real artifacts to reverse-engineer recipes from things that actually run, rather than imagining them.
- Keep the nonprofit reader (beginner, risk-averse, frontline) at the center.

---

## 1. What this project is

A second version of the Decoded Futures "Prompt Cookbook" (the v1 lives at promptcookbook.decodedfutures.nyc — 365 model-agnostic copy-paste prompts across 5 problem types, built for the summer-2025 "everyone's just prompting" moment; it became OpenAI Academy's most-accessed nonprofit resource).

**Why v2 needs to exist:** v1 treats the AI as a text generator. It predates everything that makes current models qualitatively different — that they write and run code, build real artifacts, persist context across a Project, apply a reusable Skill, and operate over connected files/email/calendar. v2's unit of work is no longer "paste a prompt, text comes out." It's "do a thing in the chat window and get back a working artifact, a tool, a reusable system, or a transformed deliverable."

---

## 2. The thesis (this is the spine — protect it)

**The unit of value has moved from the prompt to the reusable function and the design pattern.** The skill being taught is no longer "what words to type." It's *context-transfer* (how to give the AI the nuance it can't see), *knowing when to stop* (cap iterations, don't loop forever), and *climbing the ladder from one-shot use to reusable systems.*

Jake confirmed this thesis is true and central. Three of the meta-skills (§6) are really one claim: the hard part is never the prompt, it's encoding the context you understand and the AI can't.

**Corollaries that shape every decision:**
- **Differentiation lives in the unsexy frontier, not the famous use case.** Grant-writing, donor thank-yous, "summarize this" are done to death and Copilot will own them. Skip them. Jake's words: "Everyone has to write grants, duh" is the *disqualifier*, not the qualifier.
- **The edge is "common but slightly bespoke" problems nobody has made a clean recipe for** — often grounded in real nonprofit fears (data privacy, wrong answers in front of constituents).
- **Hard red line: nothing autonomous in front of the people they serve.** Every constituent-facing idea gets pulled internal or human-in-the-loop. This is both an ethical stance and a positioning stance.

### The core filter (apply to every candidate recipe)
A recipe earns its place only if it clears all three:
1. **Beats a generic prompt** — either it *runs* (calculates, persists, validates, transforms) or it encodes a *real, public, stable* body of knowledge. "You are a strategy coach" fails because the context is empty.
2. **Specific to nonprofit pain** — grounded in a real org's operations/theory of change, not "nonprofits" in the abstract.
3. **Not done-to-death** — not something Microsoft/Google will obviously ship for everyone.

**Grounding technique that works:** stop thinking about "nonprofits generally." Put yourself in a specific org — an upskilling coach at Merit America, a logistics operator at City Harvest, a volunteer manager at Catchafire — and reason from their actual operations. Specific orgs generate specific recipes; "nonprofits" generates generic ones.

---

## 3. Recipe categories (the climb)

Six clusters, deliberately ordered: **easy → hard, personal → organizational, instant-gratification → capacity-building.** A reader climbs from "look what I made in 30 seconds" to "the whole org runs this skill." Order is settled; contents are in active development.

1. **Code nibbles** — small self-contained code (usually a clickable HTML file) that solves an annoying concrete problem. The hook. *(Deep pass complete — see §4.)*
2. **Make sense of your data** — hand Claude messy data; it cleans / reconciles / analyzes / explains. The most common real nonprofit pain. *(Not yet worked.)*
3. **Remix your content** — the media-generation matrix: existing content × target format. "You're sitting on more than you think." *(Framed, not yet enumerated.)*
4. **Build an expert you can ask** — load a body of knowledge (a **document** = "baby RAG," or a **point of view** = roleplay/persona), then converse. **Includes the critic / "second opinion" use** — a critic is just an expert whose job is to push back. *(Not yet worked.)*
5. **Stand up a reusable skill** — the team/org function: ask Claude to make a repeatable workflow, shareable for consistency across a team. The capacity payoff. *(Not yet worked.)*
6. **Connected workflows (capstone)** — Claude acting over real Drive/Slack/CRM/inbox. Most powerful, most cautioned, last. *(One mockup exists — the spicy card.)*

### Decisions made along the way (all loose)
- "Second opinion / critic" folded **into** category 4 (Jake's call: it's a type of expert, not its own cluster).
- Cut from earlier drafts: **constituent-facing decision aid** (program logic is the nonprofit's core IP, often un-articulable, too high-stakes to fake — *could* return as internal/human-review only); **generic "long report → deck"** and **generic summarization** (commodity; the magic was misplaced — the value is context-transfer, not compression).
- Media-generation should be a **matrix, not a list** (one verb — "remix" — many cells). Be honest per cell whether Claude codes it or you point to an external tool.
- The **"expert over a dread document"** pattern (load the Medicaid manual / funder guidelines / licensing reg, then ask it) is high-value and sidesteps the IP-articulation problem entirely — the org points at a public document rather than explaining how they think. Consider elevating it within category 4.

---

## 4. Category 1 deep pass — "Code Nibbles" (worked example of the depth we want)

Defining trait: Claude writes a small, self-contained piece of code that solves an annoying, concrete problem — no backend, no hosting. Teaching: *"you are not a coder, but Claude-in-the-chat can hand you working software."* Organize by **mechanical verb**, because that's the sub-taxonomy a beginner can navigate ("is my problem a *calculate* problem or a *convert* problem?").

**Calculate / decide-by-rule** — benefits eligibility estimator (public SNAP/Medicaid thresholds → instant private estimate); sliding-scale fee calculator; living-wage gap calculator; grant-fit self-scorer (internal, self-scoring); honorarium/stipend pro-rater.

**Convert / transform** — spreadsheet → interactive HTML dashboard *(headline nibble)*; Excel → Notion table / clean CSV; PDF form-field extractor; plain-language rewriter with reading-level score.

**Capture / log** — volunteer-hours kiosk; donation/inventory logger; event check-in page; reading-streak tracker. *(See persistence cliff below.)*

**Privacy-safe local tools** *(the sleeper category — code that never phones home)* — private transcriber *(confirmed sleeper hit)*; local redaction tool (strip PII before anything leaves); offline batch file renamer/organizer.

**Visualize / map** — service-area / partner map (addresses → pins); simple branded chart maker; timeline/Gantt from a list.

**Tiny automations** — Google Apps Script shims (auto-label email, copy form responses to a tracker, send a digest); threshold alerter.

### The implementation cliff to teach here: persistence ("the browser line")
Stateless nibbles (calculator, converter, chart, transcriber) genuinely hand a beginner a working single HTML file. **Capture/log tools are deceptive** — the moment a beginner expects "and it saves the data," the clicked file forgets everything on refresh. This is exactly where a beginner meets the *browser line* meta-skill.

Three honest treatments for the loggers (decide per recipe):
1. **Export-only framing** — "it logs your session; hit *Export CSV* before closing; it doesn't remember on its own." Keeps it a true nibble.
2. **Point to the right tool** — "for something that truly remembers, use a Google Form / Airtable; here's how to have Claude set *that* up."
3. **Omit loggers** — keep nibbles purely stateless and 100% reliable.

**Current lean (loose):** option 1 for most loggers (export-before-close genuinely works for a single shift), with a pointer to option 2 when they outgrow it — and use the moment to *teach the browser line in situ*. **Open question Jake still owns:** loggers in or out for v2?

---

## 5. The recipe card (design is well-developed — two mockups exist)

The card **is** the product. The dimensions tagged on it ARE the teaching — they train judgment by repetition. Built in real Decoded Futures brand (cream mode, Electric Pulse blue rail, all-caps blue headlines, pixel motif, embedded DF logo). Files: `recipe-card-mockup.html` (the gentle/all-clear example — the private transcriber) and `recipe-card-spicy.html` (the cautionary example — a CRM-connected outreach drafter).

### Three-tier layout (settled and working)
- **Tier 1 — the scan strip:** five icon-led tiles, each = icon + 2-word heading + 2-word value, with all explanatory text in a **hover tooltip**. A colored accent bar under each value (green/blue/amber/red) lets you read a card's whole safety posture in one glance without hovering. The goal is a **visual vocabulary people learn to scan** — the icon carries the meaning.
- **Tier 2 — nature-of-work chips:** skill level, time-to-build, effort-after-setup. Lighter weight. *(Jake liked these as-is.)*
- **Tier 3 — the recipe itself:** numbered steps, a copyable prompt block, "what you walk away with," and an (currently faked) in-page helper chat for adapting the recipe to your org.

### The five scan-strip dimensions (final wording from Jake's edits)
1. **Where data goes** (privacy) — 4-tier scale, green→red, with **strong emotional plain-language** labels for beginners. Safest tier = **"Nowhere. It's yours"** (not "on your device"). Full scale (labels still being finalized): *Nowhere / it's yours* (green) → *passes through, not stored* (blue) → *stored by a vendor* (amber) → *out to a company / stored + usable by vendor / subpoena-reachable* (red). **This dimension is the most prominent** — it's the reader's central fear.
2. **What you use** (the AI tool you *use to create the thing*, framed as "what do I open?") — *Just the chat* (green, speech-bubble) → *Connectors, needs permission* (amber, plug) → heavier/agentic modes. **Key correction from Jake:** tag the user's actual experience, not what Claude does under the hood. A recipe where Claude replies with a clickable HTML file is **"just the chat,"** NOT "code & files" — the user never opens a special mode.
3. **Connections** — *None needed* (green, unplugged) → *CRM + Drive* etc. (amber, linked-nodes, shows actual connector glyphs).
4. **Gets smarter?** (reframes "one-shot vs iterative" as a *feature*, not effort) — **Set tool** (metal-cube icon: build once, use as-is) vs. **Living tool** (brain icon: improves as you feed it examples). The cube-vs-brain pairing is the most legible/fun icon contrast in the set and sets up the self-improvement meta-skill.
5. **User** (who sees the output — encodes the red line per-recipe) — 3 levels: **Individual** ("Just you") → **Team** → **Front-facing (constituent)** (red, people-with-caution icon; tooltip insists a human approves every send).

### Icon-vocabulary sub-project (not yet built)
Each of the five dimensions needs a small *family* of state-icons drawing from one shared visual alphabet, built once centrally. A one-page **"how to read a recipe card" legend** at the front of the cookbook would teach the whole vocabulary in ~30 seconds. The cube (set) vs. brain (living) pair is the anchor.

### Open card-design threads
- **Finalize the 4-tier privacy scale wording** — load-bearing across every card; plain-language labels matter more than technical terms but the technical truth must be right underneath.
- **Browse-tile vs. detail-page** — the existing mockups are the *detail page*. The cookbook index wants a *collapsed tile* (icon strip + title + tagline) that expands to the full card. Not yet built.
- **In-page helper** — currently a static fake showing placement/feel. Making it live = it calls the API from the page. Decide whether every card gets one or only trickier recipes (likely overkill on simple ones).
- **Spicy-card tone** — do spicy recipes feel *discouraging* (scary enough to self-select out) or *empowering-with-guardrails*? Current build aims at the second; the red bars lean toward the first. Possible fix: a "safer version available" badge that turns every spicy card into an on-ramp to a lower-risk variant.
- **Recipe ↔ skill tag** — add a "this recipe teaches ___" tag linking each card to the meta-skills it exercises (see §6). Proposed but not yet built into the card.

---

## 6. The meta-skills spine (this is the real differentiation — promote it)

Jake initially listed these as "not recipes but skills people need." **Reframe:** this layer is the actual differentiation of the whole cookbook. Everyone will have recipe lists; almost nobody teaches the *operating skills* that make recipes work. This is the thesis made teachable.

**Structure (proposed):** each meta-skill gets a short standalone treatment **and** is tagged on every recipe that exercises it. Recipes are the *practice*; skills are the *curriculum*. Critically — **never present them as a standalone "vegetables" chapter nobody reads.** Surface them only *in context*, triggered by a recipe, as a "to go further, learn this" door.

The set (expanded from Jake's four):
- **Context transfer** — the structure for high-context generation tasks: give your best thinking up front, then cap at 1–2 iterations. The single most valuable page in the book. (Note Jake's nuance: worthless looping is the "make it funnier… no, more serious… no, go back" spiral on large text-generation tasks — *not* iterating on a transcriber. The lesson targets high-context generation specifically.)
- **The browser line** — when Claude can just code it in the chat vs. when you need real infrastructure. Rough heuristic: *if it needs to remember things between sessions, talk to other systems, or be used by many people at once, it's outgrown the browser.* (Directly serves the §4 persistence cliff.)
- **Honing a living tool** — how to feed positive/negative examples to a project/skill so it self-improves over time.
- **Context management at scale** — once you dump whole folders in, how to guide the agent to find and use only the relevant parts. (Pairs with baby RAG.)
- **Knowing the privacy tier you're in** — reading the situation, not the card. The skill the cards train, stated explicitly.
- **Keeping a human in the loop** — *when* approval is non-negotiable and how to structure "draft-only, I send." The red line as learnable judgment, not just a rule.

---

## 7. Org-grounding bank (reusable personas for recipe generation)

Use these (and add more across different theories of change) to keep recipes specific. Worked so far: **Merit America** (workforce upskilling), **City Harvest** (food logistics), **Catchafire** (volunteer matching). Jake flagged wanting more variety — e.g. an arts org, an advocacy/policy shop, a direct-cash org, a healthcare provider, an environmental org. Each new theory of change surfaces mechanics the others miss.

---

## 8. Immediate next steps (menu, not a mandate)

- **Continue the category deep-passes** in climb order — next up: **Category 2 (Make sense of your data)**, then 3, 4, 5, 6 — each to the depth of §4 (ideas grouped by mechanical verb + the implementation reality / cliff that matters for that category).
- **Prototype the two highest-wattage nibbles** to reverse-engineer real recipes: the **spreadsheet → interactive HTML dashboard** and the **private transcriber**. Build something that actually runs; derive the recipe from it.
- **Resolve the open card threads** (§5): finalize privacy-scale wording; build the collapsed browse-tile; decide the in-page-helper scope; add the recipe↔skill tag.
- **Build the icon-vocabulary legend** (§5) — the shared visual alphabet + the one-page "how to read a card."
- **Expand the org-grounding bank** (§7) for the next generation wave.

---

*End of working document. Everything above is a strong default to argue with, not a frozen spec.*