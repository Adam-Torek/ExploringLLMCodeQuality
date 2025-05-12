"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""

def max_sub_array_sum(arr, sum):
    """
    :param arr: list of integers
    :param sum: sum of largest contiguous sublist
    :return: sum of largest contiguous sublist
    """
    current_sum = 0
    max_sum = 0
    start = 0
    end = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
            start = end
            end = i

        if current_sum < 0:
            current_sum = 0
            end = i

    if max_sum >= sum:
        return max_sum
    else:
        return sum

if __name__ == "__main__":
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
    assert max_sub_array_sum([1, 2, 3, 4, 5], 10) == 10
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 4) == 7
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 5) == 11
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 12) == 11
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 15) == 15
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 16) == 16
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 17) == 17
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 18) == 18
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 19) == 19
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 20) == 20
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 21) == 21
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 22) == 22
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 23) == 23
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 24) == 24
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 25) == 25
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 26) == 26
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 27) == 27
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 28) == 28
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 29) == 29
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 30) == 30
    assert max_sub_array_sum([-1, -2, 3, 5, 6], 31) == 31
    assert max_sub_array_sum([