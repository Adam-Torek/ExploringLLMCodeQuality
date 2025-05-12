"""
Write a python function to find the sum of an array.
assert _sum([1, 2, 3]) == 6
"""

def _sum(numbers):
    """
    This function takes a list of numbers as an input and returns the sum of all the numbers in the list.
    """
    total = 0
    for number in numbers:
        total += number
    return total

# test the function
assert _sum([1, 2, 3]) == 6