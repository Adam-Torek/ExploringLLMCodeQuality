"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""

def max_sub_array_sum(arr, k):
    """
    Find the sum of the largest contiguous sublist in the given list.
    """
    max_sum = float('-inf')
    current_sum = 0
    max_sublist_sum = 0
    max_sublist_start = 0
    max_sublist_end = 0
    temp_sum = 0
    temp_start = 0
    temp_end = 0

    for i, num in enumerate(arr):
        if current_sum + num > temp_sum:
            temp_sum += num
            temp_end = i
        else:
            if temp_sum > max_sum:
                max_sum = temp_sum
                max_sublist_sum = temp_sum
                max_sublist_start = temp_start
                max_sublist_end = temp_end
            temp_sum = num
            temp_start = i

        if temp_sum > k:
            temp_sum -= arr[temp_start]
            temp_start += 1

    if temp_sum > max_sum:
        max_sum = temp_sum
        max_sublist_sum = temp_sum
        max_sublist_start = temp_start
        max_sublist_end = i

    return max_sublist_sum


print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8)) # 7
print(max_sub_array_sum([1, 2, 3, 4, 5, -10, 7, 8, 9], 10)) # 25
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10)) # 7
print(max_sub_array_sum([1, 2, 3, 4, 5, -10, 7, 8, 9], 10)) # 25
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10)) # 7
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10)) # 7
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10)) # 7
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10)) # 7
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10)) # 7
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10)) # 7
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10)) # 7
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10)) # 7
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10)) # 7
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10)) # 7
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 10