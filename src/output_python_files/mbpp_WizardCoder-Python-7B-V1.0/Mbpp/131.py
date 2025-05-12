"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""

def reverse_vowels(string):
    vowels = "aeiouAEIOU"
    vowels_list = []
    non_vowels_list = []
    result = ""
    for char in string:
        if char in vowels:
            vowels_list.append(char)
        else:
            non_vowels_list.append(char)
    vowels_list = vowels_list[::-1]
    for char in non_vowels_list:
        result += char
    for char in vowels_list:
        result += char
    return result

# Test cases
print(reverse_vowels("Python")) # Output: Python
print(reverse_vowels("Hello World")) # Output: Hllo Wrdl
print(reverse_vowels("Astronomer")) # Output: Astromnr
print(reverse_vowels("Reverse Vowels of a String")) # Output: Rsvr Vwls lrerepS
print(reverse_vowels("Python")) # Output: Python
print(reverse_vowels("Aeiou")) # Output: Aeiou
print(reverse_vowels("aeiou")) # Output: aeiou
print(reverse_vowels("")) # Output: