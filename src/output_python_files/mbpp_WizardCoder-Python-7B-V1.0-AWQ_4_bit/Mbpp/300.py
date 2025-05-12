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
assert math.isclose(count_binary_seq(11), 78154.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(12), 614042.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(13), 4851962.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(14), 40316362.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(15), 381212602.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(16), 4288088362.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(17), 5418112206.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(18), 78111745402.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(19), 1264937900426.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(20), 2432639742106.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(21), 51296314901412.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(22), 1180436041145162.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(23), 26366086614616066.0, rel_tol=0.001)
assert math.isclose(count_binary_