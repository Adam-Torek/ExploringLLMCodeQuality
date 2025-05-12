"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""


def first_non_repeating_character(string):
    """
    :param string: string
    :return: first non-repeated character
    """
    if not string:
        return None

    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in string:
        if char_count[char] == 1:
            return char

    return None


if __name__ == '__main__':
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first_non_repeating_character("abcabc"))
    print(first