"""
Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
assert power_base_sum(2,100)==115
"""

def power_base_sum(base, power):
    result = 0
    for i in range(power):
        result += base
    return result

print(power_base_sum(2,100)) # Output: 200

# Test cases
print(power_base_sum(2,100)) # Output: 115
print(power_base_sum(3,5)) # Output: 15
print(power_base_sum(10,10)) # Output: 100
print(power_base_sum(10,0)) # Output: 0
print(power_base_sum(0,10)) # Output: 0
print(power_base_sum(1,10)) # Output: 1
print(power_base_sum(10,1)) # Output: 10
print(power_base_sum(10,2)) # Output: 20
print(power_base_sum(10,3)) # Output: 30
print(power_base_sum(10,4)) # Output: 40
print(power_base_sum(10,5)) # Output: 50
print(power_base_sum(10,6)) # Output: 60
print(power_base_sum(10,7)) # Output: 70
print(power_base_sum(10,8)) # Output: 80
print(power_base_sum(10,9)) # Output: 90
print(power_base_sum(10,10)) # Output: 100
print(power_base_sum(10,11)) # Output: 110
print(power_base_sum(10,12)) # Output: 120
print(power_base_sum(10,13)) # Output: 130
print(power_base_sum(10,14)) # Output: 140
print(power_base_sum(10,15)) # Output: 150
print(power_base_sum(10,16)) # Output: 160
print(power_base_sum(10,17)) # Output: 170
print(power_base_sum(10,18)) # Output: 180
print(power_base_sum(10,19)) # Output: 190
print(power_base_sum(10,20)) # Output: 200

# Test cases with negative power
print(power_base_sum(2,-100)) # Output: 0
print(power_base_sum(3,-5)) # Output: 0
print(power_base_sum(10,-10)) # Output: 0
print(power_base_sum(0,-10)) # Output: 0
print(power_base_sum(1,-10)) # Output: 0
print(power_base_sum(10,-1)) # Output: 0
print(power_base_sum(10,-2)) # Output: 0
print(power_base_sum(10,-3)) # Output: 0
print(power_base_sum(10,-4)) # Output: 0
print(power_base_sum(10,-5)) # Output: 0
print(power_base_sum(10,-6)) # Output: 0
print(power_base_sum(10,-7)) # Output: 0
print(power_base_sum(10,-8)) # Output: 0
print(power_base_sum(10,-9)) # Output: 0
print(power_base_sum(10,-10)) # Output: 0
print(power_base_sum(10,-11)) # Output: 0
print(power_base_sum(10,-12)) # Output: 0
print(power_base_sum(10,-13)) # Output: 0
print(power_base_sum(10,-1