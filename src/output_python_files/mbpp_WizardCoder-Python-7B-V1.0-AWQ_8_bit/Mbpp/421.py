"""
Write a function to concatenate each element of tuple by the delimiter.
assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""

def concatenate_tuple(tup, delimiter='-'):
    return delimiter.join(str(x) for x in tup)

print(concatenate_tuple(("ID", "is", 4, "UTS")) # Output: 'ID-is-4-UTS'
print(concatenate_tuple(("Hello", "World", "!")) # Output: 'Hello-World-!'
print(concatenate_tuple(("Python", "Programming", "Is", "Awesome", delimiter=' ')) # Output: 'Python Programming Is Awesome'