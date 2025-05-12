"""
Write a python function to find the minimum of two numbers.
assert minimum(1,2) == 1
"""

def minimum(a, b):
    """
    This function takes two numbers as arguments and returns the minimum of the two numbers.
    """
    if a < b:
        return a
    else:
        return b

# Test the function
assert minimum(1,2) == 1