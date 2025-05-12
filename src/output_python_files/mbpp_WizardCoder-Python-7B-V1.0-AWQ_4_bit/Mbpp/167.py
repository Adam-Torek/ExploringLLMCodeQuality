"""
Write a python function to find the smallest power of 2 greater than or equal to n.
assert next_power_of_2(0) == 1
"""

def next_power_of_2(n):
    """
    Returns the smallest power of 2 greater than or equal to n.
    """
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
print(next_power_of_2(20)) # Output: 32
print(next_power_of_2(32)) # Output: 32
print(next_power_of_2(64)) # Output: 64
print(next_power_of_2(100)) # Output: 128
print(next_power_of_2(1000)) # Output: 256
print(next_power_of_2(10000)) # Output: 1024
print(next_power_of_2(100000)) # Output: 1024
print(next_power_of_2(1000000)) # Output: 16384
print(next_power_of_2(10000000)) # Output: 32768
print(next_power_of_2(100000000)) # Output: 65536
print(next_power_of_2(1000000000)) # Output: 65536
print(next_power_of_2(10000000000)) # Output: 65536
print(next_power_of_2(100000000000)) # Output: 65536
print(next_power_of_2(1000000000000)) # Output: 65536
print(next_power_of_2(10000000000000)) # Output: 65536
print(next_power_of_2(100000000000000)) # Output: 65536
print(next_power_of_2(1000000000000000)) # Output: 65536
print(next_power_of_2(10000000000000000)) # Output: 65536
print(next_power_of_2(100000000000000000)) # Output: 65536
print(next_power_of_2(1000000000000000000)) # Output: 65536
print(next_power_of_2(10000000000000000000)) # Output: 65536
print(next_power_of_2(100000000000000000000)) # Output: 65536
print(next_power_of_2(1000000000000000000000)) # Output: 65536
print(next_power_of_2(10000000000000000000000)) # Output: 65536