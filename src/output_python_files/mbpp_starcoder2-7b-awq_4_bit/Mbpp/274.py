"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""

def even_binomial_Coeff_Sum(n):
    sum = 0
    for i in range(n+1):
        sum += binomial_Coeff(n,i)
    return sum

print(even_binomial_Coeff_Sum(4))
/README.md
# Python-Algorithms

This repository contains a collection of algorithms implemented in Python.

## Algorithms

### Combinatorics

* [Binomial Coefficient](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/binomial_coefficient.py)
* [Even Binomial Coefficient Sum](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/even_binomial_coefficient_sum.py)
* [Fibonacci Number](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/fibonacci_number.py)
* [Factorial](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/factorial.py)
* [Pascal's Triangle](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/pascals_triangle.py)
* [Permutation](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/permutation.py)
* [Power Set](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/power_set.py)
* [Subsets](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/subsets.py)
* [Subsets Sum](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/subsets_sum.py)
* [Subsets Sum Equal](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/subsets_sum_equal.py)
* [Subsets Sum Equal K](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/subsets_sum_equal_k.py)
* [Subsets Sum K](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/subsets_sum_k.py)
* [Subsets Sum K Equal](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/subsets_sum_k_equal.py)
* [Subsets Sum K Equal 2](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/subsets_sum_k_equal_2.py)
* [Subsets Sum K Equal 3](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/subsets_sum_k_equal_3.py)
* [Subsets Sum K Equal 4](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/subsets_sum_k_equal_4.py)
* [Subsets Sum K Equal 5](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/subsets_sum_k_equal_5.py)
* [Subsets Sum K Equal 6](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/subsets_sum_k_equal_6.py)
* [Subsets Sum K Equal 7](https://github.com/siddharth-k-s/Python-Algorithms/blob/master/combinatorics/subsets_sum_k_equal_7.py)
* [Subsets Sum K Equal 8](https://github.com/