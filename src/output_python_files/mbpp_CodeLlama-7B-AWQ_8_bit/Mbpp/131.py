"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""


def reverse_vowels(s):
    vowels = "aeiouy"
    vowel_list = []
    for i in s:
        if i in vowels:
            vowel_list.append(i)
    vowel_list.reverse()
    for i in range(len(vowel_list)):
        s = s.replace(vowel_list[i], "", 1)
    for i in range(len(vowel_list)):
        s = s + vowel_list[i]
    return s


print(reverse_vowels("Python"))
print(reverse_vowels("Hello"))
print(reverse_vowels("Hey"))
print(reverse_vowels("Hey there"))
print(reverse_vowels("Hey there you"))
print(reverse_vowels("Hey there you are"))
print(reverse_vowels("Hey there you are fine"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you are fine and dandy"))
print(reverse_vowels("Hey there you