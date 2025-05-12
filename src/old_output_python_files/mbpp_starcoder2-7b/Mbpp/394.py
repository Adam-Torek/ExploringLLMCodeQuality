"""
Write a function to check if given tuple contains no duplicates.
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""

def check_distinct(tup):
    return len(tup) == len(set(tup))

assert check_distinct((1, 4, 5, 6, 1, 4)) == False
assert check_distinct((1, 4, 5, 6, 1, 5)) == True
assert check_distinct((1, 4, 5, 6, 1, 6)) == True
assert check_distinct((1, 4, 5, 6, 1, 7)) == True
assert check_distinct((1, 4, 5, 6, 1, 8)) == True
assert check_distinct((1, 4, 5, 6, 1, 9)) == True
assert check_distinct((1, 4, 5, 6, 1, 10)) == True
assert check_distinct((1, 4, 5, 6, 1, 11)) == True
assert check_distinct((1, 4, 5, 6, 1, 12)) == True
assert check_distinct((1, 4, 5, 6, 1, 13)) == True
assert check_distinct((1, 4, 5, 6, 1, 14)) == True
assert check_distinct((1, 4, 5, 6, 1, 15)) == True
assert check_distinct((1, 4, 5, 6, 1, 16)) == True
assert check_distinct((1, 4, 5, 6, 1, 17)) == True
assert check_distinct((1, 4, 5, 6, 1, 18)) == True
assert check_distinct((1, 4, 5, 6, 1, 19)) == True
assert check_distinct((1, 4, 5, 6, 1, 20)) == True
assert check_distinct((1, 4, 5, 6, 1, 21)) == True
assert check_distinct((1, 4, 5, 6, 1, 22)) == True
assert check_distinct((1, 4, 5, 6, 1, 23)) == True
assert check_distinct((1, 4, 5, 6, 1, 24)) == True
assert check_distinct((1, 4, 5, 6, 1, 25)) == True
assert check_distinct((1, 4, 5, 6, 1, 26)) == True
assert check_distinct((1, 4, 5, 6, 1, 27)) == True
assert check_distinct((1, 4, 5, 6, 1, 28)) == True
assert check_distinct((1, 4, 5, 6, 1, 29)) == True
assert check_distinct((1, 4, 5, 6, 1, 30)) == True
assert check_distinct((1, 4, 5, 6, 1, 31)) == True
assert check_distinct((1, 4, 5, 6, 1, 32)) == True
assert check_distinct((1, 4, 5, 6, 1, 33)) == True
assert check_distinct((1, 4, 5, 6, 1, 34)) == True
assert check_distinct((1, 4, 5, 6, 1, 35)) == True
assert check_distinct((1, 4, 5, 6, 1, 36)) == True
assert check_distinct((1, 4, 5, 6, 1, 37)) == True
assert check_distinct((1, 4, 5, 6, 1, 38)) == True
assert check_distinct((1, 4, 5, 6, 1, 39)) == True
assert check_distinct((1, 4, 5, 6, 1, 40)) == True
assert check_