"""
Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
"""

def sum_name_length(sample_names):
    """
    This function takes a list of names as an input and returns the sum of the length of the names after removing the names that start with a lowercase letter.
    """
    sum_length = 0
    for name in sample_names:
        if name[0].isupper():
            sum_length += len(name)
    return sum_length

sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
assert sum_name_length(sample_names)==16