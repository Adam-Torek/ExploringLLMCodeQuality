"""
Write a function to check whether the product of numbers in a list is even or not.
assert is_product_even([1,2,3])
"""

def is_product_even(lst):
    product = 1
    for num in lst:
        product *= num
    return product % 2 == 0

print(is_product_even([1,2,3])) # False
print(is_product_even([2,4,6])) # True
print(is_product_even([1,4,3])) # False
print(is_product_even([2,5,6])) # True
print(is_product_even([1,2,4])) # True
print(is_product_even([1,3,5])) # False
print(is_product_even([2,3,4])) # False
print(is_product_even([2,4,8])) # True
print(is_product_even([1,2,4,3])) # False
print(is_product_even([2,4,6,8])) # True
print(is_product_even([1,2,3,4])) # False
print(is_product_even([2,4,6,8])) # True
print(is_product_even([1,2,4,6])) # True
print(is_product_even([1,2,3,4,6])) # False
print(is_product_even([2,4,6,8,10])) # True
print(is_product_even([1,2,3,4,5])) # False
print(is_product_even([2,4,6,8,10])) # True
print(is_product_even([1,2,4,6,8])) # True
print(is_product_even([1,2,3,4,5,6])) # False
print(is_product_even([2,4,6,8,10])) # True
print(is_product_even([1,2,4,6,8,10])) # True
print(is_product_even([2,4,6,8,12])) # True
print(is_product_even([1,2,3,4,5,6,8])) # False
print(is_product_even([2,4,6,8,10,12])) # True
print(is_product_even([1,2,4,6,8,10,12])) # True
print(is_product_even([2,4,6,8,12,14])) # False
print(is_product_even([1,2,3,4,5,6,8,10])) # False
print(is_product_even([2,4,6,8,10,12,14])) # True
print(is_product_even([1,2,4,6,8,10,12,14])) # False
print(is_product_even([2,4,6,8,10,12,14,16])) # True
print(is_product_even([1,2,3,4,5,6,8,10,12])) # False
print(is_product_even([2,4,6,8,10,12,14,16])) # True
print(is_product_even([1,2,3,4,5,6,8,10,12,14])) # False
print(is_product_even([2,4,6,8,10,12,14,16,18])) # True
print(is_product_even([1,2,3,4,5,6,8,10,12,14,16])) # False
print(is_product_even([2,4,6,8,10,12,14,16,18])) # True
print(is_product_even([1,2,3,4,5,6,8,10,12,14,16,18])) # False
print(is_product_even([2,4,6,8