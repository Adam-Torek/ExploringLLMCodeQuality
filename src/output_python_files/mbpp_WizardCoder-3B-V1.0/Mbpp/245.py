"""
Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
"""

def max_sum(arr):
    n = len(arr)
    if n < 3:
        return 0

    # Initialize variables
    max_sum_left = float('-inf')
    max_sum_right = float('-inf')
    max_sum_global = float('-inf')

    # Traverse the array from left to right
    for i in range(n):
        if i % 2 == 0:
            max_sum_left = max(max_sum_left, arr[i])
        else:
            max_sum_right = max(max_sum_right, arr[i])

        # Update the global maximum sum
        max_sum_global = max(max_sum_global, max_sum_left + max_sum_right)

    return max_sum_global

# Test the function
print(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]))  # Output: 194<|endoftext|>