"""
Write a function to check whether the product of numbers in a list is even or not.
assert is_product_even([1,2,3])
"""

def is_product_even(list):
    product = 1
    for i in list:
        product *= i
    if product % 2 == 0:
        return True
    else:
        return False

assert is_product_even([1,2,3]) == False
assert is_product_even([1,2,4]) == True
assert is_product_even([1,2,5]) == False
assert is_product_even([1,2,6]) == True
assert is_product_even([1,2,7]) == False
assert is_product_even([1,2,8]) == True
assert is_product_even([1,2,9]) == False
assert is_product_even([1,2,10]) == True
assert is_product_even([1,2,11]) == False
assert is_product_even([1,2,12]) == True
assert is_product_even([1,2,13]) == False
assert is_product_even([1,2,14]) == True
assert is_product_even([1,2,15]) == False
assert is_product_even([1,2,16]) == True
assert is_product_even([1,2,17]) == False
assert is_product_even([1,2,18]) == True
assert is_product_even([1,2,19]) == False
assert is_product_even([1,2,20]) == True
assert is_product_even([1,2,21]) == False
assert is_product_even([1,2,22]) == True
assert is_product_even([1,2,23]) == False
assert is_product_even([1,2,24]) == True
assert is_product_even([1,2,25]) == False
assert is_product_even([1,2,26]) == True
assert is_product_even([1,2,27]) == False
assert is_product_even([1,2,28]) == True
assert is_product_even([1,2,29]) == False
assert is_product_even([1,2,30]) == True
assert is_product_even([1,2,31]) == False
assert is_product_even([1,2,32]) == True
assert is_product_even([1,2,33]) == False
assert is_product_even([1,2,34]) == True
assert is_product_even([1,2,35]) == False
assert is_product_even([1,2,36]) == True
assert is_product_even([1,2,37]) == False
assert is_product_even([1,2,38]) == True
assert is_product_even([1,2,39]) == False
assert is_product_even([1,2,40]) == True
assert is_product_even([1,2,41]) == False
assert is_product_even([1,2,42]) == True
assert is_product_even([1,2,43]) == False
assert is_product_even([1,2,44]) == True
assert is_product_even([1,2,45]) == False
assert is_product_even([1,2,46]) == True
assert is_product_even([1,2,47]) == False
assert is_product_even([1,2,48]) == True
assert is_product_even([1,2,49]) == False
assert is_product_even([1,2,50]) == True
assert is_product_even([1,2,51]) == False
assert is_product_even([1,2,52]) == True
assert is_product_even([1,2,53]) == False
assert is_product_even([1,2,54]) == True
assert is_product_even([1,2,55]) == False
assert is_product_even([1,2,56]) == True
assert is_product_even([1,2,57]) == False
assert is_product_even([1,2,58