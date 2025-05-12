"""
Write a function to remove all whitespaces from the given string.
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
"""

def remove_whitespaces(string):
    return string.replace(' ','')

print(remove_whitespaces(' Google    Flutter '))
/python/strings/string_to_list.py
"""
Write a function to convert a string to a list of characters.
assert string_to_list('google') == ['g', 'o', 'o', 'g', 'l', 'e']
"""

def string_to_list(string):
    return list(string)

print(string_to_list('google'))
/python/strings/reverse_string.py
"""
Write a function to reverse a string.
assert reverse_string('google') == 'elgoog'
"""

def reverse_string(string):
    return string[::-1]

print(reverse_string('google'))
/python/strings/string_to_integer.py
"""
Write a function to convert a string to an integer.
assert string_to_integer('123') == 123
"""

def string_to_integer(string):
    return int(string)

print(string_to_integer('123'))
/python/strings/string_to_float.py
"""
Write a function to convert a string to a float.
assert string_to_float('123.45') == 123.45
"""

def string_to_float(string):
    return float(string)

print(string_to_float('123.45'))
/python/strings/string_to_list_of_words.py
"""
Write a function to convert a string to a list of words.
assert string_to_list_of_words('google flutter') == ['google', 'flutter']
"""

def string_to_list_of_words(string):
    return string.split()

print(string_to_list_of_words('google flutter'))
/python/strings/string_to_list_of_integers.py
"""
Write a function to convert a string to a list of integers.
assert string_to_list_of_integers('123 456') == [123, 456]
"""

def string_to_list_of_integers(string):
    return list(map(int, string.split()))

print(string_to_list_of_integers('123 456'))
/python/strings/string_to_list_of_floats.py
"""
Write a function to convert a string to a list of floats.
assert string_to_list_of_floats('123.45 678.90') == [123.45, 678.90]
"""

def string_to_list_of_floats(string):
    return list(map(float, string.split()))

print(string_to_list_of_floats('123.45 678.90'))
/python/strings/string_to_list_of_characters.py
"""
Write a function to convert a string to a list of characters.
assert string_to_list_of_characters('google') == ['g', 'o', 'o', 'g', 'l', 'e']
"""

def string_to_list_of_characters(string):
    return list(string)

print(string_to_list_of_characters('google'))
/python/strings/string_to_list_of_words_and_integers.py
"""
Write a function to convert a string to a list of words and integers.
assert string_to_list_of_words_and_integers('123 google 456') == [123, 'google', 456]
"""

def string_to_list_of_words_and_integers(string):
    return list(map(int, string.split()))

print(string_to_list_of_words_and_integers('123 google 456'))
/python/strings/string_to_list_of_words_and_floats.py
"""
Write a function to