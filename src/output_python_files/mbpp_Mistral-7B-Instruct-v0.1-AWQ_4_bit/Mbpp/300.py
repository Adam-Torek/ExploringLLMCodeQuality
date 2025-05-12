"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""

def count_binary_seq(n):
    """
    :type n: int
    :rtype: float
    """
    if n == 0:
        return 1.0
    elif n == 1:
        return 2.0
    else:
        return (2**n - 1) * (count_binary_seq(n-1) + count_binary_seq(n-2))


if __name__ == '__main__':
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 5.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 14.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(4), 34.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(5), 70.0, rel_tol=0.001)