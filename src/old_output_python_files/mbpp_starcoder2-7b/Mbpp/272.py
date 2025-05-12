"""
Write a function that takes in a list of tuples and returns a list containing the rear element of each tuple.
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
"""

def rear_extract(list_of_tuples):
    """
    :param list_of_tuples: list of tuples
    :return: list of integers
    """
    return [x[-1] for x in list_of_tuples]

print(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]))
<file_sep>/python_basics/python_basics_1/task_1.py
"""
Write a function that takes in a list of numbers and returns the largest number in the list.
assert largest([1, 2, 3, 4, 5]) == 5
"""

def largest(list_of_numbers):
    """
    :param list_of_numbers: list of numbers
    :return: integer
    """
    return max(list_of_numbers)

print(largest([1, 2, 3, 4, 5]))
<file_sep>/python_basics/python_basics_1/task_3.py
"""
Write a function that takes in a list of numbers and returns the smallest number in the list.
assert smallest([1, 2, 3, 4, 5]) == 1
"""

def smallest(list_of_numbers):
    """
    :param list_of_numbers: list of numbers
    :return: integer
    """
    return min(list_of_numbers)

print(smallest([1, 2, 3, 4, 5]))
<file_sep>/python_basics/python_basics_1/task_2.py
"""
Write a function that takes in a list of numbers and returns the sum of all the numbers in the list.
assert sum_of_list([1, 2, 3, 4, 5]) == 15
"""

def sum_of_list(list_of_numbers):
    """
    :param list_of_numbers: list of numbers
    :return: integer
    """
    return sum(list_of_numbers)

print(sum_of_list([1, 2, 3, 4, 5]))
<file_sep>/python_basics/python_basics_1/task_4.py
"""
Write a function that takes in a list of numbers and returns the average (mean) of all the numbers in the list.
assert average([1, 2, 3, 4, 5]) == 3
"""

def average(list_of_numbers):
    """
    :param list_of_numbers: list of numbers
    :return: float
    """
    return sum(list_of_numbers) / len(list_of_numbers)

print(average([1, 2, 3, 4, 5]))
<file_sep>/python_basics/python_basics_1/task_5.py
"""
Write a function that takes in a list of numbers and returns a new list containing only the even numbers in the original list.
assert even_only([1, 2, 3, 4, 5]) == [2, 4]
"""

def even_only(list_of_numbers):
    """
    :param list_of_numbers: list of numbers
    :return: list of integers
    """
    return [x for x in list_of_numbers if x % 2 == 0]

print(even_only([1, 2, 3, 4, 5]))
<|endoftext|>