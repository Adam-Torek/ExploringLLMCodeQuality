"""
Write a function to find the minimum product from the pairs of tuples within a given list.
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
"""

def min_product_tuple(lst):
    """
    This function takes a list of tuples as an input and returns the minimum product of all pairs of tuples in the list.
    """
    # sorting the list
    lst.sort()
    # initializing product to 1
    product = 1
    # iterating over the list
    for i in range(len(lst)-1):
        # multiplying the current product with the next tuple
        product *= lst[i+1][0]
    # returning the minimum product
    return product

# testing the function
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 8