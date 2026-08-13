# The Nonprofit AI Cookbook — V2

Recipes for getting real work back from AI. Published by Decoded Futures.

**Live site:** https://jakeporway.github.io/cookbook-v2/

## Layout

```
site/     Everything that is published, and nothing else.
          This directory IS the website. What you see here is what
          is live, at the same relative paths.
build/    Generators that write into site/. Run from the repo root.
docs/     PRD, handoff notes, the recipe slate, screenshots. Never published.
.claude/  The convert-to-guided skill used to author guided recipes.
```

## Deploying

Push to `main`. That's it.

`.github/workflows/pages.yml` publishes `site/` to GitHub Pages on any push
that touches it. There is no copy step, no rename, and no second repository to
sync. If a file is in `site/`, it is live; if it is anywhere else, it is not.

> This replaced an older setup where the site was hand-copied into a separate
> `cookbook-v2-preview` repo and `index-v3.html` was renamed to `index.html` on
> the way. That rename was invisible and broke links repeatedly. Do not
> reintroduce a build step that renames pages.

## The two page types

Every recipe exists twice:

- `site/recipe-<slug>.html` — the step-by-step version. Its prompt has a
  Simple and a Detailed variant, toggled by `site/prompt-toggle.js`.
- `site/recipe-<slug>-guided.html` — the guided version. One block the reader
  pastes; the AI then interviews them and does the work. No toggle.

They cross-link to each other in the backlink bar. `site/index.html` lists the
step recipes; `site/index-guided.html` lists the guided ones.

## Build scripts

Run from the repo root. Both resolve paths relative to themselves, so they work
from anywhere, but the output always lands in `site/`.

```bash
# Regenerate the guided index from site/index.html.
# Run after ANY edit to site/index.html.
python3 build/build-guided-index.py

# Rebuild the Simple/Detailed prompt variants on the step recipes.
# --check verifies without writing. Skips *-guided.html by design.
python3 build/build-prompt-variants.py --check
python3 build/build-prompt-variants.py

# Validate guided recipe pages against the house structure.
python3 .claude/skills/convert-to-guided/scripts/check_guided.py site/*-guided.html
```

`build-guided-index.py` fails loudly if `site/index.html` changes shape rather
than emitting a wrong page. If it errors with "has changed shape", update the
matching literal in the script to the new markup — do not work around it.

## Related repositories

- `jakeporway/cookbook-v2-preview` — the old URL. Now only a redirect stub.
- `jakeporway/nonprofit-ai-cookbook` — an earlier public site, now redirecting here.
- `jakeporway/prompt-cookbook` — the V1 cookbook (2025).
- The `library/` research system lives in the private `prompt-cookbook-library`
  repo, not here, because GitHub Pages requires this repo to be public.
