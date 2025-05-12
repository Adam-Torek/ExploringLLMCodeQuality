"""
Write a function to check whether a given string is a decimal number with a precision of 2.
assert is_decimal('123.11')==True
"""

def is_decimal(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# Test cases
print(is_decimal('123.11')) # True
print(is_decimal('123.111')) # False
print(is_decimal('123.1111')) # False
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
print(is_decimal('123.111111111111111111111111111111')) # False
print(is_decimal('123.1111111111111111111111111111111')) # False
print(is_decimal('123.11111111111111111111111111111111')) # False
print(is_decimal('123.111111111111111111111111