"""
Write a function to rotate a given list by specified number of items to the right direction. https://www.geeksforgeeks.org/python-program-right-rotate-list-n/
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
"""

def rotate_right(lst,n):
    return lst[n:] + lst[:n]

assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
/python/list/list_to_string.py
"""
Write a function to convert a list to a string. https://www.geeksforgeeks.org/python-program-to-convert-list-to-string/
assert list_to_string([1,2,3,4])=="1234"
"""

def list_to_string(lst):
    return "".join(str(x) for x in lst)

assert list_to_string([1,2,3,4])=="1234"
/python/list/list_to_tuple.py
"""
Write a function to convert a list to a tuple. https://www.geeksforgeeks.org/python-program-to-convert-list-to-tuple/
assert list_to_tuple([1,2,3,4])==(1,2,3,4)
"""

def list_to_tuple(lst):
    return tuple(lst)

assert list_to_tuple([1,2,3,4])==(1,2,3,4)
/python/list/list_to_set.py
"""
Write a function to convert a list to a set. https://www.geeksforgeeks.org/python-program-to-convert-list-to-set/
assert list_to_set([1,2,3,4])=={1,2,3,4}
"""

def list_to_set(lst):
    return set(lst)

assert list_to_set([1,2,3,4])=={1,2,3,4}
/python/list/list_to_dict.py
"""
Write a function to convert a list to a dictionary. https://www.geeksforgeeks.org/python-program-to-convert-list-to-dictionary/
assert list_to_dict([1,2,3,4])=={1:1,2:2,3:3,4:4}
"""

def list_to_dict(lst):
    return dict(zip(lst,lst))

assert list_to_dict([1,2,3,4])=={1:1,2:2,3:3,4:4}
/python/list/list_to_json.py
"""
Write a function to convert a list to a JSON. https://www.geeksforgeeks.org/python-program-to-convert-list-to-json/
assert list_to_json([1,2,3,4])=="[1,2,3,4]"
"""

def list_to_json(lst):
    return str(lst)

assert list_to_json([1,2,3,4])=="[1,2,3,4]"
/python/list/list_to_string_with_separator.py
"""
Write a function to convert a list to a string with separator. https://www.geeksforgeeks.org/python-program-to-convert-list-to-string-with-separator/
assert list_to_string_with_separator([1,2,3,4],",")=="1,2,3,4"
"""

def list_to_string_with_separator(lst,sep):
    return sep.join(str(x) for x in lst)

assert list_to_string_with_separator([1,2,3,4],",")=="1,2,3,4"
/python/list/list_to_json_with_