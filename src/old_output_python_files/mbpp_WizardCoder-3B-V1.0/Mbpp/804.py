"""
Write a function to check whether the product of numbers in a list is even or not.
assert is_product_even([1,2,3])
"""
def is_product_even(lst):
    product = 1
    for num in lst:
        product *= num
    return product % 2 == 0

# Test cases
print(is_product_even([1,2,3])) # True
print(is_product_even([4,6,8])) # False
print(is_product_even([1,2,3,4])) # True<|endoftext|>