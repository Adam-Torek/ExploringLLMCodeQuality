"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""


def expensive_items(dataset, n):
    """
    :param dataset: list of dictionaries
    :param n: number of items to return
    :return: list of n most expensive items
    """
    return sorted(dataset, key=lambda x: x['price'], reverse=True)[:n]


if __name__ == '__main__':
    print(expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 1))
    print(expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 2))
    print(expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 3))
    print(expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 4))
    print(expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 5))
    print(expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 6))
    print(expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 7))
    print(expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 8))
    print(expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 9))
    print(expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 10))
    print(expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 11))
    print(expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 12))
    print(expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 13))
    print(expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 14))
    print(expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 15))
    print(expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 16))
    print(expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.