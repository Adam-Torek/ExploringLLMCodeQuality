"""
Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
"""

def dict_filter(dictionary, n):
    new_dict = {}
    for key, value in dictionary.items():
        if value >= n:
            new_dict[key] = value
    return new_dict

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170))
/week_01/day_02/01_list_functions.py
"""
Write a function that takes in a list and returns a new list with all the elements reversed.
assert reverse([1,2,3,4,5])==[5,4,3,2,1]
"""

def reverse(list):
    new_list = []
    for i in range(len(list)-1,-1,-1):
        new_list.append(list[i])
    return new_list

print(reverse([1,2,3,4,5]))
/week_01/day_02/03_list_functions.py
"""
Write a function that takes in a list and returns a new list with all the elements reversed.
assert reverse([1,2,3,4,5])==[5,4,3,2,1]
"""

def reverse(list):
    new_list = []
    for i in range(len(list)-1,-1,-1):
        new_list.append(list[i])
    return new_list

print(reverse([1,2,3,4,5]))

"""
Write a function that takes in a list and returns a new list with all the elements reversed.
assert reverse([1,2,3,4,5])==[5,4,3,2,1]
"""

def reverse(list):
    new_list = []
    for i in range(len(list)-1,-1,-1):
        new_list.append(list[i])
    return new_list

print(reverse([1,2,3,4,5]))

"""
Write a function that takes in a list and returns a new list with all the elements reversed.
assert reverse([1,2,3,4,5])==[5,4,3,2,1]
"""

def reverse(list):
    new_list = []
    for i in range(len(list)-1,-1,-1):
        new_list.append(list[i])
    return new_list

print(reverse([1,2,3,4,5]))

"""
Write a function that takes in a list and returns a new list with all the elements reversed.
assert reverse([1,2,3,4,5])==[5,4,3,2,1]
"""

def reverse(list):
    new_list = []
    for i in range(len(list)-1,-1,-1):
        new_list.append(list[i])
    return new_list

print(reverse([1,2,3,4,5]))

"""
Write a function that takes in a list and returns a new list with all the elements reversed.
assert reverse([1,2,3,4,5])==[5,4,3,2,1]
"""

def reverse(list):
    new_list = []
    for i in range(len(list)-1,-1,-1):
        new_list.append(list[i])
    return new_list

print(reverse([1,2,3,4,5]))

"""
Write a function that takes in a list and returns a new list with all the elements reversed.
assert reverse([1,2,3,4,5])==[5,4,3,2,1]
"""

def reverse(list):
    new_list = []
    for i in range(len(list)-1,-1,-1):