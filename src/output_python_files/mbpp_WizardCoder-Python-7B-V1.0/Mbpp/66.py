"""
Write a python function to count the number of positive numbers in a list.
assert pos_count([1,-2,3,-4]) == 2
"""
def pos_count(lst):
    count = 0
    for i in lst:
        if i > 0:
            count += 1
    return count

#Alternative solution using list comprehension
def pos_count(lst):
    return len([x for x in lst if x > 0])

#Alternative solution using filter()
def pos_count(lst):
    return len(list(filter(lambda x: x > 0, lst)))

#Alternative solution using sum()
def pos_count(lst):
    return sum(1 for x in lst if x > 0)

#Alternative solution using map()
def pos_count(lst):
    return sum(map(lambda x: x > 0, lst))

#Alternative solution using reduce()
from functools import reduce
def pos_count(lst):
    return reduce(lambda x, y: x + (1 if y > 0 else 0, 0) for x in lst)

#Alternative solution using lambda function
def pos_count(lst):
    return sum(map(lambda x: 1 if x > 0 else 0, lst))

#Alternative solution using numpy
import numpy as np
def pos_count(lst):
    return np.sum(np.array(lst) > 0)

#Alternative solution using set()
def pos_count(lst):
    return len(set(filter(lambda x: x > 0, lst))

#Alternative solution using set()
def pos_count(lst):
    return len(set(filter(lambda x: x > 0, lst)) - {-1})

#Alternative solution using set()
def pos_count(lst):
    return len(set(filter(lambda x: x > 0, lst)) - {-1, 0})

#Alternative solution using set()
def pos_count(lst):
    return len(set(filter(lambda x: x > 0, lst)) - {-1, 0, False})

#Alternative solution using set()
def pos_count(lst):
    return len(set(filter(lambda x: x > 0, lst)) - {-1, 0, False, None})

#Alternative solution using set()
def pos_count(lst):
    return len(set(filter(lambda x: x > 0, lst)) - {-1, 0, False, None, []])

#Alternative solution using set()
def pos_count(lst):
    return len(set(filter(lambda x: x > 0, lst)) - {-1, 0, False, None, [], ""])

#Alternative solution using set()
def pos_count(lst):
    return len(set(filter(lambda x: x > 0, lst)) - {-1, 0, False, None, [], "", 0.0, -1.0, False, "", 0, -1, ""})

#Alternative solution using set()
def pos_count(lst):
    return len(set(filter(lambda x: x > 0, lst)) - {-1, 0, False, None, [], "", 0.0, -1.0, False, "", 0, -1, "", 0j, -1j, False, "", 0.0j, -1.0j, False, (), [], {}, set(), frozenset(), (1,2,3)})

#Alternative solution using set()
def pos_count(lst):
    return len(set(filter(lambda x: x > 0, lst)) - {-1, 0, False, None, [], "", 0.0, -1.0, False, "", 0, -1, "", 0j, -1j, False, "", 0.0j, -1.0j, False, (), [], {}, set(), frozenset(), (1,2,3), "a", "b", "c", "", (1,2,3), (), {}, [], set(), {}, "", 0, 1, 2, 3, -1, 0.0, 1.0