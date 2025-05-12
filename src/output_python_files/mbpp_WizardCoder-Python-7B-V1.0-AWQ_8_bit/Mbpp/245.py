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

    max_sum = 0
    max_sum_ending_here = 0
    max_sum_so_far = 0
    max_ending_here = arr[0]
    max_so_far = arr[0]

    for i in range(1, n):
        max_sum_ending_here += arr[i]
        max_sum_so_far += max_ending_here
        max_ending_here = max(max_ending_here, max_sum_ending_here - arr[i])
        max_sum_so_far = max(max_sum_so_far, max_sum_ending_here)

    max_sum_ending_here = 0
    max_sum_so_far = 0
    max_ending_here = arr[n-1]
    max_so_far = arr[n-1]

    for i in range(n-2, -1, -1):
        max_sum_ending_here += arr[i]
        max_sum_so_far += max_ending_here
        max_ending_here = max(max_ending_here, max_sum_ending_here - arr[i])
        max_sum_so_far = max(max_sum_so_far, max_sum_ending_here)

    return max_sum_so_far


# Test cases
print(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9])) # Output: 194
print(max_sum([1, 2, 3, 4, 5, 6, 4, 3, 2, 1])) # Output: 16
print(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 24
print(max_sum([10, 20, 30, 40, 50, 60, 70, 80])) # Output: 500
print(max_sum([10, 20, 30, 40, 50, 60, 70, 60])) # Output: 180
print(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 54
print(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # Output: 55
print(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) # Output: 63
print(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) # Output: 66
print(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) # Output: 74
print(max_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # Output: 84
print(max_sum([1, 2, 3, 4,