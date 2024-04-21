"""
Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
"""

def dict_filter(d, n):
    return {k:v for k,v in d.items() if v >= n}

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170))

"""
Write a function that takes in a dictionary and returns a list of all the values in the dictionary.
assert dict_values({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190})==[175, 180, 165, 190]
"""

def dict_values(d):
    return list(d.values())

print(dict_values({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}))

"""
Write a function that takes in a dictionary and returns a list of all the keys in the dictionary.
assert dict_keys({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190})==['Cierra Vega', 'Alden Cantrell', 'Kierra Gentry', 'Pierre Cox']
"""

def dict_keys(d):
    return list(d.keys())

print(dict_keys({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}))

"""
Write a function that takes in a dictionary and returns a list of all the keys and values in the dictionary.
assert dict_items({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190})==[('Cierra Vega', 175), ('Alden Cantrell', 180), ('Kierra Gentry', 165), ('Pierre Cox', 190)]
"""

def dict_items(d):
    return list(d.items())

print(dict_items({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}))

"""
Write a function that takes in a dictionary and returns a list of all the keys and values in the dictionary.
assert dict_items({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190})==[('Cierra Vega', 175), ('Alden Cantrell', 180), ('Kierra Gentry', 165), ('Pierre Cox', 190)]
"""

def dict_items(d):
    return list(d.items())

print(dict_items({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}))

"""
Write a function that takes in a dictionary and returns a list of all the keys and values in the dictionary.
assert dict_items({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190})==[('