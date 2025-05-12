"""
Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
assert find_Rotations("aaaa") == 1
"""

def find_Rotations(s):
    n = len(s)
    if n == 1:
        return 0
    if n == 2:
        if s[0] == s[1]:
            return 0
        else:
            return 1
    for i in range(n):
        if s[i] == s[0]:
            return i + 1
    return n

print(find_Rotations("aaaa")) # 1
print(find_Rotations("abab")) # 2
print(find_Rotations("abcde")) # 5
print(find_Rotations("abcdefgabcdefg")) # 2
print(find_Rotations("abcd")) # 3
print(find_Rotations("abcdabcd")) # 0
print(find_Rotations("abcdabcde")) # 1
print(find_Rotations("abcdabcdeabcd")) # 0
print(find_Rotations("abcdabcdeabcdabcd")) # 0
print(find_Rotations("abcdabcdeabcdefg")) # 1
print(find_Rotations("abcdabcdefgabcde")) # 1
print(find_Rotations("abcdabcdefgabcdefg")) # 0
print(find_Rotations("abcdabcdefgabcdefgabcdefg")) # 0
print(find_Rotations("abcdabcdefgabcdefgabcdefgabcdefg")) # 0
print(find_Rotations("abcdabcdefgabcdefgabcdefgabcdefgabcdefg")) # 0
print(find_Rotations("abcdabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # 0
print(find_Rotations("abcdabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # 0
print(find_Rotations("abcdabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # 0
print(find_Rotations("abcdabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # 0
print(find_Rotations("abcdabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # 0
print(find_Rotations("abcdabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # 0
print(find_Rotations("abcdabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # 0
print(find_Rotations("abcdabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # 0
print(find_Rotations("abcdabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # 0
print(find_Rotations("abcdabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # 0
print(find_Rotations("abcdabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # 0
print(find_Rotations("abcdabcdefgabc