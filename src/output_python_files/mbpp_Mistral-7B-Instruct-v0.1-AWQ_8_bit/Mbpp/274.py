"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""
def even_binomial_Coeff_Sum(n):
    """
    :param n: positive integer
    :return: sum of even index binomial coefficients
    """
    if n % 2 == 0:
        return sum(binomial_coefficients(n, k) for k in range(n))
    else:
        return sum(binomial_coefficients(n, k) for k in range(n-1))

def binomial_coefficients(n, k):
    """
    :param n: positive integer
    :param k: positive integer
    :return: binomial coefficient
    """
    if k == 0:
        return 1
    elif k == n:
        return 1
    else:
        return (n choose k) * (n-k choose n-k)

if __name__ == '__main__':
    assert even_binomial_Coeff_Sum(4) == 8
    assert even_binomial_Coeff_Sum(5) == 10
    assert even_binomial_Coeff_Sum(6) == 12
    assert even_binomial_Coeff_Sum(7) == 14