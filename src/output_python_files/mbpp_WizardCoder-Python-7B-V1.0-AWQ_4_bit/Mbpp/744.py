"""
Write a function to check if the given tuple has any none value or not.
assert check_none((10, 4, 5, 6, None)) == True
"""

def check_none(tup):
    for i in tup:
        if i is None:
            return True
    return False

# Test cases
print(check_none((10, 4, 5, 6, None)) == True) # True
print(check_none((10, 4, 5, 6, 7)) == False) # False
print(check_none((10, None, 5, 6, 7)) == True) # True
print(check_none((10, 4, None, 6, 7)) == True) # True
print(check_none((10, 4, 5, 6)) == False) # False

# Test cases with empty tuple
print(check_none(()) == False) # False
print(check_none((None,)) == True) # True
print(check_none((None, None, None) == True) # True
print(check_none((1, None, 2, None, 3) == True) # True
print(check_none((1, 2, 3, None, None) == True) # True
print(check_none((None, 1, 2, 3, None) == True) # True
print(check_none((None, None, None, None) == True) # True

# Test cases with non-tuple input
try:
    check_none(123)
except TypeError as e:
    print(e) # check_none() argument must be tuple

try:
    check_none([1, 2, 3, 4])
except TypeError as e:
    print(e) # check_none() argument must be tuple

try:
    check_none("hello")
except TypeError as e:
    print(e) # check_none() argument must be tuple

try:
    check_none(123, 456)
except TypeError as e:
    print(e) # check_none() takes 1 positional argument but 2 were given

try:
    check_none()
except TypeError as e:
    print(e) # check_none() takes 1 positional argument but 0 were given

try:
    check_none(1, 2, 3, 4)
except TypeError as e:
    print(e) # check_none() takes 1 positional argument but 4 were given

try:
    check_none(1, 2, 3, 4, 5, 6)
except TypeError as e:
    print(e) # check_none() takes 1 positional argument but 5 were given

try:
    check_none(1, 2, 3, 4, 5, 6, 7, 8)
except TypeError as e:
    print(e) # check_none() takes 1 positional argument but 6 were given

try:
    check_none(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
except TypeError as e:
    print(e) # check_none() takes 1 positional argument but 7 were given

try:
    check_none(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
except TypeError as e:
    print(e) # check_none() takes 1 positional argument but 8 were given

try:
    check_none(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
except TypeError as e:
    print(e) # check_none() takes 1 positional argument but