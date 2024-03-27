"""
Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
assert power_base_sum(2,100)==115
"""
def power_base_sum(base, power):
    sum = 0
    while power > 0:
        digit = base % 10
        sum += digit
        power -= 1
        base //= 10
    return sum

assert power_base_sum(2,100)==115<|endoftext|>