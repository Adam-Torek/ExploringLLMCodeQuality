"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""

def expensive_items(data, n):
    sorted_data = sorted(data, key=lambda x: x['price'], reverse=True)
    return sorted_data[:n]

print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1))
print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 55.22},{'name': 'Item-3', 'price': 120.3},{'name': 'Item-4', 'price': 100.5},{'name': 'Item-5', 'price': 200.1},{'name': 'Item-6', 'price': 50.2}],3))

# Output: [{'name': 'Item-2', 'price': 55.22}]
# Output: [{'name': 'Item-5', 'price': 200.1}, {'name': 'Item-1', 'price': 101.1}, {'name': 'Item-4', 'price': 100.5}]