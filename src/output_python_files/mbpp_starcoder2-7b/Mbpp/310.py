"""
Write a function to convert a given string to a tuple of characters.
assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
"""
def string_to_tuple(string):
    return tuple(string)

print(string_to_tuple("python 3.0"))

"""
Write a function to convert a given tuple of characters to a string.
assert tuple_to_string(('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0'))=="python 3.0"
"""
def tuple_to_string(tuple):
    return ''.join(tuple)

print(tuple_to_string(('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')))

"""
Write a function to convert a given string to a list of characters.
assert string_to_list("python 3.0")==['p', 'y', 't', 'h', 'o', 'n', '3', '.', '0']
"""
def string_to_list(string):
    return list(string)

print(string_to_list("python 3.0"))

"""
Write a function to convert a given list of characters to a string.
assert list_to_string(['p', 'y', 't', 'h', 'o', 'n', '3', '.', '0'])=="python 3.0"
"""
def list_to_string(list):
    return ''.join(list)

print(list_to_string(['p', 'y', 't', 'h', 'o', 'n', '3', '.', '0']))

"""
Write a function to convert a given string to a set of characters.
assert string_to_set("python 3.0")=={'0', '3','', 'n', 'y', 'h', 'o', 't', 'p'}
"""
def string_to_set(string):
    return set(string)

print(string_to_set("python 3.0"))

"""
Write a function to convert a given set of characters to a string.
assert set_to_string({'0', '3','', 'n', 'y', 'h', 'o', 't', 'p'})=="python 3.0"
"""
def set_to_string(set):
    return ''.join(set)

print(set_to_string({'0', '3','', 'n', 'y', 'h', 'o', 't', 'p'}))

"""
Write a function to convert a given string to a dictionary of characters and their counts.
assert string_to_dict("python 3.0")=={'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '3': 1, '.': 1, '0': 1}
"""
def string_to_dict(string):
    return {char: string.count(char) for char in string}

print(string_to_dict("python 3.0"))

"""
Write a function to convert a given dictionary of characters and their counts to a string.
assert dict_to_string({'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '3': 1, '.': 1, '0': 1})=="python 3.0"
"""
def dict_to_string(dict):
    return ''.join(dict.keys()) * dict.get('p')

print(dict_to_string({'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '3': 1, '.': 1, '0': 1}))

"""
Write a function to convert a given string to a dictionary of characters and their counts.
assert string_to_dict("python 3.0")=={'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '3': 1, '.': 1, '0