#!/usr/bin/env python3

def add_one(var: int) -> None:
	var += 1
	# print(id(var))

var: int = 0
print(var)
# print(id(var))
add_one(var)
print(var)
# print(id(var))