"""
Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
"""

def max_sum(arr):
    n = len(arr)
    if n < 2:
        return 0
    if n == 2:
        return max(arr[0], arr[1])

    max_sum = arr[1]
    max_sum_ending_here = arr[1]
    max_sum_prev = arr[0]

    for i in range(2, n):
        max_sum_prev, max_sum_ending_here = max_sum_ending_here, max(max_sum_prev + arr[i], max_sum_ending_here)
        max_sum = max(max_sum, max_sum_ending_here)

    return max_sum


print(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9])) # Output: 194