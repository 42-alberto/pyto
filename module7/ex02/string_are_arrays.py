#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
	print("none")
else:
	count: int = 0
	for c in sys.argv[1]:
		if c == 'z':
			count += 1
			print(c, end="")
	if count == 0:
		print("none")
	else:
		print("")
