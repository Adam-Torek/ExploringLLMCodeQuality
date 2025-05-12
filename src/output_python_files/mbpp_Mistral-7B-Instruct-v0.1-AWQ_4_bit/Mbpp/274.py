"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""
def even_binomial_Coeff_Sum(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return sum(even_binomial_Coeff(n,i) for i in range(2,n+1))

def even_binomial_Coeff(n,i):
    """
    :type n: int
    :type i: int
    :rtype: int
    """
    if i == 0:
        return 1
    elif i == 1:
        return n
    else:
        return (n*(n-1))//(i*(i-1)) - even_binomial_Coeff(n,i-1) - even_binomial_Coeff(n,i-2)