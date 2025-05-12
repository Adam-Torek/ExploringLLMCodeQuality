"""
Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
"""


def sample_nam(names):
    """
    :param names: list of names
    :return: sum of the length of the names after removing the names that start with a lowercase letter
    """
    return sum(len(name) for name in names if name[0].isupper())


if __name__ == '__main__':
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'sally']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'sally', 'sally']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'sally', 'sally', 'sally']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'sally', 'sally', 'sally', 'sally']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'sally', 'sally', 'sally', 'sally', 'sally']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally', 'sally']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'sally', 'sally', 'sally', 'sally