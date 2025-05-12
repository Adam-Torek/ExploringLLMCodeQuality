"""
Write a python function to find the highest power of 2 that is less than or equal to n.
assert highest_Power_of_2(10) == 8
"""

def highest_Power_of_2(n):
    """
    This function takes an integer n as an input and returns the highest power of 2 that is less than or equal to n.
    """
    while n > 1:
        n = n // 2
    return n


# Test the function
assert highest_Power_of_2(10) == 8