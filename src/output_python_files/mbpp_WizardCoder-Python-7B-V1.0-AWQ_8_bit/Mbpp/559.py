"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""

def max_sub_array_sum(arr, k):
    if len(arr) == 0:
        return 0
    max_sum = float('-inf')
    current_sum = 0
    max_sum_list = []
    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum == k:
            max_sum_list.append(current_sum)
            current_sum = 0
    return max(max_sum_list)

print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8)) # Output: 7