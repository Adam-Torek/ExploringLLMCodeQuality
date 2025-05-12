"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""

def count_binary_seq(n: int) -> float:
    if n == 1:
        return 2.0
    else:
        return 2 * count_binary_seq(n-1) + 2 * count_binary_seq(n-1)

# Test cases
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(2), 4.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(3), 10.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(4), 42.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(5), 306.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(6), 306.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(7), 462.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(8), 1036.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(9), 2706.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(10), 14648.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(11), 78168.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(12), 616080.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(13), 510608.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(14), 4815620.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(15), 5428800.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(16), 8838880.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(17), 15063200.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(18), 30030080.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(19), 58328960.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(20), 126432640.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(21), 264515840.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(22), 622702080.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(23), 1415974080.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(24), 3654352800.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(25), 9384848160.0, rel_tol=0.00