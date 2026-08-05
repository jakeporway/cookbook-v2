#!/usr/bin/env python3
"""Inject the Simple / Detailed prompt toggle into every recipe page.

Idempotent: run it again after editing detailed-prompts.py and it rebuilds
both variants in place. The simple prompt is always taken from the page
itself (the simple <pre> is the source of truth for simple text); the
detailed one comes from detailed-prompts.py.

	python3 build-prompt-variants.py [--check]
"""

import glob
import os
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from detailed_prompts import DETAILED  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))

# One .prompt block: header (with label), then one or two <pre> variants.
BLOCK = re.compile(
	r'(<div class="prompt">\s*<div class="ph">)(.*?)(</div>)(.*?)(</div>)',
	re.S,
)
PRE = re.compile(r'<pre(?: [^>]*)?>(.*?)</pre>', re.S)
LABEL = re.compile(r'<span>(.*?)</span>', re.S)

SCRIPT_TAG = '<script src="prompt-toggle.js"></script>'


def header(label):
	return (
		'\n        <span>%s</span>\n'
		'        <span class="pmode" role="group" aria-label="Prompt detail level">'
		'<button type="button" class="on" data-v="simple" aria-pressed="true">Simple</button>'
		'<button type="button" data-v="detailed" aria-pressed="false">Detailed</button>'
		'</span>\n'
		'        <button class="copy" type="button">Copy</button>\n      ' % label
	)


def rebuild(path, check=False):
	src = open(path, encoding='utf-8').read()
	name = os.path.basename(path)
	idx = [0]
	missing = []

	def one(m):
		i = idx[0]
		idx[0] += 1
		key = '%s#%d' % (name, i)
		label = LABEL.search(m.group(2)).group(1)
		pres = PRE.findall(m.group(4))
		simple = pres[0]
		detailed = DETAILED.get(key)
		if detailed is None:
			missing.append(key)
			return m.group(0)
		body = (
			'\n        <pre class="pv" data-v="simple">%s</pre>'
			'\n        <pre class="pv" data-v="detailed" hidden>%s</pre>\n      '
			% (simple, detailed.rstrip('\n'))
		)
		return m.group(1) + header(label) + m.group(3) + body + m.group(5)

	out = BLOCK.sub(one, src)

	if idx[0] and SCRIPT_TAG not in out:
		out = out.replace('</body>', '  ' + SCRIPT_TAG + '\n</body>')

	changed = out != src
	if changed and not check:
		open(path, 'w', encoding='utf-8').write(out)
	return idx[0], missing, changed


def main():
	check = '--check' in sys.argv
	total, all_missing, touched = 0, [], 0
	for path in sorted(glob.glob(os.path.join(HERE, 'recipe-*.html'))):
		n, missing, changed = rebuild(path, check)
		total += n
		all_missing += missing
		touched += 1 if changed else 0
	print('%d prompt blocks across %d changed files' % (total, touched))
	if all_missing:
		print('MISSING detailed variants for:')
		for k in all_missing:
			print('  ' + k)
		sys.exit(1)
	print('all %d blocks have a detailed variant' % total)


if __name__ == '__main__':
	main()
