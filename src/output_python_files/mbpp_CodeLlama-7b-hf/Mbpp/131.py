"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""


def reverse_vowels(string):
    vowels = "aeiouy"
    vowel_indexes = []
    for i, char in enumerate(string):
        if char in vowels:
            vowel_indexes.append(i)
    vowel_indexes.reverse()
    for i, vowel_index in enumerate(vowel_indexes):
        string = string[:vowel_index] + string[vowel_index].upper() + string[vowel_index + 1:]
    return string


if __name__ == "__main__":
    print(reverse_vowels("Python"))
    print(reverse_vowels("Hello World"))
    print(reverse_vowels("A man, a plan, a canal: Panama"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere I saw Elba"))
    print(reverse_vowels("Able was I, ere