"""
Write a function to sort a dictionary by value.
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""

def sort_counter(counter):
    return sorted(counter.items(), key=lambda x: x[1])

print(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}))
/python/python_basics/python_basics_002.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_numbers([1,2,3,4])==10
"""

def sum_numbers(numbers):
    return sum(numbers)

print(sum_numbers([1,2,3,4]))
/python/python_basics/python_basics_001.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest_number([1,2,3,4])==4
"""

def largest_number(numbers):
    return max(numbers)

print(largest_number([1,2,3,4]))
/python/python_basics/python_basics_004.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest_number([1,2,3,4])==1
"""

def smallest_number(numbers):
    return min(numbers)

print(smallest_number([1,2,3,4]))
/python/python_basics/python_basics_003.py
"""
Write a function that takes a list of numbers and returns the average (mean) of the numbers.
assert average([1,2,3,4])==2.5
"""

def average(numbers):
    return sum(numbers)/len(numbers)

print(average([1,2,3,4]))
/python/python_basics/python_basics_005.py
"""
Write a function that takes a list of numbers and returns a new list with only the even numbers.
assert even_numbers([1,2,3,4,5,6])==[2,4,6]
"""

def even_numbers(numbers):
    return [x for x in numbers if x%2==0]

print(even_numbers([1,2,3,4,5,6]))
/python/python_basics/python_basics_006.py
"""
Write a function that takes a list of strings and returns a new list with all strings converted to upper case.
assert upper_case(['hello','world'])==['HELLO','WORLD']
"""

def upper_case(strings):
    return [x.upper() for x in strings]

print(upper_case(['hello','world']))
/python/python_basics/python_basics_007.py
"""
Write a function that takes a list of strings and returns a list with the strings converted to lower case.
assert lower_case(['HELLO','WORLD'])==['hello','world']
"""

def lower_case(strings):
    return [x.lower() for x in strings]

print(lower_case(['HELLO','WORLD']))
/python/python_basics/python_basics_008.py
"""
Write a function that takes a list of numbers and returns a new list with the numbers converted to strings.
assert number_strings([1,2,3,4])==['1','2','3','4']
"""

def number_strings(numbers):
    return [str(x) for x in numbers]

print(number_strings([1,2,3,4]))
/python/python_basics/python_basics_009.py
"""
Write a function that takes a list of strings and returns a list with the strings converted to integers.
assert string_numbers(['1','2','3','4'])==[1,2,3,4]
"""

def string_numbers(strings):
    return [int(x) for x in strings]

print(string_numbers(['1','2','3','4']))