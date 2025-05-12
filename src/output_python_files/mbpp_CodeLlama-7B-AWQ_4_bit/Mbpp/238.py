"""
Write a python function to count the number of non-empty substrings of a given string.
assert number_of_substrings("abc") == 6
"""


def number_of_substrings(string):
    """
    Write a python function to count the number of non-empty substrings of a given string.
    assert number_of_substrings("abc") == 6
    """
    if not string:
        return 0
    count = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j + 1]:
                count += 1
    return count


if __name__ == '__main__':
    print(number_of_substrings("abc"))
    print(number_of_substrings(""))
    print(number_of_substrings("a"))
    print(number_of_substrings("ab"))
    print(number_of_substrings("abc"))
    print(number_of_substrings("abcd"))
    print(number_of_substrings("abcde"))
    print(number_of_substrings("abcdef"))
    print(number_of_substrings("abcdefg"))
    print(number_of_substrings("abcdefgh"))
    print(number_of_substrings("abcdefghi"))
    print(number_of_substrings("abcdefghij"))
    print(number_of_substrings("abcdefghijk"))
    print(number_of_substrings("abcdefghijkl"))
    print(number_of_substrings("abcdefghijklm"))
    print(number_of_substrings("abcdefghijklmn"))
    print(number_of_substrings("abcdefghijklmno"))
    print(number_of_substrings("abcdefghijklmnop"))
    print(number_of_substrings("abcdefghijklmnopq"))
    print(number_of_substrings("abcdefghijklmnopqr"))
    print(number_of_substrings("abcdefghijklmnopqrs"))
    print(number_of_substrings("abcdefghijklmnopqrst"))
    print(number_of_substrings("abcdefghijklmnopqrstu"))
    print(number_of_substrings("abcdefghijklmnopqrstuv"))
    print(number_of_substrings("abcdefghijklmnopqrstuvw"))
    print(number_of_substrings("abcdefghijklmnopqrstuvwx"))
    print(number_of_substrings("abcdefghijklmnopqrstuvwxy"))
    print(number_of_substrings("abcdefghijklmnopqrstuvwxyz"))
    print(number_of_substrings("abcdefghijklmnopqrstuvwxyz1"))
    print(number_of_substrings("abcdefghijklmnopqrstuvwxyz12"))
    print(number_of_substrings("abcdefghijklmnopqrstuvwxyz123"))
    print(number_of_substrings("abcdefghijklmnopqrstuvwxyz1234"))
    print(number_of_substrings("abcdefghijklmnopqrstuvwxyz12345"))
    print(number_of_substrings("abcdefghijklmnopqrstuvwxyz123456"))
    print(number_of_substrings("abcdefghijklmnopqrstuvwxyz1234567"))
    print(number_of_substrings("abcdefghijklmnopqrstuvwxyz12345678"))
    print(number_of_substrings("abcdefghijklmnopqrstuvwxyz123456789"))
    print(number_of_substrings("abcdefghijkl