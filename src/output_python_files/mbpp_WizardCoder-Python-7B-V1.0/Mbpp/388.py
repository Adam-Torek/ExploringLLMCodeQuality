"""
Write a python function to find the highest power of 2 that is less than or equal to n.
assert highest_Power_of_2(10) == 8
"""

def highest_Power_of_2(n):
    power = 0
    while (n > 0):
        n >>= 1
        power += 1
    return 2**(power-1)

print(highest_Power_of_2(10)) # Output: 8
print(highest_Power_of_2(16)) # Output: 16
print(highest_Power_of_2(20)) # Output: 16
print(highest_Power_of_2(32)) # Output: 32
print(highest_Power_of_2(64)) # Output: 64
print(highest_Power_of_2(128)) # Output: 128
print(highest_Power_of_2(256)) # Output: 128
print(highest_Power_of_2(512)) # Output: 256
print(highest_Power_of_2(1024)) # Output: 1024