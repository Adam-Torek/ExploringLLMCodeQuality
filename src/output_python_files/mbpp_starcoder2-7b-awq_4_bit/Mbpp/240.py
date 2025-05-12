"""
Write a function that takes in two lists and replaces the last element of the first list with the elements of the second list.
assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
"""

def replace_list(list1, list2):
    list1[-len(list2):] = list2
    return list1

print(replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]))
/python/list_comprehension.py
"""
Write a function that takes in a list of numbers and returns a new list with the numbers in reverse order.
assert reverse([1, 2, 3, 4])==[4, 3, 2, 1]
"""

def reverse(list):
    return [x for x in reversed(list)]

print(reverse([1, 2, 3, 4]))
/python/list_of_lists.py
"""
Write a function that takes in a list of lists and returns a new list with the elements of the lists in order.
assert list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]])==[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

def list_of_lists(list):
    return [x for y in list for x in y]

print(list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
/python/list_of_lists_2.py
"""
Write a function that takes in a list of lists and returns a new list with the elements of the lists in order.
assert list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]])==[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

def list_of_lists(list):
    return [x for y in list for x in y]

print(list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

def list_of_lists_2(list):
    return [x for y in list for x in y]

print(list_of_lists_2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
/python/list_of_lists_3.py
"""
Write a function that takes in a list of lists and returns a new list with the elements of the lists in order.
assert list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]])==[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

def list_of_lists(list):
    return [x for y in list for x in y]

print(list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

def list_of_lists_2(list):
    return [x for y in list for x in y]

print(list_of_lists_2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

def list_of_lists_3(list):
    return [x for y in list for x in y]

print(list_of_lists_3([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
/python/list_of_lists_4.py
"""
Write a function that takes in a list of lists and returns a new list with the elements of the lists in order.
assert list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]])==[1