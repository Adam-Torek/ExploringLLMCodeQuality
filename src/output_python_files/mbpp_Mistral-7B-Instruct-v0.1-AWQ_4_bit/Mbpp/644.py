"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""

def reverse_Array_Upto_K(arr, k):
    """
    :param arr: array
    :param k: position upto which array should be reversed
    :return: reversed array
    """
    if k > len(arr) or k < 0:
        return []
    else:
        return arr[:k] + arr[k:]