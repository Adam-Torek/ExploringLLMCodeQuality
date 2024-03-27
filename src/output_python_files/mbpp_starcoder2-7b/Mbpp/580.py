"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""

def extract_even(tup):
    new_tup = ()
    for i in tup:
        if type(i) == tuple:
            new_tup += (extract_even(i),)
        elif i % 2 == 0:
            new_tup += (i,)
    return new_tup

print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8)))
<file_sep>/01_python_basics/04_functions/01_functions.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
"""

def sum_list(lst):
    return sum(lst)

print(sum_list([1, 2, 3, 4, 5]))
<file_sep>/01_python_basics/03_lists/02_lists.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
"""

def max_list(lst):
    return max(lst)

print(max_list([1, 2, 3, 4, 5]))
<file_sep>/01_python_basics/03_lists/03_lists.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
"""

def min_list(lst):
    return min(lst)

print(min_list([1, 2, 3, 4, 5]))
<file_sep>/01_python_basics/04_functions/02_functions.py
"""
Write a function that takes a list of numbers and returns the product of all the numbers.
"""

def product_list(lst):
    return reduce(lambda x, y: x * y, lst)

print(product_list([1, 2, 3, 4, 5]))
<file_sep>/01_python_basics/03_lists/04_lists.py
"""
Write a function that takes a list of numbers and returns a new list with only the odd numbers.
"""

def odd_list(lst):
    return [i for i in lst if i % 2!= 0]

print(odd_list([1, 2, 3, 4, 5]))
<file_sep>/01_python_basics/03_lists/01_lists.py
"""
Write a function that takes a list of numbers and returns the average of the numbers.
"""

def avg_list(lst):
    return sum(lst) / len(lst)

print(avg_list([1, 2, 3, 4, 5]))
<file_sep>/01_python_basics/02_strings/02_strings.py
"""
Write a function that takes a string and returns the number of vowels in the string.
"""

def count_vowels(string):
    return len([i for i in string if i in 'aeiou'])

print(count_vowels('hello'))
<file_sep>/01_python_basics/02_strings/01_strings.py
"""
Write a function that takes a string and returns the number of characters in the string.
"""

def count_chars(string):
    return len(string)

print(count_chars('hello'))
<file_sep>/01_python_basics/04_functions/03_functions.py
"""
Write a function that takes a list of numbers and returns the sum of the even numbers.
"""

def sum_even(lst):
    return sum([i for i in lst if i % 2 == 0])

print(sum_even([1, 2, 3, 4, 5]))
<file_sep>/01_python_basics/04_functions/04_functions.py
"""
Write a function that takes a list of numbers and returns the sum of the odd numbers.
"""

def sum_odd(lst):
    return sum([i for i in lst if i % 2!= 0])

print(sum_odd([1, 2, 3, 4, 5]))
<file_sep>/01_python_basics/02