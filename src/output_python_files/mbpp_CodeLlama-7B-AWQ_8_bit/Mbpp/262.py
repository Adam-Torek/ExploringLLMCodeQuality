"""
Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple.
assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
"""


def split_two_parts(lst, L):
    """
    :param lst: list
    :param L: int
    :return: tuple
    """
    return lst[:L], lst[L:]


if __name__ == '__main__':
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 3))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 4))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 5))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 6))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 7))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 8))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 9))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 10))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 11))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 12))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 13))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 14))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 15))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 16))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 17))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 18))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 19))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 20))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 21))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 22))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 23))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 24))
    print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 25))
    print(split_two_parts([1, 1,