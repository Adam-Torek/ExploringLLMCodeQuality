"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""
def binomial_coefficient(n, k):
    """
    Calculate the binomial coefficient using the formula: nCk = n! / (k!(n-k)!)
    """
    if k > n or k < 0:
        return 0
    return (1/fact(k)) * (1/fact(n-k)) * fact(n)

def fact(n):
    """
    Calculate the factorial of a number
    """
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def even_binomial_Coeff_Sum(n):
    """
    Find the sum of even index binomial coefficients
    """
    sum = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum += binomial_coefficient(n, i)
    return sum

if __name__ == "__main__":
    assert even_binomial_Coeff_Sum(4) == 8
    print("Test passed!")