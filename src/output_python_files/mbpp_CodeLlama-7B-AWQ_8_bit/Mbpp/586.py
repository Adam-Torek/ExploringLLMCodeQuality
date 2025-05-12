"""
Write a python function to split a list at the nth eelment and add the first part to the end.
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
"""


def split_Arr(arr, n):
    """
    :param arr: list
    :param n: int
    :return: list
    """
    return arr[n:] + arr[:n]


if __name__ == '__main__':
    print(split_Arr([12, 10, 5, 6, 52, 36], 2))
    print(split_Arr([12, 10, 5, 6, 52, 36], 3))
    print(split_Arr([12, 10, 5, 6, 52, 36], 4))
    print(split_Arr([12, 10, 5, 6, 52, 36], 5))
    print(split_Arr([12, 10, 5, 6, 52, 36], 6))
    print(split_Arr([12, 10, 5, 6, 52, 36], 7))
    print(split_Arr([12, 10, 5, 6, 52, 36], 8))
    print(split_Arr([12, 10, 5, 6, 52, 36], 9))
    print(split_Arr([12, 10, 5, 6, 52, 36], 10))
    print(split_Arr([12, 10, 5, 6, 52, 36], 11))
    print(split_Arr([12, 10, 5, 6, 52, 36], 12))
    print(split_Arr([12, 10, 5, 6, 52, 36], 13))
    print(split_Arr([12, 10, 5, 6, 52, 36], 14))
    print(split_Arr([12, 10, 5, 6, 52, 36], 15))
    print(split_Arr([12, 10, 5, 6, 52, 36], 16))
    print(split_Arr([12, 10, 5, 6, 52, 36], 17))
    print(split_Arr([12, 10, 5, 6, 52, 36], 18))
    print(split_Arr([12, 10, 5, 6, 52, 36], 19))
    print(split_Arr([12, 10, 5, 6, 52, 36], 20))
    print(split_Arr([12, 10, 5, 6, 52, 36], 21))
    print(split_Arr([12, 10, 5, 6, 52, 36], 22))
    print(split_Arr([12, 10, 5, 6, 52, 36], 23))
    print(split_Arr([12, 10, 5, 6, 52, 36], 24))
    print(split_Arr([12, 10, 5, 6, 52, 36], 25))
    print(split_Arr([12, 10, 5, 6, 52, 36], 26))
    print(split_Arr([12, 10, 5, 6, 52, 36], 27))
    print(split_Arr([12, 10, 5, 6, 52, 36], 28))
    print(split_