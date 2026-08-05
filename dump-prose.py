#!/usr/bin/env python3
"""Dump the exact prose strings of recipe pages (everything outside <pre> blocks).

	python3 dump-prose.py recipe-a.html recipe-b.html ...
"""

import re
import sys

PRE = re.compile(r'<pre.*?</pre>', re.S)

FIELDS = [
	('TAGLINE', r'<p class="tagline">(.*?)</p>'),
	('FLAGTEXT', r'<span class="clear">\s*<svg.*?</svg>\s*(.*?)\s*</span>'),
	('FLAGLABEL', r'<span class="fl">(.*?)</span>'),
	('TIP', r'<div class="tip">(.*?)(?:</div>|$)'),
	('GIVE', r'<div class="gh">(?:.*?)</div>\s*<p>(.*?)</p>'),
	('PRENOTE', r'<p class="prenote">(.*?)</p>'),
	('STEP-H', r'class="st-h">(.*?)</div>'),
	('STEP-B', r'class="st-b">(.*?)</div>'),
	('CALLOUT', r'<div class="browserline">(.*?)</div>'),
	('YIELD', r'<div class="yh">(?:.*?)</div>\s*<p>(.*?)</p>'),
	('SECH', r'<div class="sech">(?:.*?)</span>\s*(.*?)</div>'),
	('DEMO', r'<p class="demo-note">(.*?)</p>|<div class="demo-note">(.*?)</div>'),
]


def main():
	for name in sys.argv[1:]:
		src = open(name, encoding='utf-8').read()
		body = PRE.sub('', src)
		h1 = re.search(r'<h1>(.*?)</h1>', body, re.S)
		print('\n########## %s :: %s' % (name, h1.group(1) if h1 else '?'))
		for label, pat in FIELDS:
			for m in re.finditer(pat, body, re.S):
				txt = next(g for g in m.groups() if g is not None) if m.groups() else m.group(0)
				print('--%s--\n%s' % (label, txt.strip()))


if __name__ == '__main__':
	main()
