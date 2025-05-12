"""
Write a python function to find the highest power of 2 that is less than or equal to n.
assert highest_Power_of_2(10) == 8
"""

def highest_Power_of_2(n):
    power = 1
    while (power * 2 <= n):
        power *= 2
    return power

print(highest_Power_of_2(10)) # Output: 8
print(highest_Power_of_2(20)) # Output: 16
print(highest_Power_of_2(32)) # Output: 32
print(highest_Power_of_2(64)) # Output: 64
print(highest_Power_of_2(128)) # Output: 128
print(highest_Power_of_2(256)) # Output: 128
print(highest_Power_of_2(512)) # Output: 256
print(highest_Power_of_2(1024)) # Output: 1024
print(highest_Power_of_2(2048)) # Output: 2048
print(highest_Power_of_2(4096)) # Output: 2048
print(highest_Power_of_2(8192)) # Output: 4096
print(highest_Power_of_2(16384)) # Output: 8192
print(highest_Power_of_2(32768)) # Output: 16384
print(highest_Power_of_2(65536)) # Output: 32768
print(highest_Power_of_2(131072)) # Output: 65536
print(highest_Power_of_2(262144)) # Output: 131072
print(highest_Power_of_2(524288)) # Output: 262144
print(highest_Power_of_2(1048576)) # Output: 524288
print(highest_Power_of_2(2097152)) # Output: 1048576
print(highest_Power_of_2(4194304)) # Output: 2097152
print(highest_Power_of_2(8388608)) # Output: 4194304
print(highest_Power_of_2(16777216)) # Output: 8388608
print(highest_Power_of_2(33554432)) # Output: 16777216
print(highest_Power_of_2(67108864)) # Output: 33554432
print(highest_Power_of_2(134217728)) # Output: 67108864
print(highest_Power_of_2(268435456)) # Output: 134217728
print(highest_Power_of_2(536870912)) # Output: 335544320
print(highest_Power_of_2(1073741824)) # Output: 671088640
print(highest_Power_of_2(2147483648)) # Output: 1342177280
print(highest_Power_of_2(4294967296)) # Output: 2684354560
print(highest_Power_of_2(8589934592)) # Output: 5368709120
print(highest_Power_of_2(17179869184)) # Output: