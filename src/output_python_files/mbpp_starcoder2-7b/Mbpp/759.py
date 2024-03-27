"""
Write a function to check whether a given string is a decimal number with a precision of 2.
assert is_decimal('123.11')==True
"""

def is_decimal(s):
    if '.' in s:
        if s.count('.') == 1:
            if s.split('.')[0].isdigit() and s.split('.')[1].isdigit():
                return True
    return False

print(is_decimal('123.11'))
print(is_decimal('123.11.1'))
print(is_decimal('123.111'))
print(is_decimal('123.111.1'))
print(is_decimal('123.111.1.1'))
print(is_decimal('123.111.1.1.1'))
print(is_decimal('123.111.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1.1.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1.1.1.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1.1.1.1.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1'))
print(is_decimal('123.111.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.