"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""

def find_tuples(lst, k):
    return [x for x in lst if all(x[i] % k == 0 for i in range(len(x)))]

print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6))
<file_sep>/python/list_comprehension.py
"""
Write a function to return a list of all the numbers in a given list that are divisible by 3.
assert divisible_by_three([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [3, 6, 9]
"""

def divisible_by_three(lst):
    return [x for x in lst if x % 3 == 0]

print(divisible_by_three([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
<file_sep>/python/list_of_lists.py
"""
Write a function to return a list of lists, where each list contains the numbers in the range 1..n.
assert list_of_lists(5) == [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
"""

def list_of_lists(n):
    return [[x for x in range(1, n+1)] for i in range(n)]

print(list_of_lists(5))
<file_sep>/python/list_of_lists_2.py
"""
Write a function to return a list of lists, where each list contains the numbers in the range 1..n.
assert list_of_lists(5) == [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
"""

def list_of_lists(n):
    return [[x for x in range(1, n+1)] for i in range(n)]

print(list_of_lists(5))

def list_of_lists_2(n):
    return [[x for x in range(1, n+1)] for i in range(n)]

print(list_of_lists_2(5))
<file_sep>/python/list_of_lists_3.py
"""
Write a function to return a list of lists, where each list contains the numbers in the range 1..n.
assert list_of_lists(5) == [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
"""

def list_of_lists(n):
    return [[x for x in range(1, n+1)] for i in range(n)]

print(list_of_lists(5))

def list_of_lists_2(n):
    return [[x for x in range(1, n+1)] for i in range(n)]

print(list_of_lists_2(5))

def list_of_lists_3(n):
    return [[x for x in range(1, n+1)] for i in range(n)]

print(list_of_lists_3(5))
<file_sep>/python/list_of_lists_4.py
"""
Write a function to return a list of lists, where each list contains the numbers in the range 1