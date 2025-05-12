"""
Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
assert get_Char("abc") == "f"
"""


def get_Char(string):
    """
    :param string: string
    :return: character
    """
    return chr(sum(ord(i) for i in string) % 26 + 97)


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
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
    print(get_Char("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabc