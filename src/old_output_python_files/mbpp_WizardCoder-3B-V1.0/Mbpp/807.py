"""
Write a python function to find the first odd number in a given list of numbers.
assert first_odd([1,3,5]) == 1
"""

def first_odd(lst):
    for num in lst:
        if num % 2!= 0:
            return num
    return None

# Test the function
print(first_odd([1,3,5])) # Output: 1<|endoftext|>