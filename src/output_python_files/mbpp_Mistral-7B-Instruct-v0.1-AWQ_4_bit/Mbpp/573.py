"""
Write a python function to calculate the product of the unique numbers in a given list.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
"""

def unique_product(lst):
    """
    Calculate the product of the unique numbers in a given list.
    """
    # Create a set from the list to remove duplicates
    unique_lst = set(lst)

    # Calculate the product of the unique numbers
    product = 1
    for num in unique_lst:
        product *= num

    return product


if __name__ == "__main__":
    # Test the function with the given input
    assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000