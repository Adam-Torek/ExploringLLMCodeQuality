"""
Write a python function to calculate the product of the unique numbers in a given list.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
"""

def unique_product(lst):
    unique_lst = list(set(lst))
    product = 1
    for num in unique_lst:
        product *= num
    return product

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40])) # Output: 720000000