"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""


def remove_Occ(string, char):
    """
    :param string: string to remove char from
    :param char: char to remove
    :return: string without first and last occurrence of char
    """
    if string.count(char) == 1:
        return string.replace(char, "")
    else:
        return string[string.find(char) + 1:string.rfind(char)]


if __name__ == '__main__':
    print(remove_Occ("hello", "l"))
    print(remove_Occ("hello", "e"))
    print(remove_Occ("hello", "h"))
    print(remove_Occ("hello", "o"))
    print(remove_Occ("hello", "x"))
    print(remove_Occ("hello", "hello"))
    print(remove_Occ("hello", "he"))
    print(remove_Occ("hello", "ll"))
    print(remove_Occ("hello", "eo"))
    print(remove_Occ("hello", "heo"))
    print(remove_Occ("hello", "heol"))
    print(remove_Occ("hello", "heoll"))
    print(remove_Occ("hello", "heolll"))
    print(remove_Occ("hello", "heollll"))
    print(remove_Occ("hello", "heolllll"))
    print(remove_Occ("hello", "heollllll"))
    print(remove_Occ("hello", "heolllllll"))
    print(remove_Occ("hello", "heollllllll"))
    print(remove_Occ("hello", "heolllllllll"))
    print(remove_Occ("hello", "heollllllllll"))
    print(remove_Occ("hello", "heolllllllllll"))
    print(remove_Occ("hello", "heollllllllllll"))
    print(remove_Occ("hello", "heolllllllllllll"))
    print(remove_Occ("hello", "heollllllllllllll"))
    print(remove_Occ("hello", "heolllllllllllllll"))
    print(remove_Occ("hello", "heollllllllllllllll"))
    print(remove_Occ("hello", "heolllllllllllllllll"))
    print(remove_Occ("hello", "heollllllllllllllllll"))
    print(remove_Occ("hello", "heolllllllllllllllllll"))
    print(remove_Occ("hello", "heollllllllllllllllllll"))
    print(remove_Occ("hello", "heolllllllllllllllllllll"))
    print(remove_Occ("hello", "heollllllllllllllllllllll"))
    print(remove_Occ("hello", "heolllllllllllllllllllllll"))
    print(remove_Occ("hello", "heollllllllllllllllllllllll"))
    print(remove_Occ("hello", "heolllllllllllllllllllllllll"))
    print(remove_Occ("hello", "heollllllllllllllllllllllllll"))
    print(remove_Occ("hello", "heolllllllllllllllllllllllllll"))
    print(remove_Occ("hello", "heollllllllllllllllllllllllllll"))
    print(remove_Occ("hello", "heolllllllllllllllllllllllllllll"))
    print(remove_Occ("hello", "heollllllllllllllllllllllllllllll"))
    print(remove_Occ("hello", "heolllllllllllllllllllllllllllllll"))
    print(remove_Occ("hello", "heollllllllllllllllllllllllllllllll"))
    print(remove_Occ("hello", "heolllllllllllllllllllllllllllllllll"))
    print(remove_Occ("hello", "heollllllllllllllllllll