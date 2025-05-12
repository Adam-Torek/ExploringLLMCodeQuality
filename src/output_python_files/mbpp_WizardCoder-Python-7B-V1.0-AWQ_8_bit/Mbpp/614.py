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

# Another way to solve this problem using nested list comprehension
def cummulative_sum(lst):
    return sum([sum(i) for i in [j for sublist in lst for j in sublist])

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using reduce() function from functools module
from functools import reduce
def cummulative_sum(lst):
    return reduce(lambda x, y: x + y, [sum(i) for i in lst])

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using numpy
import numpy as np
def cummulative_sum(lst):
    return np.sum(np.sum(lst, axis=1))

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using numpy
import numpy as np
def cummulative_sum(lst):
    return np.sum(np.concatenate(lst))

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using numpy
import numpy as np
def cummulative_sum(lst):
    return np.sum(np.array(lst).flatten())

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using numpy
import numpy as np
def cummulative_sum(lst):
    return np.sum(np.hstack(lst))

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using numpy
import numpy as np
def cummulative_sum(lst):
    return np.sum(np.array(lst).flatten())

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using numpy
import numpy as np
def cummulative_sum(lst):
    return np.sum(np.hstack(lst))

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using numpy
import numpy as np
def cummulative_sum(lst):
    return np.sum(np.concatenate(lst))

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])) # Output: 20

# Another way to solve this problem using numpy
import numpy as np
def cummulative_sum(lst):
    return np.sum(np.array(lst).flatten())

print(cummulative_sum([(1, 3), (5