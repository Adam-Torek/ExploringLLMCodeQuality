"""
Write a python function to find the highest power of 2 that is less than or equal to n.
assert highest_Power_of_2(10) == 8
"""
def highest_Power_of_2(n):
    power = 0
    while (n > 0):
        n = n >> 1
        power += 1
    return (1 << power)

assert highest_Power_of_2(10) == 8
assert highest_Power_of_2(1) == 1
assert highest_Power_of_2(2) == 2
assert highest_Power_of_2(3) == 2
assert highest_Power_of_2(4) == 4
assert highest_Power_of_2(5) == 4
assert highest_Power_of_2(16) == 16
assert highest_Power_of_2(25) == 16
assert highest_Power_of_2(26) == 32
assert highest_Power_of_2(32) == 32
assert highest_Power_of_2(64) == 64
assert highest_Power_of_2(128) == 128
assert highest_Power_of_2(256) == 256
assert highest_Power_of_2(512) == 512
assert highest_Power_of_2(1024) == 1024
assert highest_Power_of_2(2097152) == 2097152
assert highest_Power_of_2(4194304) == 4194304
assert highest_Power_of_2(8388608) == 8388608
assert highest_Power_of_2(16777216) == 16777216
assert highest_Power_of_2(33554432) == 33554432
assert highest_Power_of_2(67108864) == 67108864
assert highest_Power_of_2(134217728) == 134217728
assert highest_Power_of_2(268435456) == 268435456
assert highest_Power_of_2(536870912) == 536870912
assert highest_Power_of_2(1073741824) == 1073741824
assert highest_Power_of_2(2147483648) == 2147483648
assert highest_Power_of_2(4294967296) == 4294967296
assert highest_Power_of_2(8589934592) == 8589934592
assert highest_Power_of_2(17179869184) == 17179869184
assert highest_Power_of_2(34359738368) == 34359738368
assert highest_Power_of_2(710559905600) == 710559905600
assert highest_Power_of_2(14411518807527) == 14411518807527
assert highest_Power_of_2(281474976710656) == 281474976710656
assert highest_Power_of_2(562949953421312) == 562949953421312
assert highest_Power_of_2(1125899906842624) == 1125899906842624
assert highest_Power_