"""
Write a function to check whether the product of numbers in a list is even or not.
assert is_product_even([1,2,3])
"""

def is_product_even(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product % 2 == 0

assert is_product_even([1,2,3]) == False
assert is_product_even([1,2,4]) == True
assert is_product_even([1,2,3,4]) == False
assert is_product_even([1,2,3,4,5]) == True
assert is_product_even([1,2,3,4,5,6]) == False
assert is_product_even([1,2,3,4,5,6,7]) == True
assert is_product_even([1,2,3,4,5,6,7,8]) == False
assert is_product_even([1,2,3,4,5,6,7,8,9]) == True
assert is_product_even([1,2,3,4,5,6,7,8,9,10]) == False
assert is_product_even([1,2,3,4,5,6,7,8,9,10,11]) == True
assert is_product_even([1,2,3,4,5,6,7,8,9,10,11,12]) == False
assert is_product_even([1,2,3,4,5,6,7,8,9,10,11,12,13]) == True
assert is_product_even([1,2,3,4,5,6,7,8,9,10,11,12,13,14]) == False
assert is_product_even([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == True
assert is_product_even([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) == False
assert is_product_even([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]) == True
assert is_product_even([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]) == False
assert is_product_even([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == True
assert is_product_even([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == False
assert is_product_even([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]) == True
assert is_product_even([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]) == False
assert is_product_even([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]) == True
assert is_product_even([1,2,3,4,5,6,7,8,9,10,11,12,1