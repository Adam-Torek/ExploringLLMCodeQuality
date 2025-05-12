"""
Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
"""
def sample_names(names_list):
    sum = 0
    for name in names_list:
        if name[0].isupper():
            sum += len(name)
    return sum

assert sample_names(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']) == 16
print(sample_names(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))