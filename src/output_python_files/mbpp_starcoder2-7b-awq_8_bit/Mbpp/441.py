"""
Write a function to find the surface area of a cube of a given size.
assert surfacearea_cube(5)==150
"""

def surfacearea_cube(size):
    return 6*size**2

print(surfacearea_cube(5))/02_python_fundamentals/01_python_fundamentals_exercises/01_python_fundamentals_exercises.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_list([1,2,3,4])==10
"""

def sum_list(numbers):
    return sum(numbers)

print(sum_list([1,2,3,4]))

"""
Write a function that takes a list of numbers and returns the average (mean) of the numbers.
assert average([1,2,3,4])==2.5
"""

def average(numbers):
    return sum(numbers)/len(numbers)

print(average([1,2,3,4]))

"""
Write a function that takes a list of numbers and returns the minimum value in the list.
assert min_list([1,2,3,4])==1
"""

def min_list(numbers):
    return min(numbers)

print(min_list([1,2,3,4]))

"""
Write a function that takes a list of numbers and returns the maximum value in the list.
assert max_list([1,2,3,4])==4
"""

def max_list(numbers):
    return max(numbers)

print(max_list([1,2,3,4]))

"""
Write a function that takes a list of numbers and returns a new list with only the even numbers.
assert even_list([1,2,3,4,5,6])==[2,4,6]
"""

def even_list(numbers):
    return [x for x in numbers if x%2==0]

print(even_list([1,2,3,4,5,6]))

"""
Write a function that takes a list of strings and returns a new list with the strings converted to upper case.
assert upper_list(["hello","world"])==["HELLO","WORLD"]
"""

def upper_list(strings):
    return [x.upper() for x in strings]

print(upper_list(["hello","world"]))

"""
Write a function that takes a list of numbers and returns a new list with the numbers converted to strings.
assert string_list([1,2,3,4])==["1","2","3","4"]
"""

def string_list(numbers):
    return [str(x) for x in numbers]

print(string_list([1,2,3,4]))

"""
Write a function that takes a list of numbers and returns a new list with the numbers converted to strings and separated by a comma.
assert comma_list([1,2,3,4])=="1,2,3,4"
"""

def comma_list(numbers):
    return ",".join([str(x) for x in numbers])

print(comma_list([1,2,3,4]))

"""
Write a function that takes a list of words and returns a list of words.
assert unique_list(["hello","world","hello"])==["hello","world"]
"""

def unique_list(words):
    return list(set(words))

print(unique_list(["hello","world","hello"]))

"""
Write a function that takes a list of words and returns a list of words.
assert unique_list(["hello","world","hello"])==["hello","world"]
"""

def unique_list(words):
    return list(set(words))

print(unique_list(["hello","world","hello"]))

"""
Write a function that takes a list of words and returns a list of words.
assert unique_list(["hello","world","hello"])==["hello","world"]
"""

def unique_list(words):
    return list(set(words))

print(unique_list(["hello","world","hello"]))

"""
Write a function that takes a list of words and returns a list of words.
assert unique_list(["hello","world","hello"])==["hello","world"]
"""

def unique_list(words):
    return list(set(words))

print(unique_list(["hello","world","hello"]))

"""
Write a