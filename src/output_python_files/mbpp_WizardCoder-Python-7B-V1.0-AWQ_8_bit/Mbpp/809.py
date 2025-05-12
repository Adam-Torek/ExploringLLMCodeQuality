"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
"""

def check_smaller(tup1, tup2):
    if len(tup1) != len(tup2):
        return False
    for i in range(len(tup1)):
        if tup1[i] > tup2[i]:
            return False
    return True

print(check_smaller((1, 2, 3), (2, 3, 4))) # False
print(check_smaller((1, 2, 3), (1, 2, 3))) # True
print(check_smaller((1, 2, 3), (1, 2, 2))) # False
print(check_smaller((1, 2, 3), (1, 2, 1))) # False
print(check_smaller((1, 2, 3), (1, 1, 2))) # False
print(check_smaller((1, 2, 3), (1, 1, 1)) # False
print(check_smaller((1, 2, 3), (2, 3, 4)) # False
print(check_smaller((1, 2, 3), (3, 2, 1)) # True
print(check_smaller((1, 2, 3), (3, 3, 2)) # True
print(check_smaller((1, 2, 3), (4, 2, 1)) # False
print(check_smaller((1, 2, 3), (4, 3, 2)) # False
print(check_smaller((1, 2, 3), (5, 4, 3)) # False
print(check_smaller((1, 2, 3), (1, 4, 5)) # False
print(check_smaller((1, 2, 3), (1, 3, 2)) # False
print(check_smaller((1, 2, 3), (1, 2, 3)) # True