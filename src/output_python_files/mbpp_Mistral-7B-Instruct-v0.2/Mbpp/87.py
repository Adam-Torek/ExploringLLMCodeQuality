"""
Write a function to merge three dictionaries into a single dictionary.
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
"""
def merge_dictionaries_three(*args):
    result = {}
    for dictionary in args:
        for key, value in dictionary.items():
            if key not in result:
                result[key] = value
            elif result[key] != value:
                raise ValueError(f"Key {key} already exists with different values: {result[key]}, {value}")
    return result

# Test case
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}

# Test case with different values for the same key
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "R": "Blue", "B": "Black" })=={'B': 'Black', 'R': 'Blue'}

# Test case with empty dictionary
assert merge_dictionaries_three({}, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'G': 'Green', 'W': 'White', 'O': 'Orange', 'B': 'Black'}

# Test case with one dictionary
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" })=={'R': 'Red', 'B': 'Black', 'P': 'Pink'}