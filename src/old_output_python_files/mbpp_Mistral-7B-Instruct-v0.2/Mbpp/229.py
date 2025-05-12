"""
Write a function that takes in an array and an integer n, and re-arranges the first n elements of the given array so that all negative elements appear before positive ones, and where the relative order among negative and positive elements is preserved.
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
"""
def re_arrange_array(arr, n):
    """
    :param arr: list of integers
    :param n: integer
    :return: list of integers with negative elements first and positive elements after
    """
    negative_index = 0
    positive_index = n
    negative_elements = []
    positive_elements = []

    while positive_index < len(arr):
        if arr[positive_index] < 0:
            negative_elements.append(arr[positive_index])
            negative_index += 1
        else:
            positive_elements.append(arr[positive_index])
        positive_index += 1

    result = []
    result += negative_elements[:negative_index]
    result += positive_elements

    return result

# Test cases
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
assert re_arrange_array([-1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == [3, 4, 5, 6, 7, 8, 2, 9, 1]
assert re_arrange_array([-1, -2, 3, 4, 5, 6, 7, 8, 9], 9) == [-2, -1, 3, 4, 5, 6, 7, 8, 9]
assert re_arrange_array([], 0) == []
assert re_arrange_array([1], 1) == [1]
assert re_arrange_array([-1], 1) == [-1]
assert re_arrange_array([-1, 1], 2) == [-1, 1]
assert re_arrange_array([1, -1], 2) == [1, -1]
assert re_arrange_array([-1, 1, 1], 3) == [-1, 1, 1]
assert re_arrange_array([1, -1, 1], 3) == [1, 1, -1]