"""
Write a python function to move all zeroes to the end of the given list.
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
"""

def move_zero(arr):
    return [x for x in arr if x != 0] + [0] * arr.count(0)

# Test cases
print(move_zero([1,0,2,0,3,4])) # Output: [1,2,3,4,0,0]
print(move_zero([0,0,1,2,0,3,4,0])) # Output: [1,2,3,4,0,0,0]
print(move_zero([1,2,3,4])) # Output: [1,2,3,4]
print(move_zero([0,0,0])) # Output: [0,0,0]
print(move_zero([1,2,3,4,5])) # Output: [1,2,3,4,5]
print(move_zero([0,1,2,3,4,5])) # Output: [1,2,3,4,5,0]
print(move_zero([0,0,0,1,2,3,0,4,0,5])) # Output: [1,2,3,4,5,0,0,0,0]
print(move_zero([0,0,0,0,0,0])) # Output: [0,0,0,0,0,0]
print(move_zero([1,1,1,1,1])) # Output: [1,1,1,1,1]

# Time Complexity: O(n)
# Space Complexity: O(1)
# where n is the length of the input array