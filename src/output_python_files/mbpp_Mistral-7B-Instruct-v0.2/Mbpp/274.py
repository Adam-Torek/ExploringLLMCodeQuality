"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""
def binomial_coefficient(n, k):
    """
    Calculate binomial coefficient using the formula: nCk = n! / (k!(n-k)!)
    """
    if k > n or k < 0:
        return 0
    numerator = 1
    for i in range(k+1, n+1):
        numerator *= i
    denominator = 1
    for i in range(1, min(k, n-k)+1):
        denominator *= i
    return numerator // denominator

def even_binomial_Coeff_Sum(n):
    """
    Calculate the sum of even index binomial coefficients for n
    """
    sum = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum += binomial_coefficient(n, i//2)
    return sum

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])</s>