"""
Write a function to drop empty items from a given dictionary.
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
"""

def drop_empty(d):
    return {k: v for k, v in d.items() if v is not None}

print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})) # {'c1': 'Red', 'c2': 'Green'}
print(drop_empty({'c1': 'Red', 'c2': None, 'c3': None, 'c4': 'Blue', 'c5': ''})) # {'c1': 'Red', 'c4': 'Blue'}
print(drop_empty({'c1': 'Red', 'c2': '', 'c3': 'Green', 'c4': None, 'c5': ''})) # {'c1': 'Red', 'c3': 'Green'}
print(drop_empty({'c1': 'Red', 'c2': '', 'c3': 'Green', 'c4': None, 'c5': 'Yellow', 'c6': None})) # {'c1': 'Red', 'c2': '', 'c3': 'Green', 'c5': 'Yellow'}
print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': 'Blue', 'c5': 'Yellow', 'c6': None})) # {'c1': 'Red', 'c2': 'Green', 'c4': 'Blue', 'c5': 'Yellow'}
print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Yellow', 'c4': 'Blue', 'c5': 'Yellow', 'c6': None})) # {'c1': 'Red', 'c2': 'Green', 'c3': 'Yellow', 'c4': 'Blue', 'c5': 'Yellow'}
print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Yellow', 'c4': 'Blue', 'c5': 'Yellow', 'c6': None, 'c7': None})) # {'c1': 'Red', 'c2': 'Green', 'c3': 'Yellow', 'c4': 'Blue', 'c5': 'Yellow'}
print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Yellow', 'c4': 'Blue', 'c5': 'Yellow', 'c6': None, 'c7': None, 'c8': None})) # {'c1': 'Red', 'c2': 'Green', 'c3': 'Yellow', 'c4': 'Blue', 'c5': 'Yellow'}
print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Yellow', 'c4': 'Blue', 'c5': 'Yellow', 'c6': None, 'c7': None, 'c8': None, 'c9': None})) # {'c1': 'Red', 'c2': 'Green', 'c3': 'Yellow', 'c4': 'Blue', 'c5': 'Yellow'}
print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Yellow', 'c4': 'Blue', 'c5': 'Yellow', 'c6': None, 'c7': None, 'c8': None, 'c9': None, 'c10': None})) # {'c1': 'Red', 'c2': 'Green', 'c3': 'Yellow', 'c4': 'Blue', 'c5': 'Yellow'}
print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Yellow', 'c4': 'Blue', 'c5': 'Y