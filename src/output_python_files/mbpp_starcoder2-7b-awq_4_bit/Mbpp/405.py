"""
Write a function to check whether an element exists within a tuple.
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
"""

def check_tuplex(tuplex, element):
    return element in tuplex

assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'z')==False

"""
Write a function to check whether an element exists within a list.
assert check_listx([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)==True
"""

def check_listx(listx, element):
    return element in listx

assert check_listx([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)==True
assert check_listx([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)==False

"""
Write a function to check whether an element exists within a set.
assert check_setx({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 3)==True
"""

def check_setx(setx, element):
    return element in setx

assert check_setx({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 3)==True
assert check_setx({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 11)==False

"""
Write a function to check whether an element exists within a dictionary.
assert check_dictx({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}, "c")==True
"""

def check_dictx(dictx, element):
    return element in dictx.keys()

assert check_dictx({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}, "c")==True
assert check_dictx({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}, "z")==False

"""
Write a function to check whether an element exists within a string.
assert check_stringx("w3resource", "r")==True
"""

def check_stringx(stringx, element):
    return element in stringx

assert check_stringx("w3resource", "r")==True
assert check_stringx("w3resource", "z")==False

"""
Write a function to check whether an element exists within a byte string.
assert check_bytesx(b"w3resource", b"r")==True
"""

def check_bytesx(bytesx, element):
    return element in bytesx

assert check_bytesx(b"w3resource", b"r")==True
assert check_bytesx(b"w3resource", b"z")==False

"""
Write a function to check whether an element exists within a byte array.
assert check_bytearrayx(bytearray(b"w3resource"), b"r")==True
"""

def check_bytearrayx(bytearrayx, element):
    return element in bytearrayx

assert check_bytearrayx(bytearray(b"w3resource"), b"r")==True
assert check_bytearrayx(bytearray(b"w3resource"), b