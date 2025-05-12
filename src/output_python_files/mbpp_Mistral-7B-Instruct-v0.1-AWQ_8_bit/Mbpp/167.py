"""
Write a python function to find the smallest power of 2 greater than or equal to n.
assert next_power_of_2(0) == 1
"""

def next_power_of_2(n):
    """
    Find the smallest power of 2 greater than or equal to n.
    """
    while True:
        n += 1
        if n % 2 == 0:
            return n


if __name__ == "__main__":
    assert next_power_of_2(0) == 1
    assert next_power_of_2(1) == 2
    assert next_power_of_2(2) == 4
    assert next_power_of_2(3) == 8
    assert next_power_of_2(4) == 16
    assert next_power_of_2(5) == 32
    assert next_power_of_2(6) == 64
    assert next_power_of_2(7) == 128
    assert next_power_of_2(8) == 256
    assert next_power_of_2(9) == 512
    assert next_power_of_2(10) == 1024
    assert next_power_of_2(11) == 2048
    assert next_power_of_2(12) == 4096
    assert next_power_of_2(13) == 8192
    assert next_power_of_2(14) == 16384
    assert next_power_of_2(15) == 32768
    assert next_power_of_2(16) == 65536
    assert next_power_of_2(17) == 131072
    assert next_power_of_2(18) == 262144
    assert next_power_of_2(19) == 524288
    assert next_power_of_2(20) == 1048576
    assert next_power_of_2(21) == 2097152
    assert next_power_of_2(22) == 4194304
    assert next_power_of_2(23) == 8388608
    assert next_power_of_2(24) == 16777216
    assert next_power_of_2(25) == 33544032
    assert next_power_of_2(26) == 67108872
    assert next_power_of_2(27) == 134217728
    assert next_power_of_2(28) == 268435456
    assert next_power_of_2(29) == 536870912
    assert next_power_of_2(30) == 1073741824
    assert next_power_of_2(31) == 2147483648
    assert next_power_of_2(32) == 4294967296
    assert next_power_of_2(33) == 8589934592
    assert next_power_of_2(34) == 17179969152
    assert next_power_of_2(35) == 34359837170
    assert next_power_of_2(36) == 68719871702
    assert next_power_of_2(37) == 137439717010
    assert next_power_of_2(38) == 274879408736
    assert next_power_of_2(39) == 549758716402
    assert next_power_of_2(40) == 1099511622