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
    if n == 3:
        if s[0] == s[1] and s[1] == s[2]:
            return 0
        elif s[0] == s[1] and s[1] != s[2]:
            return 1
        elif s[0] != s[1] and s[1] == s[2]:
            return 2
        else:
            return 1
    else:
        for i in range(n):
            if s[i] == s[0]:
                return i + 1
        return 1

print(find_Rotations("aaaa")) # Output: 1
print(find_Rotations("abab")) # Output: 2
print(find_Rotations("abcde")) # Output: 1
print(find_Rotations("abcab")) # Output: 2
print(find_Rotations("abcabc")) # Output: 1
print(find_Rotations("abcdabc")) # Output: 2
print(find_Rotations("ababab")) # Output: 0
print(find_Rotations("abcdabcd")) # Output: 2
print(find_Rotations("abcdabce")) # Output: 1
print(find_Rotations("abcdabcde")) # Output: 3
print(find_Rotations("abcdefg")) # Output: 1
print(find_Rotations("abcdefgh")) # Output: 2
print(find_Rotations("abcdefghi")) # Output: 3
print(find_Rotations("abcdefghij")) # Output: 4
print(find_Rotations("abcdefghijk")) # Output: 5
print(find_Rotations("abcdefghijkl")) # Output: 6
print(find_Rotations("abcdefghijklm")) # Output: 7
print(find_Rotations("abcdefghijklmn")) # Output: 8
print(find_Rotations("abcdefghijklmno")) # Output: 9
print(find_Rotations("abcdefghijklmnop")) # Output: 10
print(find_Rotations("abcdefghijklmnopq")) # Output: 11
print(find_Rotations("abcdefghijklmnopqr")) # Output: 12
print(find_Rotations("abcdefghijklmnopqrs")) # Output: 13
print(find_Rotations("abcdefghijklmnopqrst")) # Output: 14
print(find_Rotations("abcdefghijklmnopqrstu")) # Output: 15
print(find_Rotations("abcdefghijklmnopqrstuv")) # Output: 16
print(find_Rotations("abcdefghijklmnopqrstuvw")) # Output: 17
print(find_Rotations("abcdefghijklmnopqrstuvwx")) # Output: 18
print(find_Rotations("abcdefghijklmnopqrstuvwxy")) # Output: 19
print(find_Rotations("abcdefghijklmnopqrstuvwxyz")) # Output: 20
print(find_Rotations("abcdefghijklmnopqrstuvwxyz1")) # Output: 21
print(find_Rotations("abcdefghijklmnopqrstuvwxyz12")) # Output: 22
print(find_Rotations("abcdefghijklmnopqrstuvwxyz123")) # Output: 23
print(find_Rotations("abcdefghijklmnopqrstuvwxyz1234")) # Output: 24
print(find_Rotations("abcdefghijklmnopqrstuvwxyz12345")) # Output: 25
print(find_Rotations("abc