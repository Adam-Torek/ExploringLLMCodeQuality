from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = [numbers[0]]
    for i in range(1, len(numbers)):
        max_so_far.append(max(numbers[i], max_so_far[i-1]))
    return max_so_far

def max_sum_subarray(arr: List[int]) -> Tuple[int, int, int]:
    """ Find the maximum sum of a subarray in a given list of integers.
    Return a tuple with the sum, starting index and ending index of the subarray.
    >>> max_sum_subarray([-2, 1, -3, 4, -1, -2, 1, 5, -3])
    (7, 1, 5)
    """
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    end = 0
    temp_start = 0
    for i, num in enumerate(arr):
        if current_sum + num > num:
            current_sum += num
        else:
            current_sum = num
            temp_start = i
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    return max_sum, start, end

def max_sum_subarray_dp(arr: List[int]) -> Tuple[int, int, int]:
    """ Find the maximum sum of a subarray in a given list of integers using dynamic programming.
    Return a tuple with the sum, starting index and ending index of the subarray.
    >>> max_sum_subarray_dp([-2, 1, -3, 4, -1, -2, 1, 5, -3])
    (7, 1, 5)
    """
    n = len(arr)
    max_sum = arr[0]
    max_ending_here = arr[0]
    start = 0
    end = 0
    temp_start = 0
    for i in range(1, n):
        if max_ending_here + arr[i] > arr[i]:
            max_ending_here += arr[i]
        else:
            max_ending_here = arr[i]
            temp_start = i
        if max_ending_here > max_sum:
            max_sum = max_ending_here
            end = i
    return max_sum, start, end

def max_sum_subarray_divide_conquer(arr: List[int]) -> Tuple[int, int, int]:
    """ Find the maximum sum of a subarray in a given list of integers using divide and conquer approach.
    Return a tuple with the sum, starting index and ending index of the subarray.
    >>> max_sum_subarray_divide_conquer([-2, 1, -3, 4, -1, -2, 1, 5, -3])
    (7, 1, 5)
    """
    def max_sum_subarray_rec(arr: List[int], start: int, end: int) -> Tuple[int, int, int]:
        if start == end:
            return arr[start], start, end
        mid = (start + end) // 2
        left_sum, left_start, left_end = max_sum_subarray_rec(arr, start, mid)
        right_sum, right_start, right_end = max_sum_subarray_rec(arr, mid+1, end)
        cross_sum, cross_start, cross_end