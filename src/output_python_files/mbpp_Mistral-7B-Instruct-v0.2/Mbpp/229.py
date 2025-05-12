"""
Write a function that takes in an array and an integer n, and re-arranges the first n elements of the given array so that all negative elements appear before positive ones, and where the relative order among negative and positive elements is preserved.
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
"""
def re_arrange_array(arr, n):
    """
    :param arr: list of integers
    :param n: integer
    :return: list of integers with negative elements before positive ones
    """
    negative_index = 0
    positive_index = n
    negative_elements = []
    positive_elements = []

    while len(negative_elements) < n:
        if arr[positive_index] < 0:
            negative_elements.append(arr.pop(positive_index))
        else:
            positive_elements.append(arr.pop(positive_index))
        positive_index += 1

    return negative_elements + positive_elements

# Test cases
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
assert re_arrange_array([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert re_arrange_array([-1, -2, -3, 4, 5, 6, 7, 8, 9], 5) == [-1, -2, 4, 5, 6]
assert re_arrange_array([], 0) == []
assert re_arrange_array([-1], 1) == [-1]
assert re_arrange_array([-1, 1], 1) == [1, -1]
assert re_arrange_array([-1, 1], 2) == [-1, 1]
assert re_arrange_array([], 1) == []
assert re_arrange_array([1], 1) == [1]
assert re_arrange_array([1, 1], 1) == [1, 1]
assert re_arrange_array([1, 1], 2) == [1, 1]
assert re_arrange_array([1, 1], 3) == [1, 1, 1]
assert re_arrange_array([1, 1], 4) == [1, 1, 1, 1]
assert re_arrange_array([1, 1], 5) == [1, 1, 1, 1, 1]
assert re_arrange_array([1, 1], 6) == [1, 1, 1, 1, 1, 1]
assert re_arrange_array([1, 1], 7) == [1, 1, 1, 1, 1, 1, 1]
assert re_arrange_array([1, 1], 8) == [1, 1, 1, 1, 1, 1, 1, 1]
assert re_arrange_array([1, 1], 9) == [1, 1, 1, 1, 1, 1, 1, 1, 1]
assert re_arrange_array([1, 1], 10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert re_arrange_array([1, 1], 11) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert re_arrange_array([1, 1], 12) == [1, 1, 1,