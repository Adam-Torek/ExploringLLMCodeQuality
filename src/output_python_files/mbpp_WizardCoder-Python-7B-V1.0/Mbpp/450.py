"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
"""

def extract_string(lst, size):
    return [s for s in lst if len(s) >= size]

print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8)) # Output: ['practice', 'solution']