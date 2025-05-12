"""
Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.
assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
"""

def combinations_colors(list, n):
    if n == 0:
        return [()]
    else:
        return [(x,) + y for x in list for y in combinations_colors(list, n-1)]

print(combinations_colors(["Red","Green","Blue"],1))
/week01/day04/02_count_letters.py
"""
Write a function that takes a string and counts the number of times each letter appears.
assert count_letters("apple") == {'a': 1, 'p': 2, 'l': 1, 'e': 1}
"""

def count_letters(string):
    dict = {}
    for letter in string:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict

print(count_letters("apple"))
/week01/day04/01_sum_numbers.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_numbers([1,2,3,4]) == 10
"""

def sum_numbers(list):
    sum = 0
    for number in list:
        sum += number
    return sum

print(sum_numbers([1,2,3,4]))
/week01/day04/03_count_letters_2.py
"""
Write a function that takes a string and counts the number of times each letter appears.
assert count_letters("apple") == {'a': 1, 'p': 2, 'l': 1, 'e': 1}
"""

def count_letters(string):
    dict = {}
    for letter in string:
        dict[letter] = dict.get(letter, 0) + 1
    return dict

print(count_letters("apple"))
/week01/day04/04_count_letters_3.py
"""
Write a function that takes a string and counts the number of times each letter appears.
assert count_letters("apple") == {'a': 1, 'p': 2, 'l': 1, 'e': 1}
"""

def count_letters(string):
    dict = {}
    for letter in string:
        dict[letter] = dict.get(letter, 0) + 1
    return dict

print(count_letters("apple"))

def count_letters_2(string):
    dict = {}
    for letter in string:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict

print(count_letters_2("apple"))
/week01/day04/05_count_letters_4.py
"""
Write a function that takes a string and counts the number of times each letter appears.
assert count_letters("apple") == {'a': 1, 'p': 2, 'l': 1, 'e': 1}
"""

def count_letters(string):
    dict = {}
    for letter in string:
        dict[letter] = dict.get(letter, 0) + 1
    return dict

print(count_letters("apple"))

def count_letters_2(string):
    dict = {}
    for letter in string:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict

print(count_letters_2("apple"))

def count_letters_3(string):
    dict = {}
    for letter in string:
        dict[letter] = dict.get(letter, 0) + 1
    return dict

print(count_letters_3("apple"))

def count_letters_4(string):
    dict = {}
    for letter in string:
        dict[letter] = dict.get(letter, 0) + 1
    return dict

print(count_letters_4("apple"))

def count_letters_5(string):
    dict = {}
    for letter in string:
        dict[letter] = dict.get(letter, 0) + 1
    return dict

print(count