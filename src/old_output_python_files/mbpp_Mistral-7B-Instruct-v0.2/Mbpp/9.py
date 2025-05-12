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
assert find_Rotations("abcdefghijklmnopqrstuvwxyz") == 26
assert find_Rotations("pypy") == 1
assert find_Rotations("pypyz") == 3
assert find_Rotations("pypyzp") == 1
assert find_Rotations("pypyzpz") == 2
assert find_Rotations("pypyzpzy") == 1
assert find_Rotations("pypyzpzyz") == 2
assert find_Rotations("pypyzpzyzy") == 1
assert find_Rotations("pypyzpzyzyz") == 2
assert find_Rotations("pypyzpzyzyzy") == 1
assert find_Rotations("pypyzpzyzyzyz") == 2
assert find_Rotations("pypyzpzyzyzyzy") == 1
assert find_Rotations("pypyzpzyzyzyzyz") == 2
assert find_Rotations("pypyzpzyzyzyzyzy") == 1
assert find_Rotations("pypyzpzyzyzyzyzyz") == 2
assert find_Rotations("pypyzpzyzyzyzyzyzy") == 1
assert find_Rotations("pypyzpzyzyzyzyzyzyz") == 2
assert find_Rotations("pypyzpzyzyzyzyzyzyzy") == 1
assert find_Rotations("pypyzpzyzyzyzyzyzyzyz") == 2
assert find_Rotations("pypyzpzyzyzyzyzyzyzyzy") == 1
assert find_Rotations("pypyzpzyzyzyzyzyzyzyzyz") == 2
assert find_Rotations("pypyzpzyzyzyzyzyzyzyzyzy") == 1
assert find_Rotations("pypyzpzyzyzyzyzyzyzyzyzyz") == 2
assert find_Rotations("pypyzpzyzyzyzyzyzyzyzyzyzy") == 1
assert find_Rotations("pypyzpzyzyzyzyzyzyzyzyzyzyz") == 2
assert find_Rotations("pypyzpzyzyzyzyzyzyzyzyzyzyzy") == 1
assert find_Rotations("pypyzpzyzyzyzyzyzyzyzyzyzyzyz") == 2
assert find_Rotations("pypyzpzyzyzyzyzyzyzyzyzyzyzyzy") == 1
assert find_Rotations("pypyzpzyzyzyzyzyzyzyzyzyzyzyzyz") == 2
assert find_Rotations("pypyzpzyzyzyzyzyzyzyzyzyzyzyzyzy") == 1
assert find_Rotations("pypyzpzyzyzyzyzyzyzyzyzyzyzyzyzyz") == 2
assert find_Rotations("pypyzpzyzyzyzyzyzyzyzyzyzyzyzyzyzy") == 1
assert find_Rotations("pypyzpzyzyzyzyzyzyzyzyzyzyzyzyzyzyz") == 2
assert find_Rotations("pypyzpzyzyzyzyzyzyzyzyzyzyzyzyzyzyzz") == 1
assert find_Rotations("pypyzpzyzyzyzyzyzyzyzyzyzyzyzyzyzyzzz") == 2
assert find_Rotations("pypyzpzyzyzyzyzyzyzyzyzyzyzyzyzy