"""
Write a function to find the ration of positive numbers in an array of integers.
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
"""

def positive_count(arr):
    """
    Count the number of positive numbers in an array of integers
    :param arr: array of integers
    :return: float
    """
    count = 0
    for i in arr:
        if i > 0:
            count += 1
    return count/len(arr)

assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54