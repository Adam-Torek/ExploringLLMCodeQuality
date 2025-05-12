"""
Write a python function to get the first element of each sublist.
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
"""

def Extract(lst):
    return [lst[i][0] for i in range(len(lst))]

print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))
/Python/Python_Basics/Python_Basics_01.py
"""
Write a python function to get the first element of each sublist.
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
"""

def Extract(lst):
    return [lst[i][0] for i in range(len(lst))]

print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))

"""
Write a python function to get the last element of each sublist.
assert ExtractLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [2, 5, 9]
"""

def ExtractLast(lst):
    return [lst[i][-1] for i in range(len(lst))]

print(ExtractLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))

"""
Write a python function to get the first and last element of each sublist.
assert ExtractFirstLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [[1, 2], [3, 5], [6, 9]]
"""

def ExtractFirstLast(lst):
    return [[lst[i][0], lst[i][-1]] for i in range(len(lst))]

print(ExtractFirstLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))

"""
Write a python function to get the first and last element of each sublist.
assert ExtractFirstLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [[1, 2], [3, 5], [6, 9]]
"""

def ExtractFirstLast(lst):
    return [[lst[i][0], lst[i][-1]] for i in range(len(lst))]

print(ExtractFirstLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))

"""
Write a python function to get the first and last element of each sublist.
assert ExtractFirstLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [[1, 2], [3, 5], [6, 9]]
"""

def ExtractFirstLast(lst):
    return [[lst[i][0], lst[i][-1]] for i in range(len(lst))]

print(ExtractFirstLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))

"""
Write a python function to get the first and last element of each sublist.
assert ExtractFirstLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [[1, 2], [3, 5], [6, 9]]
"""

def ExtractFirstLast(lst):
    return [[lst[i][0], lst[i][-1]] for i in range(len(lst))]

print(ExtractFirstLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))

"""
Write a python function to get the first and last element of each sublist.
assert ExtractFirstLast([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [[1, 2], [3, 5], [6, 9]]
"""

def ExtractFirstLast(lst):
    return [[lst[i][0],