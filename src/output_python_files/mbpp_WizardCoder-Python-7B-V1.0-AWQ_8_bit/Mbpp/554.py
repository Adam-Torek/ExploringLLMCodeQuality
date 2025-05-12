"""
Write a python function which takes a list of integers and only returns the odd ones.
assert Split([1,2,3,4,5,6]) == [1,3,5]
"""

def Split(lst):
    return [num for num in lst if num % 2 != 0]

print(Split([1,2,3,4,5,6])) # Output: [1, 3, 5]