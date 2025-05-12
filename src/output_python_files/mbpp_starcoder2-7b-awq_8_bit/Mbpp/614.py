"""
Write a function to find the cumulative sum of all the values that are present in the given tuple list.
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
"""

def cummulative_sum(tuple_list):
    sum = 0
    for i in tuple_list:
        for j in i:
            sum += j
    return sum

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]))
/python_basics/python_basics_001.py
"""
Write a function to find the sum of all the values that are present in the given tuple list.
assert sum_of_all_values([(1, 3), (5, 6, 7), (2, 6)]) == 28
"""

def sum_of_all_values(tuple_list):
    sum = 0
    for i in tuple_list:
        for j in i:
            sum += j
    return sum

print(sum_of_all_values([(1, 3), (5, 6, 7), (2, 6)]))
/python_basics/python_basics_003.py
"""
Write a function to find the sum of all the values that are present in the given tuple list.
assert sum_of_all_values([(1, 3), (5, 6, 7), (2, 6)]) == 28
"""

def sum_of_all_values(tuple_list):
    sum = 0
    for i in tuple_list:
        sum += sum(i)
    return sum

print(sum_of_all_values([(1, 3), (5, 6, 7), (2, 6)]))
/python_basics/python_basics_002.py
"""
Write a function to find the sum of all the values that are present in the given tuple list.
assert sum_of_all_values([(1, 3), (5, 6, 7), (2, 6)]) == 28
"""

def sum_of_all_values(tuple_list):
    sum = 0
    for i in tuple_list:
        for j in i:
            sum += j
    return sum

print(sum_of_all_values([(1, 3), (5, 6, 7), (2, 6)]))
/python_basics/python_basics_004.py
"""
Write a function to find the sum of all the values that are present in the given tuple list.
assert sum_of_all_values([(1, 3), (5, 6, 7), (2, 6)]) == 28
"""

def sum_of_all_values(tuple_list):
    sum = 0
    for i in tuple_list:
        for j in i:
            sum += j
    return sum

print(sum_of_all_values([(1, 3), (5, 6, 7), (2, 6)]))
/python_basics/python_basics_005.py
"""
Write a function to find the sum of all the values that are present in the given tuple list.
assert sum_of_all_values([(1, 3), (5, 6, 7), (2, 6)]) == 28
"""

def sum_of_all_values(tuple_list):
    sum = 0
    for i in tuple_list:
        for j in i:
            sum += j
    return sum

print(sum_of_all_values([(1, 3), (5, 6, 7), (2, 6)]))