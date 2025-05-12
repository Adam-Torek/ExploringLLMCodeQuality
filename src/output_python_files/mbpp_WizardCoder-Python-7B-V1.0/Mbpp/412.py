"""
Write a python function to remove odd numbers from a given list.
assert remove_odd([1,2,3]) == [2]
"""

def remove_odd(lst):
    return [num for num in lst if num % 2 == 0]

# Test cases
print(remove_odd([1,2,3])) # Output: [2]
print(remove_odd([4,5,6,7,8,9])) # Output: [4, 6, 8]
print(remove_odd([1,3,5,7,9])) # Output: []
print(remove_odd([2,4,6,8])) # Output: [2, 4, 6, 8]
print(remove_odd([1,2,3,4,5,6,7,8,9])) # Output: [2, 4, 6, 8]
print(remove_odd([1,3,5,7,9,2,4,6,8])) # Output: [2, 4, 6, 8]
print(remove_odd([1,2,3,4,5,6,7,8,9,2,4,6,8])) # Output: [2, 4, 6, 8, 2, 4, 6, 8]
print(remove_odd([1,3,5,7,9,2,4,6,8,2,4,6,8])) # Output: [2, 4, 6, 8, 2, 4, 6, 8]
print(remove_odd([1,3,5,7,9,2,4,6,8,2,4,6,8,1,3,5,7,9])) # Output: [2, 4, 6, 8, 2, 4, 6, 8]
print(remove_odd([1,3,5,7,9,2,4,6,8,2,4,6,8,1,3,5,7,9])) # Output: [2, 4, 6, 8, 2, 4, 6, 8]
print(remove_odd([1,3,5,7,9,2,4,6,8,2,4,6,8,1,3,5,7,9,2,4,6,8])) # Output: [2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8]
print(remove_odd([1,3,5,7,9,2,4,6,8,2,4,6,8,1,3,5,7,9,2,4,6,8])) # Output: [2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8]
print(remove_odd([1,3,5,7,9,2,4,6,8,2,4,6,8,1,3,5,7,9,2,4,6,8,1,3,5,7,9])) # Output: [2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8]
print(remove_odd([1,3,5,7,9,2,4,6,8,2,4,6,8,1,3,5,7,9,2,4,6,8,1,3,5,7,9])) # Output: [2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8]
print(remove_odd([1,3,5,7,9,2,4,6,8,2,4,6,8,1,3,5,7,9,2,4