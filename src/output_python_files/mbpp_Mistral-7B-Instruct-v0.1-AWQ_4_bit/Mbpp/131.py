"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""
def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    reversed_vowels = ""
    for i in range(len(s)):
        if s[i] in vowels:
            reversed_vowels += s[i]
        else:
            reversed_vowels += s[i]
    return reversed_vowels

# Test the function
assert reverse_vowels("Python") == "Python"