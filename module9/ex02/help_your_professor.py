#!/usr/bin/env python3

def average(scores: {str, float}) -> float:
	sum: float = 0
	for value in scores.values():
		sum += value
	return sum / len(scores.values())

class_3B = {
	"marine": 18,
	"jean": 15,
	"coline": 8,
	"luc": 9
}
class_3C = {
	"quentin": 17,
	"julie": 15,
	"marc": 8,
	"stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")