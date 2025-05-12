"""
Write a function which takes a tuple of tuples and returns the average value for each tuple as a list.
assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]
"""

def average_tuple(tup):
    return [sum(i)/len(i) for i in tup]

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))
/Python/Python_Basics/03_Lists/01_list_basics.py
"""
Write a function which takes a list of numbers and returns the sum of the numbers.
assert sum_list([1, 2, 3, 4, 5, 6]) == 21
"""

def sum_list(lst):
    return sum(lst)

print(sum_list([1, 2, 3, 4, 5, 6]))
/Python/Python_Basics/03_Lists/05_list_of_lists.py
"""
Write a function which takes a list of lists and returns the sum of all the numbers in the lists.
assert sum_list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 45
"""

def sum_list_of_lists(lst):
    return sum([sum(i) for i in lst])

print(sum_list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
/Python/Python_Basics/03_Lists/04_list_of_lists_2.py
"""
Write a function which takes a list of lists and returns the average of all the numbers in the lists.
assert average_list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.0
"""

def average_list_of_lists(lst):
    return sum([sum(i) for i in lst])/len(lst)

print(average_list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
/Python/Python_Basics/03_Lists/03_list_of_lists_1.py
"""
Write a function which takes a list of lists and returns the maximum number in the lists.
assert max_list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 9
"""

def max_list_of_lists(lst):
    return max([max(i) for i in lst])

print(max_list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
/Python/Python_Basics/03_Lists/02_list_of_lists_2.py
"""
Write a function which takes a list of lists and returns the minimum number in the lists.
assert min_list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 1
"""

def min_list_of_lists(lst):
    return min([min(i) for i in lst])

print(min_list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
/Python/Python_Basics/03_Lists/06_list_of_lists_3.py
"""
Write a function which takes a list of lists and returns the maximum number in each list.
assert max_list_of_lists_2([[1, 2, 3], [4, 5, 6], [7, 8, 9]])