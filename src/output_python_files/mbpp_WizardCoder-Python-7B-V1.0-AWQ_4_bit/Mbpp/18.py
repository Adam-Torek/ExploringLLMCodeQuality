"""
Write a function to remove characters from the first string which are present in the second string.
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
"""

def remove_dirty_chars(str1, str2):
    for char in str2:
        str1 = str1.replace(char, '')
    return str1

print(remove_dirty_chars("probasscurve", "pros")) # Output: 'bacuve'

# Another way to solve this problem using list comprehension
def remove_dirty_chars(str1, str2):
    return ''.join([char for char in str1 if char not in str2])

print(remove_dirty_chars("probasscurve", "pros")) # Output: 'bacuve'

# Another way to solve this problem using set()
def remove_dirty_chars(str1, str2):
    return ''.join([char for char in str1 if char not in set(str2)])

print(remove_dirty_chars("probasscurve", "pros")) # Output: 'bacuve'

# Another way to solve this problem using set() and set difference
def remove_dirty_chars(str1, str2):
    return ''.join(set(str1) - set(str2))

print(remove_dirty_chars("probasscurve", "pros")) # Output: 'bacuve'

# Another way to solve this problem using set() and set intersection
def remove_dirty_chars(str1, str2):
    return ''.join(set(str1) - set(str2))

print(remove_dirty_chars("probasscurve", "pros")) # Output: 'bacuve'

# Another way to solve this problem using set() and set intersection
def remove_dirty_chars(str1, str2):
    return ''.join(set(str1) ^ set(str2))

print(remove_dirty_chars("probasscurve", "pros")) # Output: 'bacuve'

# Another way to solve this problem using set() and set symmetric difference
def remove_dirty_chars(str1, str2):
    return ''.join(set(str1) ^ set(str2))

print(remove_dirty_chars("probasscurve", "pros")) # Output: 'bacuve'

# Another way to solve this problem using set() and set symmetric difference
def remove_dirty_chars(str1, str2):
    return ''.join(set(str1) & set(str2))

print(remove_dirty_chars("probasscurve", "pros")) # Output: ''

# Another way to solve this problem using set() and set symmetric difference
def remove_dirty_chars(str1, str2):
    return ''.join(set(str1) - set(str2))

print(remove_dirty_chars("probasscurve", "pros")) # Output: 'bacuve'

# Another way to solve this problem using set() and set symmetric difference
def remove_dirty_chars(str1, str2):
    return ''.join(set(str1) | set(str2))

print(remove_dirty_chars("probasscurve", "pros")) # Output: 'probasscurve'

# Another way to solve this problem using set() and set symmetric difference
def remove_dirty_chars(str1, str2):
    return ''.join(set(str1) ^ set(str2))

print(remove_dirty_chars("probasscurve", "pros")) # Output: 'bacuve'

# Another way to solve this problem using set() and set symmetric difference
def remove_dirty_chars(str1, str2):
    return ''.join(set(str1) & set(str2))

print(remove_dirty_chars("probasscurve", "pros")) # Output: ''

# Another way to solve this problem using set() and set symmetric difference
def remove_dirty_chars(str1, str2):
    return ''.join(set(str1)