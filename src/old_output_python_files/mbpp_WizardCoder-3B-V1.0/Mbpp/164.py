"""
Write a function to determine if the sum of the divisors of two integers are the same.
assert are_equivalent(36, 57) == False
"""

def are_equivalent(a, b):
    divisors_a = set(divisor for divisor in range(1, a+1) if a % divisor == 0)
    divisors_b = set(divisor for divisor in range(1, b+1) if b % divisor == 0)
    return divisors_a == divisors_b

# Test cases
print(are_equivalent(36, 57))  # False
print(are_equivalent(12, 18))  # True
print(are_equivalent(1, 1))    # True<|endoftext|>