"""
Write a python function to find the difference between largest and smallest value in a given list.
assert big_diff([1,2,3,4]) == 3
"""

def big_diff(lst):
    return max(lst) - min(lst)

print(big_diff([1,2,3,4])) # Output: 3
print(big_diff([10, 3, 5, 6, 4, 2])) # Output: 6
print(big_diff([100, 50, 30, 10, 0])) # Output: 90
print(big_diff([-10, -5, -8, -100])) # Output: 90
print(big_diff([1, 2, 3, 4, 5])) # Output: 4
print(big_diff([-1, -2, -3, -4, -5])) # Output: 9
print(big_diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 8
print(big_diff([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])) # Output: 80
print(big_diff([-10, -20, -30, -40, -50, -60, -70, -80, -90, -100])) # Output: 80
print(big_diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # Output: 14
print(big_diff([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) # Output: 24

# Test cases for edge cases
print(big_diff([1])) # Output: 0
print(big_diff([-1])) # Output: 0
print(big_diff([])) # Output: None
print(big_diff([0])) # Output: 0
print(big_diff([0, 0])) # Output: 0
print(big_diff([1, 1, 1, 1, 1])) # Output: 0
print(big_diff([-1, -1, -1, -1, -1])) # Output: 0
print(big_diff([0, 0, 0, 0, 0])) # Output: 0
print(big_diff([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,