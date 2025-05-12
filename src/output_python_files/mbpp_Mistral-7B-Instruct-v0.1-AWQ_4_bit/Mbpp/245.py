"""
Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
"""

def max_sum(arr):
    n = len(arr)
    if n == 0:
        return 0
    elif n == 1:
        return arr[0]
    elif n == 2:
        return max(arr[0], arr[1])
    else:
        mid = n // 2
        left = max_sum(arr[:mid])
        right = max_sum(arr[mid:])
        return max(left, right) + max(arr[mid-1], arr[mid])

# test
arr = [1, 15, 51, 45, 33, 100, 12, 18, 9]
print(max_sum(arr))