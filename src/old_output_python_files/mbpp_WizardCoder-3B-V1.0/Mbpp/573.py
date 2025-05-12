"""
Write a python function to calculate the product of the unique numbers in a given list.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
"""

def unique_product(lst):
    unique_numbers = set(lst)
    product = 1
    for num in unique_numbers:
        product *= num
    return product

# Test the function
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000<|endoftext|>