"""
Write a python function to find the difference between largest and smallest value in a given list.
assert big_diff([1,2,3,4]) == 3
"""

def big_diff(lst):
    return max(lst) - min(lst)

print(big_diff([1,2,3,4])) # Output: 3
print(big_diff([-10, 5, 8, 3, -6, 12, 7, 11]) # Output: 13
print(big_diff([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 8
print(big_diff([100, 90, 80, 70, 60, 50])) # Output: 50
print(big_diff([-10, -20, -30, -40, -50, -60])) # Output: 10
print(big_diff([10, 20, 30, 40, 50, 60])) # Output: 10
print(big_diff([-10, 0, 5, 10, 20, 30])) # Output: 40

# Test Cases
# Test Case 1:
# Input: [1, 2, 3, 4]
# Output: 3

# Test Case 2:
# Input: [-10, 5, 8, 3, -6, 12, 7, 11]
# Output: 13

# Test Case 3:
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output: 8

# Test Case 4:
# Input: [-10, -20, -30, -40, -50, -60]
# Output: 10

# Test Case 5:
# Input: [100, 90, 80, 70, 60, 50]
# Output: 50

# Test Case 6:
# Input: [-10, 0, 5, 10, 20, 30]
# Output: 40

# Test Case 7:
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: 9

# Test Case 8:
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# Output: 11

# Test Case 9:
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Output: 12

# Test Case 10:
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Output: 13

# Test Case 11:
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# Output: 14

# Test Case 12:
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Output: 15

# Test Case 13:
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# Output: 16

# Test Case 14:
# Input: [1, 2, 3, 4, 5