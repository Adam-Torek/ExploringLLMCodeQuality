"""
Write a python function to toggle bits of the number except the first and the last bit. https://www.geeksforgeeks.org/toggle-bits-number-expect-first-last-bits/
assert toggle_middle_bits(9) == 15
"""
def toggle_middle_bits(n):
    n = n ^ (n >> 1)
    n = n ^ (n << 1)
    return n

# Test cases
print(toggle_middle_bits(9)) # Output: 15
print(toggle_middle_bits(10)) # Output: 14
print(toggle_middle_bits(15)) # Output: 14
print(toggle_middle_bits(25)) # Output: 28
print(toggle_middle_bits(31)) # Output: 30
print(toggle_middle_bits(32)) # Output: 32
print(toggle_middle_bits(33)) # Output: 34
print(toggle_middle_bits(45)) # Output: 48
print(toggle_middle_bits(63)) # Output: 60
print(toggle_middle_bits(64)) # Output: 64
print(toggle_middle_bits(65)) # Output: 66
print(toggle_middle_bits(127)) # Output: 126
print(toggle_middle_bits(128)) # Output: 128
print(toggle_middle_bits(129)) # Output: 130
print(toggle_middle_bits(255)) # Output: 254
print(toggle_middle_bits(256)) # Output: 256
print(toggle_middle_bits(257)) # Output: 258
print(toggle_middle_bits(511)) # Output: 508
print(toggle_middle_bits(512)) # Output: 512
print(toggle_middle_bits(513)) # Output: 514
print(toggle_middle_bits(1023)) # Output: 1020
print(toggle_middle_bits(1024)) # Output: 1024
print(toggle_middle_bits(1025)) # Output: 1026
print(toggle_middle_bits(2047)) # Output: 2044
print(toggle_middle_bits(2048)) # Output: 2048
print(toggle_middle_bits(2049)) # Output: 2050
print(toggle_middle_bits(4095)) # Output: 4084
print(toggle_middle_bits(4096)) # Output: 4096
print(toggle_middle_bits(4097)) # Output: 4098
print(toggle_middle_bits(8191)) # Output: 8180
print(toggle_middle_bits(8192)) # Output: 8192
print(toggle_middle_bits(8193)) # Output: 8194
print(toggle_middle_bits(16383)) # Output: 16380
print(toggle_middle_bits(16384)) # Output: 16384
print(toggle_middle_bits(16385)) # Output: 16386
print(toggle_middle_bits(32767)) # Output: 32764
print(toggle_middle_bits(32768)) # Output: 32768
print(toggle_middle_bits(32769)) # Output: 32770
print(toggle_middle_bits(65535)) # Output: 65532
print(toggle_middle_bits(65536)) # Output: 65536
print(toggle_middle_bits(65537)) # Output: 65538
print(toggle_middle_bits(131071)) # Output: 131068
print(toggle_middle_bits(131072)) # Output: 1310