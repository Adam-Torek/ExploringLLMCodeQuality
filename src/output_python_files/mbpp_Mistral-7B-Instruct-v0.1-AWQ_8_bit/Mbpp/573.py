"""
Write a python function to calculate the product of the unique numbers in a given list.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
"""

def unique_product(lst):
    # Create a set from the list to remove duplicates
    unique_lst = set(lst)
    # Multiply all the elements in the set
    product = 1
    for num in unique_lst:
        product *= num
    return product

# Test the function
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000