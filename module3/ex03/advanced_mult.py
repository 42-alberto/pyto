#!/usr/bin/env python3

i: int = 0
j: int = 0

while i <= 10:
	j = 0
	print(f"Table of {i}:", end="")
	while j <= 10:
		print(f" {i * j}", end="")
		j += 1
	print("")
	i += 1
