"""
Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
"""
def max_sum(arr):
    n = len(arr)
    if n <= 1:
        return arr[0]

    mid = n // 2
    left_sum = max_subsequence(arr[:mid])
    right_sum = max_subsequence(arr[mid:])

    left_tail = arr[:mid][-1] if mid > 0 else 0
    right_tail = arr[mid:][0] if mid < n else 0

    return max(left_sum, right_sum, left_sum + right_sum + left_tail + right_tail)

def max_subsequence(arr):
    if len(arr) <= 1:
        return arr[0]

    i = 0
    j = 1
    max_sum = arr[0]

    while j < len(arr):
        if arr[j] > arr[i]:
            i = j
        j += 1

    return max_sum + max_subsequence(arr[i+1:])

assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
assert max_sum([-1, 1, 1, 1, 1, 1, 1, 1, 1]) == 6
assert max_sum([-1, 1, 1, 1, 1, 1, 1, 1, -1]) == 5
assert max_sum([-1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 11
assert max_sum([-1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1]) == 10
assert max_sum([-1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1]) == 12
assert max_sum([-1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1]) == 15
assert max_sum([-1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1]) == 18
assert max_sum([-1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1]) == 23
assert max_sum([-1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1]) == 28
assert max_sum([-1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1]) == 33
assert max_sum([-1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1]) == 40
assert max_sum([-1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 48
assert max_sum([-1, 1, 1, 1, 1, 1, 1, 1