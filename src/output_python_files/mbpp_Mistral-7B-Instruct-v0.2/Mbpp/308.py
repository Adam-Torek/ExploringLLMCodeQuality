"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""
def large_product(list1, list2, num):
    # Create a list of tuples from the cartesian product of the two lists
    product_list = [(i, j) for i in list1 for j in list2]

    # Sort the list of tuples in descending order based on their product
    product_list.sort(key=lambda x: x[0]*x[1], reverse=True)

    # Return the first 'num' tuples from the sorted list
    return [(i, j) for i, j in product_list[:num]]

assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[(6, 3), (5, 6), (5, 10)]
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)[0][0]*assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)[0][1]==60
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)[1][0]*assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)[1][1]==54
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)[2][0]*assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)[2][1]==50</s>