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
print(is_product_even([1,3,3])) # False
print(is_product_even([2,4,4])) # True
print(is_product_even([1,5,3])) # False
print(is_product_even([2,5,2])) # False
print(is_product_even([1,6,3])) # True
print(is_product_even([2,6,2])) # True
print(is_product_even([1,8,3])) # True
print(is_product_even([2,8,2])) # True
print(is_product_even([1,10,5])) # False
print(is_product_even([2,10,5])) # True
print(is_product_even([1,12,4])) # True
print(is_product_even([2,12,4])) # True
print(is_product_even([1,14,3])) # False
print(is_product_even([2,14,4])) # True
print(is_product_even([1,16,4])) # True
print(is_product_even([2,16,4])) # True
print(is_product_even([1,20,5])) # False
print(is_product_even([2,20,5])) # True
print(is_product_even([1,22,4])) # True
print(is_product_even([2,22,4])) # True
print(is_product_even([1,24,3])) # False
print(is_product_even([2,24,4])) # True
print(is_product_even([1,26,4])) # True
print(is_product_even([2,26,4])) # True
print(is_product_even([1,28,3])) # False
print(is_product_even([2,28,4])) # True
print(is_product_even([1,30,5])) # False
print(is_product_even([2,30,5])) # True
print(is_product_even([1,32,4])) # True
print(is_product_even([2,32,4])) # True
print(is_product_even([1,34,3])) # False
print(is_product_even([2,34,4])) # True
print(is_product_even([1,36,4])) # True
print(is_product_even([2,36,4])) # True
print(is_product_even([1,40,5])) # False
print(is_product_even([2,40,5])) # True
print(is_product_even([1,42,4])) # True
print(is_product_even([2,42,4])) # True
print(is_product_even([1,44,3])) # False
print(is_product_even([2,44,4])) # True
print(is_product_even([1,46,4])) # True
print(is_product_even([2,46,4])) # True
print(is_product_even([1,48,3])) # False
print(is_product_even([2,48,4])) # True
print(is_product_even([1,50,5])) # False
print(is_product_even([2,50,5])) # True
print(is_product_even([1,52,4])) #