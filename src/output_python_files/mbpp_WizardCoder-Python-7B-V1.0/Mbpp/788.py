"""
Write a function to create a new tuple from the given string and list.
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
"""

def new_tuple(lst, str1):
    return tuple(lst + [str1])

print(new_tuple(["WEB", "is"], "best")) # Output: ('WEB', 'is', 'best')