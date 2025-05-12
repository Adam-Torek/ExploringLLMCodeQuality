"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""

def reverse_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_list = []
    for i in string:
        if i in vowels:
            vowels_list.append(i)
    vowels_list.reverse()
    new_string = ""
    for i in string:
        if i in vowels:
            new_string += vowels_list.pop()
        else:
            new_string += i
    return new_string

print(reverse_vowels("Python"))
/python/python_fundamentals/fundamentals/fundamentals_2/fundamentals_2_1.py
"""
Write a function that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
assert remove_duplicates([1, 2, 3, 4, 3, 2, 1]) == [1, 2, 3, 4]
"""

def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(remove_duplicates([1, 2, 3, 4, 3, 2, 1]))
/python/python_fundamentals/fundamentals/fundamentals_1/fundamentals_1_1.py
"""
Write a function that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
assert remove_duplicates([1, 2, 3, 4, 3, 2, 1]) == [1, 2, 3, 4]
"""

def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(remove_duplicates([1, 2, 3, 4, 3, 2, 1]))
/python/python_fundamentals/fundamentals/fundamentals_2/fundamentals_2_3.py
"""
Write a function that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
assert remove_duplicates([1, 2, 3, 4, 3, 2, 1]) == [1, 2, 3, 4]
"""

def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(remove_duplicates([1, 2, 3, 4, 3, 2, 1]))

"""
Write a function that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
assert remove_duplicates([1, 2, 3, 4, 3, 2, 1]) == [1, 2, 3, 4]
"""

def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(remove_duplicates([1, 2, 3, 4, 3, 2, 1]))

"""
Write a function that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
assert remove_duplicates([1, 2, 3, 4, 3, 2, 1]) == [1, 2, 3, 4]
"""

def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(remove_duplicates([1, 2, 3, 4, 3, 2, 1]))

"""
Write a function that takes a list and returns a new list that contains all the elements