"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""


def reverse_Array_Upto_K(arr, k):
    """
    :param arr: array to be reversed
    :param k: position upto which array is to be reversed
    :return: reversed array
    """
    if k < 0 or k > len(arr):
        return "Invalid position"
    else:
        arr[0:k] = arr[0:k][::-1]
        return arr


if __name__ == '__main__':
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 1))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 6))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 7))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -1))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 0))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 10))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -10))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 100))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -100))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 1000))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -1000))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 10000))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -10000))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 100000))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -100000))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 1000000))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -1000000))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 10000000))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -10000000))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 100000000))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -100000000))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 1000000