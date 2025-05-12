"""
Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
"""


def sample_nam(names):
    """
    :param names: list of names
    :return: sum of the length of the names of a given list of names after removing the names that start with a lowercase letter
    """
    return sum(len(name) for name in names if name[0].isupper())


if __name__ == '__main__':
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'john']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'john', 'jane']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'john', 'jane', 'jim']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'john', 'jane', 'jim', 'johnny']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'john', 'jane', 'jim', 'johnny', 'john']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'john', 'jane', 'jim', 'johnny', 'john', 'johnny']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'john', 'jane', 'jim', 'johnny', 'john', 'johnny', 'john']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'john', 'jane', 'jim', 'johnny', 'john', 'johnny', 'john', 'johnny']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'john', 'jane', 'jim', 'johnny', 'john', 'johnny', 'john', 'johnny', 'john']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'john', 'jane', 'jim', 'johnny', 'john', 'johnny', 'john', 'johnny', 'john', 'johnny']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'john', 'jane', 'jim', 'johnny', 'john', 'johnny', 'john', 'johnny', 'john', 'johnny', 'john']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'john', 'jane', 'jim', 'johnny', 'john', 'johnny', 'john', 'johnny', 'john', 'johnny', 'john', 'johnny']))
    print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith', 'john', 'jane', 'jim', 'johnny', 'john', 'johnny', 'john', 'johnny', 'john', 'johnny', 'john', 'johnny', 'john']))
    print(sample_nam(['sally', '