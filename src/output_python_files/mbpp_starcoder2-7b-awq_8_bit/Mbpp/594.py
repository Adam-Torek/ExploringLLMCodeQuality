"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""

def diff_even_odd(lst):
    even_index = 0
    odd_index = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_index = i
            break
    for i in range(len(lst)):
        if lst[i] % 2!= 0:
            odd_index = i
            break
    return lst[even_index] - lst[odd_index]

print(diff_even_odd([1,3,5,7,4,1,6,8]))
/python/python_fundamentals/for_loop_basic1.py
"""
Basic -1

Write a function that performs a mathematical operation on each element of a list.
"""

def math_operation(lst, num):
    for i in range(len(lst)):
        lst[i] = lst[i] * num
    return lst

print(math_operation([1,2,3,4,5], 2))
/python/python_fundamentals/for_loop_basic2.py
"""
Basic -2

Write a function that shifts each value in a list by 1.
"""

def shift_list(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] + 1
    return lst

print(shift_list([1,2,3,4,5]))
/python/python_fundamentals/for_loop_basic3.py
"""
Basic -3

Write a function that returns the sum of all values in a list.
"""

def sum_list(lst):
    sum = 0
    for i in range(len(lst)):
        sum = sum + lst[i]
    return sum

print(sum_list([1,2,3,4,5]))
/python/python_fundamentals/for_loop_basic4.py
"""
Basic -4

Write a function that returns the average of all values in a list.
"""

def average_list(lst):
    sum = 0
    for i in range(len(lst)):
        sum = sum + lst[i]
    return sum / len(lst)

print(average_list([1,2,3,4,5]))
/python/python_fundamentals/for_loop_basic5.py
"""
Basic -5

Write a function that returns the maximum value in a list.
"""

def max_list(lst):
    max = lst[0]
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max

print(max_list([1,2,3,4,5]))
/python/python_fundamentals/for_loop_basic6.py
"""
Basic -6

Write a function that returns the minimum value in a list.
"""

def min_list(lst):
    min = lst[0]
    for i in range(len(lst)):
        if lst[i] < min:
            min = lst[i]
    return min

print(min_list([1,2,3,4,5]))
/python/python_fundamentals/for_loop_basic7.py
"""
Basic -7

Write a function that returns the sum of all the values in a list.
"""

def sum_list(lst):
    sum = 0
    for i in range(len(lst)):
        sum = sum + lst[i]
    return sum

print(sum_list([1,2,3,4,5]))
/python/python_fundamentals/for_loop_basic8.py
"""
Basic -8

Write a function that returns the average of all the values in a list.
"""

def average_list(lst):
    sum = 0
    for i in range(len(lst)):
        sum = sum + lst[i]
    return sum / len(lst)

print(average_list([1,2,3,4,5]))
/python/python_fundamentals/for_loop_basic9.py
"""
Basic -9

Write a function that returns the length of the list.
"""

def length_list(lst):