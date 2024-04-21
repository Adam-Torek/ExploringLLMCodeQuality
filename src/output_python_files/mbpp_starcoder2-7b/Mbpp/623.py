"""
Write a function to compute the n-th power of each number in a list.
assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

def nth_nums(nums,n):
    return [num**n for num in nums]

print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2))<file_sep>/python_basics/python_basics_1.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
"""

def largest_num(nums):
    return max(nums)

print(largest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))<file_sep>/python_basics/python_basics_10.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
"""

def smallest_num(nums):
    return min(nums)

print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))<file_sep>/python_basics/python_basics_11.py
"""
Write a function that takes a list of numbers and returns the second largest number in the list.
assert second_largest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
"""

def second_largest_num(nums):
    nums.sort()
    return nums[-2]

print(second_largest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))<file_sep>/python_basics/python_basics_12.py
"""
Write a function that takes a list of numbers and returns the second smallest number in the list.
assert second_smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
"""

def second_smallest_num(nums):
    nums.sort()
    return nums[1]

print(second_smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))<file_sep>/python_basics/python_basics_13.py
"""
Write a function that takes a list of numbers and returns the second smallest number in the list.
assert second_smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
"""

def second_smallest_num(nums):
    nums.sort()
    return nums[1]

print(second_smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))<file_sep>/python_basics/python_basics_14.py
"""
Write a function that takes a list of numbers and returns the second smallest number in the list.
assert second_smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
"""

def second_smallest_num(nums):
    nums.sort()
    return nums[1]

print(second_smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))<file_sep>/python_basics/python_basics_15.py
"""
Write a function that takes a list of numbers and returns the second smallest number in