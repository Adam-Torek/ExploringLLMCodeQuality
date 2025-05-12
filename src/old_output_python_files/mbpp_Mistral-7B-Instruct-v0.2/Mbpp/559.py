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
        while current_sum > sum:
            current_sum -= arr[start]
            start += 1
        if current_sum > max_sum:
            max_sum = current_sum
            end = i

    return max_sum if max_sum >= sum else 0

if __name__ == "__main__":
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10) == 9
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 5) == 4
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 12) == 11
    assert max_sub_array_sum([], 10) == 0
    assert max_sub_array_sum([1, 2, 3, 4, 5], 10) == 10
    assert max_sub_array_sum([1, 2, 3, 4, 5], 15) == 15
    assert max_sub_array_sum([1, 2, 3, 4, 5], 20) == 15
    assert max_sub_array_sum([1, 2, 3, 4, 5], 25) == 15
    assert max_sub_array_sum([1, 2, 3, 4, 5], 30) == 15
    assert max_sub_array_sum([1, 2, 3, 4, 5], 35) == 15
    assert max_sub_array_sum([1, 2, 3, 4, 5], 40) == 15
    assert max_sub_array_sum([1, 2, 3, 4, 5], 45) == 15
    assert max_sub_array_sum([1, 2, 3, 4, 5], 50) == 15
    assert max_sub_array_sum([1, 2, 3, 4, 5], 55) == 15
    assert max_sub_array_sum([1, 2, 3, 4, 5], 60) == 15
    assert max_sub_array_sum([1, 2, 3, 4, 5], 65) == 15
    assert max_sub_array_sum([1, 2, 3, 4, 5], 70) == 15
    assert max_sub_array_sum([1, 2, 3, 4, 5], 75) == 15
    assert max_sub_array_sum([1, 2, 3, 4, 5], 80) == 15
    assert max_sub_array_sum([1, 2, 3, 4, 5], 85) == 15
    assert max_sub_array_sum([1, 2, 3, 4, 5], 90) == 15
    assert max_sub_array_sum([1, 2, 3, 4, 5], 9