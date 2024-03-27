"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""


def remove_odd(string):
    """
    :param string: string
    :return: string without odd characters
    """
    return ''.join([char for char in string if not char % 2])


if __name__ == '__main__':
    print(remove_odd("python"))
    print(remove_odd("hello"))
    print(remove_odd("abcd"))
    print(remove_odd(""))
    print(remove_odd("a"))
    print(remove_odd("ab"))
    print(remove_odd("abc"))
    print(remove_odd("abcd"))
    print(remove_odd("abcde"))
    print(remove_odd("abcdef"))
    print(remove_odd("abcdefg"))
    print(remove_odd("abcdefgh"))
    print(remove_odd("abcdefghi"))
    print(remove_odd("abcdefghij"))
    print(remove_odd("abcdefghijk"))
    print(remove_odd("abcdefghijkl"))
    print(remove_odd("abcdefghijklm"))
    print(remove_odd("abcdefghijklmn"))
    print(remove_odd("abcdefghijklmno"))
    print(remove_odd("abcdefghijklmnop"))
    print(remove_odd("abcdefghijklmnopq"))
    print(remove_odd("abcdefghijklmnopqr"))
    print(remove_odd("abcdefghijklmnopqrs"))
    print(remove_odd("abcdefghijklmnopqrst"))
    print(remove_odd("abcdefghijklmnopqrstu"))
    print(remove_odd("abcdefghijklmnopqrstuv"))
    print(remove_odd("abcdefghijklmnopqrstuvw"))
    print(remove_odd("abcdefghijklmnopqrstuvwx"))
    print(remove_odd("abcdefghijklmnopqrstuvwxy"))
    print(remove_odd("abcdefghijklmnopqrstuvwxyz"))
    print(remove_odd("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
    print(remove_odd("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
    print(remove_odd("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
    print(remove_odd("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
    print(remove_odd("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
    print(remove_odd("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
    print(remove_odd("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvw