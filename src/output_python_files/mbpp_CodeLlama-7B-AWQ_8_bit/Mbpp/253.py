"""
Write a python function that returns the number of integer elements in a given list.
assert count_integer([1,2,'abc',1.2]) == 2
"""


def count_integer(lst):
    """
    :param lst: list of elements
    :return: number of integer elements in the list
    """
    return len([x for x in lst if isinstance(x, int)])


if __name__ == '__main__':
    print(count_integer([1, 2, 'abc', 1.2]))
    print(count_integer([1, 2, 'abc', 1.2, 1]))
    print(count_integer([1, 2, 'abc', 1.2, 1, 1]))
    print(count_integer([1, 2, 'abc', 1.2, 1, 1, 1]))
    print(count_integer([1, 2, 'abc', 1.2, 1, 1, 1, 1]))
    print(count_integer([1, 2, 'abc', 1.2, 1, 1, 1, 1, 1]))
    print(count_integer([1, 2, 'abc', 1.2, 1, 1, 1, 1, 1, 1]))
    print(count_integer([1, 2, 'abc', 1.2, 1, 1, 1, 1, 1, 1, 1]))
    print(count_integer([1, 2, 'abc', 1.2, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(count_integer([1, 2, 'abc', 1.2, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(count_integer([1, 2, 'abc', 1.2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(count_integer([1, 2, 'abc', 1.2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(count_integer([1, 2, 'abc', 1.2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(count_integer([1, 2, 'abc', 1.2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(count_integer([1, 2, 'abc', 1.2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(count_integer([1, 2, 'abc', 1.2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(count_integer([1, 2, 'abc', 1.2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(count_integer([1, 2, 'abc', 1.2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(count_integer([1, 2, 'abc', 1.2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))