"""
Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
assert power_base_sum(2,100)==115
"""
def power_base_sum(base, power):
    sum = 0
    while power > 0:
        sum += int(pow(base, power % 5))
        power //= 5
    return sum

assert power_base_sum(2,100) == 115