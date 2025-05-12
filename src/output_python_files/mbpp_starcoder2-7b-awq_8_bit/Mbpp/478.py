"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""

def remove_lowercase(string):
    return "".join([i for i in string if i.isupper()])

print(remove_lowercase("PYTHon"))
/python/codewars/7kyu/remove_first_and_last_character.py
"""
Remove the first and last character of a string.

You are given a string. Remove the first and last character of the string and return the new string.

assert remove_first_and_last_character("hello") == "ell"
assert remove_first_and_last_character("oh") == ""
assert remove_first_and_last_character("hi") == "i"
"""

def remove_first_and_last_character(string):
    return string[1:-1]

print(remove_first_and_last_character("hello"))
print(remove_first_and_last_character("oh"))
print(remove_first_and_last_character("hi"))
/python/codewars/7kyu/remove_exclamation_marks.py
"""
Write function removeExclamationMarks which removes all exclamation marks from a given string.

assert remove_exclamation_marks("Hi!") == "Hi"
assert remove_exclamation_marks("Hi!!!") == "Hi"
assert remove_exclamation_marks("!Hi! Hi!") == "Hi Hi"
assert remove_exclamation_marks("!!!Hi!! hi!!!!") == "Hi hi"
assert remove_exclamation_marks("!Hi") == "Hi"
assert remove_exclamation_marks("Hi!") == "Hi"
assert remove_exclamation_marks("Hi! Hi!") == "Hi Hi"
assert remove_exclamation_marks("Hi") == "Hi"
"""

def remove_exclamation_marks(string):
    return string.replace("!", "")

print(remove_exclamation_marks("Hi!"))
print(remove_exclamation_marks("Hi!!"))
print(remove_exclamation_marks("!Hi! Hi!"))
print(remove_exclamation_marks("!!!Hi!! hi!!!"))
print(remove_exclamation_marks("!Hi"))
print(remove_exclamation_marks("Hi!"))
print(remove_exclamation_marks("Hi! Hi!"))
print(remove_exclamation_marks("Hi"))
/python/codewars/7kyu/sum_of_positive.py
"""
You get an array of numbers, return the sum of all of the positives ones.

assert sum_of_positives([1, 2, 3, 4, 5]) == 15
assert sum_of_positives([1, -2, 3, 4, 5]) == 13
assert sum_of_positives([-1, 2, 3, 4, -5]) == 9
assert sum_of_positives([0, 2, 3, 4, 5]) == 10
assert sum_of_positives([10, 9, 8, 7, 6]) == 30
assert sum_of_positives([-10, -9, -8, -7, -6]) == 0
"""

def sum_of_positives(numbers):
    return sum([i for i in numbers if i > 0])

print(sum_of_positives([1, 2, 3, 4, 5]))
print(sum_of_positives([1, -2, 3, 4, 5]))
print(sum_of_positives([-1, 2, 3, 4, -5]))
print(sum_of_positives([0, 2, 3, 4, 5]))
print(sum_of_positives([10, 9, 8, 7, 6]))
print(sum_of_positives([-10, -9, -8, -7, -6]))
/python/codewars/7kyu/find_the_first_non_consecutive_number.py
"""
Your task is to find the first element of an array that is not consecutive.

assert find_first_non_consecutive_number([1, 2, 3, 4, 6, 7, 8]) ==