"""
Write a python function to remove the characters which have odd index values of a given string.
assert odd_values_string('abcdef') == 'ace'
"""


def odd_values_string(string):
    """
    Write a python function to remove the characters which have odd index values of a given string.
    assert odd_values_string('abcdef') == 'ace'
    """
    return ''.join([char for index, char in enumerate(string) if index % 2 == 0])


if __name__ == '__main__':
    print(odd_values_string('abcdef'))
    print(odd_values_string('abcdefg'))
    print(odd_values_string('abcdefgh'))
    print(odd_values_string('abcdefghi'))
    print(odd_values_string('abcdefghij'))
    print(odd_values_string('abcdefghijk'))
    print(odd_values_string('abcdefghijkl'))
    print(odd_values_string('abcdefghijklm'))
    print(odd_values_string('abcdefghijklmn'))
    print(odd_values_string('abcdefghijklmno'))
    print(odd_values_string('abcdefghijklmnop'))
    print(odd_values_string('abcdefghijklmnopq'))
    print(odd_values_string('abcdefghijklmnopqr'))
    print(odd_values_string('abcdefghijklmnopqrs'))
    print(odd_values_string('abcdefghijklmnopqrst'))
    print(odd_values_string('abcdefghijklmnopqrstu'))
    print(odd_values_string('abcdefghijklmnopqrstuv'))
    print(odd_values_string('abcdefghijklmnopqrstuvw'))
    print(odd_values_string('abcdefghijklmnopqrstuvwx'))
    print(odd_values_string('abcdefghijklmnopqrstuvwxy'))
    print(odd_values_string('abcdefghijklmnopqrstuvwxyz'))
    print(odd_values_string('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'))
    print(odd_values_string('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'))
    print(odd_values_string('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'))
    print(odd_values_string('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'))
    print(odd_values_string('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'))
    print(odd_values_string('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefgh