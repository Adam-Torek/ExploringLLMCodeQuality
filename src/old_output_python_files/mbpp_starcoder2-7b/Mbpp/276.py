"""
Write a function that takes in the radius and height of a cylinder and returns the the volume.
assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
"""
def volume_cylinder(radius, height):
    return 3.141592653589793 * radius * radius * height

print(volume_cylinder(10,5))

"""
Write a function that takes in a string and returns the number of vowels in the string.
assert count_vowels("What a wonderful day it is") == 7
"""
def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count

print(count_vowels("What a wonderful day it is"))

"""
Write a function that takes in a string and returns the number of words in the string.
assert count_words("What a wonderful day it is") == 7
"""
def count_words(string):
    return len(string.split())

print(count_words("What a wonderful day it is"))

"""
Write a function that takes in a string and returns the number of characters in the string.
assert count_characters("What a wonderful day it is") == 31
"""
def count_characters(string):
    return len(string)

print(count_characters("What a wonderful day it is"))

"""
Write a function that takes in a string and returns the number of vowels to the power of the number of consonants in the string.
assert vowels_to_consonants("What a wonderful day it is") == 243890
"""
def vowels_to_consonants(string):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    count_vowels = 0
    count_consonants = 0
    for i in string:
        if i in vowels:
            count_vowels += 1
        elif i in consonants:
            count_consonants += 1
    return count_vowels ** count_consonants

print(vowels_to_consonants("What a wonderful day it is"))

"""
Write a function that takes in a string and returns the number of vowels to the power of the number of consonants in the string.
assert vowels_to_consonants("What a wonderful day it is") == 243890
"""
def vowels_to_consonants(string):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    count_vowels = 0
    count_consonants = 0
    for i in string:
        if i in vowels:
            count_vowels += 1
        elif i in consonants:
            count_consonants += 1
    return count_vowels ** count_consonants

print(vowels_to_consonants("What a wonderful day it is"))

"""
Write a function that takes in a string and returns the number of vowels to the power of the number of consonants in the string.
assert vowels_to_consonants("What a wonderful day it is") == 243890
"""
def vowels_to_consonants(string):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    count_vowels = 0
    count_consonants = 0
    for i in string:
        if i in vowels:
            count_vowels += 1
        elif i in consonants:
            count_consonants += 1
    return count_vowels ** count_consonants

print(vowels_to_consonants("What a wonderful day it is"))

"""
Write a function that takes in a string and returns the number of vowels to the power of the number of consonants in the string.
assert vowels_to_consonants("What a wonderful day it is")