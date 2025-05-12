"""
Write a python function to set the left most unset bit.
assert set_left_most_unset_bit(10) == 14
"""


def set_left_most_unset_bit(n):
    """
    :param n: int
    :return: int
    """
    return n | (n + 1)


if __name__ == '__main__':
    print(set_left_most_unset_bit(10))
    print(set_left_most_unset_bit(100))
    print(set_left_most_unset_bit(1000))
    print(set_left_most_unset_bit(10000))
    print(set_left_most_unset_bit(100000))
    print(set_left_most_unset_bit(1000000))
    print(set_left_most_unset_bit(10000000))
    print(set_left_most_unset_bit(100000000))
    print(set_left_most_unset_bit(1000000000))
    print(set_left_most_unset_bit(10000000000))
    print(set_left_most_unset_bit(100000000000))
    print(set_left_most_unset_bit(1000000000000))
    print(set_left_most_unset_bit(10000000000000))
    print(set_left_most_unset_bit(100000000000000))
    print(set_left_most_unset_bit(1000000000000000))
    print(set_left_most_unset_bit(10000000000000000))
    print(set_left_most_unset_bit(100000000000000000))
    print(set_left_most_unset_bit(1000000000000000000))
    print(set_left_most_unset_bit(10000000000000000000))
    print(set_left_most_unset_bit(100000000000000000000))
    print(set_left_most_unset_bit(1000000000000000000000))
    print(set_left_most_unset_bit(10000000000000000000000))
    print(set_left_most_unset_bit(100000000000000000000000))
    print(set_left_most_unset_bit(1000000000000000000000000))
    print(set_left_most_unset_bit(10000000000000000000000000))
    print(set_left_most_unset_bit(100000000000000000000000000))
    print(set_left_most_unset_bit(1000000000000000000000000000))
    print(set_left_most_unset_bit(10000000000000000000000000000))
    print(set_left_most_unset_bit(1000000000000000000000000000