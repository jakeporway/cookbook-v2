# Recipe family: "Turn your spreadsheet into a tool" (reverse-engineered from working prototypes)

**Category 1 — Code Nibbles · verb: Convert / transform · the headline nibble**

> **Structure (Jake's call):** ONE pattern — *"take this doc and turn it into an interface in HTML"* —
> packaged as **two linked cards** that form a mini-climb:
>
> - **Card A — the Viewer** (`index.html`): see / sort / chart / filter. All-clear green. *(below)*
> - **Card B — the Editor** (`editor.html`): + edit cells + **Export**. Teaches **the browser line**. *(§Card B)*
>
> The interface *shape* (table, chart, map, form) is a **menu** you pick from inside the recipe —
> not separate recipes. The *capability* (view → edit/export) is the **climb** — and only the Export
> step earns its own card, because it's the door to the persistence/browser-line meta-skill.
>
> Built the artifacts first, then derived every card field from what shipping them taught us.
> Notes flagged **⚑** are things the build surfaced that weren't obvious from the PRD.

---

## CARD A — the Viewer

---

## The one-liner
**"Hand Claude a messy spreadsheet, get back a clickable dashboard you run on your own computer."**

## Who it's for (org-grounded)
A logistics/ops person at **City Harvest** keeps a food-rescue log in Excel — donors, pounds,
boroughs, partner agencies, routes. They want to *see* where the food is going this month without
learning Excel pivot tables, and without emailing the file (it's operational data) to some web app.

---

## The steps (what the reader does)
1. Open a normal Claude chat.
2. Paste **2–3 fake/sample rows** of your spreadsheet (just enough to show the column names) and say
   what you want to see. *(See prompt below.)* ⚑ **You do not paste the real file** — see privacy note.
3. Claude replies with a single **HTML file**. Download it.
4. Double-click it. It opens in your browser like any web page.
5. Drag your **real** CSV onto it. The chart fills in. Nothing uploads — it's read on your machine.
6. Re-drop a new export next month to refresh it. No rebuilding.

## The copy-paste prompt (starter — adapt to your columns)
```
I have a spreadsheet I export as CSV. The columns are:
Date, Source/Donor, Food Category, Pounds Rescued, Borough, Partner Agency, Route, Notes.

Build me a SINGLE self-contained HTML file (no internet connection needed, no libraries
loaded from the web) that lets me drag my CSV onto the page and shows:
- total pounds, number of records, and the date range at the top
- a bar chart of total pounds by a group I can switch (donor, category, borough, agency)
- a line chart of pounds over time
- a sortable, searchable table of all my rows

The file must read the CSV in my browser only — my data should never be uploaded anywhere.
My spreadsheet is messy: dates are in mixed formats, some weights are blank or written like
"880 lbs" or "1,240", and the same agency is sometimes spelled two ways. Handle that, and
show me a short note listing what you had to clean up so I can trust the numbers.
```
⚑ That last sentence — *"show me a note listing what you cleaned"* — is the load-bearing line.
It's what turns a black-box chart into something an ops person can trust. Promote it in the teaching.

## What you walk away with
A reusable, offline `.html` tool. Not a one-time answer — a **set tool** you keep and reuse every
month by dropping in a fresh export.

---

## The recipe card — five scan-strip dimensions (derived from the build)

| # | Dimension | Value | Bar | Why (what the build proved) |
|---|-----------|-------|-----|------------------------------|
| 1 | **Where data goes** (privacy) | **Nowhere. It's yours** | 🟢 green | The finished tool parses the CSV client-side; nothing is sent anywhere. Verified: works fully offline. ⚑ **But the *building* step has a caveat — see below.** |
| 2 | **What you use** | **Just the chat** | 🟢 green | Claude replies with a clickable HTML file. The user never opens a "code" mode. (Exactly the §5 correction: tag the user's experience, not what Claude does under the hood.) |
| 3 | **Connections** | **None needed** | 🟢 green | No CRM, no Drive, no connectors. A file and a browser. |
| 4 | **Gets smarter?** | **Set tool** (cube) | — | Build once, use as-is. You feed it new *data*, not new *examples*; the tool itself doesn't learn. Clean anchor for the cube icon. |
| 5 | **User** (who sees output) | **Just you / your team** | 🟢→🔵 | Internal ops reporting. Never constituent-facing — the red line is not even in play here. A genuinely "all-clear" card, like the transcriber. |

### Tier-2 chips
- **Skill level:** Beginner.
- **Time to build:** ~5–10 min of chatting.
- **Effort after setup:** Near zero — drop a new CSV, done.

---

## ⚑ The privacy subtlety this build surfaced (this is a teaching gift)
The *tool* is green end-to-end. But to **build** it, a beginner's instinct is to paste their whole
real spreadsheet into the chat — and **that** sample DOES go to Anthropic. So the honest recipe
teaches the move that keeps it green:

> **Build it with fake or sample rows. Run it on your real file.**
> Claude only needs to see your *column names* and the *shape* of the mess — not your actual
> donors or numbers. Paste two made-up rows, get your tool, then feed it the real CSV locally.

This is **"Knowing the privacy tier you're in"** (§6 meta-skill) made concrete in 30 seconds. The
card should carry a small note tag, and this recipe is a perfect *in-context door* to that skill.

## ⚑ The cliff for THIS nibble (it's NOT the persistence cliff)
Loggers hit the "browser line" because they need to *remember*. This one sidesteps that entirely —
it's stateless by design (you re-drop the CSV each time, which is fine). Its cliff is different:

> **The cleaning is a smart guess, not gospel.** Merging "St John's" and "St. John's" is a
> heuristic. It's usually right; it can be wrong. That's *why* the tool prints what it merged —
> so a human can catch a bad merge. Teaches **"knowing when to trust the output."**

## Meta-skills this recipe teaches (the "this recipe teaches ___" tag)
- **Knowing the privacy tier you're in** — the build-with-fake-data move.
- **Knowing when to trust the output** — the cleaning-notes panel as a trust check.
- *(Light touch)* **The browser line** — by contrast: this one is honestly stateless, so it
  *doesn't* need infrastructure. A good foil to the loggers.

---

---

## CARD B — the Editor (the "level up", linked from Card A)

**The one-liner:** *"Card A showed you the mess. This one lets you fix it in place and export a clean file —
without ever uploading it."*

### Why this is a separate card (not just a bigger prompt)
The Export button crosses a conceptual line: the HTML file stops being a *viewer* and becomes a
*tool that produces a new artifact*. That's exactly where a beginner meets **the browser line**, so
the card is built to teach it in situ — the UI literally says *"This is a worksheet, not a database…
export to keep your changes; close the tab and it starts fresh."*

### What you do
1. Same build move as Card A, but ask for an **editable grid + an Export button**.
2. Drop your CSV in. Cells that were blank/unreadable are **highlighted** (chained from Card A's
   cleaning report — the Viewer *found* the holes, the Editor lets you *fill* them).
3. Edit cells, add/delete rows. The running total updates live so a fix feels real.
4. Hit **Export clean CSV** → a corrected file downloads. Done.

### Added prompt lines (on top of Card A's prompt)
```
Make the table editable — I want to fix values directly in the page, add rows, and delete rows.
Highlight any cell that was blank or unreadable in my file so I know what to fix.
Show a running total at the top that updates as I edit.
Add an "Export clean CSV" button that downloads my edited data as a new file.
Important: it should NOT try to save or remember anything on its own — I'll export when I'm done.
```

### Card B scan-strip (deltas from Card A)
| Dimension | Value | Bar | Note |
|-----------|-------|-----|------|
| Where data goes | **Nowhere. It's yours** | 🟢 | ⚑ *Still green even though data now goes IN and comes OUT* — the surprise worth teaching: editing + export stays 100% local. |
| What you use | **Just the chat** | 🟢 | Still a clickable HTML file. |
| Connections | **None needed** | 🟢 | A file and a browser. |
| Gets smarter? | **Set tool** (cube) | — | Same — you feed it data, not examples. |
| User | **Just you / your team** | 🟢→🔵 | Internal. |

The whole card is still green — but it carries the **browser-line** teaching front and center, where
Card A only hinted at it. That contrast (a green card that still has a lesson) is the point.

### ⚑ Bug the build caught (worth a teaching aside)
First version of the Editor auto-detected the **Date** column as the metric to total, because
`3/2/25` survives naive number-cleaning as `3225`. The Viewer dodged this by checking date-shape
first; the Editor didn't. **Lesson for the cookbook:** "ask the tool to show its work / sanity-check
the first number it gives you" — the same *knowing-when-to-trust* skill, proven on our own build.

---

## Files in this prototype
- `index.html` — **Card A (Viewer)**: drag a CSV on, see/sort/chart it. The artifact Claude hands back.
- `editor.html` — **Card B (Editor)**: edit cells, fix the blanks, Export a clean CSV. Teaches the browser line.
- `sample-city-harvest.csv` — realistically messy City Harvest food-rescue log (the shared input).
- `RECIPE.md` — this file.

Run them: `python3 -m http.server 8485` in this folder → http://localhost:8485/index.html and /editor.html
(or just double-click the files — they work offline).

## Open questions for Jake
1. **Default group-by:** the tool opens grouped by *Source/Donor*. For City Harvest the more
   moving story might be *Partner Agency* (where food landed) or *Food Category*. Should the recipe
   tell people to name their "headline" dimension, or let the tool pick the first one? (Tiny, but
   it's the difference between a dashboard that lands and one that shrugs.)
2. **How hard to lean on the cleaning-notes panel.** I think it's the secret sauce of this nibble
   and deserves promotion to a named pattern ("ask the tool to show its work"). Agree?
3. **Pair or sequence with the transcriber?** Both are "all-clear green" cards. Showing them side
   by side early might be the strongest way to establish the green end of the privacy scale before
   any spicy card appears.
