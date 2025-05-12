"""
Write a python function to find the maximum of two numbers.
assert maximum(5,10) == 10
"""

def maximum(a, b):
    """
    This function takes two numbers as arguments and returns the maximum of the two numbers.
    """
    if a > b:
        return a
    else:
        return b

# Test the function
assert maximum(5,10) == 10