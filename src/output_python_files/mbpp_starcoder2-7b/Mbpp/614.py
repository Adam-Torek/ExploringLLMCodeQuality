"""
Write a function to find the cumulative sum of all the values that are present in the given tuple list.
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
"""

def cummulative_sum(tuple_list):
    sum = 0
    for i in tuple_list:
        sum += sum(i)
    return sum

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]))
<file_sep>/python_basics/python_basics_1.py
"""
Write a function to find the sum of all the values that are present in the given tuple list.
assert sum_of_values([(1, 3), (5, 6, 7), (2, 6)]) == 28
"""

def sum_of_values(tuple_list):
    sum = 0
    for i in tuple_list:
        sum += sum(i)
    return sum

print(sum_of_values([(1, 3), (5, 6, 7), (2, 6)]))
<file_sep>/python_basics/python_basics_2.py
"""
Write a function to find the maximum value that is present in the given tuple list.
assert max_value([(1, 3), (5, 6, 7), (2, 6)]) == 7
"""

def max_value(tuple_list):
    max = 0
    for i in tuple_list:
        if max < max(i):
            max = max(i)
    return max

print(max_value([(1, 3), (5, 6, 7), (2, 6)]))
<file_sep>/python_basics/python_basics_3.py
"""
Write a function to find the minimum value that is present in the given tuple list.
assert min_value([(1, 3), (5, 6, 7), (2, 6)]) == 1
"""

def min_value(tuple_list):
    min = 0
    for i in tuple_list:
        if min > min(i):
            min = min(i)
    return min

print(min_value([(1, 3), (5, 6, 7), (2, 6)]))
<|endoftext|>