"""
Write a function to convert a given string to a tuple of characters.
assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
"""
def string_to_tuple(string):
    return tuple(string)

# Test cases
print(string_to_tuple("python 3.0")) # Output: ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
print(string_to_tuple("hello world")) # Output: ('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')
print(string_to_tuple("12345")) # Output: ('1', '2', '3', '4', '5')
print(string_to_tuple("")) # Output: ()