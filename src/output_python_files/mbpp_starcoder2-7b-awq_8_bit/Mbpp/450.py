"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice','solution'],8)==['practice','solution']
"""
def extract_string(list_of_string,size):
    return list_of_string[-size:]

assert extract_string(['Python', 'list', 'exercises', 'practice','solution'],8)==['practice','solution']

"""
Write a function to convert a given list of strings to a list of integers.
assert convert_string_to_int(['1', '2', '3', '4', '5'])==[1, 2, 3, 4, 5]
"""
def convert_string_to_int(list_of_string):
    return [int(i) for i in list_of_string]

assert convert_string_to_int(['1', '2', '3', '4', '5'])==[1, 2, 3, 4, 5]

"""
Write a function to convert a given list of integers to a list of strings.
assert convert_int_to_string([1, 2, 3, 4, 5])==['1', '2', '3', '4', '5']
"""
def convert_int_to_string(list_of_int):
    return [str(i) for i in list_of_int]

assert convert_int_to_string([1, 2, 3, 4, 5])==['1', '2', '3', '4', '5']

"""
Write a function to convert a given list of strings to a list of floats.
assert convert_string_to_float(['1', '2', '3', '4', '5'])==[1.0, 2.0, 3.0, 4.0, 5.0]
"""
def convert_string_to_float(list_of_string):
    return [float(i) for i in list_of_string]

assert convert_string_to_float(['1', '2', '3', '4', '5'])==[1.0, 2.0, 3.0, 4.0, 5.0]

"""
Write a function to convert a given list of floats to a list of strings.
assert convert_float_to_string([1.0, 2.0, 3.0, 4.0, 5.0])==['1.0', '2.0', '3.0', '4.0', '5.0']
"""
def convert_float_to_string(list_of_float):
    return [str(i) for i in list_of_float]

assert convert_float_to_string([1.0, 2.0, 3.0, 4.0, 5.0])==['1.0', '2.0', '3.0', '4.0', '5.0']

"""
Write a function to convert a given list of strings to a list of booleans.
assert convert_string_to_boolean(['True', 'False', 'True', 'False', 'True'])==[True, False, True, False, True]
"""
def convert_string_to_boolean(list_of_string):
    return [bool(i) for i in list_of_string]

assert convert_string_to_boolean(['True', 'False', 'True', 'False', 'True'])==[True, False, True, False, True]

"""
Write a function to convert a given list of booleans to a list of strings.
assert convert_boolean_to_string([True, False, True, False, True])==['True', 'False', 'True', 'False', 'True']
"""
def convert_boolean_to_string(list_of_boolean):
    return [str(i) for i in list_of_boolean]

assert convert_boolean_to_string([True, False, True, False, True])==['True', 'False', 'True', 'False', 'True']

"""
Write a function to convert a given list of strings to a list of lists.
assert convert_string_to_list(['Python', 'list', 'exercises', 'practice','solution'])==[['Python'], ['list'], ['exercises'], ['practice'], ['solution']]
"""
def