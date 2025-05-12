"""
Write a function to check whether the given number is undulating or not.
assert is_undulating(1212121) == True
"""

def is_undulating(n):
    if n < 0:
        return False
    i = 0
    while i < len(n) - 1:
        if n[i] == n[i + 1]:
            i += 1
        else:
            return True
    return False