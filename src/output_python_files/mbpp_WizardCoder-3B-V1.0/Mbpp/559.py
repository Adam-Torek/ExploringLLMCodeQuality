"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""

def max_sub_array_sum(arr, n):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(n):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum

# Test cases
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8))  # Output: 7<|endoftext|>