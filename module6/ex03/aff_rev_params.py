#!/usr/bin/env python3

import sys

args_len: int = len(sys.argv)
if args_len == 1:
	print("none")
else:
	while args_len > 1:
		try:
			float(sys.argv[args_len - 1])
		except:
			print(sys.argv[args_len - 1])
		args_len -= 1
