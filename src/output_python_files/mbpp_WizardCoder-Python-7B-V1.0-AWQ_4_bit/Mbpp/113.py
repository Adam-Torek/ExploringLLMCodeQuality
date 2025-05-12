"""
Write a function to check if a string represents an integer or not.
assert check_integer("python")==False
"""

def check_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

# Test cases
print(check_integer("python")) # False
print(check_integer("123")) # True
print(check_integer("-123")) # True
print(check_integer("0")) # True
print(check_integer("123abc")) # False
print(check_integer("123.45")) # False
print(check_integer("123.0")) # False
print(check_integer("123e4")) # False
print(check_integer("123.00")) # False
print(check_integer("123.000")) # False
print(check_integer("123.0000")) # False
print(check_integer("123.00000")) # False
print(check_integer("123.000000")) # False
print(check_integer("123.0000000")) # False
print(check_integer("123.00000000")) # False
print(check_integer("123.000000000")) # False
print(check_integer("123.0000000000")) # False
print(check_integer("123.00000000000")) # False
print(check_integer("123.000000000000")) # False
print(check_integer("123.0000000000000")) # False
print(check_integer("123.00000000000000")) # False
print(check_integer("123.000000000000000")) # False
print(check_integer("123.0000000000000000")) # False
print(check_integer("123.00000000000000000")) # False
print(check_integer("123.000000000000000000")) # False
print(check_integer("123.0000000000000000000")) # False
print(check_integer("123.00000000000000000000")) # False
print(check_integer("123.000000000000000000000")) # False
print(check_integer("123.0000000000000000000000")) # False
print(check_integer("123.00000000000000000000000")) # False
print(check_integer("123.000000000000000000000000")) # False
print(check_integer("123.0000000000000000000000000")) # False
print(check_integer("123.00000000000000000000000000")) # False
print(check_integer("123.000000000000000000000000000")) # False
print(check_integer("123.000000000000000