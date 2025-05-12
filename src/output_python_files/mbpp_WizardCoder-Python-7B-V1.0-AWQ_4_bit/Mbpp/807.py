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
print(first_odd([2,4,6,8,1])) # Output: 1
print(first_odd([1,4,6,8])) # Output: None
print(first_odd([2,4,6,8])) # Output: None
print(first_odd([3,5,7,9])) # Output: 3
print(first_odd([1,3,5,7,9])) # Output: 1
print(first_odd([2,4,6,8])) # Output: None
print(first_odd([1])) # Output: 1
print(first_odd([])) # Output: None
print(first_odd([2,4,6])) # Output: None
print(first_odd([1,3,5,7,9,11,13,15])) # Output: 1
print(first_odd([2,4,6,8,10,12,14,16])) # Output: None
print(first_odd([1,3,5,7,9,11,13,15,17,19])) # Output: 1
print(first_odd([2,4,6,8,10,12,14,16,18,20])) # Output: None
print(first_odd([1,3,5,7,9,11,13,15,17,19,21])) # Output: 1
print(first_odd([2,4,6,8,10,12,14,16,18,20,22])) # Output: None
print(first_odd([1,3,5,7,9,11,13,15,17,19,21,23])) # Output: 1
print(first_odd([2,4,6,8,10,12,14,16,18,20,22,24])) # Output: None
print(first_odd([1,3,5,7,9,11,13,15,17,19,21,23,25])) # Output: 1
print(first_odd([2,4,6,8,10,12,14,16,18,20,22,24,26])) # Output: None
print(first_odd([1,3,5,7,9,11,13,15,17,19,21,23,25,27])) # Output: 1
print(first_odd([2,4,6,8,10,12,14,16,18,20,22,24,26,28])) # Output: None
print(first_odd([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29])) # Output: 1
print(first_odd([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30])) # Output: None
print(first_odd([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31])) # Output: 1
print(first_odd([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32])) # Output: None
print(first_odd([1,3,5,7,9,11,13,15,17,19,21,23,25,