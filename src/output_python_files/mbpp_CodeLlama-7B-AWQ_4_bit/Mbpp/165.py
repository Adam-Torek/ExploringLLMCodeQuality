"""
Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
assert count_char_position("xbcefg") == 2
"""


def count_char_position(string):
    """
    :param string: string
    :return: int
    """
    count = 0
    for i in range(len(string)):
        if string[i].lower() == string[i].lower()[ord(string[i].lower()) - 97]:
            count += 1
    return count


if __name__ == '__main__':
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_position("xbcefg"))
    print(count_char_