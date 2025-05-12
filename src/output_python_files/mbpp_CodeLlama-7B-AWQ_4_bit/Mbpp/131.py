"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""


def reverse_vowels(string):
    vowels = "aeiouy"
    vowel_list = []
    for char in string:
        if char in vowels:
            vowel_list.append(char)
    vowel_list.reverse()
    for i in range(len(vowel_list)):
        string = string.replace(vowel_list[i], vowel_list[i], 1)
    return string


if __name__ == "__main__":
    print(reverse_vowels("Python"))
    print(reverse_vowels("Hello World"))
    print(reverse_vowels("Astronomy"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("God"))
    print(reverse_vowels("