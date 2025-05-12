"""
Write a function to calculate the value of 'a' to the power 'b'.
assert power(3,4) == 81
"""
def power(a, b):
    """
    Calculate the value of 'a' to the power 'b'
    """
    result = 1
    for _ in range(b):
        result *= a
    return result