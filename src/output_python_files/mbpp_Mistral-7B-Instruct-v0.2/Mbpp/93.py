"""
Write a function to calculate the value of 'a' to the power 'b'.
assert power(3,4) == 81
"""
def power(a, b):
    """
    Calculate the value of 'a' to the power 'b'
    :param a: base number
    :param b: exponent
    :return: result of 'a' raised to the power of 'b'
    """
    result = 1
    for _ in range(b):
        result *= a
    return result</s>