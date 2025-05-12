"""
Write a python function to find the sum of the product of consecutive binomial co-efficients.
assert sum_Of_product(3) == 15
"""
import math

def binomial_coefficient(n, k):
    """
    Calculate the binomial coefficient nCk
    """
    return math.comb(n, k)

def sum_of_product(n):
    """
    Calculate the sum of the product of consecutive binomial coefficients
    """
    result = 0
    for i in range(1, n+1):
        product = binomial_coefficient(n, i)
        result += product
    return result

if __name__ == "__main__":
    assert sum_of_product(3) == 15
    print("Test passed")