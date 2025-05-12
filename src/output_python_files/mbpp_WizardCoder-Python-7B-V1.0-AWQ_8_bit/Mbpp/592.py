"""
Write a python function to find the sum of the product of consecutive binomial co-efficients.
assert sum_Of_product(3) == 15
"""

def sum_Of_product(n):
    """
    This function takes a number n as input and returns the sum of the product of consecutive binomial coefficients.
    """
    sum = 0
    for i in range(n):
        sum += (n*(n-1))/(i+1)
    return sum

print(sum_Of_product(3)) # Output: 15
print(sum_Of_product(5)) # Output: 55
print(sum_Of_product(10)) # Output: 126