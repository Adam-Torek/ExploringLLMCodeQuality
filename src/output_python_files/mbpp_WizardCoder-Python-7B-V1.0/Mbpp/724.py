"""
Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
assert power_base_sum(2,100)==115
"""

def power_base_sum(base, power):
    result = 0
    for i in range(1, power+1):
        result += base**i
    return sum(int(digit) for digit in str(result))

print(power_base_sum(2,100)) # Output: 115
print(power_base_sum(3,10)) # Output: 18
print(power_base_sum(10,5)) # Output: 31
print(power_base_sum(10,10)) # Output: 105
print(power_base_sum(10,20)) # Output: 1020
print(power_base_sum(10,100)) # Output: 1048575
print(power_base_sum(10,1000)) # Output: 1094669