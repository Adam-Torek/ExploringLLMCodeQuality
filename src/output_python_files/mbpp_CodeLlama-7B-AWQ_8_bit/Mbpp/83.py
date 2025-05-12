"""
Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
assert get_Char("abc") == "f"
"""


def get_Char(string):
    """
    :param string: string
    :return: character
    """
    result = 0
    for i in string:
        result += ord(i)
    result = result % 26
    return chr(result + 64)


if __name__ == '__main__':
    print(get_Char("abc"))
    print(get_Char("abcd"))
    print(get_Char("abcde"))
    print(get_Char("abcdef"))
    print(get_Char("abcdefg"))
    print(get_Char("abcdefgh"))
    print(get_Char("abcdefghi"))
    print(get_Char("abcdefghij"))
    print(get_Char("abcdefghijk"))
    print(get_Char("abcdefghijkl"))
    print(get_Char("abcdefghijklm"))
    print(get_Char("abcdefghijklmn"))
    print(get_Char("abcdefghijklmno"))
    print(get_Char("abcdefghijklmnop"))
    print(get_Char("abcdefghijklmnopq"))
    print(get_Char("abcdefghijklmnopqr"))
    print(get_Char("abcdefghijklmnopqrs"))
    print(get_Char("abcdefghijklmnopqrst"))
    print(get_Char("abcdefghijklmnopqrstu"))
    print(get_Char("abcdefghijklmnopqrstuv"))
    print(get_Char("abcdefghijklmnopqrstuvw"))
    print(get_Char("abcdefghijklmnopqrstuvwx"))
    print(get_Char("abcdefghijklmnopqrstuvwxy"))
    print(get_Char("abcdefghijklmnopqrstuvwxyz"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzab"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabc"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcd"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcde"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdef"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefg"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefgh"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghi"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghij"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijk"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijkl"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijklm"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijklmn"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijklmno"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijklmnop"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopq"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqr"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrs"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrst"))
    print(