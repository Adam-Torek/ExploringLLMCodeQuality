"""
Write a python function to find the sum of the product of consecutive binomial co-efficients.
assert sum_Of_product(3) == 15
"""

def sum_Of_product(n):
    if n == 1:
        return 1
    else:
        return (n * (n - 1)) + sum_Of_product(n - 1)

print(sum_Of_product(3))<|endoftext|>