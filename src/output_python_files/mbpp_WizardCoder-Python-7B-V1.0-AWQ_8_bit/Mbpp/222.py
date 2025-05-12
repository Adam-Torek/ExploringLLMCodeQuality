"""
Write a function to check if all the elements in tuple have same data type or not.
assert check_type((5, 6, 7, 3, 5, 6) ) == True
"""

def check_type(tup):
    return len(set(type(i) for i in tup)) == 1

# Test cases
print(check_type((5, 6, 7, 3, 5, 6)) == True) # True
print(check_type((5, "hello", 3, 5, 6)) == False) # False
print(check_type((5, 6, 7, 3, 5, 6, "hello")) == False) # False
print(check_type((5, 6, 7, 3, 5, 6, 7)) == True) # True
print(check_type((5, 6, 7, 3, 5, 6, 7, "hello")) == False) # False
print(check_type((5, 6, 7, 3, 5, 6, 7, "hello", "world")) == False) # False
print(check_type((5, 6, 7, 3, 5, 6, 7, "hello", "world", 8)) == False) # False
print(check_type((5, 6, 7, 3, 5, 6, 7, "hello", "world", 8, 9)) == False) # False
print(check_type((5, 6, 7, 3, 5, 6, 7, "hello", "world", 8, 9, 10)) == False) # False
print(check_type((5, 6, 7, 3, 5, 6, 7, "hello", "world", 8, 9, 10, "hello")) == False) # False
print(check_type((5, 6, 7, 3, 5, 6, 7, "hello", "world", 8, 9, 10, "hello", "world")) == False) # False
print(check_type((5, 6, 7, 3, 5, 6, 7, "hello", "world", 8, 9, 10, "hello", "world", 11)) == False) # False
print(check_type((5, 6, 7, 3, 5, 6, 7, "hello", "world", 8, 9, 10, "hello", "world", 11, 12)) == False) # False
print(check_type((5, 6, 7, 3, 5, 6, 7, "hello", "world", 8, 9, 10, "hello", "world", 11, 12, 13)) == False) # False
print(check_type((5, 6, 7, 3, 5, 6, 7, "hello", "world", 8, 9, 10, "hello", "world", 11, 12, 13, 14)) == False) # False
print(check_type((5, 6, 7, 3, 5, 6, 7, "hello", "world", 8, 9, 10, "hello", "world", 11, 12, 13, 14, 15)) == False) # False
print(check_type((5, 6, 7, 3, 5, 6, 7, "hello", "world", 8, 9, 10, "hello", "world", 11, 12, 13, 14, 15, 16)) == False) # False
print(check_type((5, 6, 7, 3, 5, 6, 7, "hello", "world", 8, 9, 10, "hello", "world", 11, 12, 13, 14, 15, 16, 17)) == False) # False
print(check_type((5, 6, 7, 3,