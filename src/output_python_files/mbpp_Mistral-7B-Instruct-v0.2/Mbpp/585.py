"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""
def expensive_items(items, n):
    """
    :param items: list of dictionaries, where each dictionary represents an item with name and price
    :param n: int, number of most expensive items to return
    :return: list of dictionaries, where each dictionary represents the most expensive n items
    """
    # sort the items by price in descending order
    items.sort(key=lambda x: x['price'], reverse=True)
    # return the first n items
    return items[:n]

# test the function
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22},{'name': 'Item-3', 'price': 333.33}],2)==[{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-1', 'price': 101.1}]
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22},{'name': 'Item-3', 'price': 333.33},{'name': 'Item-4', 'price': 444.44}],3)==[{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-1', 'price': 101.1}, {'name': 'Item-4', 'price': 444.44}]
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22},{'name': 'Item-3', 'price': 333.33},{'name': 'Item-4', 'price': 444.44},{'name': 'Item-5', 'price': 222.22}],5)==[{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-1', 'price': 101.1}, {'name': 'Item-4', 'price': 444.44}, {'name': 'Item-3', 'price': 333.33}, {'name': 'Item-5', 'price': 222.22}]