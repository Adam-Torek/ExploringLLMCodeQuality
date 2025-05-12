"""
Write a function to merge three dictionaries into a single dictionary.
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
"""

def merge_dictionaries_three(dict1, dict2, dict3):
    merged_dict = {}
    for key in dict1:
        if key in dict2 and dict1[key] != dict2[key]:
            merged_dict[key] = dict1[key]
        else:
            merged_dict[key] = dict2[key]
    for key in dict3:
        if key in merged_dict:
            merged_dict[key] = dict3[key]
        else:
            merged_dict[key] = dict3[key]
    return merged_dict

assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}