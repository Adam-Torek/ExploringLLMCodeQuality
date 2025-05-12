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

assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),10) == 2
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),8) == 3
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),5) == 2
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),2) == 2
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),15) == 1

"""
Write a python function that takes in a tuple and returns a new tuple with the elements in reverse order.
assert reverse_tuple((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)) == (2, 8, 5, 10, 8, 15, 10, 8, 5, 8, 10, 5)
"""

def reverse_tuple(tup):
    return tup[::-1]

assert reverse_tuple((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)) == (2, 8, 5, 10, 8, 15, 10, 8, 5, 8, 10, 5)

"""
Write a python function that takes in a tuple and returns a new tuple with the elements in reverse order.
assert reverse_tuple((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)) == (2, 8, 5, 10, 8, 15, 10, 8, 5, 8, 10, 5)
"""

def reverse_tuple(tup):
    return tup[::-1]

assert reverse_tuple((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)) == (2, 8, 5, 10, 8, 15, 10, 8, 5, 8, 10, 5)

"""
Write a python function that takes in a tuple and returns a new tuple with the elements in reverse order.
assert reverse_tuple((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)) == (2, 8, 5, 10, 8, 15, 10, 8, 5, 8, 10, 5)
"""

def reverse_tuple(tup):
    return tup[::-1]

assert reverse_tuple((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8,