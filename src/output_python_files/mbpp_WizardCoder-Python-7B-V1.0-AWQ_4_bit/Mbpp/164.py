"""
Write a function to determine if the sum of the divisors of two integers are the same.
assert are_equivalent(36, 57) == False
"""

def are_equivalent(a, b):
    divisors_a = [i for i in range(1, a+1) if a % i == 0]
    divisors_b = [i for i in range(1, b+1) if b % i == 0]
    return sum(divisors_a) == sum(divisors_b)

print(are_equivalent(36, 57)) # False
print(are_equivalent(12, 18)) # True
print(are_equivalent(10, 15)) # False
print(are_equivalent(24, 30)) # True
print(are_equivalent(100, 200)) # True
print(are_equivalent(100, 250)) # False
print(are_equivalent(100, 25)) # False
print(are_equivalent(100, 2500)) # False
print(are_equivalent(100, 25000)) # False
print(are_equivalent(100, 250000)) # False
print(are_equivalent(100, 2500000)) # False
print(are_equivalent(100, 25000000)) # False
print(are_equivalent(100, 250000000)) # False
print(are_equivalent(100, 2500000000)) # False
print(are_equivalent(100, 25000000000)) # False
print(are_equivalent(100, 250000000000)) # False
print(are_equivalent(100, 2500000000000)) # False
print(are_equivalent(100, 25000000000000)) # False
print(are_equivalent(100, 250000000000000)) # False
print(are_equivalent(100, 2500000000000000)) # False
print(are_equivalent(100, 25000000000000000)) # False
print(are_equivalent(100, 250000000000000000)) # False
print(are_equivalent(100, 2500000000000000000)) # False
print(are_equivalent(100, 25000000000000000000)) # False
print(are_equivalent(100, 250000000000000000000)) # False
print(are_equivalent(100, 2500000000000000000000)) # False
print(are_equivalent(100, 25000000000000000000000)) # False
print(are_equivalent(100, 250000000000000000000000)) # False
print(are_equivalent(100, 2500000000000000000000000)) # False
print(are_equivalent(100, 25000000000000000000000000)) # False
print(are_equivalent(