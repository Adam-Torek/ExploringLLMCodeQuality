"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""
def large_product(list1, list2, num):
    # Create a list of tuples, where each tuple contains one element from list1 and one element from list2
    product_list = [(i, j) for i in list1 for j in list2]
    # Sort the list of tuples in descending order based on their product
    product_list.sort(key=lambda x: x[0]*x[1], reverse=True)
    # Return the first num elements of the sorted list
    return [product[0] * product[1] for product in product_list[:num]]

assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
assert large_product([1, 2, 3, 4, 5],[3, 6, 8, 9, 10],2)==[48, 36]
assert large_product([1, 2, 3, 4, 5],[3, 6, 8, 9, 10],5)==[120, 108, 105, 96, 90]