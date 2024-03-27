"""
Write a python function to count the number of set bits (binary digits with value 1) in a given number.
assert count_Set_Bits(2) == 1
"""

def count_Set_Bits(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count

# Test cases
assert count_Set_Bits(2) == 1
assert count_Set_Bits(10) == 3
assert count_Set_Bits(100) == 6
assert count_Set_Bits(1000) == 10
assert count_Set_Bits(10000) == 12
assert count_Set_Bits(100000) == 14
assert count_Set_Bits(1000000) == 16
assert count_Set_Bits(10000000) == 18
assert count_Set_Bits(100000000) == 20
assert count_Set_Bits(1000000000) == 22
assert count_Set_Bits(10000000000) == 24
assert count_Set_Bits(100000000000) == 26
assert count_Set_Bits(1000000000000) == 28
assert count_Set_Bits(10000000000000) == 30
assert count_Set_Bits(100000000000000) == 32<|endoftext|>