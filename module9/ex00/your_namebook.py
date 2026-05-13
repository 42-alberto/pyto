#!/usr/bin/env python3

def array_of_names(persons: {str, str}) -> list[str]:
	full_names: list[str] = []
	for key in persons:
		name: str = key.capitalize() + " " + persons[key].capitalize()
		full_names.append(name)
	return full_names


persons: {str, str} = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))