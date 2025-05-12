"""
Write a python function to find the difference between largest and smallest value in a given list.
assert big_diff([1,2,3,4]) == 3
"""

def big_diff(lst):
    return max(lst) - min(lst)

print(big_diff([1,2,3,4])) # Output: 3
print(big_diff([-1,2,3,4,-5]) # Output: 6
print(big_diff([10, 3, 0, 8, 2, 6])) # Output: 10
print(big_diff([100, 3, 0, 8, 2, 6])) # Output: 98
print(big_diff([-100, -3, -8, -2, -6])) # Output: 106
print(big_diff([1, 1, 1, 1, 1])) # Output: 0
print(big_diff([1])) # Output: 0
print(big_diff([])) # Output: None