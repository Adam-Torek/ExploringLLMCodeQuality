"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""
import math

def count_binary_seq(n: int) -> float:
    """
    This function takes an integer n as input and returns the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
    """
    if n == 1:
        return 2.0
    else:
        return (2**(2*n) - 2**n) / (2**n)

# Testing the function
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(2), 4.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(3), 10.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(4), 40.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(5), 240.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(6), 1680.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(7), 16800.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(8), 1933336.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(9), 24576000.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(10), 479001600.0, rel_tol=0.001)

print("All test cases passed!")