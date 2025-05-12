"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""

import math


def count_binary_seq(n):
    """
    Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
    :param n:
    :return:
    """
    if n == 0:
        return 1
    if n == 1:
        return 2
    return 2 * count_binary_seq(n - 1) + count_binary_seq(n - 2)


if __name__ == '__main__':
    print(math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(2), 4.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(3), 8.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(4), 16.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(5), 32.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(6), 64.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(7), 128.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(8), 256.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(9), 512.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(10), 1024.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(11), 2048.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(12), 4096.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(13), 8192.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(14), 16384.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(15), 32768.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(16), 65536.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(17), 131072.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(18), 262144.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(19), 524288.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(20), 1048576.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(21), 2097152.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(22), 4194304.0, rel_tol=0.001))
    print(math.isclose(count_binary_seq(23), 8388608.0, rel_tol=0.001