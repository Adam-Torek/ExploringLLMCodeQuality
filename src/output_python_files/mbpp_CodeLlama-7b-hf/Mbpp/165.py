"""
Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
assert count_char_position("xbcefg") == 2
"""


def count_char_position(string):
    """
    :param string: string to count characters in
    :return: number of characters in string that occur at the same position in the string as in the English alphabet
    """
    count = 0
    for i in range(len(string)):
        if string[i].lower() == string[ord(string[i].lower()) - 97].lower():
            count += 1
    return count


if __name__ == '__main__':
    print(count_char_position("xbcefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))
    print(count_char_position("abcdefg"))