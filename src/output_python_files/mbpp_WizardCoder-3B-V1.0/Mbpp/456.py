"""
Write a function to reverse each string in a given list of string values.
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
"""

def reverse_string_list(lst):
    return [x[::-1] for x in lst]

# Test the function
print(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']))<|endoftext|>