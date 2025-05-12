"""
Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
assert find_Rotations("aaaa") == 1
"""

def find_Rotations(s):
    if len(s) == 1:
        return 0
    for i in range(1, len(s)):
        if s[i:] + s[:i] == s:
            return i
    return 0

print(find_Rotations("aaaa"))
print(find_Rotations("abcd"))
print(find_Rotations("abcda"))
print(find_Rotations("abcde"))
print(find_Rotations("abcdef"))
print(find_Rotations("abcdefg"))
print(find_Rotations("abcdefga"))
print(find_Rotations("abcdefgaa"))
print(find_Rotations("abcdefgaaa"))
print(find_Rotations("abcdefgaaaa"))
print(find_Rotations("abcdefgaaaaa"))
print(find_Rotations("abcdefgaaaaaa"))
print(find_Rotations("abcdefgaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(find_Rotations("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa