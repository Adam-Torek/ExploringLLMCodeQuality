"""
Write a python function to find the smallest power of 2 greater than or equal to n.
assert next_power_of_2(0) == 1
"""

def next_power_of_2(n):
    if n == 0:
        return 1
    else:
        return 2**((n-1).bit_length())

# Test cases
print(next_power_of_2(0)) # 1
print(next_power_of_2(1)) # 2
print(next_power_of_2(2)) # 4
print(next_power_of_2(3)) # 4
print(next_power_of_2(4)) # 8
print(next_power_of_2(5)) # 8
print(next_power_of_2(6)) # 16
print(next_power_of_2(7)) # 16
print(next_power_of_2(8)) # 32
print(next_power_of_2(9)) # 32
print(next_power_of_2(10)) # 64
print(next_power_of_2(11)) # 64
print(next_power_of_2(12)) # 128
print(next_power_of_2(13)) # 128
print(next_power_of_2(14)) # 256
print(next_power_of_2(15)) # 256
print(next_power_of_2(16)) # 512
print(next_power_of_2(17)) # 512
print(next_power_of_2(18)) # 1024
print(next_power_of_2(19)) # 1024
print(next_power_of_2(20)) # 2048
print(next_power_of_2(21)) # 2048
print(next_power_of_2(22)) # 4096
print(next_power_of_2(23)) # 4096
print(next_power_of_2(24)) # 8192
print(next_power_of_2(25)) # 8192
print(next_power_of_2(26)) # 16384
print(next_power_of_2(27)) # 16384
print(next_power_of_2(28)) # 32768
print(next_power_of_2(29)) # 32768
print(next_power_of_2(30)) # 65536
print(next_power_of_2(31)) # 65536
print(next_power_of_2(32)) # 131072
print(next_power_of_2(33)) # 131072
print(next_power_of_2(34)) # 262144
print(next_power_of_2(35)) # 262144
print(next_power_of_2(36)) # 524288
print(next_power_of_2(37)) # 524288
print(next_power_of_2(38)) # 1048576
print(next_power_of_2(39)) # 1048576
print(next_power_of_2(40)) # 2097152
print(next_power_of_2(41)) # 2097152
print(next_power_of_2(42)) # 4194304
print(next_power_of_2(43)) # 4194304
print(next_power_of_2(44)) # 8388608
print(next_power_of_2(45)) # 8388608
print(next_power_of_2(46)) # 16777216