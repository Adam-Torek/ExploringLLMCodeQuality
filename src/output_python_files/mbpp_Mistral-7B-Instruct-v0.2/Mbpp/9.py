"""
Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
assert find_Rotations("aaaa") == 1
"""
def find_Rotations(str):
    if len(str) < 2:
        return 0
    return len(str) - len(str[::-1] if str[-1] == str[0] else str[:len(str)-1].find(str[1:]))

assert find_Rotations("aaaa") == 1
assert find_Rotations("abcd") == 2
assert find_Rotations("abcde") == 3
assert find_Rotations("abcdef") == 6
assert find_Rotations("abcdefg") == 7
assert find_Rotations("abcdefgh") == 8
assert find_Rotations("abcdefghi") == 9
assert find_Rotations("abcdefghij") == 10
assert find_Rotations("abcdefghijk") == 11
assert find_Rotations("abcdefghijkl") == 12
assert find_Rotations("abcdefghijklm") == 13
assert find_Rotations("abcdefghijklmn") == 14
assert find_Rotations("abcdefghijklmno") == 15
assert find_Rotations("abcdefghijklmnoa") == 16
assert find_Rotations("abcdefghijklmnoab") == 17
assert find_Rotations("abcdefghijklmnoabc") == 18
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoabcd") == 19
assert find_Rotations("abcdefghijklmnoab