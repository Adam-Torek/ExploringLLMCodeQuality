"""
Write a function to check whether the product of numbers in a list is even or not.
assert is_product_even([1,2,3])
"""
def is_product_even(numbers):
    """
    :param numbers: list of integers
    :return: boolean
    """
    product = 1
    for number in numbers:
        product *= number
    return product % 2 == 0

assert is_product_even([1,2,3]) == False
assert is_product_even([2,2,2]) == True
assert is_product_even([-2,-2,-2]) == True
assert is_product_even([1,2,4]) == True
assert is_product_even([1,2,4,4]) == True