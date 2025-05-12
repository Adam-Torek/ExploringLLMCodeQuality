"""
Write a python function to find the first odd number in a given list of numbers.
assert first_odd([1,3,5]) == 1
"""

def first_odd(numbers):
    """
    This function takes a list of numbers as an input and returns the first odd number in the list.
    """
    for number in numbers:
        if number % 2 != 0:
            return number
    return None

# Test the function
print(first_odd([1,3,5])) # 1
print(first_odd([2,4,6])) # None