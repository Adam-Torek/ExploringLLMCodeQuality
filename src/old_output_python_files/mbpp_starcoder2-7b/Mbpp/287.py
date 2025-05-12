"""
Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
assert square_Sum(2) == 20
"""

def square_Sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    return sum

print(square_Sum(2))
<file_sep>/python_basics/python_basics_1.py
"""
Write a python function that takes in a string and returns the number of vowels in the string.
assert count_vowels("hello") == 2
"""

def count_vowels(string):
    vowels = ['a','e','i','o','u']
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count

print(count_vowels("hello"))
<file_sep>/python_basics/python_basics_3.py
"""
Write a python function that takes in a string and returns the number of words in the string.
assert count_words("hello world") == 2
"""

def count_words(string):
    return len(string.split())

print(count_words("hello world"))
<file_sep>/python_basics/python_basics_2.py
"""
Write a python function that takes in a string and returns the number of consonants in the string.
assert count_consonants("hello") == 5
"""

def count_consonants(string):
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    count = 0
    for i in string:
        if i in consonants:
            count += 1
    return count

print(count_consonants("hello"))
<|endoftext|>