"""
Write a python function to count the upper case characters in a given string.
assert upper_ctr('PYthon') == 1
"""


def upper_ctr(string):
    """
    :param string: string
    :return: int
    """
    return sum(1 for c in string if c.isupper())


if __name__ == '__main__':
    print(upper_ctr('PYthon'))
    print(upper_ctr('Python'))
    print(upper_ctr('Pyth