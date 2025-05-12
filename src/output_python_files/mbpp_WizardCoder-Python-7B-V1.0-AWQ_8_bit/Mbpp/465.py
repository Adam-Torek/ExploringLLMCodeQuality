"""
Write a function to drop empty items from a given dictionary.
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
"""

def drop_empty(d: dict) -> dict:
    return {k: v for k, v in d.items() if v is not None}

# Test cases
print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})) # {'c1': 'Red', 'c2': 'Green'}
print(drop_empty({'c1': 'Red', 'c2': None, 'c3': None, 'c4': 'Blue'})) # {'c1': 'Red', 'c4': 'Blue'}
print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Yellow', 'c4': None})) # {'c1': 'Red', 'c2': 'Green', 'c3': 'Yellow'}
print(drop_empty({'c1': 'Red', 'c2': None, 'c3': None, 'c4': None})) # {}
print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Yellow', 'c4': 'Blue', 'c5': 'Violet'})) # {'c1': 'Red', 'c2': 'Green', 'c3': 'Yellow', 'c4': 'Blue', 'c5': 'Violet'}
print(drop_empty({})) # {}

# Test cases with empty dictionary
print(drop_empty({})) # {}

# Test cases with nested dictionaries
print(drop_empty({'c1': 'Red', 'c2': {'c3': None, 'c4': 'Green'}, 'c5': {'c6': {'c7': None, 'c8': 'Yellow'}}}) # {'c1': 'Red', 'c2': {'c4': 'Green'}, 'c5': {'c6': {'c8': 'Yellow'}}
print(drop_empty({'c1': 'Red', 'c2': {'c3': None, 'c4': {'c5': None, 'c6': 'Green'}, 'c7': 'Yellow', 'c8': {'c9': None, 'c10': 'Blue'}}}) # {'c1': 'Red', 'c2': {'c4': {'c6': 'Green'}, 'c7': 'Yellow', 'c8': {'c10': 'Blue'}
print(drop_empty({'c1': 'Red', 'c2': {'c3': None, 'c4': {'c5': None, 'c6': {'c7': None, 'c8': {'c9': None, 'c10': None}, 'c11': 'Green'}}}) # {'c1': 'Red', 'c2': {'c4': {'c6': {'c11': 'Green'}
print(drop_empty({'c1': 'Red', 'c2': {'c3': None, 'c4': {'c5': None, 'c6': {'c7': {'c8': None, 'c9': None, 'c10': 'Green'}}}) # {'c1': 'Red', 'c2': {'c4': {'c6': {'c10': 'Green'}
print(drop_empty({'c1': 'Red', 'c2': {'c3': None, 'c4': {'c5': None, 'c6': {'c7': {'c8': {'c9': None, 'c10': None, 'c11': 'Green'}}}) # {'c1': 'Red', 'c2': {'c4': {'c6': {'c7': {'c11': 'Green'}

# Test cases with empty nested dictionaries
print(drop_empty({'c1': 'Red', 'c2': {}, 'c3': {'c4': {}, 'c5': 'Green'})) # {'c1': 'Red', 'c3': {'c5': 'Green'}
print(drop_empty({'c1': 'Red', 'c2': {'c3': {}, 'c4': {'c5': {'c6': {}}}) # {'c1': 'Red', 'c2': {'c4': {'c5': {