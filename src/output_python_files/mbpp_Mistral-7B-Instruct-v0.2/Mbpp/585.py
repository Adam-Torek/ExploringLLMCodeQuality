"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""
def expensive_items(items, n):
    # Sort the items in descending order of price
    items.sort(key=lambda x: x['price'], reverse=True)

    # Return the first n items
    return items[:n]

# Test the function
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 333.33}],2)==[{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-1', 'price': 101.1}]
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 333.33}, {'name': 'Item-4', 'price': 777.77}],3)==[{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-1', 'price': 101.1}, {'name': 'Item-4', 'price': 777.77}]
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 333.33}, {'name': 'Item-4', 'price': 777.77}, {'name': 'Item-5', 'price': 999.99}],4)==[{'name': 'Item-5', 'price': 999.99}, {'name': 'Item-2', 'price': 555.22}, {'name': 'Item-1', 'price': 101.1}, {'name': 'Item-4', 'price': 777.77}]
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 333.33}, {'name': 'Item-4', 'price': 777.77}, {'name': 'Item-5', 'price': 999.99}, {'name': 'Item-6', 'price': 888.88}],5)==[{'name': 'Item-5', 'price': 999.99}, {'name': 'Item-2', 'price': 555.22}, {'name': 'Item-1', 'price': 101.1}, {'name': 'Item-4', 'price': 777.77}, {'name': 'Item-6', 'price': 888.88}]
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 333.33}, {'name': 'Item-4', 'price': 777.77}, {'name': 'Item-5', 'price': 999.99}, {'name': 'Item-6', 'price': 888.88}, {'name': 'Item-7', 'price': 666.66}],6)==[{'name': 'Item-5', 'price': 999.99}, {'