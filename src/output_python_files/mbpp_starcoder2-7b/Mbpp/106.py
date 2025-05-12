"""
Write a function to append the given list to the given tuples.
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
"""

def add_lists(list1, tuple1):
    return tuple1 + tuple(list1)

print(add_lists([5, 6, 7], (9, 10)))
/python_basics/python_basics_1/python_basics_1_1.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest([1, 2, 3, 4, 0]) == 4
"""

def largest(list1):
    return max(list1)

print(largest([1, 2, 3, 4, 0]))
/python_basics/python_basics_1/python_basics_1_2.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest([1, 2, 3, 4, 0]) == 0
"""

def smallest(list1):
    return min(list1)

print(smallest([1, 2, 3, 4, 0]))
/python_basics/python_basics_1/python_basics_1_3.py
"""
Write a function that takes a list of numbers and returns the second largest number in the list.
assert second_largest([1, 2, 3, 4, 0]) == 3
"""

def second_largest(list1):
    return sorted(list1)[-2]

print(second_largest([1, 2, 3, 4, 0]))
/python_basics/python_basics_1/python_basics_1_4.py
"""
Write a function that takes a list of numbers and returns the second smallest number in the list.
assert second_smallest([1, 2, 3, 4, 0]) == 1
"""

def second_smallest(list1):
    return sorted(list1)[1]

print(second_smallest([1, 2, 3, 4, 0]))
/python_basics/python_basics_1/python_basics_1_5.py
"""
Write a function that takes a list of numbers and returns the average (mean) of all the numbers in the list.
assert average([1, 2, 3, 4, 0]) == 2
"""

def average(list1):
    return sum(list1) / len(list1)

print(average([1, 2, 3, 4, 0]))
/python_basics/python_basics_1/python_basics_1_6.py
"""
Write a function that takes a list of numbers and returns the median of all the numbers in the list.
assert median([1, 2, 3, 4, 0]) == 2
"""

def median(list1):
    return sorted(list1)[len(list1) // 2]

print(median([1, 2, 3, 4, 0]))
/python_basics/python_basics_1/python_basics_1_7.py
"""
Write a function that takes a list of numbers and returns the mode of all the numbers in the list.
assert mode([1, 2, 3, 4, 0]) == 0
"""

def mode(list1):
    return max(set(list1), key=list1.count)

print(mode([1, 2, 3, 4, 0]))
/python_basics/python_basics_1/python_basics_1_8.py
"""
Write a function that takes a list of numbers and returns the range of all the numbers in