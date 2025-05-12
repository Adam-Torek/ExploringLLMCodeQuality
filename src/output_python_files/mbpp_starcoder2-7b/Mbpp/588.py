"""
Write a python function to find the difference between largest and smallest value in a given list.
assert big_diff([1,2,3,4]) == 3
"""

def big_diff(nums):
    return max(nums) - min(nums)

assert big_diff([1,2,3,4]) == 3
assert big_diff([10,3,10,4]) == 7
assert big_diff([1,10,10,4]) == 9
assert big_diff([10,10,10,4]) == 6
assert big_diff([1,2,3,4,5,6,7,8,9,10]) == 9
assert big_diff([10,10,10,4,5,6,7,8,9,10]) == 9
assert big_diff([10,10,10,4,5,6,7,8,9,10,10]) == 9
assert big_diff([10,10,10,4,5,6,7,8,9,10,10,10]) == 9
assert big_diff([10,10,10,4,5,6,7,8,9,10,10,10,10]) == 9
assert big_diff([10,10,10,4,5,6,7,8,9,10,10,10,10,10]) == 9
assert big_diff([10,10,10,4,5,6,7,8,9,10,10,10,10,10,10]) == 9
assert big_diff([10,10,10,4,5,6,7,8,9,10,10,10,10,10,10,10]) == 9
assert big_diff([10,10,10,4,5,6,7,8,9,10,10,10,10,10,10,10,10]) == 9
assert big_diff([10,10,10,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10]) == 9
assert big_diff([10,10,10,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10,10]) == 9
assert big_diff([10,10,10,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10,10,10]) == 9
assert big_diff([10,10,10,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10,10,10,10]) == 9
assert big_diff([10,10,10,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10,10,10,10,10]) == 9
assert big_diff([10,10,10,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10]) == 9
assert big_diff([10,10,10,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]) == 9
assert big_