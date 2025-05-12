"""
Write a function to find the ration of positive numbers in an array of integers.
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
"""
def positive_count(arr):
    """
    Function to find the ratio of positive numbers in an array of integers.
    :param arr: list of integers
    :return: float
    """
    count_positive = sum(1 for num in arr if num > 0)
    total_numbers = len(arr)
    ratio = count_positive / total_numbers
    return ratio

assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.54