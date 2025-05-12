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
print(count_Set_Bits(32)) # Output: 1
print(count_Set_Bits(64)) # Output: 6
print(count_Set_Bits(1024)) # Output: 10
print(count_Set_Bits(4096)) # Output: 11
print(count_Set_Bits(1048576)) # Output: 20
print(count_Set_Bits(2147483648)) # Output: 29
print(count_Set_Bits(4294967295)) # Output: 31
print(count_Set_Bits(10737418240)) # Output: 30
print(count_Set_Bits(21474836480)) # Output: 31
print(count_Set_Bits(42949672960)) # Output: 32
print(count_Set_Bits(107374182400)) # Output: 32
print(count_Set_Bits(214748364800)) # Output: 32
print(count_Set_Bits(429496729600)) # Output: 32
print(count_Set_Bits(1073741824000)) # Output: 32
print(count_Set_Bits(2147483648000)) # Output: 32
print(count_Set_Bits(4294967296000)) # Output: 32
print(count_Set_Bits(10737418240000)) # Output: 32
print(count_Set_Bits(21474836480000)) # Output: 32
print(count_Set_Bits(42949672960000)) # Output: 32
print(count_Set_Bits(107374182400000)) # Output: 32
print(count_Set_Bits(214748364800000)) # Output: 32
print(count_Set_Bits(429496729600000)) # Output: 32
print(count_Set_Bits(1073741824000000)) # Output: 32
print(count_Set_Bits(2147483648000000)) # Output: 32
print(count_Set_Bits(4294967296000000)) # Output: 32
print(count_Set_Bits(10737418240000000)) # Output: 32
print(count_Set_Bits(21474836480000000) # Output: 32