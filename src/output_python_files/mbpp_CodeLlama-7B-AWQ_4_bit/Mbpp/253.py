"""
Write a python function that returns the number of integer elements in a given list.
assert count_integer([1,2,'abc',1.2]) == 2
"""


def count_integer(lst):
    return sum(1 for i in lst if isinstance(i, int))


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
    print(count_integer([1, 2, 'abc', 1.2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,