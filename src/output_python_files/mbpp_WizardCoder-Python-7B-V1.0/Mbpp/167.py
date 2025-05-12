"""
Write a python function to find the smallest power of 2 greater than or equal to n.
assert next_power_of_2(0) == 1
"""

def next_power_of_2(n):
    if n == 0:
        return 1
    else:
        return 2**(n-1).bit_length()

# Test cases
print(next_power_of_2(0)) # Output: 1
print(next_power_of_2(1)) # Output: 1
print(next_power_of_2(2)) # Output: 2
print(next_power_of_2(3)) # Output: 4
print(next_power_of_2(10)) # Output: 16
print(next_power_of_2(16)) # Output: 16
print(next_power_of_2(21)) # Output: 32
print(next_power_of_2(32)) # Output: 32
print(next_power_of_2(64)) # Output: 64
print(next_power_of_2(100)) # Output: 128
print(next_power_of_2(1024)) # Output: 1024
print(next_power_of_2(1025)) # Output: 1024
print(next_power_of_2(1023)) # Output: 1024
print(next_power_of_2(1027)) # Output: 1028
print(next_power_of_2(1028)) # Output: 1028
print(next_power_of_2(1029)) # Output: 2048
print(next_power_of_2(1030)) # Output: 2048
print(next_power_of_2(1031)) # Output: 2048
print(next_power_of_2(1032)) # Output: 2048
print(next_power_of_2(1033)) # Output: 2048
print(next_power_of_2(1034)) # Output: 2048
print(next_power_of_2(1035)) # Output: 2048
print(next_power_of_2(1036)) # Output: 2048
print(next_power_of_2(1037)) # Output: 2048
print(next_power_of_2(1038)) # Output: 2048
print(next_power_of_2(1039)) # Output: 2048
print(next_power_of_2(1040)) # Output: 2048
print(next_power_of_2(1041)) # Output: 2048
print(next_power_of_2(1042)) # Output: 2048
print(next_power_of_2(1043)) # Output: 2048
print(next_power_of_2(1044)) # Output: 2048
print(next_power_of_2(1045)) # Output: 2048
print(next_power_of_2(1046)) # Output: 2048
print(next_power_of_2(1047)) # Output: 2048
print(next_power_of_2(1048)) # Output: 2048
print(next_power_of_2(1049)) # Output: 2048
print(next_power_of_2(1050)) # Output: 2048
print(next_power_of_2(1051)) # Output: 2048
print(next_power_of_2(1052)) # Output: 2048
print(next_power_of_2(1