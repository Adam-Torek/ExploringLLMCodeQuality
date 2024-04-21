"""
Write a python function to get the first element of each sublist.
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
"""

def Extract(list):
    new_list = []
    for i in list:
        new_list.append(i[0])
    return new_list

print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))
<file_sep>/python/python_basics/python_basics_1.py
"""
Write a python function to get the first element of each sublist.
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
"""

def Extract(list):
    new_list = []
    for i in list:
        new_list.append(i[0])
    return new_list

print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))

"""
Write a python function to get the last element of each sublist.
assert ExtractLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [2, 5, 9]
"""

def ExtractLast(list):
    new_list = []
    for i in list:
        new_list.append(i[-1])
    return new_list

print(ExtractLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))

"""
Write a python function to get the first and last element of each sublist.
assert ExtractFirstLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [[1, 2], [3, 5], [6, 9]]
"""

def ExtractFirstLast(list):
    new_list = []
    for i in list:
        new_list.append([i[0], i[-1]])
    return new_list

print(ExtractFirstLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))

"""
Write a python function to get the first and last element of each sublist.
assert ExtractFirstLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [[1, 2], [3, 5], [6, 9]]
"""

def ExtractFirstLast(list):
    new_list = []
    for i in list:
        new_list.append([i[0], i[-1]])
    return new_list

print(ExtractFirstLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))

"""
Write a python function to get the first and last element of each sublist.
assert ExtractFirstLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [[1, 2], [3, 5], [6, 9]]
"""

def ExtractFirstLast(list):
    new_list = []
    for i in list:
        new_list.append([i[0], i[-1]])
    return new_list

print(ExtractFirstLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))

"""
Write a python function to get the first and last element of each sublist.
assert ExtractFirstLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [[1, 2], [3, 5], [6, 9]]
"""

def ExtractFirstLast(list):
    new_list = []
    for i in list:
        new_list.append([i[0], i[-1]])
    return new_list

print(ExtractFirstLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))

"""
Write a python function to get the first and last element of each sublist.
assert ExtractFirstLast([[1, 2], [3,