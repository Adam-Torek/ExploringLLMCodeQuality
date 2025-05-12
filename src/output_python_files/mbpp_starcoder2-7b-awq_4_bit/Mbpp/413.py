"""
Write a function to extract the nth element from a given list of tuples.
assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)],0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
"""

def extract_nth_element(list_of_tuples, n):
    return [i[n] for i in list_of_tuples]

assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)],0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']

"""
Write a function to find the first element of a list that is greater than n.
assert find_first_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)==6
"""

def find_first_element(list_of_numbers, n):
    for i in list_of_numbers:
        if i > n:
            return i

assert find_first_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)==6

"""
Write a function to find the last element of a list that is greater than n.
assert find_last_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)==10
"""

def find_last_element(list_of_numbers, n):
    for i in list_of_numbers[::-1]:
        if i > n:
            return i

assert find_last_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)==10

"""
Write a function to find the first element of a list that is greater than n.
assert find_first_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)==6
"""

def find_first_element(list_of_numbers, n):
    for i in list_of_numbers:
        if i > n:
            return i

assert find_first_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)==6

"""
Write a function to find the last element of a list that is greater than n.
assert find_last_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)==10
"""

def find_last_element(list_of_numbers, n):
    for i in list_of_numbers[::-1]:
        if i > n:
            return i

assert find_last_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)==10

"""
Write a function to find the first element of a list that is greater than n.
assert find_first_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)==6
"""

def find_first_element(list_of_numbers, n):
    for i in list_of_numbers:
        if i > n:
            return i

assert find_first_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)==6

"""
Write a function to find the last element of a list that is greater than n.
assert find_last_element([1, 2, 3, 4, 5, 6,