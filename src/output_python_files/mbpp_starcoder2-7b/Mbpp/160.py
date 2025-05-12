"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""

def find_solution(a, b, n):
    x = 0
    y = 0
    while x < n:
        if (a * x + b * y) == n:
            return (x, y)
        elif (a * x + b * y) > n:
            y += 1
        else:
            x += 1
    return None

print(find_solution(2, 3, 7))
/python/python_practice/python_practice_1.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest([1, 2, 3, 4]) == 4
"""

def largest(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest

print(largest([1, 2, 3, 4]))
/python/python_practice/python_practice_10.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest([1, 2, 3, 4]) == 1
"""

def smallest(list):
    smallest = list[0]
    for i in list:
        if i < smallest:
            smallest = i
    return smallest

print(smallest([1, 2, 3, 4]))
/python/python_practice/python_practice_12.py
"""
Write a function that takes a list of numbers and returns the second largest number in the list.
assert second_largest([1, 2, 3, 4]) == 3
"""

def second_largest(list):
    largest = list[0]
    second_largest = list[0]
    for i in list:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest:
            second_largest = i
    return second_largest

print(second_largest([1, 2, 3, 4]))
/python/python_practice/python_practice_11.py
"""
Write a function that takes a list of numbers and returns the second smallest number in the list.
assert second_smallest([1, 2, 3, 4]) == 2
"""

def second_smallest(list):
    smallest = list[0]
    second_smallest = list[0]
    for i in list:
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif i < second_smallest:
            second_smallest = i
    return second_smallest

print(second_smallest([1, 2, 3, 4]))
/python/python_practice/python_practice_14.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_list([1, 2, 3, 4]) == 10
"""

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(sum_list([1, 2, 3, 4]))
/python/python_practice/python_practice_13.py
"""
Write a function that takes a list of numbers and returns the average (mean) of the numbers.
assert average([1, 2, 3, 4]) == 2.5
"""

def average(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)

print(average([1, 2, 3, 4]))
/python/python_practice/python_practice_15.py
"""
Write a function that takes a list of numbers and returns the product of the numbers.
assert product([1, 2, 3, 4]) == 24
"""

def product(list):
    product = 1
    for i in list:
        product *= i
    return product

print(product([1, 2, 3, 4]))
/python/python_practice/python_practice_16.py