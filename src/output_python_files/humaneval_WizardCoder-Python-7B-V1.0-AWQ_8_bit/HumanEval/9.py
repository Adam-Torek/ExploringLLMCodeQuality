from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = [numbers[0]]
    for i in range(1, len(numbers)):
        max_so_far.append(max(numbers[i], max_so_far[-1]))
    return max_so_far

def max_sum_subarray(arr: List[int]) -> Tuple[int, int, int]:
    """
    Given an array of integers, find the maximum sum of a subarray in O(n) time complexity.
    Returns a tuple (max_sum, start_index, end_index)
    """
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    end = 0
    max_start = 0
    max_end = 0
    temp_start = 0

    for i, num in enumerate(arr):
        if current_sum <= 0:
            current_sum = num
            temp_start = i
        else:
            current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum
            max_start = temp_start
            max_end = i

    return max_sum, max_start, max_end

def max_subarray_sum(arr: List[int]) -> int:
    """
    Given an array of integers, find the maximum sum of a subarray in O(n) time complexity.
    """
    max_sum, _, _ = max_sum_subarray(arr)
    return max_sum

def max_subarray_sum_with_negative(arr: List[int]) -> int:
    """
    Given an array of integers, find the maximum sum of a subarray with at least one negative element in it.
    """
    max_sum = float('-inf')
    current_sum = 0
    max_sum_with_negative = float('-inf')

    for num in arr:
        if current_sum < 0:
            current_sum = 0
        current_sum += num
        max_sum = max(max_sum, current_sum)
        max_sum_with_negative = max(max_sum_with_negative, current_sum)

    return max_sum_with_negative

def max_subarray_sum_with_negative_rolling(arr: List[int]) -> int:
    """
    Given an array of integers, find the maximum sum of a subarray with at least one negative element in it.
    """
    max_sum = float('-inf')
    current_sum = 0
    max_sum_with_negative = float('-inf')
    max_sum_with_negative_rolling = float('-inf')

    for num in arr:
        if current_sum < 0:
            current_sum = 0
        current_sum += num
        max_sum = max(max_sum, current_sum)
        max_sum_with_negative = max(max_sum_with_negative, current_sum)
        max_sum_with_negative_rolling = max(max_sum_with_negative_rolling, max_sum_with_negative)

    return max_sum_with_negative_rolling

def max_subarray_sum_with_negative_rolling_improved(arr: List[int]) -> int:
    """
    Given an array of integers, find the maximum sum of a subarray with at least one negative element in it.
    """
    max_sum = float('-inf')
    current_sum = 0
    max_sum_with_negative = float('-inf')
    max_sum_with_negative_rolling = float('-inf')
    max_sum_with_negative_temp = float('-inf')

    for num in arr:
        if current_sum < 0:
            current_sum = 0
        current_sum += num