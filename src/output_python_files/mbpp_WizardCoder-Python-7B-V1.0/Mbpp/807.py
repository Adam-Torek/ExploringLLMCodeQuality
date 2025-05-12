"""
Write a python function to find the first odd number in a given list of numbers.
assert first_odd([1,3,5]) == 1
"""

def first_odd(lst):
    for num in lst:
        if num % 2 != 0:
            return num
    return None

# Test cases
print(first_odd([1,3,5])) # Output: 1
print(first_odd([2,4,6,8,9])) # Output: 9
print(first_odd([1,4,6,8])) # Output: 1
print(first_odd([2,4,6,8])) # Output: None
print(first_odd([3,6,8,10])) # Output: 3
print(first_odd([1])) # Output: 1
print(first_odd([])) # Output: None