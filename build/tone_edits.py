# -*- coding: utf-8 -*-
"""Data file for apply-tone-edits.py — (old, new[, count]) prose replacements per page.

Emptied after the July 2026 tone pass. Refill it when the next prose edit comes
through: run `python3 dump-prose.py recipe-*.html` to get exact strings, add the
pairs here, then `python3 apply-tone-edits.py`. Every <pre> block is carved out
before replacement, so an edit here can never reach prompt text.
"""

EDITS = {}
