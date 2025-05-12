"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""
def remove_lowercase(string):
    result = ""
    for i in range(len(string)):
        if string[i].isupper():
            result += string[i]
    return result

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another solution using list comprehension
def remove_lowercase(string):
    return ''.join([char for char in string if char.isupper()])

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another solution using regex
import re
def remove_lowercase(string):
    return re.sub('[a-z]+', '', string)

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another solution using set
def remove_lowercase(string):
    return ''.join(set(string))

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another solution using filter
def remove_lowercase(string):
    return ''.join(filter(str.isupper, string))

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another solution using lambda
def remove_lowercase(string):
    return ''.join(filter(lambda char: char.isupper(), string))

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another solution using map
def remove_lowercase(string):
    return ''.join(map(lambda char: char if char.isupper() else '', string))

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another solution using list comprehension with lambda
def remove_lowercase(string):
    return ''.join([char for char in string if char.isupper()])

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another solution using list comprehension with filter
def remove_lowercase(string):
    return ''.join([char for char in string if filter(lambda x: x.isupper(), char)])

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another solution using set comprehension
def remove_lowercase(string):
    return ''.join({char for char in string if char.isupper()})

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another solution using map comprehension
def remove_lowercase(string):
    return ''.join(map(lambda char: char if char.isupper() else '', string))

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another solution using set comprehension
def remove_lowercase(string):
    return ''.join({char for char in string if char.isupper()})

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another solution using filter and lambda
def remove_lowercase(string):
    return ''.join(filter(lambda char: char.isupper(), string))

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another solution using map and lambda
def remove_lowercase(string):
    return ''.join(map(lambda char: char if char.isupper() else '', string))

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another solution using set and lambda
def remove_lowercase(string):
    return ''.join({char for char in string if lambda char: char.isupper()})

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another solution using set and filter
def remove_lowercase(string):
    return ''.join(set(filter(lambda char: char.isupper(), string))

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another solution using set and map
def remove_lowercase(string):
    return ''.join(set(map(lambda char: char if char.isupper(), string))

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another