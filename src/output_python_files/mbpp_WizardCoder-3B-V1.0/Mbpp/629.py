"""
Write a python function to find even numbers from a list of numbers.
assert Split([1,2,3,4,5]) == [2,4]
"""

def Split(lst):
    return [x for x in lst if x % 2 == 0]

# Test the function
print(Split([1,2,3,4,5])) # Output: [2, 4]<|endoftext|>