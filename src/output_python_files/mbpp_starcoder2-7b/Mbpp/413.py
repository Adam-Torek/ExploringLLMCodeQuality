"""
Write a function to extract the nth element from a given list of tuples.
assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)],0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
"""

def extract_nth_element(list_of_tuples,n):
    return [i[n] for i in list_of_tuples]

print(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)],0))
/Python/Python_Fundamentals/Functions_Intermediate_I/functions_intermediate_i.py
"""
Functions Intermediate I
"""

"""
1. Update Values in Dictionaries and Lists

Write a function that takes a dictionary as an argument and adds a new key to each key:value pair.

The function should also add a new key:value pair to the dictionary. The key should be "first_name" and the value should be "Michael".

The function should then return the dictionary.

For example, if this code were to be run:

update_dictionary({'first_name': 'Elie', 'last_name': 'Schoppik'})

It would return the following dictionary:

{'first_name': 'Elie', 'last_name': 'Schoppik', 'first_name': 'Michael'}
"""

def update_dictionary(dict,key,value):
    dict[key] = value
    return dict

print(update_dictionary({'first_name': 'Elie', 'last_name': 'Schoppik'},'first_name','Michael'))

"""
2. Iterate Through a Dictionary with List Values

Write a function that takes in a dictionary and returns a new list of values based on a key.

For example, if this code were to be run:

iterateDictionary2({'first_name': 'Elie', 'last_name': 'Schoppik'})

It would return the following list:

['Elie', 'Schoppik']
"""

def iterateDictionary2(dict):
    return list(dict.values())

print(iterateDictionary2({'first_name': 'Elie', 'last_name': 'Schoppik'}))

"""
3. Iterate Through a Dictionary with List Values

Write a function that takes in a dictionary and returns a new list of values based on a key.

For example, if this code were to be run:

iterateDictionary2({'first_name': 'Elie', 'last_name': 'Schoppik'})

It would return the following list:

['Elie', 'Schoppik']
"""

def iterateDictionary2(dict):
    return list(dict.values())

print(iterateDictionary2({'first_name': 'Elie', 'last_name': 'Schoppik'}))

"""
4. Iterate Through a Dictionary with List Values

Write a function that takes in a dictionary and returns a new list of values based on a key.

For example, if this code were to be run:

iterateDictionary2({'first_name': 'Elie', 'last_name': 'Schoppik'})

It would return the following list:

['Elie', 'Schoppik']
"""

def iterateDictionary2(dict):
    return list(dict.values())

print(iterateDictionary2({'first_name': 'Elie', 'last_name': 'Schoppik'}))

"""
5. Get Values From a List of Dictionaries

Write a function that takes a list of dictionaries and returns a new list of values from the key:value pairs.

For example, if this code were to be run:

iterateDictionary2([{'first_name': 'Elie', 'last_name': 'Schoppik'}, {'first_name': 'Matt', 'last_name': 'Lane'}])

It would return the following list:

['Elie', 'Schoppik', 'Matt', 'Lane']
"""

def iterateDictionary