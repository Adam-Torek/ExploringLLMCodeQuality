"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please','move', 'back','stream'])
"""

def find_char_long(string):
    return [word for word in string.split() if len(word) >= 4]

print(find_char_long('Please move back to stream'))
/python/python_fundamentals/fundamentals/for_loop_basic2.py
"""
Basic -2

Write a function that takes any list and returns a new list that contains all the values
except the first 4 elements.

assert new_list([1,2,3,4,5,6,7,8,9,10]) == [5,6,7,8,9,10]
"""

def new_list(list):
    return list[4:]

print(new_list([1,2,3,4,5,6,7,8,9,10]))
/python/python_fundamentals/fundamentals/for_loop_basic1.py
"""
Basic -1

Write a function that takes any list and returns a new list that contains all the values
except the last one.

assert new_list([1,2,3,4,5,6]) == [1,2,3,4,5]
"""

def new_list(list):
    return list[:-1]

print(new_list([1,2,3,4,5,6]))
/python/python_fundamentals/fundamentals/for_loop_basic3.py
"""
Basic -3

Write a function that takes any list and returns a new list that contains all the values
except the last 4 elements.

assert new_list([1,2,3,4,5,6,7,8,9,10]) == [1,2,3,4]
"""

def new_list(list):
    return list[:-4]

print(new_list([1,2,3,4,5,6,7,8,9,10]))
/python/python_fundamentals/fundamentals/for_loop_basic4.py
"""
Basic -4

Write a function that takes any list and returns a new list that contains all the values
except every other value.

assert new_list([1,2,3,4,5,6,7,8,9,10]) == [1,3,5,7,9]
"""

def new_list(list):
    return list[::2]

print(new_list([1,2,3,4,5,6,7,8,9,10]))
/python/python_fundamentals/fundamentals/for_loop_basic5.py
"""
Basic -5

Write a function that takes any list and returns a new list that contains all the values
except every other value, starting with the first one.

assert new_list([1,2,3,4,5,6,7,8,9,10]) == [1,3,5,7,9]
"""

def new_list(list):
    return list[::2]

print(new_list([1,2,3,4,5,6,7,8,9,10]))
/python/python_fundamentals/fundamentals/for_loop_basic6.py
"""
Basic -6

Write a function that takes any list and returns a new list that contains all the values
except every other value, starting with the last one.

assert new_list([1,2,3,4,5,6,7,8,9,10]) == [10,8,6,4,2]
"""

def new_list(list):
    return list[::-2]

print(new_list([1,2,3,4,5,6,7,8,9,10]))
/python/python_fundamentals/fundamentals/for_loop_basic7.py
"""
Basic -7

Write a function that takes any list and returns a new list that contains all the values
except every other value, starting with