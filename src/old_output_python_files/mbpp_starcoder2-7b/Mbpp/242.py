"""
Write a function to count the total number of characters in a string.
assert count_charac("python programming")==18
"""
def count_charac(string):
    count=0
    for i in string:
        count+=1
    return count
print(count_charac("python programming"))

"""
Write a function to count the total number of words in a string.
assert count_words("python programming")==2
"""
def count_words(string):
    count=0
    for i in string.split():
        count+=1
    return count
print(count_words("python programming"))

"""
Write a function to count the total number of digits in a string.
assert count_digits("python programming")==0
"""
def count_digits(string):
    count=0
    for i in string:
        if i.isdigit():
            count+=1
    return count
print(count_digits("python programming"))

"""
Write a function to count the total number of alphabets in a string.
assert count_alphabets("python programming")==10
"""
def count_alphabets(string):
    count=0
    for i in string:
        if i.isalpha():
            count+=1
    return count
print(count_alphabets("python programming"))

"""
Write a function to count the total number of alphabets and digits in a string.
assert count_alphabets_digits("python programming")==18
"""
def count_alphabets_digits(string):
    count=0
    for i in string:
        if i.isalnum():
            count+=1
    return count
print(count_alphabets_digits("python programming"))

"""
Write a function to count the total number of vowels in a string.
assert count_vowels("python programming")==5
"""
def count_vowels(string):
    count=0
    for i in string:
        if i in "aeiouAEIOU":
            count+=1
    return count
print(count_vowels("python programming"))

"""
Write a function to count the total number of vowels and consonants in a string.
assert count_vowels_consonants("python programming")==10
"""
def count_vowels_consonants(string):
    count=0
    for i in string:
        if i in "aeiouAEIOU":
            count+=1
    return count
print(count_vowels_consonants("python programming"))

"""
Write a function to count the total number of vowels and consonants in a string.
assert count_vowels_consonants("python programming")==10
"""
def count_vowels_consonants(string):
    count=0
    for i in string:
        if i in "aeiouAEIOU":
            count+=1
    return count
print(count_vowels_consonants("python programming"))

"""
Write a function to count the total number of vowels and consonants in a string.
assert count_vowels_consonants("python programming")==10
"""
def count_vowels_consonants(string):
    count=0
    for i in string:
        if i in "aeiouAEIOU":
            count+=1
    return count
print(count_vowels_consonants("python programming"))

"""
Write a function to count the total number of vowels and consonants in a string.
assert count_vowels_consonants("python programming")==10
"""
def count_vowels_consonants(string):
    count=0
    for i in string:
        if i in "aeiouAEIOU":
            count+=1
    return count
print(count_vowels_consonants("python programming"))

"""
Write a function to count the total number of vowels and consonants in a string.
assert count_vowels_consonants("python programming")==10
"""
def count_vowels_consonants(string):
    count=0
    for i in string:
        if i in "aeiouAEIOU":
            count+=1
    return count
print(count_vowels_consonants("python programming"))

"""
Write a function to count the total number of vowels and consonants in a string.
assert count_vowels_consonants("python programming")==10
"""
def count_vowels_consonants(string):