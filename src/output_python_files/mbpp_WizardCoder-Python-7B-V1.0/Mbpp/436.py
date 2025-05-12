"""
Write a python function to return the negative numbers in a list.
assert neg_nos([-1,4,5,-6]) == [-1,-6]
"""

def neg_nos(lst):
    return [num for num in lst if num < 0]

# Test cases
print(neg_nos([-1,4,5,-6])) # Output: [-1, -6]
print(neg_nos([1,2,3,4,5])) # Output: []
print(neg_nos([-5,-3,-2,-4])) # Output: [-5, -3, -2, -4]
print(neg_nos([0,-1,2,3,-4])) # Output: [-1, -4]
print(neg_nos([-1,0,1,2,-3])) # Output: [-1, -3]
print(neg_nos([-1])) # Output: [-1]
print(neg_nos([])) # Output: []

# Time Complexity: O(n)
# Space Complexity: O(n)