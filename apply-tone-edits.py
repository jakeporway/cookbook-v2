#!/usr/bin/env python3
"""Apply prose tone edits to recipe pages, guaranteeing prompt blocks stay untouched.

Every <pre>...</pre> region is carved out before replacement and restored after, so
no edit can ever reach the simple or detailed prompt text. Each (old, new) pair must
match exactly once in the remaining prose, or the file is left alone and the mismatch
is reported.

	python3 apply-tone-edits.py [--check]
"""

import os
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tone_edits import EDITS  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
PRE = re.compile(r'<pre.*?</pre>', re.S)


def apply_file(name, pairs, check=False):
	path = os.path.join(HERE, name)
	src = open(path, encoding='utf-8').read()

	stash = []

	def hide(m):
		stash.append(m.group(0))
		return '\x00PRE%d\x00' % (len(stash) - 1)

	body = PRE.sub(hide, src)

	problems = []
	for pair in pairs:
		# (old, new) must match exactly once; (old, new, count) must match `count` times.
		old, new = pair[0], pair[1]
		want = pair[2] if len(pair) > 2 else 1
		n = body.count(old)
		if n != want:
			problems.append('  %s match%s (wanted %s): %s'
				% (n, '' if n == 1 else 'es', want, old[:90]))
			continue
		body = body.replace(old, new, want)

	out = re.sub(r'\x00PRE(\d+)\x00', lambda m: stash[int(m.group(1))], body)

	if problems:
		return 0, problems
	if out != src and not check:
		open(path, 'w', encoding='utf-8').write(out)
	return len(pairs), []


def main():
	check = '--check' in sys.argv
	total, files, bad = 0, 0, 0
	for name in sorted(EDITS):
		n, problems = apply_file(name, EDITS[name], check)
		if problems:
			bad += 1
			print('%s — NOT APPLIED:' % name)
			for p in problems:
				print(p)
			continue
		total += n
		files += 1
	print('%d edits applied across %d files (%d files skipped)' % (total, files, bad))
	sys.exit(1 if bad else 0)


if __name__ == '__main__':
	main()
