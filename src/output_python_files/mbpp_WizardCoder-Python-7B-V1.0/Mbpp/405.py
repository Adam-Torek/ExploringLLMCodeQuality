"""
Write a function to check whether an element exists within a tuple.
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
"""
def check_tuplex(tup, element):
    for i in tup:
        if i == element:
            return True
    return False

# Test the function
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'z')==False
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),3)==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"e")==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),3)==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"w")==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"c")==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"e")==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"c")==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"e")==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"c")==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"e")==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"e")==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"e")==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"e")==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"e")==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"e")==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"e")==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"e")==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"e")==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"e")==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),"e")==True