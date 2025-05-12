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
        return len(string)


if __name__ == '__main__':
    print(find_Rotations("aaaa"))
    print(find_Rotations("abcd"))
    print(find_Rotations("abcda"))
    print(find_Rotations("abcdaa"))
    print(find_Rotations("abcdaaa"))
    print(find_Rotations("abcdaaaa"))
    print(find_Rotations("abcdaaaaa"))
    print(find_Rotations("abcdaaaaaa"))
    print(find_Rotations("abcdaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(find_Rotations("abcda