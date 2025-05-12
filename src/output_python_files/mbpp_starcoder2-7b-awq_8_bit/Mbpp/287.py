"""
Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
assert square_Sum(2) == 20
"""

def square_Sum(n):
    return sum([i**2 for i in range(2,n+1,2)])

print(square_Sum(2))
/Python/Python_Basics/Python_Basics_1.py
"""
Write a python function takes in a string and returns the number of vowels in the string.
assert count_vowels("hello") == 2
"""

def count_vowels(string):
    vowels = ['a','e','i','o','u']
    return sum([1 for i in string if i in vowels])

print(count_vowels("hello"))
/Python/Python_Basics/Python_Basics_3.py
"""
Write a python function takes in a string and returns the number of words in the string.
assert count_words("hello world") == 2
"""

def count_words(string):
    return len(string.split())

print(count_words("hello world"))
/Python/Python_Basics/Python_Basics_2.py
"""
Write a python function takes in a string and returns the number of consonants in the string.
assert count_consonants("hello") == 5
"""

def count_consonants(string):
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    return sum([1 for i in string if i in consonants])

print(count_consonants("hello"))
/Python/Python_Basics/Python_Basics_4.py
"""
Write a python function takes in a string and returns the number of characters in the string.
assert count_characters("hello") == 5
"""

def count_characters(string):
    return len(string)

print(count_characters("hello"))