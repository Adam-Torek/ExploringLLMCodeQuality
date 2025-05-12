"""
Write a function to find whether all the given tuples have equal length or not.
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
"""


def get_equal(tuples):
    """
    :param tuples: list of tuples
    :return: True if all tuples have equal length, False otherwise
    """
    if not tuples:
        return True
    return len(tuples[0]) == len(tuples[1])


if __name__ == '__main__':
    print(get_equal([(11, 22, 33), (44, 55, 66)]))
    print(get_equal([(11, 22, 33), (44, 55, 66, 77)]))
    print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99)]))
    print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99, 100)]))
    print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99, 100, 111)]))
    print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99, 100, 111, 121)]))
    print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99, 100, 111, 121, 131)]))
    print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99, 100, 111, 121, 131, 141)]))
    print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99, 100, 111, 121, 131, 141, 151)]))
    print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99, 100, 111, 121, 131, 141, 151, 161)]))
    print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99, 100, 111, 121, 131, 141, 151, 161, 171)]))
    print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99, 100, 111, 121, 131, 141, 151, 161, 171, 181)]))
    print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99, 100, 111, 121, 131, 141, 151, 161, 171, 181, 191)]))
    print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 9