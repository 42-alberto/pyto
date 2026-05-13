#!/usr/bin/env python3

import sys


def shrink(string: str):
	print(string[:8])

def enlarge(string: str) -> str:
	while len(string) < 8:
		string += 'Z'
	return string

if len(sys.argv) < 2:
	print("none")
else:
	for arg in sys.argv[1:]:
		if len(arg) == 8:
			print(arg)
		elif len(arg) > 8:
			shrink(arg)
		elif len(arg) < 8:
			arg = enlarge(arg)
			shrink(arg)