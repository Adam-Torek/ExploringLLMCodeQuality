"""
Write a function to check whether the product of numbers in a list is even or not.
assert is_product_even([1,2,3])
"""

def is_product_even(lst):
    product = reduce(lambda x,y: x*y, lst)
    return product % 2 == 0

# assert is_product_even([1,2,3])
# assert is_product_even([2,3,4])
# assert is_product_even([1,2,3,4])
# assert is_product_even([-1,2,3,4])
# assert is_product_even([1,2,3,4,5])