"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""

def even_binomial_Coeff_Sum(n):
    """
    This function takes in a positive integer n and finds the sum of even index binomial coefficients.
    """
    sum = 0
    for i in range(1, n+1, 2):
        sum += i * (n-i+1) // 2
    return sum

# Test the function
assert even_binomial_Coeff_Sum(4) == 8<|endoftext|>