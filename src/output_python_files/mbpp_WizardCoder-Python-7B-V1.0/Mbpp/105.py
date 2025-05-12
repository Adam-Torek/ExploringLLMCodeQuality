"""
Write a python function to count true booleans in the given list.
assert count([True,False,True]) == 2
"""

def count(lst):
    count = 0
    for i in lst:
        if i == True:
            count += 1
    return count

#Alternate solution using list comprehension
def count(lst):
    return len([i for i in lst if i == True])

#Alternate solution using filter()
def count(lst):
    return len(list(filter(lambda x: x == True, lst)))

#Alternate solution using sum()
def count(lst):
    return sum(1 for i in lst if i == True)

#Alternate solution using map()
def count(lst):
    return sum(map(lambda x: x == True, lst))

#Alternate solution using reduce()
from functools import reduce
def count(lst):
    return reduce(lambda x, y: x + (1 if y == True else 0, 0, lst)

#Alternate solution using lambda function
def count(lst):
    return sum(map(lambda x: 1 if x else 0, lst)

#Alternate solution using numpy
import numpy as np
def count(lst):
    return np.sum(np.array(lst) == True)

#Alternate solution using numpy
import numpy as np
def count(lst):
    return np.count_nonzero(np.array(lst))

#Alternate solution using set()
def count(lst):
    return len(set(lst) & {True})

#Alternate solution using set()
def count(lst):
    return len(set(filter(lambda x: x, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(None, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(bool, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(None, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(bool, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(lambda x: x, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(lambda x: x, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(bool, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(bool, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(bool, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(bool, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(bool, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(bool, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(bool, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(bool, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(bool, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(bool, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(bool, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(bool, lst))

#Alternate solution using set()
def count(lst):
    return len(set(filter(bool, lst))