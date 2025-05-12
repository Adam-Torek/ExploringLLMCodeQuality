"""
Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
assert find_Rotations("aaaa") == 1
"""


def find_Rotations(string):
    """
    :param string: string
    :return: minimum number of rotations required to get the same string
    """
    if len(string) == 1:
        return 0
    else:
        for i in range(len(string)):
            if string[i:] == string[:i]:
                return i
        return 0


if __name__ == '__main__':
    print(find_Rotations("aaaa"))
    print(find_Rotations("abcd"))
    print(find_Rotations("abcde"))
    print(find_Rotations("abcdef"))
    print(find_Rotations("abcdefg"))
    print(find_Rotations("abcdefgh"))
    print(find_Rotations("abcdefghi"))
    print(find_Rotations("abcdefghij"))
    print(find_Rotations("abcdefghijk"))
    print(find_Rotations("abcdefghijkl"))
    print(find_Rotations("abcdefghijklm"))
    print(find_Rotations("abcdefghijklmn"))
    print(find_Rotations("abcdefghijklmno"))
    print(find_Rotations("abcdefghijklmnop"))
    print(find_Rotations("abcdefghijklmnopq"))
    print(find_Rotations("abcdefghijklmnopqr"))
    print(find_Rotations("abcdefghijklmnopqrs"))
    print(find_Rotations("abcdefghijklmnopqrst"))
    print(find_Rotations("abcdefghijklmnopqrstu"))
    print(find_Rotations("abcdefghijklmnopqrstuv"))
    print(find_Rotations("abcdefghijklmnopqrstuvw"))
    print(find_Rotations("abcdefghijklmnopqrstuvwx"))
    print(find_Rotations("abcdefghijklmnopqrstuvwxy"))
    print(find_Rotations("abcdefghijklmnopqrstuvwxyz"))
    print(find_Rotations("abcdefghijklmnopqrstuvwxyzab"))
    print(find_Rotations("abcdefghijklmnopqrstuvwxyzabc"))
    print(find_Rotations("abcdefghijklmnopqrstuvwxyzabcd"))
    print(find_Rotations("abcdefghijklmnopqrstuvwxyzabcde"))
    print(find_Rotations("abcdefghijklmnopqrstuvwxyzabcdef"))
    print(find_Rotations("abcdefghijklmnopqrstuvwxyzabcdefg"))
    print(find_Rotations("abcdefghijklmnopqrstuvwxyzabcdefgh"))
    print(find_Rotations("abcdefghijklmnopqrstuvwxyzabcdefghi"))
    print(find_Rotations("abcdefghijklmnopqrstuvwxyzabcdefghij"))
    print(find_Rotations("abcdefghijklmnopqrstuvwxyzabcdefghijk"))
    print(find_Rotations("abcdefghijklmnopqrstuvwxyzabcdefghijkl"))
    print(find_Rotations("abcdefghijklmnopqrstuvwxyzabcdefghijklm"))
    print(find_Rotations("abcdefghijklmnopqrstuvwxyzabcdefghijklmn"))
    print(find_Rotations("abcdefghijklmnopqrstuvwxyzabcdefghijklmno"))
    print(find_Rotations("abcdefghijklmnopqrstuvwxyzabcdefghijklmnop"))
    print(find_Rotations("abcdefghijklmnopqr