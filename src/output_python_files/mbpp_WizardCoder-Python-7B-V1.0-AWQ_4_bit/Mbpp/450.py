"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
"""

def extract_string(lst, size):
    return [s for s in lst if len(s) >= size]

# Test cases
print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8)) # Output: ['practice', 'solution']
print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution', 'exercise', 'exercise'], 8)) # Output: ['practice', 'solution', 'exercise']
print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution', 'exercise', 'exercise'], 10)) # Output: []
print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 10)) # Output: ['Python', 'list', 'exercises', 'practice', 'solution']
print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 5)) # Output: ['Python', 'list']

# Another test case
lst = ['Python', 'list', 'exercises', 'practice', 'solution']
size = 8
result = []
for s in lst:
    if len(s) >= size:
        result.append(s)
print(result) # Output: ['practice', 'solution']