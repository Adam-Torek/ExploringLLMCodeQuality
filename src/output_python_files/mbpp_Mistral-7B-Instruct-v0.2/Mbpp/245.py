"""
Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
"""
def max_sum(arr):
    n = len(arr)
    if n <= 2:
        return sum(arr)

    mid = n // 2
    left_sum = arr[:mid]
    right_sum = arr[mid:]

    left_max = max_sub_array_sum(left_sum)
    right_max = max_sub_array_sum(right_sum)

    # The maximum sum of a bitonic subsequence is the sum of the maximum increasing subsequence in the left half and the maximum decreasing subsequence in the right half
    return left_max + right_max

def max_sub_array_sum(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]

    dp = [arr[0]] * len(arr)
    for i in range(1, len(arr)):
        dp[i] = max(dp[i - 1], arr[i])

    return sum(dp)

assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
assert max_sum([-1, 1, 2, 3, 4, 5]) == 13
assert max_sum([-1, 1, 2, 3, 4, 5, 6]) == 15
assert max_sum([-1, 1, 2, 3, 4, 5, 6, 7]) == 21
assert max_sum([-1, 1, 2, 3, 4, 5, 6, 7, 8]) == 24
assert max_sum([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 31
assert max_sum([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 36
assert max_sum([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 42
assert max_sum([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 49
assert max_sum([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 56
assert max_sum([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 64
assert max_sum([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 72
assert max_sum([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 81
assert max_sum([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 90
assert max_sum([-