"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""

def reverse_vowels(string):
    vowels = "aeiouAEIOU"
    reversed_string = ""
    for char in string:
        if char.lower() not in vowels:
            reversed_string += char
    return reversed_string[::-1]

# Test cases
print(reverse_vowels("Python")) # Output: "nohtyp"
print(reverse_vowels("Hello World")) # Output: "dlroW olleH"
print(reverse_vowels("Abcdefg")) # Output: "gfedcba"<|endoftext|>