#!/usr/bin/env python3
"""Validate a guided recipe page against the conversion template.

	python3 check_guided.py site/recipe-<slug>-guided.html [more...]
	python3 check_guided.py site/*-guided.html

Errors are template violations. Warnings are judgment calls worth a second look.
Exits 1 if any file has an error.
"""

import html
import os
import re
import sys

MAX_COL = 65

PRODUCTS = re.compile(r'\b(ChatGPT|Claude|Gemini|Copilot)\b')

# (label, regex) -- every one required in the prompt body.
CLAUSES = [
	('one question at a time', r'ONE question at a time'),
	('question count announced', r'how many questions to expect'),
	('no technical questions', r'[Nn]ever ask me a technical question directly'),
	('recipe-specific example pair', r'do NOT ask'),
	('product detection', r"which AI product I'?m talking to you in"),
	('plan detection', r'free or paid plan'),
	("don't assume software", r"[Dd]on'?t assume what software I use"),
	('answers my questions', r'answer it in plain language'),
	('recovers from mismatch', r"what'?s on my screen"),
	('one step at a time outside chat',
	 r"ONE (?:step|screen'?s worth of instructions) at a time.{0,140}?"
	 r'check(?:ing)? that it worked'),
]

# Ordered required sections; each entry is a list of acceptable header patterns.
SECTIONS = [
	("WHAT WE'RE MAKING/DOING", [r"^WHAT WE'RE (MAKING|DOING)$"]),
	('HOW TO WORK WITH ME', [r'^HOW TO WORK WITH ME$']),
	('QUESTIONS YOU\'LL NEED ANSWERED', [
		r"^QUESTIONS YOU'LL NEED ANSWERED \(in your own words, one at a time\)$"]),
	('technical spec', [r'^WHAT TO BUILD\b', r'^WHAT TO SET UP\b', r'^HOW TO DO THE\b']),
	('walkthrough', [r'^AFTER .*WALK ME THROUGH$']),
	('rules or escape hatch', [r'^RULES$', r'^IF \b']),
]

HEADER = re.compile(r'^[A-Z][A-Z0-9\'’ ,/-]{3,}(\(.*\))?$')
BRACKET = re.compile(r'\[([^\]]+)\]')


def strip_tags(s):
	return html.unescape(re.sub(r'<[^>]+>', '', s))


def check(path):
	errs, warns = [], []
	name = os.path.basename(path)
	src = open(path, encoding='utf-8').read()

	m = re.match(r'recipe-(.+)-guided\.html$', name)
	if not m:
		errs.append('filename must be recipe-<slug>-guided.html')
		slug = None
	else:
		slug = m.group(1)

	# --- page structure -------------------------------------------------
	if '(Guided)' not in src:
		errs.append('<title> is missing "(Guided)"')
	if not re.search(r'·\s*Guided\s*</span>', src):
		errs.append('backlink bar is missing the "· Guided" marker')
	if 'Guided setup' not in src:
		errs.append('eyebrow is missing "· Guided setup"')
	if 'What it will ask you' not in src:
		errs.append('missing the "What it will ask you" block')
	if 'Information you give it' in src:
		errs.append('still has the step-page "Information you give it" block')
	if 'How to use this' not in src:
		errs.append('section heading should be "How to use this"')
	if 'The whole recipe, in one paste' not in src:
		errs.append('prompt header label should be "The whole recipe, in one paste"')
	if 'margin-left:auto' not in src:
		errs.append('Copy button needs style="margin-left:auto" (no toggle in that slot)')
	if 'class="yield"' not in src:
		errs.append('yield block was dropped')
	if 'card-styles.css' not in src:
		errs.append('stylesheet link was dropped')
	if 'prompt-toggle.js' not in src:
		errs.append('prompt-toggle.js was dropped (the Copy button needs it)')
	if slug and 'recipe-%s.html' % slug not in src:
		errs.append('backlink is missing the cross-link to recipe-%s.html' % slug)

	for bad, why in (('data-v=', 'Simple/Detailed toggle'),
	                 ('class="tok"', 'fill-in-the-blank token spans'),
	                 ('class="prenote"', 'step-page prompt prenote')):
		if bad in src:
			errs.append('leftover %s (%s)' % (bad, why))

	pres = re.findall(r'<pre[^>]*>(.*?)</pre>', src, re.S)
	if len(pres) != 1:
		errs.append('expected exactly 1 <pre>, found %d' % len(pres))
		return errs, warns

	# --- prompt body ----------------------------------------------------
	body = strip_tags(pres[0])
	lines = body.split('\n')

	for i, ln in enumerate(lines, 1):
		if len(ln) > MAX_COL:
			errs.append('prompt line %d is %d cols (max %d): %s'
			            % (i, len(ln), MAX_COL, ln[:50] + '...'))

	# Clauses are matched against a whitespace-flattened body so a required
	# phrase that happens to wrap across two lines still counts.
	flat = re.sub(r'\s+', ' ', body)
	for label, pat in CLAUSES:
		if not re.search(pat, flat):
			errs.append('HOW TO WORK WITH ME is missing the "%s" clause' % label)

	headers = [(i, ln.strip()) for i, ln in enumerate(lines) if HEADER.match(ln.strip())]
	pos = -1
	for label, pats in SECTIONS:
		hit = next((i for i, h in headers
		            if i > pos and any(re.search(p, h) for p in pats)), None)
		if hit is None:
			errs.append('missing (or out of order) section: %s' % label)
		else:
			pos = hit

	if not re.search(r'Start now by telling me, in two sentences, what we\'re going\s+to (do|make|set up) together, then ask your first question\.',
	                 body.replace('\n', ' ').replace('  ', ' ')) \
	   and 'then ask your first question' not in body:
		errs.append('missing the closing "Start now by telling me..." line')

	for tok in BRACKET.findall(body):
		if tok != tok.upper():
			errs.append('leftover reader-fill token %s -- guided prompts ask a '
			            'question instead; only ALL-CAPS assistant-filled slots '
			            'are allowed' % ('[' + tok + ']'))

	# --- warnings -------------------------------------------------------
	# Naming one product reads as a requirement; naming several reads as an
	# illustration. Only the former is a portability risk.
	for i, ln in enumerate(lines):
		if PRODUCTS.search(ln):
			ctx = re.sub(r'\s+', ' ', ' '.join(lines[max(0, i - 1):i + 2]))
			if 'for example' not in ctx and len(set(PRODUCTS.findall(ctx))) < 2:
				warns.append('line %d names a product outside a "for example" '
				             'list: %s' % (i + 1, ln.strip()[:60]))

	qs = re.search(r"^QUESTIONS YOU'LL NEED ANSWERED.*?$(.*?)^[A-Z][A-Z ]{4,}",
	               body, re.S | re.M)
	if qs:
		n = len(re.findall(r'^\d+\.', qs.group(1), re.M))
		if n > 6:
			warns.append('%d questions in the interview; more than 6 and readers '
			             'abandon it' % n)
		if n < 2:
			warns.append('only %d question(s) in the interview' % n)

	return errs, warns


def main():
	paths = sys.argv[1:]
	if not paths:
		print(__doc__)
		return 2
	bad = 0
	# index-guided.html is the guided index, not a guided recipe. A site/*-guided.html
	# glob always sweeps it in, so skip it rather than report a permanent failure.
	paths = [p for p in paths if os.path.basename(p) != 'index-guided.html']
	for p in paths:
		errs, warns = check(p)
		tag = 'FAIL' if errs else ('warn' if warns else ' ok ')
		print('[%s] %s' % (tag, os.path.basename(p)))
		for e in errs:
			print('       ERROR  ' + e)
		for w in warns:
			print('       warn   ' + w)
		bad += 1 if errs else 0
	print('\n%d/%d files clean' % (len(paths) - bad, len(paths)))
	return 1 if bad else 0


if __name__ == '__main__':
	sys.exit(main())
