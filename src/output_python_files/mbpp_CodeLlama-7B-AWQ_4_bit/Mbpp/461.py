"""
Write a python function to count the upper case characters in a given string.
assert upper_ctr('PYthon') == 1
"""


def upper_ctr(string):
    """
    :param string: string
    :return: int
    """
    return sum(1 for char in string if char.isupper())


if __name__ == '__main__':
    print(upper_ctr('PYthon'))
    print(upper_ctr('Python'))
    print(upper_ctr('Python123'))
    print(upper_ctr('Python1234'))
    print(upper_ctr('Python12345'))
    print(upper_ctr('Python123456'))
    print(upper_ctr('Python1234567'))
    print(upper_ctr('Python12345678'))
    print(upper_ctr('Python123456789'))
    print(upper_ctr('Python1234567890'))
    print(upper_ctr('Python12345678901'))
    print(upper_ctr('Python123456789012'))
    print(upper_ctr('Python1234567890123'))
    print(upper_ctr('Python12345678901234'))
    print(upper_ctr('Python123456789012345'))
    print(upper_ctr('Python1234567890123456'))
    print(upper_ctr('Python12345678901234567'))
    print(upper_ctr('Python123456789012345678'))
    print(upper_ctr('Python1234567890123456789'))
    print(upper_ctr('Python12345678901234567890'))
    print(upper_ctr('Python123456789012345678901'))
    print(upper_ctr('Python1234567890123456789012'))
    print(upper_ctr('Python12345678901234567890123'))
    print(upper_ctr('Python123456789012345678901234'))
    print(upper_ctr('Python1234567890123456789012345'))
    print(upper_ctr('Python12345678901234567890123456'))
    print(upper_ctr('Python123456789012345678901234567'))
    print(upper_ctr('Python1234567890123456789012345678'))
    print(upper_ctr('Python12345678901234567890123456789'))
    print(upper_ctr('Python123456789012345678901234567890'))
    print(upper_ctr('Python1234567890123456789012345678901'))
    print(upper_ctr('Python12345678901234567890123456789012'))
    print(upper_ctr('Python123456789012345678901234567890123'))
    print(upper_ctr('Python12345