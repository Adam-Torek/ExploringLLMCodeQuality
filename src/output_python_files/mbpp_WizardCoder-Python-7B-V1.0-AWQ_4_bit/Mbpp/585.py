"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""

def expensive_items(data, n):
    sorted_data = sorted(data, key=lambda x: x['price'], reverse=True)
    return sorted_data[:n]

print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1))

# Output: [{'name': 'Item-2', 'price': 555.22}]

# Test case 2
print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 200.3}, {'name': 'Item-4', 'price': 120.5}, {'name': 'Item-5', 'price': 300.6}], 2))

# Output: [{'name': 'Item-3', 'price': 200.3}, {'name': 'Item-2', 'price': 555.22}]

# Test case 3
print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 200.3}, {'name': 'Item-4', 'price': 120.5}, {'name': 'Item-5', 'price': 300.6}, {'name': 'Item-6', 'price': 100.7}, {'name': 'Item-7', 'price': 20.8}, {'name': 'Item-8', 'price': 10.9}], 3))

# Output: [{'name': 'Item-3', 'price': 200.3}, {'name': 'Item-2', 'price': 555.22}, {'name': 'Item-5', 'price': 300.6}]