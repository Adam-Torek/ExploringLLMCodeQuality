"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""
def expensive_items(dataset,n):
    return sorted(dataset,key=lambda x: x['price'],reverse=True)[:n]<|endoftext|>