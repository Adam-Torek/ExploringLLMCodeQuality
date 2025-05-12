"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""

def max_sub_array_sum_repeated(arr, k, n):
    if k > len(arr):
        return 0

    max_sum = float('-inf')
    current_sum = 0
    for i in range(k):
        current_sum += arr[i]
        max_sum = max(max_sum, current_sum)

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

# Test cases
print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3))  # Output: 30<|endoftext|>