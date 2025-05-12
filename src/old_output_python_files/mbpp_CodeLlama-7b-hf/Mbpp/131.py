"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""


def reverse_vowels(string):
    """
    Reverse only the vowels of a given string (where y is not a vowel).
    :param string: string to reverse
    :return: reversed string
    """
    vowels = "aeiouAEIOU"
    vowel_indexes = []
    for index, char in enumerate(string):
        if char in vowels:
            vowel_indexes.append(index)

    for index in range(len(vowel_indexes) - 1, -1, -1):
        string = string[:vowel_indexes[index]] + string[vowel_indexes[index] + 1] + string[vowel_indexes[index]] + string[
                                                                                                                  vowel_indexes[
                                                                                                                      index] + 2:]

    return string


if __name__ == '__main__':
    print(reverse_vowels("Python"))
    print(reverse_vowels("Hello"))
    print(reverse_vowels("Hey"))
    print(reverse_vowels("Heyy"))
    print(reverse_vowels("Heyyy"))
    print(reverse_vowels("Heyyyy"))
    print(reverse_vowels("Heyyyyy"))
    print(reverse_vowels("Heyyyyyy"))
    print(reverse_vowels("Heyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("Heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
    print(reverse_vowels("H