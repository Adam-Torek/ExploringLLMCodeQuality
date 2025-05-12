"""
Write a function to check whether the given string is starting with a vowel or not using regex.
assert check_str("annie")
"""

import re


def check_str(str):
    return re.match(r"^[aeiouAEIOU]", str)


if __name__ == "__main__":
    print(check_str("annie"))
    print(check_str("ann"))
    print(check_str("a"))
    print(check_str("A"))
    print(check_str("annie1"))
    print(check_str("annie "))
    print(check_str("annie1 "))
    print(check_str("annie1a"))
    print(check_str("annie1a "))
    print(check_str("annie1a1"))
    print(check_str("annie1a1 "))
    print(check_str("annie1a1b"))
    print(check_str("annie1a1b "))
    print(check_str("annie1a1b2"))
    print(check_str("annie1a1b2 "))
    print(check_str("annie1a1b2c"))
    print(check_str("annie1a1b2c "))
    print(check_str("annie1a1b2c3"))
    print(check_str("annie1a1b2c3 "))
    print(check_str("annie1a1b2c3d"))
    print(check_str("annie1a1b2c3d "))
    print(check_str("annie1a1b2c3d4"))
    print(check_str("annie1a1b2c3d4 "))
    print(check_str("annie1a1b2c3d4e"))
    print(check_str("annie1a1b2c3d4e "))
    print(check_str("annie1a1b2c3d4e5"))
    print(check_str("annie1a1b2c3d4e5 "))
    print(check_str("annie1a1b2c3d4e5f"))
    print(check_str("annie1a1b2c3d4e5f "))
    print(check_str("annie1a1b2c3d4e5f6"))
    print(check_str("annie1a1b2c3d4e5f6 "))
    print(check_str("annie1a1b2c3d4e5f6g"))
    print(check_str("annie1a1b2c3d4e5f6g "))
    print(check_str("annie1a1b2c3d4e5f6g7"))
    print(check_str("annie1a1b2c3d4e5f6g7 "))
    print(check_str("annie1a1b2c3d4e5f6g7h"))
    print(check_str("annie1a1b2c3d4e5f6g7h "))
    print(check_str("annie1a1b2c3d4e5f6g7h8"))
    print(check_str("annie1a1b2c3d4e5f6g7h8 "))
    print(check_str("annie1a1b2c3d4e5f6g7h8i"))
    print(check_str("annie1a1b2c3d4e5f6g7h8i "))
    print(check_str("annie1a1b2c3d4e5f6g7h8i9"))
    print(check_str("annie1a1b2c3d4e5f6g7h8i9 "))
    print(check_str("annie1a1b2c3d4e5f6g7h8i9j"))
    print(check_str("annie1a1b2c3d4e5f6g7h8i9j "))
    print(check_str("