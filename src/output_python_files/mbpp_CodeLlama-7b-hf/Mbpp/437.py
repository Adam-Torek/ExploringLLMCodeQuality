"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""


def remove_odd(string):
    """
    :param string: string
    :return: string without odd characters
    """
    return ''.join([char for char in string if char.isalpha() and not char.isdigit()])


if __name__ == '__main__':
    print(remove_odd("python"))
    print(remove_odd("1234567890"))
    print(remove_odd("1234567890a"))
    print(remove_odd("1234567890ab"))
    print(remove_odd("1234567890abc"))
    print(remove_odd("1234567890abcd"))
    print(remove_odd("1234567890abcde"))
    print(remove_odd("1234567890abcdef"))
    print(remove_odd("1234567890abcdefg"))
    print(remove_odd("1234567890abcdefgh"))
    print(remove_odd("1234567890abcdefghi"))
    print(remove_odd("1234567890abcdefghij"))
    print(remove_odd("1234567890abcdefghijk"))
    print(remove_odd("1234567890abcdefghijkl"))
    print(remove_odd("1234567890abcdefghijklm"))
    print(remove_odd("1234567890abcdefghijklmn"))
    print(remove_odd("1234567890abcdefghijklmno"))
    print(remove_odd("1234567890abcdefghijklmnop"))
    print(remove_odd("1234567890abcdefghijklmnopq"))
    print(remove_odd("1234567890abcdefghijklmnopqr"))
    print(remove_odd("1234567890abcdefghijklmnopqrs"))
    print(remove_odd("1234567890abcdefghijklmnopqrst"))
    print(remove_odd("1234567890abcdefghijklmnopqrstu"))
    print(remove_odd("1234567890abcdefghijklmnopqrstuv"))
    print(remove_odd("1234567890abcdefghijklmnopqrstuvw"))
    print(remove_odd("1234567890abcdefghijklmnopqrstuvwx"))
    print(remove_odd("1234567890abcdefghijklmnopqrstuvwxy"))
    print(remove_odd("1234567890abcdefghijklmnopqrstuvwxyz"))
    print(remove_odd("1234567890abcdefghijklmnopqrstuvwxyzab"))
    print(remove_odd("1234567890abcdefghijklmnopqrstuvwxyzabc"))
    print(remove_odd("1234567890abcdefghijklmnopqrstuvwxyzabcd"))
    print(remove_odd("1234567890abcdefghijklmnopqrstuvwxyzabcde"))
    print(remove_odd("1234567890abcdefghijklmnopqrstuvwxyzabcdef"))
    print(remove_odd("1234567890abcdefghijklmnopqrstuvwxyzabcdefg"))
    print(remove_odd("12