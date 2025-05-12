"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""
def reverse_vowels(string):
    vowels = "aeiouAEIOU"
    i = 0
    j = len(string) - 1
    while i < len(string) and j >= 0:
        if string[i] not in vowels:
            i += 1
        elif string[j] not in vowels:
            j -= 1
        else:
            string = string[:i] + string[j] + string[i:j] + string[i+1:]
            i += 1
            j -= 1
    return string

assert reverse_vowels("Python") == "Python"
assert reverse_vowels("racecar") == "racecar"
assert reverse_vowels("hello") == "holleh"
assert reverse_vowels("aeiou") == "euioa"