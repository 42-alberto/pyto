#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
	print("none")
else:
	count: int = 0
	for arg in sys.argv[1:]:
		end: int = len(arg) - 3
		ignore : bool = False

		if end >= 0:
			index_ism: int = arg.find("ism")

		if end < 0 or index_ism != end:
			print(f"{arg}ism")