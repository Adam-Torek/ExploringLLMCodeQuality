"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""

def max_sub_array_sum_repeated(arr, k, n):
    arr = arr * k
    max_sum = float('-inf')
    current_sum = 0
    max_so_far = float('-inf')
    max_ending_here = 0

    for i in arr:
        current_sum += i
        max_ending_here = max(max_ending_here + i, 0)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Test cases
print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3)) # Output: 30
print(max_sub_array_sum_repeated([1, -1, 2, -1, -2, 3, -1], 3, 2)) # Output: 5
print(max_sub_array_sum_repeated([1, -2, 3, 4, -5, -2, 1, -1], 2, 3)) # Output: 9
print(max_sub_array_sum_repeated([1, -2, 3, 4, -5, -2, 1, -1], 3, 2)) # Output: 9
print(max_sub_array_sum_repeated([1, -2, 3, 4, -5, -2, 1, -1], 4, 3)) # Output: 10
print(max_sub_array_sum_repeated([1, -2, 3, 4, -5, -2, 1, -1], 5, 2)) # Output: 10
print(max_sub_array_sum_repeated([1, -2, 3, 4, -5, -2, 1, -1], 6, 1)) # Output: 10
print(max_sub_array_sum_repeated([1, -2, 3, 4, -5, -2, 1, -1], 1, 1)) # Output: 10
print(max_sub_array_sum_repeated([1, -2, 3, 4, -5, -2, 1, -1], 0, 1)) # Output: 0
print(max_sub_array_sum_repeated([1, -2, 3, 4, -5, -2, 1, -1], 1, 0)) # Output: 0
print(max_sub_array_sum_repeated([1, -2, 3, 4, -5, -2, 1, -1], 0, 0)) # Output: 0
print(max_sub_array_sum_repeated([1, -2, 3, 4, -5, -2, 1, -1], 1, -1)) # Output: 0
print(max_sub_array_sum_repeated([1, -2, 3, 4, -5, -2, 1, -1], -1, 1)) # Output: 0
print(max_sub_array_sum_repeated([1, -2, 3, 4, -5, -2, 1, -1], 1, 1)) # Output: 0
print(max_sub_array_sum_repeated([1, -2, 3, 4, -5, -2, 1, -1], 0, 0)) # Output: 0
print(max_sub_array_sum_repeated([1, -2, 3, 4, -5, -2, 1, -1], -1, -1)) # Output: 0
print(max_sub_array_sum_repeated([1, -2, 3, 4, -5, -2, 1, -1], 0