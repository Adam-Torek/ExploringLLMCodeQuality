"""
Write a function to concatenate each element of tuple by the delimiter.
assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""
def concatenate_tuple(tuple_data, delimiter="-"):
    return delimiter.join(tuple_data)

assert concatenate_tuple(("ID", "is", 4, "UTS")) == 'ID-is-4-UTS'

"""
Write a function to convert a list of tuples into a dictionary.
assert convert_list_of_tuples_to_dict([('ID', 'is', 4), ('UTS', 'is', 'awesome')]) == {'ID': 'is', 'UTS': 'is'}
"""
def convert_list_of_tuples_to_dict(list_of_tuples):
    return dict(list_of_tuples)

assert convert_list_of_tuples_to_dict([('ID', 'is', 4), ('UTS', 'is', 'awesome')]) == {'ID': 'is', 'UTS': 'is'}

"""
Write a function to convert a dictionary into a list of tuples.
assert convert_dict_to_list_of_tuples({'ID': 'is', 'UTS': 'is'}) == [('ID', 'is'), ('UTS', 'is')]
"""
def convert_dict_to_list_of_tuples(dict_data):
    return list(dict_data.items())

assert convert_dict_to_list_of_tuples({'ID': 'is', 'UTS': 'is'}) == [('ID', 'is'), ('UTS', 'is')]

"""
Write a function to convert a list of dictionaries into a list of tuples.
assert convert_list_of_dicts_to_list_of_tuples([{'ID': 'is', 'UTS': 'is'}, {'ID': 'is', 'UTS': 'awesome'}]) == [('ID', 'is', 'UTS', 'is'), ('ID', 'is', 'UTS', 'awesome')]
"""
def convert_list_of_dicts_to_list_of_tuples(list_of_dicts):
    return list(zip(*list_of_dicts.values()))

assert convert_list_of_dicts_to_list_of_tuples([{'ID': 'is', 'UTS': 'is'}, {'ID': 'is', 'UTS': 'awesome'}]) == [('ID', 'is', 'UTS', 'is'), ('ID', 'is', 'UTS', 'awesome')]

"""
Write a function to convert a list of tuples into a list of dictionaries.
assert convert_list_of_tuples_to_list_of_dicts([('ID', 'is', 4), ('UTS', 'is', 'awesome')]) == [{'ID': 'is', 'UTS': 'is'}, {'ID': 4, 'UTS': 'awesome'}]
"""
def convert_list_of_tuples_to_list_of_dicts(list_of_tuples):
    return [dict(list_of_tuples[i:i+2]) for i in range(0, len(list_of_tuples), 2)]

assert convert_list_of_tuples_to_list_of_dicts([('ID', 'is', 4), ('UTS', 'is', 'awesome')]) == [{'ID': 'is', 'UTS': 'is'}, {'ID': 4, 'UTS': 'awesome'}]

"""
Write a function to convert a list of dictionaries into a list of lists.
assert convert_list_of_dicts_to_list_of_lists([{'ID': 'is', 'UTS': 'is'}, {'ID': 'is', 'UTS': 'awesome'}]) == [['ID', 'is', 'UTS', 'is'], ['ID', 'is', 'UTS', 'awesome']]
"""
def convert_list_of_dicts_to_list_of_lists(list_of_dicts):
    return [list(list_of_dicts[i].keys()) + list(list_of_dicts[i].values()) for i in range(len(list_of_dicts))]

assert convert_list_of_dicts_to_list_of_lists([{'ID': 'is', 'UTS': 'is'}, {'ID': 'is', 'UTS': 'awesome'}]) == [['ID', 'is', 'UTS', 'is'], ['ID', 'is', 'UTS', 'awesome']]

"""
Write