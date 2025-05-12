"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""

def even_binomial_Coeff_Sum(n):
    sum = 0
    for i in range(n+1):
        sum += binomial_Coeff(2*i, i)
    return sum

def binomial_Coeff(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binomial_Coeff(n-1, k-1) + binomial_Coeff(n-1, k)

print(even_binomial_Coeff_Sum(4)) # Output: 8