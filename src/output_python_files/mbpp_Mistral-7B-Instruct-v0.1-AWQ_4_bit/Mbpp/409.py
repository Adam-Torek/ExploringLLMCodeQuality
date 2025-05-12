"""
Write a function to find the minimum product from the pairs of tuples within a given list.
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
"""

def min_product_tuple(lst):
    """
    This function takes a list of tuples as an input and returns the minimum product of the pairs of tuples.
    """
    # sorting the list of tuples in ascending order
    lst.sort()
    # initializing the minimum product to be 1
    min_product = 1
    # iterating over the list of tuples
    for i in range(len(lst)):
        # checking if the current tuple's product is less than the minimum product
        if lst[i][0]*lst[i][1] < min_product:
            # updating the minimum product with the current tuple's product
            min_product = lst[i][0]*lst[i][1]
    # returning the minimum product
    return min_product

# testing the function
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 8