"""
Write a python function that takes in a tuple and an element and counts the occcurences of the element in the tuple.
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
"""

def count_X(tup, x):
    count = 0
    for i in tup:
        if i == x:
            count += 1
    return count

print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4))

"""
Write a python function that takes in a tuple and an element and returns a new tuple with the element removed.
assert remove_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
"""

def remove_X(tup, x):
    new_tup = []
    for i in tup:
        if i != x:
            new_tup.append(i)
    return tuple(new_tup)

print(remove_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4))

"""
Write a python function that takes in a tuple and an element and returns a new tuple with the element removed.
assert remove_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
"""

def remove_X(tup, x):
    new_tup = []
    for i in tup:
        if i != x:
            new_tup.append(i)
    return tuple(new_tup)

print(remove_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4))

"""
Write a python function that takes in a tuple and an element and returns a new tuple with the element removed.
assert remove_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
"""

def remove_X(tup, x):
    new_tup = []
    for i in tup:
        if i != x:
            new_tup.append(i)
    return tuple(new_tup)

print(remove_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4))

"""
Write a python function that takes in a tuple and an element and returns a new tuple with the element removed.
assert remove_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
"""

def remove_X(tup, x):
    new_tup = []
    for i in tup:
        if i != x:
            new_tup.append(i)
    return tuple(new_tup)

print(remove_X((