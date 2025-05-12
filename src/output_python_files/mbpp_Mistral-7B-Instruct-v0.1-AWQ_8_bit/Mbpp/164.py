"""
Write a function to determine if the sum of the divisors of two integers are the same.
assert are_equivalent(36, 57) == False
"""

def are_equivalent(num1, num2):
    """
    Determine if the sum of the divisors of two integers are the same.
    """
    div1 = sum(range(1, num1+1))
    div2 = sum(range(1, num2+1))
    return div1 == div2

assert are_equivalent(36, 57) == False