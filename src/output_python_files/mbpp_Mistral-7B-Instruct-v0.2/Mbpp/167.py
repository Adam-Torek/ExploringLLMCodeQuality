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
    assert next_power_of_2(20) == 64
    assert next_power_of_2(25) == 128
    assert next_power_of_2(30) == 256
    assert next_power_of_2(35) == 512
    assert next_power_of_2(40) == 1024
    assert next_power_of_2(45) == 2048
    assert next_power_of_2(50) == 4096
    assert next_power_of_2(55) == 8192
    assert next_power_of_2(60) == 16384
    assert next_power_of_2(65) == 32768
    assert next_power_of_2(70) == 65536
    assert next_power_of_2(75) == 131072
    assert next_power_of_2(80) == 262144
    assert next_power_of_2(85) == 524288
    assert next_power_of_2(90) == 1048576
    assert next_power_of_2(95) == 2097152
    assert next_power_of_2(100) == 4194304
    assert next_power_of_2(105) == 8388608
    assert next_power_of_2(110) == 16777216
    assert next_power_of_2(115) == 33554432
    assert next_power_of_2(120) == 67108864
    assert next_power_of_2(125) == 134217728
    assert next_power_of_2(130) == 268435456
    assert next_power_of_2(135) == 536870912
    assert next_power_of_2(140) == 1073741824
    assert next_power_of_2(145) == 2147483648
    assert next_power_of_2(150) == 4294967296
    assert next_power_of_2(155) == 8589934592
    assert next_power_of_2(160) == 17179869184
    assert next_power_of_2(165) == 34359738368
    assert next_power_of_2(170) == 68719476736
    assert next_power_of_2(175) == 137438953472
    assert next_power_of_2(180) == 274877906944
    assert next_power_of_2(185) == 54975