"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""

def similar_elements(list1, list2):
    return set(list1).intersection(set(list2))

print(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)))/python_basics/python_basics_1.py
"""
Write a function to find the sum of the given list of numbers.
assert sum_of_numbers([1, 2, 3, 4, 5]) == 15
"""

def sum_of_numbers(list):
    return sum(list)

print(sum_of_numbers([1, 2, 3, 4, 5]))/python_basics/python_basics_10.py
"""
Write a function to find the maximum number from the given list of numbers.
assert maximum_number([1, 2, 3, 4, 5]) == 5
"""

def maximum_number(list):
    return max(list)

print(maximum_number([1, 2, 3, 4, 5]))/python_basics/python_basics_11.py
"""
Write a function to find the minimum number from the given list of numbers.
assert minimum_number([1, 2, 3, 4, 5]) == 1
"""

def minimum_number(list):
    return min(list)

print(minimum_number([1, 2, 3, 4, 5]))/python_basics/python_basics_12.py
"""
Write a function to find the average of the given list of numbers.
assert average_of_numbers([1, 2, 3, 4, 5]) == 3
"""

def average_of_numbers(list):
    return sum(list)/len(list)

print(average_of_numbers([1, 2, 3, 4, 5]))/python_basics/python_basics_13.py
"""
Write a function to find the median of the given list of numbers.
assert median_of_numbers([1, 2, 3, 4, 5]) == 3
"""

def median_of_numbers(list):
    list.sort()
    return list[len(list)//2]

print(median_of_numbers([1, 2, 3, 4, 5]))/python_basics/python_basics_14.py
"""
Write a function to find the mode of the given list of numbers.
assert mode_of_numbers([1, 2, 3, 4, 5]) == 1
"""

def mode_of_numbers(list):
    return max(set(list), key=list.count)

print(mode_of_numbers([1, 2, 3, 4, 5]))/python_basics/python_basics_15.py
"""
Write a function to find the factorial of the given number.
assert factorial(5) == 120
"""

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)

print(factorial(5))/python_basics/python_basics_16.py
"""
Write a function to find the factorial of the given number.
assert factorial(5) == 120
"""

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)

print(factorial(5))

def factorial_iterative(number):
    fact = 1
    for i in range(1, number+1):
        fact = fact * i
    return fact

print(factorial_iterative(5))/python_basics/python_basics_17.py
"""
Write a function to find the factorial of the given number.
assert factorial(5) == 120
"""

def factorial(number):
    if number ==