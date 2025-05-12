"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""

def max_aggregate(list_of_tuples):
    max_name = ''
    max_score = 0
    for name, score in list_of_tuples:
        if score > max_score:
            max_name = name
            max_score = score
    return max_name, max_score

assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
<file_sep>/week_02/day_03/01_list_to_dict.py
"""
Write a function that converts a list to a dictionary.
assert list_to_dict(['a', 'b', 'c', 'd']) == {'a': 0, 'b': 1, 'c': 2, 'd': 3}
"""

def list_to_dict(list_of_strings):
    dict_of_strings = {}
    for i in range(len(list_of_strings)):
        dict_of_strings[list_of_strings[i]] = i
    return dict_of_strings

assert list_to_dict(['a', 'b', 'c', 'd']) == {'a': 0, 'b': 1, 'c': 2, 'd': 3}
<file_sep>/week_02/day_03/02_dict_to_list.py
"""
Write a function that converts a dictionary to a list.
assert dict_to_list({'a': 0, 'b': 1, 'c': 2, 'd': 3}) == ['a', 'b', 'c', 'd']
"""

def dict_to_list(dict_of_strings):
    list_of_strings = []
    for key in dict_of_strings:
        list_of_strings.append(key)
    return list_of_strings

assert dict_to_list({'a': 0, 'b': 1, 'c': 2, 'd': 3}) == ['a', 'b', 'c', 'd']
<file_sep>/week_02/day_03/03_dict_to_tuple.py
"""
Write a function that converts a dictionary to a tuple.
assert dict_to_tuple({'a': 0, 'b': 1, 'c': 2, 'd': 3}) == (('a', 0), ('b', 1), ('c', 2), ('d', 3))
"""

def dict_to_tuple(dict_of_strings):
    tuple_of_strings = ()
    for key in dict_of_strings:
        tuple_of_strings += ((key, dict_of_strings[key]),)
    return tuple_of_strings

assert dict_to_tuple({'a': 0, 'b': 1, 'c': 2, 'd': 3}) == (('a', 0), ('b', 1), ('c', 2), ('d', 3))
<file_sep>/week_02/day_03/04_tuple_to_dict.py
"""
Write a function that converts a tuple to a dictionary.
assert tuple_to_dict(('a', 0), ('b', 1), ('c', 2), ('d', 3)) == {'a': 0, 'b': 1, 'c': 2, 'd': 3}
"""

def tuple_to_dict(tuple_of_strings):
    dict_of_strings = {}
    for i in range(len(tuple_of_strings)):
        dict_of_strings[tuple_of_strings[i][0]] = tuple_of_strings[i][1]
    return dict_of_strings

assert tuple_to_dict(('a', 0), ('b', 1), ('c', 2), ('d', 3)) == {'a': 0, 'b': 1, 'c': 2, '