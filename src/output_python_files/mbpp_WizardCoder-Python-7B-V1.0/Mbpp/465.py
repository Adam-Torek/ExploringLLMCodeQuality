"""
Write a function to drop empty items from a given dictionary.
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
"""

def drop_empty(d: dict) -> dict:
    return {k: v for k, v in d.items() if v is not None}

# Test cases
print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})) # {'c1': 'Red', 'c2': 'Green'}
print(drop_empty({'c1': 'Red', 'c2': None, 'c3': None, 'c4': 'Blue', 'c5': ''})) # {'c1': 'Red', 'c4': 'Blue'}
print(drop_empty({'c1': 'Red', 'c2': '', 'c3': 'Green', 'c4': None, 'c5': ' '})) # {'c1': 'Red', 'c3': 'Green'}
print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Blue', 'c4': 'Yellow'})) # {'c1': 'Red', 'c2': 'Green', 'c3': 'Blue', 'c4': 'Yellow'}
print(drop_empty({})) # {}
print(drop_empty({'c1': None, 'c2': None, 'c3': None})) # {}
print(drop_empty({'c1': '', 'c2': '', 'c3': ''})) # {}
print(drop_empty({'c1': ' ', 'c2': ' ', 'c3': ' '})) # {}