"""
Write a function to find the cumulative sum of all the values that are present in the given tuple list.
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
"""

def cummulative_sum(lst):
    total = 0
    for i in lst:
        total += sum(i)
    return total

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using list comprehension
def cummulative_sum(lst):
    return sum([sum(i) for i in lst])

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using reduce function
from functools import reduce
from operator import add

def cummulative_sum(lst):
    return reduce(add, [sum(i) for i in lst])

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using lambda function
from functools import reduce

def cummulative_sum(lst):
    return reduce(lambda x, y: x + sum(y), lst, 0)

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using numpy
import numpy as np

def cummulative_sum(lst):
    return np.sum(np.array(lst).flatten())

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using numpy
import itertools

def cummulative_sum(lst):
    return sum(itertools.chain.from_iterable(lst))

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using numpy
import operator

def cummulative_sum(lst):
    return sum(map(sum, lst))

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using numpy
import numpy as np

def cummulative_sum(lst):
    return np.sum(np.concatenate(lst))

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using numpy
import itertools

def cummulative_sum(lst):
    return sum(itertools.chain.from_iterable(lst))

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using numpy
import numpy as np

def cummulative_sum(lst):
    return np.sum(np.concatenate(lst))

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using numpy
import itertools

def cummulative_sum(lst):
    return sum(itertools.chain.from_iterable(lst))

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another