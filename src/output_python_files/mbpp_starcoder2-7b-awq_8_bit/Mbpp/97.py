"""
Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""

def frequency_lists(lst):
    """
    :param lst: list of lists
    :return: dictionary with frequency of each element
    """
    d = {}
    for sublist in lst:
        for element in sublist:
            d[element] = d.get(element, 0) + 1
    return d

print(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]))
/python/python_basics/python_basics_1.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_list([1, 2, 3, 4, 5]) == 15
"""

def sum_list(lst):
    """
    :param lst: list of numbers
    :return: sum of the numbers
    """
    return sum(lst)

print(sum_list([1, 2, 3, 4, 5]))
/python/python_basics/python_basics_10.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest_number([1, 2, 3, 4, 5]) == 5
"""

def largest_number(lst):
    """
    :param lst: list of numbers
    :return: largest number in the list
    """
    return max(lst)

print(largest_number([1, 2, 3, 4, 5]))
/python/python_basics/python_basics_11.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest_number([1, 2, 3, 4, 5]) == 1
"""

def smallest_number(lst):
    """
    :param lst: list of numbers
    :return: smallest number in the list
    """
    return min(lst)

print(smallest_number([1, 2, 3, 4, 5]))
/python/python_basics/python_basics_12.py
"""
Write a function that takes a list of numbers and returns a list of the even numbers in the list.
assert even_numbers([1, 2, 3, 4, 5]) == [2, 4]
"""

def even_numbers(lst):
    """
    :param lst: list of numbers
    :return: list of the even numbers in the list
    """
    return [x for x in lst if x % 2 == 0]

print(even_numbers([1, 2, 3, 4, 5]))
/python/python_basics/python_basics_13.py
"""
Write a function that takes a list of numbers and returns a list of the odd numbers in the list.
assert odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5]
"""

def odd_numbers(lst):
    """
    :param lst: list of numbers
    :return: list of the odd numbers in the list
    """
    return [x for x in lst if x % 2!= 0]

print(odd_numbers([1, 2, 3, 4, 5]))
/python/python_basics/python_basics_14.py
"""
Write a function that takes a list of numbers and returns a list of the positive numbers in the list.
assert positive_numbers([1, -2, 3, -4, 5]) == [1, 3, 5]
"""

def positive_numbers(lst):
    """
    :param lst: list of numbers
    :return: list of the positive numbers in the list
    """
    return [x for x in lst if x > 0]

print(positive_numbers([1, -2, 3, -4,