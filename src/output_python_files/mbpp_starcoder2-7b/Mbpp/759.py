"""
Write a function to check whether a given string is a decimal number with a precision of 2.
assert is_decimal('123.11')==True
"""

def is_decimal(s):
    if '.' not in s:
        return False
    else:
        if s.count('.') > 1:
            return False
        else:
            if s.count('.') == 1:
                if s.split('.')[1].isdigit():
                    return True
                else:
                    return False
            else:
                if s.isdigit():
                    return True
                else:
                    return False

print(is_decimal('123.11'))
print(is_decimal('123.11.1'))
print(is_decimal('123.11a'))
print(is_decimal('123.11.1a'))
print(is_decimal('123.11a.1'))
print(is_decimal('123.11a1'))
print(is_decimal('123.111'))
print(is_decimal('123.111a'))
print(is_decimal('123.111.1'))
print(is_decimal('123.111.1a'))
print(is_decimal('123.111a.1'))
print(is_decimal('123.111a1'))
print(is_decimal('123.1111'))
print(is_decimal('123.1111a'))
print(is_decimal('123.1111.1'))
print(is_decimal('123.1111.1a'))
print(is_decimal('123.1111a.1'))
print(is_decimal('123.1111a1'))
print(is_decimal('123.11111'))
print(is_decimal('123.11111a'))
print(is_decimal('123.11111.1'))
print(is_decimal('123.11111.1a'))
print(is_decimal('123.11111a.1'))
print(is_decimal('123.11111a1'))
print(is_decimal('123.111111'))
print(is_decimal('123.111111a'))
print(is_decimal('123.111111.1'))
print(is_decimal('123.111111.1a'))
print(is_decimal('123.111111a.1'))
print(is_decimal('123.111111a1'))
print(is_decimal('123.1111111'))
print(is_decimal('123.1111111a'))
print(is_decimal('123.1111111.1'))
print(is_decimal('123.1111111.1a'))
print(is_decimal('123.1111111a.1'))
print(is_decimal('123.1111111a1'))
print(is_decimal('123.11111111'))
print(is_decimal('123.11111111a'))
print(is_decimal('123.11111111.1'))
print(is_decimal('123.11111111.1a'))
print(is_decimal('123.11111111a.1'))
print(is_decimal('123.11111111a1'))
print(is_decimal('123.111111111'))
print(is_decimal('123.111111111a'))
print(is_decimal('123.111111111.1'))
print(is_decimal('123.