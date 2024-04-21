"""
Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
assert find_Rotations("aaaa") == 1
"""
def find_Rotations(s):
    n = len(s)
    if n == 1:
        return 0
    if n == 2:
        return 1 if s[0] < s[1] else 0
    if n == 3:
        return 2 if s[0] < s[1] and s[1] < s[2] else 1 if s[0] < s[2] and s[2] < s[1] else 0
    if n == 4:
        return 3 if s[0] < s[1] and s[1] < s[2] and s[2] < s[3] else 2 if s[0] < s[2] and s[2] < s[1] and s[1] < s[3] else 1 if s[0] < s[3] and s[3] < s[1] and s[1] < s[2] else 0
    if n == 5:
        return 4 if s[0] < s[1] and s[1] < s[2] and s[2] < s[3] and s[3] < s[4] else 3 if s[0] < s[2] and s[2] < s[1] and s[1] < s[3] and s[3] < s[4] else 2 if s[0] < s[3] and s[3] < s[1] and s[1] < s[2] and s[2] < s[4] else 1 if s[0] < s[4] and s[4] < s[1] and s[1] < s[2] and s[2] < s[3] else 0
    if n == 6:
        return 5 if s[0] < s[1] and s[1] < s[2] and s[2] < s[3] and s[3] < s[4] and s[4] < s[5] else 4 if s[0] < s[2] and s[2] < s[1] and s[1] < s[3] and s[3] < s[4] and s[4] < s[5] else 3 if s[0] < s[3] and s[3] < s[1] and s[1] < s[2] and s[2] < s[4] and s[4] < s[5] else 2 if s[0] < s[4] and s[4] < s[1] and s[1] < s[2] and s[2] < s[3] and s[3] < s[5] else 1 if s[0] < s[5] and s[5] < s[1] and s[1] < s[2] and s[2] < s[3] and s[3] < s[4] else 0
    if n == 7:
        return 6 if s[0] < s[1] and s[1] < s[2] and s[2] < s[3] and s[3] < s[4] and s[4] < s[5] and s[5] < s[6] else 5 if s[0] < s[2] and s[2] < s[1] and s[1] < s[3] and s[3] < s[4] and s[4] < s[5] and s[5] < s[6] else 4 if s[0] < s[3] and s[3] < s[1] and s[1] < s[2] and s[2] < s[4] and s[4] < s[5] and s[5] < s[6] else 3 if s[0] < s[4] and s[4] < s[1] and s[1] < s[2] and s[2] < s[3] and s[3] < s[5] and s[5] < s[6] else 2 if s[0] < s[5] and s[5] < s[1] and s[1] < s[2] and s[2] < s[3] and s[