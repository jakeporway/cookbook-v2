#!/usr/bin/env python3
"""Generate index-guided.html from index-v3.html.

The guided landing page is the same categories, same cards, same search, with
every link pointing at the -guided.html twin and the framing copy rewritten for
the one-paste model. Generating it means the two pages can't drift: re-run this
after any edit to index-v3.html.

	python3 build-guided-index.py [--check]

--check exits 1 if the generated output differs from what's on disk.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'index-v3.html')
OUT = os.path.join(HERE, 'index-guided.html')

LINK = re.compile(r'href="(recipe-[a-z0-9-]+)\.html"')


def sub_once(src, old, new, label):
	"""Replace exactly one occurrence, or fail loudly: index-v3.html changed."""
	n = src.count(old)
	if n != 1:
		raise SystemExit(
			'build-guided-index: expected 1 occurrence of %s, found %d.\n'
			'index-v3.html has changed shape; update this script.' % (label, n))
	return src.replace(old, new)


HERO_OLD_START = '    <div class="eyebrow">The Prompt Cookbook - V2</div>'
HERO_NEW = '''    <div class="eyebrow">The Prompt Cookbook &middot; Guided</div>
    <h1>Let the AI walk you through it.</h1>
    <p class="lede">The same recipes, in a different shape. Instead of steps to
    follow and blanks to fill in, each one is a single block you paste into your AI
    chat. It then asks you a few plain questions, does the technical part itself,
    and walks you through checking the result before you use it.</p>
    <p class="lede">Nothing here assumes you're technical, and nothing assumes which
    AI you use. Every recipe starts by working out what your product and plan can
    actually do, and tells you plainly if this one is beyond it rather than letting
    you find out halfway through.</p>
    <p class="lede">Prefer to read the steps yourself? Every recipe still has its
    original version: <a href="index-v3.html" style="color:var(--blue);text-decoration:underline">the
    step-by-step cookbook</a>. Each page links across to the other, so you can switch
    at any point.</p>
    <p class="lede">Please send any feedback you have to
    <a href="mailto:info@decodedfutures.nyc" style="color:var(--blue);text-decoration:underline">info@decodedfutures.nyc</a>
    and we hope you enjoy!</p>
'''

HOWTO_NEW = '''    <details class="howto">
      <summary>How to Use This Cookbook</summary>
      <div class="howto-body">
        <div class="howto-col">
          <h4>Step by step</h4>
          <ol>
            <li><b>Browse or search</b>: use the sections or the search bar to find a task you actually face.</li>
            <li><b>Copy the whole block</b>: there's one per recipe, and nothing to fill in first.</li>
            <li><b>Paste it into your AI chat</b>: whichever one you use.</li>
            <li><b>Answer its questions</b>: it asks one at a time, in plain language, and works out the technical details from your answers.</li>
            <li><b>Check the result</b>: it walks you through this at the end. That part is still yours.</li>
          </ol>
        </div>
        <div class="howto-col">
          <h4>Tips for success</h4>
          <ul>
            <li><b>Answer in your own words</b>: it's built to work from how you'd actually describe your work, not technical terms.</li>
            <li><b>Ask it questions back</b>: it will answer in plain language and then pick up where you left off.</li>
            <li><b>Say when something looks different</b>: if an instruction doesn't match your screen, describe what you see and it will adapt.</li>
            <li><b>Stop if it tells you to stop</b>: several recipes check whether your material is safe to paste. That check is the point.</li>
          </ul>
        </div>
      </div>
    </details>
'''

GETTING_STARTED_NEW = '''  <div class="gettingstarted">
    <h3>Getting Started</h3>
    <p class="blurb">Before you begin, we have two quick tricks to increase your safety and privacy.
    The first walks you through your settings on your software of choice so they're set for minimal
    data tracking. The second has your AI build you a webpage that removes sensitive data from your
    files before anything goes into a chat. Both of them now do the work with you, one question at
    a time.</p>
  </div>
'''

START_SUB_NEW = ('    <p class="sub">These two recipes make every other recipe in the book safer and '
                 'smoother. After them,\n    there is no required order, find the section that '
                 'matches your problem and start there.</p>')

NAV_NEW = '''  <nav class="topnav">
    <a href="#start">Start here</a>
    <a href="#c1">The recipes</a>
    <a href="index-v3.html">Step-by-step version</a>
  </nav>'''

# Five recipes exist as pages but were never listed on index-v3.html. This page
# is meant to be all of them, so they get cards here. Badge colours follow the
# key on the page (green nothing leaves your computer, blue public or
# non-sensitive, amber your files go in), which is not always the same axis as
# the recipe page's own flag.
MISSING = {
	# section id -> grid index within that section -> cards
	('c1', 0): '''
      <a class="card" href="recipe-annual-report-social-guided.html">
        <div class="ttl">Mine your annual report for a quarter of social posts</div>
        <div class="desc">The report you already finished holds months of content: stat callouts,
        story excerpts, milestone posts, quote graphics. It pulls them out in one pass, labels every
        one with the page it came from, and helps you check the figures before anything is scheduled.</div>
        <div class="meta"><span class="chip"><span class="dot b"></span>Public content</span></div>
      </a>

      <a class="card" href="recipe-quote-card-press-guided.html">
        <div class="ttl">Turn any quote or statistic into a ready-to-post graphic</div>
        <div class="desc">A small page on your own computer that makes branded cards from your own
        colors and logo. You type, click, and download. It never rewords a quote, and it asks who
        checks a card before it posts.</div>
        <div class="meta"><span class="chip"><span class="dot b"></span>Public content</span></div>
      </a>

      <a class="card" href="recipe-training-kit-guided.html">
        <div class="ttl">Turn a training document into a whole volunteer kit</div>
        <div class="desc">A facilitator guide, a plain-language handout, and a click-through practice
        quiz that runs on any laptop or phone with no login. It asks who your volunteers are and
        writes for them, rather than at a fixed reading level.</div>
        <div class="meta"><span class="chip"><span class="dot g"></span>Nothing sensitive involved</span></div>
      </a>
''',
	('c3', 0): '''
      <a class="card" href="recipe-spreadsheet-editor-guided.html">
        <div class="ttl">Fix the mess in the page, then export a clean file</div>
        <div class="desc">The next step after the Viewer: edit cells and add rows in the page itself,
        then download a corrected file. Still nothing uploaded, and it deliberately won't remember
        your edits, so the clean export is the thing you keep.</div>
        <div class="meta"><span class="chip"><span class="dot g"></span>Nothing leaves your computer</span></div>
      </a>

      <a class="card" href="recipe-whos-missing-guided.html">
        <div class="ttl">Find who registered, attended, and never finished</div>
        <div class="desc">Three lists reconciled into plain lists of names rather than a pivot table,
        so you can see exactly where people fall out. It checks first whether these lists are safe to
        paste, and offers a version that runs on your own computer if they aren't.</div>
        <div class="meta"><span class="chip"><span class="dot a"></span>Names go into the chat</span></div>
      </a>
''',
}


def append_cards(out, section_id, grid_index, cards):
	"""Insert cards at the end of the grid_index-th .cards grid in a section."""
	i = out.index('<section class="cat" id="%s">' % section_id)
	pos = i
	for _ in range(grid_index + 1):
		pos = out.index('<div class="cards">', pos) + 1
	end = out.index('\n\n    </div>', pos)
	return out[:end] + '\n' + cards.rstrip('\n') + out[end:]


def build():
	src = open(SRC, encoding='utf-8').read()

	# 1. Every card and link points at the guided twin.
	def relink(m):
		slug = m.group(1)
		if slug.endswith('-guided'):
			return m.group(0)
		if not os.path.exists(os.path.join(HERE, slug + '-guided.html')):
			raise SystemExit('build-guided-index: no guided twin for %s.html' % slug)
		return 'href="%s-guided.html"' % slug

	out = LINK.sub(relink, src)
	n_links = len(LINK.findall(src))

	# 2. Title and nav.
	out = sub_once(out, '<title>The Prompt Cookbook - V2 · Decoded Futures</title>',
	               '<title>The Prompt Cookbook · Guided · Decoded Futures</title>', '<title>')
	out = sub_once(out,
	               '  <nav class="topnav">\n    <a href="#start">Start here</a>\n'
	               '    <a href="#c1">The recipes</a>\n  </nav>',
	               NAV_NEW, 'topnav')

	# 3. Hero copy: replace everything from the eyebrow to the </details>.
	i = out.index(HERO_OLD_START)
	j = out.index('    </details>\n', i) + len('    </details>\n')
	out = out[:i] + HERO_NEW + '\n' + HOWTO_NEW + out[j:]

	# 4. Getting Started and the start-here subhead.
	i = out.index('  <div class="gettingstarted">')
	j = out.index('  </div>\n', i) + len('  </div>\n')
	out = out[:i] + GETTING_STARTED_NEW + out[j:]

	out = sub_once(out, '<h2>Start with these two, then go anywhere</h2>',
	               '<h2>Start with these two, then go anywhere</h2>', 'start heading')

	# 5. The five recipes index-v3.html never listed.
	for (section_id, grid_index), cards in MISSING.items():
		out = append_cards(out, section_id, grid_index, cards)

	# 6. Footer count, from the cards actually on the page.
	n_cards = out.count('class="card"') + out.count('class="card first"')
	out = re.sub(r'<div>Decoded Futures · The Prompt Cookbook[^<]*</div>',
	             '<div>Decoded Futures · The Prompt Cookbook · Guided · August 2026.</div>', out)
	out = re.sub(r'<div>\d+ recipes · \d+ sections · start anywhere\.</div>',
	             '<div>%d recipes · 6 sections · one paste each.</div>' % n_cards, out)

	return out, n_links, n_cards


def main():
	out, n_links, n_cards = build()
	check = '--check' in sys.argv
	old = open(OUT, encoding='utf-8').read() if os.path.exists(OUT) else None
	if check:
		if old != out:
			print('index-guided.html is out of date; run build-guided-index.py')
			return 1
		print('index-guided.html is up to date (%d cards)' % n_cards)
		return 0
	open(OUT, 'w', encoding='utf-8').write(out)
	print('wrote index-guided.html: %d cards, %d links repointed' % (n_cards, n_links))
	return 0


if __name__ == '__main__':
	sys.exit(main())
