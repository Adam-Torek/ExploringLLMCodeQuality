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
print(is_product_even([2,2,2])) # True
print(is_product_even([1,4,3])) # False
print(is_product_even([2,4,2])) # True
print(is_product_even([1,2,4])) # True
print(is_product_even([1,3,3])) # False
print(is_product_even([2,3,4])) # False
print(is_product_even([4,2,4])) # True
print(is_product_even([1,5,3])) # False
print(is_product_even([2,5,2])) # False
print(is_product_even([1,6,3])) # True
print(is_product_even([2,6,2])) # True
print(is_product_even([1,8,3])) # True
print(is_product_even([2,8,2])) # True
print(is_product_even([1,10,5])) # False
print(is_product_even([2,10,5])) # True
print(is_product_even([1,12,6])) # True
print(is_product_even([2,12,6])) # True
print(is_product_even([1,14,7])) # False
print(is_product_even([2,14,7])) # False
print(is_product_even([1,16,8])) # True
print(is_product_even([2,16,8])) # True
print(is_product_even([1,20,10])) # True
print(is_product_even([2,20,10])) # True
print(is_product_even([1,22,11])) # False
print(is_product_even([2,22,11])) # False
print(is_product_even([1,24,12])) # True
print(is_product_even([2,24,12])) # True
print(is_product_even([1,26,13])) # False
print(is_product_even([2,26,13])) # False
print(is_product_even([1,28,14])) # True
print(is_product_even([2,28,14])) # True
print(is_product_even([1,30,15])) # False
print(is_product_even([2,30,15])) # False
print(is_product_even([1,32,16])) # True
print(is_product_even([2,32,16])) # True
print(is_product_even([1,34,17])) # False
print(is_product_even([2,34,17])) # False
print(is_product_even([1,36,18])) # True
print(is_product_even([2,36,18])) # True
print(is_product_even([1,38,19])) # False
print(is_product_even([2,38,19])) # False
print(is_product_even([1,40,20])) # True
print(is_product_even([2,40,20])) # True
print(is_product_even([1,42,21])) # False
print(is_product_even([2,42,21])) # False
print(is_product_even([1,44,22])) # True
print(is_product_even([2,44,22])) # True
print(is_product_even([1,46,23])) # False
print(is_product_even([2,46,23])) # False
print(is_product_even([1,48,24])) # True
print(is_product_even([2,4