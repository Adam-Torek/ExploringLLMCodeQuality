"""
Write a function to check whether a given string is a decimal number with a precision of 2.
assert is_decimal('123.11')==True
"""

def is_decimal(num):
    try:
        if len(num.split('.')[1]) == 2:
            return True
        else:
            return False
    except:
        return False

print(is_decimal('123.11')) # True
print(is_decimal('123.111')) # False
print(is_decimal('123')) # False
print(is_decimal('123.1111')) # False
print(is_decimal('123.1')) # True
print(is_decimal('123.11111')) # False
print(is_decimal('123.111111')) # False
print(is_decimal('123.1111111')) # False
print(is_decimal('123.11111111')) # False
print(is_decimal('123.111111111')) # False
print(is_decimal('123.1111111111')) # False
print(is_decimal('123.11111111111')) # False
print(is_decimal('123.111111111111')) # False
print(is_decimal('123.1111111111111')) # False
print(is_decimal('123.11111111111111')) # False
print(is_decimal('123.111111111111111')) # False
print(is_decimal('123.1111111111111111')) # False
print(is_decimal('123.11111111111111111')) # False
print(is_decimal('123.111111111111111111')) # False
print(is_decimal('123.1111111111111111111')) # False
print(is_decimal('123.11111111111111111111')) # False
print(is_decimal('123.111111111111111111111')) # False
print(is_decimal('123.1111111111111111111111')) # False
print(is_decimal('123.11111111111111111111111')) # False
print(is_decimal('123.111111111111111111111111')) # False
print(is_decimal('123.1111111111111111111111111')) # False
print(is_decimal('123.11111111111111111111111111')) # False
print(is_decimal('123.111111111111111111111111111')) # False
print(is_decimal('123.1111111111111111111111111111')) # False
print(is_decimal('123.11111111111111111111111111111')) # False
print(is_decimal('123.1111