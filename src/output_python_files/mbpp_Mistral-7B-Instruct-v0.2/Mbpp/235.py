"""
Write a python function to set all even bits of a given number.
assert even_bit_set_number(10) == 10
"""
def even_bit_set_number(num):
    """
    Sets all even-indexed bits of a given number to 1.
    :param num: An integer number
    :return: The number with all even-indexed bits set to 1
    """
    return num | (num << 1) | (num >> 1)

if __name__ == "__main__":
    assert even_bit_set_number(10) == 22
    assert even_bit_set_number(5) == 6
    assert even_bit_set_number(0) == 0
    assert even_bit_set_number(1) == 2
    assert even_bit_set_number(12) == 29
    assert even_bit_set_number(15) == 30
    assert even_bit_set_number(20) == 62
    assert even_bit_set_number(21) == 64
    assert even_bit_set_number(3) == 4
    assert even_bit_set_number(4) == 12
    assert even_bit_set_number(13) == 28
    assert even_bit_set_number(14) == 30
    assert even_bit_set_number(16) == 32
    assert even_bit_set_number(17) == 64
    assert even_bit_set_number(18) == 128
    assert even_bit_set_number(19) == 256
    assert even_bit_set_number(22) == 1024
    assert even_bit_set_number(23) == 2048
    assert even_bit_set_number(24) == 4096
    assert even_bit_set_number(25) == 8192
    assert even_bit_set_number(26) == 16384
    assert even_bit_set_number(27) == 32768
    assert even_bit_set_number(28) == 65536
    assert even_bit_set_number(29) == 131072
    assert even_bit_set_number(30) == 262144
    assert even_bit_set_number(31) == 524288
    assert even_bit_set_number(32) == 1048576
    assert even_bit_set_number(33) == 2097152
    assert even_bit_set_number(34) == 4194304
    assert even_bit_set_number(35) == 8388608
    assert even_bit_set_number(36) == 16777216
    assert even_bit_set_number(37) == 33554432
    assert even_bit_set_number(38) == 67108864
    assert even_bit_set_number(39) == 134217728
    assert even_bit_set_number(40) == 268435456
    assert even_bit_set_number(41) == 536870912
    assert even_bit_set_number(42) == 1073741824
    assert even_bit_set_number(43) == 2147483648
    assert even_bit_set_number(44) == 4294967296
    assert even_bit_set_number(45) == 8589934592
    assert even_bit_set_number(46) == 17179869184
    assert even_bit_set_number(47) == 34359738368
    assert even_bit_set_number