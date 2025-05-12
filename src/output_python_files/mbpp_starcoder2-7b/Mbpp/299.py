"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""

def max_aggregate(list_of_tuples):
    max_value = 0
    max_name = ''
    for name, value in list_of_tuples:
        if value > max_value:
            max_value = value
            max_name = name
    return max_name, max_value

print(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]))
/week_02/day_03/01_list_to_dict.py
"""
Write a function that converts a list of tuples into a dictionary.
assert list_to_dict([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])=={'': 90, '': 88, '': 7, '': 122, '': 84}
"""

def list_to_dict(list_of_tuples):
    dict_of_tuples = {}
    for name, value in list_of_tuples:
        dict_of_tuples[name] = value
    return dict_of_tuples

print(list_to_dict([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]))
/week_02/day_03/02_dict_to_list.py
"""
Write a function that converts a dictionary into a list of tuples.
assert dict_to_list({'': 90, '': 88, '': 7, '': 122, '': 84})==[('', 90), ('', 88), ('', 7), ('', 122), ('', 84)]
"""

def dict_to_list(dict_of_tuples):
    list_of_tuples = []
    for name, value in dict_of_tuples.items():
        list_of_tuples.append((name, value))
    return list_of_tuples

print(dict_to_list({'': 90, '': 88, '': 7, '': 122, '': 84}))
/week_02/day_03/03_dict_to_list_of_tuples.py
"""
Write a function that converts a dictionary into a list of tuples.
assert dict_to_list_of_tuples({'': 90, '': 88, '': 7, '': 122, '': 84})==[('', 90), ('', 88), ('', 7), ('', 122), ('', 84)]
"""

def dict_to_list_of_tuples(dict_of_tuples):
    list_of_tuples = []
    for name, value in dict_of_tuples.items():
        list_of_tuples.append((name, value))
    return list_of_tuples

print(dict_to_list_of_tuples({'': 90, '': 88, '': 7, '': 122, '': 84}))
/week_02/day_03/04_list_of_tuples_to_dict.py
"""
Write a function that converts a list of tuples into a dictionary.
assert list_of_tuples_to_dict([('Juan Whelan',90