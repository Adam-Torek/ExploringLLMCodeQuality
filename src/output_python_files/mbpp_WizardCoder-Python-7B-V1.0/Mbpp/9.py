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
        if s[0] == s[2]:
            return 0
        elif s[0] == s[1]:
            return 1
        else:
            return 2
    if n == 4:
        if s[0] == s[3]:
            return 0
        elif s[0] == s[1]:
            return 1
        elif s[1] == s[2]:
            return 2
        else:
            return 3
    if n == 5:
        if s[0] == s[4]:
            return 0
        elif s[0] == s[1]:
            return 1
        elif s[1] == s[2]:
            return 2
        elif s[2] == s[3]:
            return 3
        else:
            return 4
    if n == 6:
        if s[0] == s[5]:
            return 0
        elif s[0] == s[1]:
            return 1
        elif s[1] == s[2]:
            return 2
        elif s[2] == s[3]:
            return 3
        elif s[3] == s[4]:
            return 4
        else:
            return 5
    if n == 7:
        if s[0] == s[6]:
            return 0
        elif s[0] == s[1]:
            return 1
        elif s[1] == s[2]:
            return 2
        elif s[2] == s[3]:
            return 3
        elif s[3] == s[4]:
            return 4
        elif s[4] == s[5]:
            return 5
        else:
            return 6
    if n == 8:
        if s[0] == s[7]:
            return 0
        elif s[0] == s[1]:
            return 1
        elif s[1] == s[2]:
            return 2
        elif s[2] == s[3]:
            return 3
        elif s[3] == s[4]:
            return 4
        elif s[4] == s[5]:
            return 5
        elif s[5] == s[6]:
            return 6
        else:
            return 7
    if n == 9:
        if s[0] == s[8]:
            return 0
        elif s[0] == s[1]:
            return 1
        elif s[1] == s[2]:
            return 2
        elif s[2] == s[3]:
            return 3
        elif s[3] == s[4]:
            return 4
        elif s[4] == s[5]:
            return 5
        elif s[5] == s[6]:
            return 6
        elif s[6] == s[7]:
            return 7
        else:
            return 8
    if n == 10:
        if s[0] == s[9]:
            return 0
        elif s[0] == s[1]:
            return 1
        elif s[1] == s[2]:
            return 2
        elif s[2] == s[3]:
            return 3
        elif s[3] == s[4]:
            return 4
        elif s[4] == s[5]:
            return 5
        elif s[5] == s[6]:
            return 6
        elif s[6] == s[7]:
            return 7
        elif s[