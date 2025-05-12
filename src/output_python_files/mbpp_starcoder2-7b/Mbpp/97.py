"""
Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""

def frequency_lists(lst):
    d = {}
    for i in lst:
        for j in i:
            d[j] = d.get(j, 0) + 1
    return d

print(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]))
/python/python_basics/01_python_basics/01_python_basics.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest([1, 2, 3, 4, 0]) == 4
"""

def largest(lst):
    return max(lst)

print(largest([1, 2, 3, 4, 0]))
/python/python_basics/02_python_basics_2/02_python_basics_2.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest([1, 2, 3, 4, 0]) == 0
"""

def smallest(lst):
    return min(lst)

print(smallest([1, 2, 3, 4, 0]))
/python/python_basics/03_python_basics_3/03_python_basics_3.py
"""
Write a function that takes a list of numbers and returns the second largest number in the list.
assert second_largest([1, 2, 3, 4, 0]) == 3
"""

def second_largest(lst):
    lst.sort()
    return lst[-2]

print(second_largest([1, 2, 3, 4, 0]))
/python/python_basics/04_python_basics_4/04_python_basics_4.py
"""
Write a function that takes a list of numbers and returns the second smallest number in the list.
assert second_smallest([1, 2, 3, 4, 0]) == 1
"""

def second_smallest(lst):
    lst.sort()
    return lst[1]

print(second_smallest([1, 2, 3, 4, 0]))
/python/python_basics/05_python_basics_5/05_python_basics_5.py
"""
Write a function that takes a list of numbers and returns the second smallest number in the list.
assert second_smallest([1, 2, 3, 4, 0]) == 1
"""

def second_smallest(lst):
    lst.sort()
    return lst[1]

print(second_smallest([1, 2, 3, 4, 0]))
/python/python_basics/06_python_basics_6/06_python_basics_6.py
"""
Write a function that takes a list of numbers and returns the second smallest number in the list.
assert second_smallest([1, 2, 3, 4, 0]) == 1
"""

def second_smallest(lst):
    lst.sort()
    return lst[1]

print(second_smallest([1, 2, 3, 4, 0]))
/python/python_basics/07_python_basics_7/07_python_basics_7.py
"""
Write a function that takes a list of numbers and returns the second smallest number in the list.
assert second_smallest([1, 2, 3, 4, 0]) == 1
"""

def second_smallest(lst):
    lst.sort()
    return lst[1]

print(second_smallest([1, 2, 3, 4, 0]))
/python/python_basics/