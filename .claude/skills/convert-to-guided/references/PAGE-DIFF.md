# Page diff: step recipe → guided recipe

Clone `site/recipe-<slug>.html` to `site/recipe-<slug>-guided.html` and change only
what is listed here. Everything unlisted — the rail, the card wrapper, the
stylesheet link, the script tag — is copied byte for byte.

## Head and chrome

```html
<title>Recipe: <Name> (Guided) · Decoded Futures Cookbook</title>
```

Backlink bar — left span gains the mode link, right span gains `· Guided`:

```html
<div class="backlink">
  <span><a href="index.html">← The Cookbook</a> · <a href="recipe-<slug>.html">Read the steps instead</a></span>
  <span><Category> · Recipe <NN> · Guided</span>
</div>
```

Eyebrow first span gains `· Guided setup`:

```html
<span><Category> · <Verb> · Guided setup</span>
```

`<h1>` and `.tagline` are unchanged.

## Warning flags

Keep verbatim when the risk is unchanged. Re-voice when the assistant now
enforces the gate, e.g. district-lookup's green flag became:

```
Nothing to flag, if the addresses are public ones. The assistant checks this with you first
```

Never downgrade a flag's colour. The guided prompt makes the gate harder to skip;
it does not remove the risk.

## "Information you give it" → "What it will ask you"

Replace the whole `.give` block. New icon is the question-mark-in-circle:

```html
<div class="give">
  <div class="ic">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 10h8M8 14h5"/><path d="M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0z"/></svg>
  </div>
  <div>
    <div class="gh">What it will ask you</div>
    <p>...</p>
  </div>
</div>
```

The `<p>` previews the interview in everyday terms — the questions themselves, not
the data. Say plainly what the reader does *not* have to supply, since that is the
selling point: "You never attach a recording", "You write nothing new", "It never
asks for a single real name or number".

## Section heading

```html
<div class="sech"><span class="px"><i></i><i></i></span> How to use this</div>
```

## Steps

The whole `<ol class="steps">` collapses to one item:

```html
<ol class="steps">
  <li><div>
    <div class="st-h">Copy the whole block below and paste it into your AI chat</div>
    <div class="st-b">...</div>
  </div></li>
</ol>
```

The `st-b` says what the assistant does first and what the reader must prepare.
When nothing needs preparing, say so — "Nothing to fill in and nothing to
prepare" — because the step page trained the reader to expect otherwise.

## Prompt block

No Simple/Detailed toggle, no `data-v`, no `class="tok"` spans, no `.prenote`.
One plain `<pre>`.

```html
<div class="prompt">
  <div class="ph">
    <span>The whole recipe, in one paste</span>
    <button class="copy" type="button" style="margin-left:auto">Copy</button>
  </div>
  <pre>...</pre>
</div>
```

The `margin-left:auto` is required — the toggle normally occupies that slot and
without it the Copy button sits against the label.

The block moves **out** of the `<li>` and sits as a direct child of `.recipe`,
after the `<ol>`.

## Browserlines

Keep every one. Rewrite each to say what the assistant now enforces and what
remains the reader's job, e.g.:

> The assistant is instructed to enforce all three, but the spot-check is yours.

> The prompt makes the assistant check whose addresses these are before it accepts
> your list.

A browserline that reads identically to the step page's is a missed edit: the
division of labour changed, so the caution should say so.

## Yield

`.yield` is preserved. Adjust only wording made wrong by the conversion (e.g.
"councilmember" → "representative" when the guided prompt generalised the district
type).

## Ordering inside `.recipe`

Gold pages vary. Prefer: `sech` → `ol.steps` → `div.prompt` → browserlines →
`yield`. `recipe-district-lookup-guided.html` puts browserlines before the yield;
`recipe-private-transcriber-guided.html` does the same. Match that.

## Do not

- Do not add the page to `index-v3.html` — index cards are whole-tile `<a>`
  elements and cannot nest a second link. The backlink cross-link is the wiring.
- Do not register the page in `detailed_prompts.py`. Guided pages have no detailed
  variant, and `build-prompt-variants.py` skips `-guided.html`.
