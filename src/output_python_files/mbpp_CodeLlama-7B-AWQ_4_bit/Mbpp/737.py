"""
Write a function to check whether the given string is starting with a vowel or not using regex.
assert check_str("annie")
"""

import re


def check_str(string):
    """
    Checks if the given string starts with a vowel or not.
    :param string: String to check
    :return: True if the string starts with a vowel, False otherwise
    """
    return re.match(r"^[aeiouAEIOU].*", string)


if __name__ == "__main__":
    print(check_str("annie"))
    print(check_str("ann"))
    print(check_str("a"))
    print(check_str(""))
    print(check_str("123"))
    print(check_str("a123"))
    print(check_str("123a"))
    print(check_str("123a456"))
    print(check_str("123456a"))
    print(check_str("1234567890"))
    print(check_str("1234567890a"))
    print(check_str("1234567890abcdefghijklmnopqrstuvwxyz"))
    print(check_str("1234567890abcdefghijklmnopqrstuvwxyzA"))
    print(check_str("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    print(check_str("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZa"))
    print(check_str("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"))
    print(check_str("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzA"))
    print(check_str("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    print(check_str("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZa"))
    print(check_str("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"))
    print(check_str("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzA"))
    print(check_str("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY