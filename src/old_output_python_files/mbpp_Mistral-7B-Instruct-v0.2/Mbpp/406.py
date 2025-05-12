"""
Write a python function to find whether the parity of a given number is odd.
assert find_Parity(12) == False
"""
def find_parity(num):
    """
    This function takes an integer as an argument and returns a boolean value indicating whether the parity of the number is odd.
    """
    return num % 2 != 0