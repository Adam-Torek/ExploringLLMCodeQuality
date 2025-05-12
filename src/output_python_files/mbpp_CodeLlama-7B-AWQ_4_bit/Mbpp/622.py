"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""


def get_median(list1, list2, size):
    """
    :param list1: sorted list
    :param list2: sorted list
    :param size: size of the list
    :return: median of the two lists
    """
    if size % 2 == 0:
        return (list1[size // 2 - 1] + list1[size // 2]) / 2
    else:
        return list1[size // 2]


if __name__ == '__main__':
    print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5))
    print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 6))
    print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 7))
    print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 8))
    print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 9))
    print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 10))
    print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 11))
    print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 12))
    print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 13))
    print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 14))
    print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 15))
    print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 16))
    print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 17))
    print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 18))
    print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 19))
    print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 20))