"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""

def expensive_items(data, n):
    sorted_data = sorted(data, key=lambda x: x['price'], reverse=True)
    return sorted_data[:n]

# Test cases
print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)) # should return [{'name': 'Item-2', 'price': 555.22}]
print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 12.5}, {'name': 'Item-4', 'price': 120.0}],2)) # should return [{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-1', 'price': 101.1}]
print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 12.5}, {'name': 'Item-4', 'price': 120.0}],3)) # should return [{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-1', 'price': 101.1}, {'name': 'Item-4', 'price': 120.0}]
print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 12.5}, {'name': 'Item-4', 'price': 120.0}],4)) # should return [{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-1', 'price': 101.1}, {'name': 'Item-4', 'price': 120.0}]
print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 12.5}, {'name': 'Item-4', 'price': 120.0}],0)) # should return []
print(expensive_items([],1)) # should return []
print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 12.5}, {'name': 'Item-4', 'price': 120.0}],0)) # should return []
print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 12.5}, {'name': 'Item-4', 'price': 120.0}],-1)) # should return []
print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 12.5}, {'name': 'Item-4', 'price': 120.0}],5)) # should return [{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-1', 'price': 101.1}, {'name': 'Item-4',