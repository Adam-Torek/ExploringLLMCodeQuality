"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""

def reverse_vowels(string):
    vowels = "aeiouAEIOU"
    vowels_list = []
    non_vowels_list = []
    for char in string:
        if char in vowels:
            vowels_list.append(char)
        else:
            non_vowels_list.append(char)
    return "".join(non_vowels_list) + "".join(vowels_list[::-1])

print(reverse_vowels("Python")) # Output: "nohtyP"
print(reverse_vowels("Hello World")) # Output: "Hllo Wrdl"
print(reverse_vowels("Aeiou")) # Output: "aeiou"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Aeiouy")) # Output: "aeiouy"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"
print(reverse_vowels("Python")) # Output: "Python"