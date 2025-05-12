"""
Write a function to find the volume of a cube given its side length.
assert volume_cube(3)==27
"""

def volume_cube(side_length):
    return side_length**3

print(volume_cube(3))
/01_python_fundamentals/02_data_types/01_numbers/02_number_types.py
"""
Write a function to find the type of a number.
assert number_type(1)==int
assert number_type(1.0)==float
assert number_type(1+1j)==complex
"""

def number_type(number):
    return type(number)

print(number_type(1))
print(number_type(1.0))
print(number_type(1+1j))
/01_python_fundamentals/02_data_types/01_numbers/01_number_operations.py
"""
Write a function to add two numbers.
assert add(1, 1)==2
"""

def add(a, b):
    return a+b

print(add(1, 1))
/01_python_fundamentals/02_data_types/02_strings/01_string_operations.py
"""
Write a function to concatenate two strings.
assert concatenate("Hello", "World")=="HelloWorld"
"""

def concatenate(a, b):
    return a+b

print(concatenate("Hello", "World"))
/01_python_fundamentals/02_data_types/02_strings/02_string_length.py
"""
Write a function to find the length of a string.
assert length("Hello")==5
"""

def length(string):
    return len(string)

print(length("Hello"))
/01_python_fundamentals/02_data_types/02_strings/03_string_index.py
"""
Write a function to find the index of a character in a string.
assert index("Hello", "e")==1
"""

def index(string, character):
    return string.index(character)

print(index("Hello", "e"))
/01_python_fundamentals/02_data_types/02_strings/04_string_replace.py
"""
Write a function to replace a character in a string.
assert replace("Hello", "e", "a")=="Hallo"
"""

def replace(string, character, replacement):
    return string.replace(character, replacement)

print(replace("Hello", "e", "a"))
/01_python_fundamentals/02_data_types/02_strings/05_string_split.py
"""
Write a function to split a string into a list of words.
assert split("Hello World")==["Hello", "World"]
"""

def split(string):
    return string.split()

print(split("Hello World"))
/01_python_fundamentals/02_data_types/02_strings/06_string_join.py
"""
Write a function to join a list of words into a string.
assert join(["Hello", "World"])=="Hello World"
"""

def join(words):
    return " ".join(words)

print(join(["Hello", "World"]))
/01_python_fundamentals/02_data_types/02_strings/07_string_strip.py
"""
Write a function to strip whitespace from the beginning and end of a string.
assert strip(" Hello ")=="Hello"
"""

def strip(string):
    return string.strip()

print(strip(" Hello "))
/01_python_fundamentals/02_data_types/02_strings/08_string_lower.py
"""
Write a function to convert a string to lowercase.
assert lower("Hello")=="hello"
"""

def lower(string):
    return string.lower()

print(lower("Hello"))
/01_python_fundamentals/02_data_types/02_strings/09_string_upper.py
"""
Write a function to convert a string to uppercase.
assert upper("Hello")=="HELLO"
"""

def upper(string):
    return string.upper()

print(upper("Hello"))
/01_python_fundamentals/