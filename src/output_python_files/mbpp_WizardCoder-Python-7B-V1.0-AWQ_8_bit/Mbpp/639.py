"""
Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
"""

def sample_nam(names):
    total_length = 0
    for name in names:
        if name[0].isupper():
            total_length += len(name)
    return total_length

print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])) # Output: 16

# Another way to solve this problem is to use a list comprehension to filter out the names that start with a lowercase letter and then use the sum() function to add up the lengths of the remaining names.

def sample_nam(names):
    return sum(len(name) for name in names if name[0].isupper())

print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])) # Output: 16

# This solution is more concise and easier to read.