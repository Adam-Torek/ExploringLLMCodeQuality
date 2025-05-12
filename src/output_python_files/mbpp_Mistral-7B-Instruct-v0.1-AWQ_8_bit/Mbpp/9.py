"""
Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
assert find_Rotations("aaaa") == 1
"""

def find_Rotations(s):
    if len(s) == 1:
        return 0
    else:
        for i in range(1,len(s)):
            if s[0] == s[i]:
                return i
            else:
                break
        return -1

# test
assert find_Rotations("aaaa") == 1
assert find_Rotations("aab") == 2
assert find_Rotations("abc") == -1