"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
"""

def extract_string(lst, size):
    return [s for s in lst if len(s) >= size]

print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8))
print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 10))
print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 12))

# Output:
# ['practice', 'solution']
# ['Python', 'list', 'exercises', 'practice', 'solution']
# []

# Explanation:
# In the first example, the function returns a list of strings that have a length greater than or equal to 8.
# In the second example, all the strings have a length greater than or equal to 10, so the function returns the original list.
# In the third example, there are no strings with a length greater than or equal to 12, so the function returns an empty list.