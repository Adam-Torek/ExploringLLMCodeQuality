"""
Write a python function to find the highest power of 2 that is less than or equal to n.
assert highest_Power_of_2(10) == 8
"""
def highest_Power_of_2(n):
    power = 0
    while (n > 0):
        n = n >> 1
        power += 1
    return n << power

assert highest_Power_of_2(10) == 8
assert highest_Power_of_2(1) == 1
assert highest_Power_of_2(16) == 16
assert highest_Power_of_2(25) == 16
assert highest_Power_of_2(27) == 16
assert highest_Power_of_2(2**31-1) == 2147483648
assert highest_Power_of_2(2**64-1) == 18446744073709551615
assert highest_Power_of_2(2**63) == 9223372036854775808
assert highest_Power_of_2(2**62) == 4503599627370496
assert highest_Power_of_2(2**61) == 22517041287136452752
assert highest_Power_of_2(2**60) == 1073741824
assert highest_Power_of_2(2**59) == 549755813888
assert highest_Power_of_2(2**58) == 268435456
assert highest_Power_of_2(2**57) == 134217728
assert highest_Power_of_2(2**56) == 67108864
assert highest_Power_of_2(2**55) == 33554432
assert highest_Power_of_2(2**54) == 16777216
assert highest_Power_of_2(2**53) == 8388608
assert highest_Power_of_2(2**52) == 4194304
assert highest_Power_of_2(2**51) == 2097152
assert highest_Power_of_2(2**50) == 1048576
assert highest_Power_of_2(2**49) == 524288
assert highest_Power_of_2(2**48) == 262144
assert highest_Power_of_2(2**47) == 131072
assert highest_Power_of_2(2**46) == 65536
assert highest_Power_of_2(2**45) == 32768
assert highest_Power_of_2(2**44) == 16384
assert highest_Power_of_2(2**43) == 8192
assert highest_Power_of_2(2**42) == 4096
assert highest_Power_of_2(2**41) == 2048
assert highest_Power_of_2(2**40) == 1024
assert highest_Power_of_2(2**39) == 512
assert highest_Power_of_2(2**38) == 256
assert highest_Power_of_2(2**37) == 128
assert highest_Power_of_2(2**36) == 64
assert highest_Power_of_2(2**35) == 32
assert highest_Power_of_2(2**34) == 16
assert highest_Power_of_2(2**33) == 8
assert highest_Power_of_2(2**32) == 4
assert highest_Power_