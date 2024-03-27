"""
Write a python function to find the smallest power of 2 greater than or equal to n.
assert next_power_of_2(0) == 1
"""

def next_power_of_2(n):
    """
    :param n: int
    :return: int
    """
    power = 1
    while power < n:
        power *= 2
    return power

if __name__ == "__main__":
    assert next_power_of_2(0) == 1
    assert next_power_of_2(3) == 4
    assert next_power_of_2(5) == 8
    assert next_power_of_2(10) == 16
    assert next_power_of_2(15) == 32
    assert next_power_of_2(21) == 64
    assert next_power_of_2(22) == 128
    assert next_power_of_2(23) == 256
    assert next_power_of_2(24) == 512
    assert next_power_of_2(25) == 1024
    assert next_power_of_2(26) == 2048
    assert next_power_of_2(27) == 4096
    assert next_power_of_2(28) == 8192
    assert next_power_of_2(29) == 16384
    assert next_power_of_2(30) == 32768
    assert next_power_of_2(31) == 65536
    assert next_power_of_2(32) == 131072
    assert next_power_of_2(33) == 262144
    assert next_power_of_2(34) == 524288
    assert next_power_of_2(35) == 1048576
    assert next_power_of_2(36) == 2097152
    assert next_power_of_2(37) == 4194304
    assert next_power_of_2(38) == 8388608
    assert next_power_of_2(39) == 16777216
    assert next_power_of_2(40) == 33554432
    assert next_power_of_2(41) == 67108864
    assert next_power_of_2(42) == 134217728
    assert next_power_of_2(43) == 268435456
    assert next_power_of_2(44) == 536870912
    assert next_power_of_2(45) == 1073741824
    assert next_power_of_2(46) == 2147483648
    assert next_power_of_2(47) == 4294967296
    assert next_power_of_2(48) == 8589934592
    assert next_power_of_2(49) == 17179869184
    assert next_power_of_2(50) == 34359738368
    assert next_power_of_2(51) == 68719476736
    assert next_power_of_2(52) == 137438953472
    assert next_power_of_2(53) == 274877906944
    assert next_power_of_2(54) == 549755813888
    assert next_power_of_2(55) == 1099511627776
    assert next_power_of_2(56)