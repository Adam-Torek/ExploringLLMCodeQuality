"""
Write a python function to calculate the product of the unique numbers in a given list.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
"""
def unique_product(numbers):
    unique_numbers = list(set(numbers)) # convert list to set to remove duplicates, then convert back to list
    product = 1
    for number in unique_numbers:
        product *= number
    return product

assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000