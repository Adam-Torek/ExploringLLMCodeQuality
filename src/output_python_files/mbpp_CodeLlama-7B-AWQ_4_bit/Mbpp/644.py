"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""


def reverse_Array_Upto_K(arr, k):
    """
    :param arr: array
    :param k: position
    :return: reversed array
    """
    if k < 0 or k > len(arr) - 1:
        return arr
    else:
        for i in range(k):
            arr[i], arr[k] = arr[k], arr[i]
        return arr


if __name__ == '__main__':
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 3))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 2))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 1))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 0))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -1))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -2))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -3))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -4))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -5))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -6))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -7))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -8))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -9))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -10))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -11))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -12))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -13))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -14))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -15))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -16))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -17))
    print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], -18))
    print(