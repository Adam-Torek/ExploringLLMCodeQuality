"""
Write a function to check if all the elements in tuple have same data type or not.
assert check_type((5, 6, 7, 3, 5, 6) ) == True
"""

def check_type(tup):
    return len(set(type(i) for i in tup)) == 1

# Test cases
print(check_type((5, 6, 7, 3, 5, 6)) == True) # True
print(check_type((5, 6, 7, 3, 5, "6") == False) # False
print(check_type((5, 6, 7, 3, 5, 6, "6") == False) # False
print(check_type((5, 6, 7, 3, 5, 6, 7.5) == True) # True
print(check_type((5, 6, 7, 3, 5, 6, "6", 7.5) == False) # False
print(check_type((5, 6, 7, 3, 5, 6, "6", 7.5, "7") == False) # False
print(check_type((5, 6, 7, 3, 5, 6, "6", 7.5, 7) == True) # True
print(check_type((5, 6, 7, 3, 5, 6, "6", 7.5, 7, "7") == False) # False
print(check_type((5, 6, 7, 3, 5, 6, "6", 7.5, 7, 7) == True) # True
print(check_type((5, 6, 7, 3, 5, 6, "6", 7.5, 7, 7, "7") == False) # False
print(check_type((5, 6, 7, 3, 5, 6, "6", 7.5, 7, 7, 7) == True) # True
print(check_type((5, 6, 7, 3, 5, 6, "6", 7.5, 7, 7, 7, 7) == True) # True
print(check_type((5, 6, 7, 3, 5, 6, "6", 7.5, 7, 7, 7, 7, 7) == True) # True
print(check_type((5, 6, 7, 3, 5, 6, "6", 7.5, 7, 7, 7, 7, 7, 7) == True) # True
print(check_type((5, 6, 7, 3, 5, 6, "6", 7.5, 7, 7, 7, 7, 7, 7, 7) == True) # True
print(check_type((5, 6, 7, 3, 5, 6, "6", 7.5, 7, 7, 7, 7, 7, 7, 7, 7) == True) # True
print(check_type((5, 6, 7, 3, 5, 6, "6", 7.5, 7, 7, 7, 7, 7, 7, 7, 7, 7) == True) # True
print(check_type((5, 6, 7, 3, 5, 6, "6", 7.5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7) == True) # True
print(check_type((5, 6, 7, 3, 5, 6, "6", 7.5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7) == True) # True
print(