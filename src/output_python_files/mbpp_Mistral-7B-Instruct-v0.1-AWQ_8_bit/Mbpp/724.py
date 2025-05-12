"""
Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
assert power_base_sum(2,100)==115
"""
def power_base_sum(base, power):
    sum = 0
    for i in range(1, power+1):
        sum += int(str(base)**i)
    return sum

assert power_base_sum(2,100)==115