#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
	print("none")
else:
	num1: int = int(sys.argv[1])
	num2: int = int(sys.argv[2])
	if num1 < num2:
		num_list: list[int] = [n for n in range(num1, num2 + 1)]
		print(num_list)
