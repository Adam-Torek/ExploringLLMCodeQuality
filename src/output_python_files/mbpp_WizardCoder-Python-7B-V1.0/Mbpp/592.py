"""
Write a python function to find the sum of the product of consecutive binomial co-efficients.
assert sum_Of_product(3) == 15
"""

def sum_Of_product(n):
    import math
    return sum([math.comb(n, i) * math.comb(n, n-i) for i in range(n+1)])

print(sum_Of_product(3)) # Output: 15
print(sum_Of_product(5)) # Output: 126
print(sum_Of_product(10)) # Output: 4183