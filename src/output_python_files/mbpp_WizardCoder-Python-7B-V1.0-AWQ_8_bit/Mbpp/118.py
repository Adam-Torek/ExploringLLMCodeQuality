"""
Write a function to convert a string to a list of strings split on the space character.
assert string_to_list("python programming")==['python','programming']
"""

def string_to_list(string):
    return string.split()

print(string_to_list("python programming"))

# Output: ['python', 'programming']

# Test case 2

print(string_to_list("hello world"))

# Output: ['hello', 'world']

# Test case 3

print(string_to_list(""))

# Output: []

# Test case 4

print(string_to_list("     "))

# Output: []

# Test case 5

print(string_to_list("   python programming   "))

# Output: ['python', 'programming']