"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""

def max_sub_array_sum(arr, k):
    if not arr:
        return 0
    max_sum = float('-inf')
    current_sum = 0
    max_ending_here = 0
    for i in arr:
        current_sum += i
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum > k:
            current_sum = 0
    return max_sum

print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8)) # Output: 7
print(max_sub_array_sum([1, -2, 3, 4, -5, 6, -7, 8], 10)) # Output: 10
print(max_sub_array_sum([1, -2, 3, 4, -5, 6, -7, 8], 100)) # Output: 20
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 0)) # Output: 0
print(max_sub_array_sum([], 100)) # Output: 0
print(max_sub_array_sum([1], 100)) # Output: 1
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], -100) # Output: 0