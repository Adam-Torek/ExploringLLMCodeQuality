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
    new_string = ''
    for i in string:
        if i in vowels:
            new_string += vowels_list.pop()
        else:
            new_string += i
    return new_string

print(reverse_vowels("Python"))
/python_practice/python_practice_1.py
"""
Write a python function to reverse a given string.
assert reverse("Python") == "nohtyP"
"""

def reverse(string):
    return string[::-1]

print(reverse("Python"))
/python_practice/python_practice_4.py
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
    new_string = ''
    for i in string:
        if i in vowels:
            new_string += vowels_list.pop()
        else:
            new_string += i
    return new_string

print(reverse_vowels("Python"))
/python_practice/python_practice_3.py
"""
Write a python function to reverse a given string.
assert reverse("Python") == "nohtyP"
"""

def reverse(string):
    return string[::-1]

print(reverse("Python"))
/python_practice/python_practice_2.py
"""
Write a python function to reverse a given string.
assert reverse("Python") == "nohtyP"
"""

def reverse(string):
    return string[::-1]

print(reverse("Python"))