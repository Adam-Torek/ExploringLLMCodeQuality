"""
Write a function to concatenate each element of tuple by the delimiter.
assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""

def concatenate_tuple(tuple_of_strings, delimiter="-"):
    return delimiter.join(tuple_of_strings)

print(concatenate_tuple(("ID", "is", 4, "UTS")))

"""
Write a function to convert a list of strings to a list of integers.
assert convert_list_of_strings_to_integers(["1", "2", "3"]) == [1, 2, 3]
"""

def convert_list_of_strings_to_integers(list_of_strings):
    return [int(string) for string in list_of_strings]

print(convert_list_of_strings_to_integers(["1", "2", "3"]))

"""
Write a function to convert a list of strings to a list of floats.
assert convert_list_of_strings_to_floats(["1.0", "2.0", "3.0"]) == [1.0, 2.0, 3.0]
"""

def convert_list_of_strings_to_floats(list_of_strings):
    return [float(string) for string in list_of_strings]

print(convert_list_of_strings_to_floats(["1.0", "2.0", "3.0"]))

"""
Write a function to convert a list of strings to a list of booleans.
assert convert_list_of_strings_to_booleans(["True", "False", "True"]) == [True, False, True]
"""

def convert_list_of_strings_to_booleans(list_of_strings):
    return [bool(string) for string in list_of_strings]

print(convert_list_of_strings_to_booleans(["True", "False", "True"]))

"""
Write a function to convert a list of strings to a list of None.
assert convert_list_of_strings_to_none(["None", "None", "None"]) == [None, None, None]
"""

def convert_list_of_strings_to_none(list_of_strings):
    return [None for string in list_of_strings]

print(convert_list_of_strings_to_none(["None", "None", "None"]))

"""
Write a function to convert a list of strings to a list of lists of strings.
assert convert_list_of_strings_to_list_of_lists_of_strings(["1", "2", "3"]) == [[1], [2], [3]]
"""

def convert_list_of_strings_to_list_of_lists_of_strings(list_of_strings):
    return [[string] for string in list_of_strings]

print(convert_list_of_strings_to_list_of_lists_of_strings(["1", "2", "3"]))

"""
Write a function to convert a list of strings to a list of lists of integers.
assert convert_list_of_strings_to_list_of_lists_of_integers(["1", "2", "3"]) == [[1], [2], [3]]
"""

def convert_list_of_strings_to_list_of_lists_of_integers(list_of_strings):
    return [[int(string)] for string in list_of_strings]

print(convert_list_of_strings_to_list_of_lists_of_integers(["1", "2", "3"]))

"""
Write a function to convert a list of strings to a list of lists of floats.
assert convert_list_of_strings_to_list_of_lists_of_floats(["1.0", "2.0", "3.0"]) == [[1.0], [2.0], [3.0]]
"""

def convert_list_of_strings_to_list_of_lists_of_floats(list_of_strings):
    return [[float(string)] for string in list_of_strings]

print(convert_list_of_strings_to_list_of_lists_of_floats(["1.0", "2.0", "3.0"]))

"""
Write a function to convert a