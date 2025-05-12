"""
Write a python function to find even numbers from a list of numbers.
assert Split([1,2,3,4,5]) == [2,4]
"""

def split(lst):
    """
    This function takes a list of numbers and returns a list of even numbers.
    """
    even_numbers = []
    for number in lst:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

# Test the function
print(split([1,2,3,4,5]))