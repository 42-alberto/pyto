#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
	print("none")
else:
	arg: str = sys.argv[1]
	word: str = input("What was the parameter? ")
	if arg == word:
		print("Good job!")
	else:
		print("Nope, sorry...")