"""
Write a python function to count the number of set bits (binary digits with value 1) in a given number.
assert count_Set_Bits(2) == 1
"""

def count_Set_Bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

print(count_Set_Bits(2)) # Output: 1
print(count_Set_Bits(7)) # Output: 3
print(count_Set_Bits(9)) # Output: 2
print(count_Set_Bits(10)) # Output: 2
print(count_Set_Bits(15)) # Output: 4
print(count_Set_Bits(23)) # Output: 3
print(count_Set_Bits(25)) # Output: 1
print(count_Set_Bits(32)) # Output: 1
print(count_Set_Bits(0)) # Output: 0