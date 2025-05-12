"""
Write a function to convert a tuple to a string.
assert tup_string(('e', 'x', 'e', 'r', 'c', 'i','s', 'e','s'))==("exercises")
"""

def tup_string(tup):
    return ''.join(tup)

print(tup_string(('e', 'x', 'e', 'r', 'c', 'i','s', 'e','s')))

"""
Write a function that takes a list of numbers and returns the sum.
assert sum_list([1, 2, 3, 4, 5])==15
"""

def sum_list(lst):
    return sum(lst)

print(sum_list([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns the average.
assert average_list([1, 2, 3, 4, 5])==3
"""

def average_list(lst):
    return sum(lst)/len(lst)

print(average_list([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns the minimum.
assert min_list([1, 2, 3, 4, 5])==1
"""

def min_list(lst):
    return min(lst)

print(min_list([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns the maximum.
assert max_list([1, 2, 3, 4, 5])==5
"""

def max_list(lst):
    return max(lst)

print(max_list([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns a list of the unique values.
assert unique_list([1, 2, 3, 4, 5, 5, 5])==[1, 2, 3, 4, 5]
"""

def unique_list(lst):
    return list(set(lst))

print(unique_list([1, 2, 3, 4, 5, 5, 5]))

"""
Write a function that takes a list of numbers and returns a list of the even values.
assert even_list([1, 2, 3, 4, 5, 6, 7, 8])==[2, 4, 6, 8]
"""

def even_list(lst):
    return [x for x in lst if x%2==0]

print(even_list([1, 2, 3, 4, 5, 6, 7, 8]))

"""
Write a function that takes a list of numbers and returns a list of the odd values.
assert odd_list([1, 2, 3, 4, 5, 6, 7, 8])==[1, 3, 5, 7]
"""

def odd_list(lst):
    return [x for x in lst if x%2!=0]

print(odd_list([1, 2, 3, 4, 5, 6, 7, 8]))

"""
Write a function that takes a list of numbers and returns a list of the square values.
assert square_list([1, 2, 3, 4, 5])==[1, 4, 9, 16, 25]
"""

def square_list(lst):
    return [x**2 for x in lst]

print(square_list([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns a list of the square values.
assert square_list([1, 2, 3, 4, 5])==[1, 4, 9, 16, 25]
"""

def square_list(lst):
    return [x**2 for x in lst]

print(square_list([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns a list of the square values.
assert square_list([1, 2, 3, 4, 5