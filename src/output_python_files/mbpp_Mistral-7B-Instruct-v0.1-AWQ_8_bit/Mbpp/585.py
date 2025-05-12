"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""

def expensive_items(data,n):
    """
    This function takes in a list of dictionaries and returns a list of the n most expensive items.
    """
    # sort the data by price in descending order
    sorted_data = sorted(data,key=lambda x:x['price'],reverse=True)
    # return the first n items
    return [item for item in sorted_data[:n]]

# test the function
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]