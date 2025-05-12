"""
Write a function to check whether an element exists within a tuple.
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
"""

def check_tuplex(tup, element):
    return element in tup

# Test cases
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True) # True
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'t')==False) # False
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'w')==True) # True
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'e')==True) # True
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'c')==True) # True
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'z')==False) # False
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'w')==True) # True
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'e')==True) # True
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'c')==True) # True
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'z')==False) # False
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'w')==True) # True
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'e')==True) # True
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'c')==True) # True
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'z')==False) # False
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'w')==True) # True
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'e')==True) # True
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'c')==True) # True
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'z')==False) # False
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'w')==True) # True
print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'e')==True) # True
print(check_tuplex(("w", 3, "r", "