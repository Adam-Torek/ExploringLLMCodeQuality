"""
Write a python function takes in an integer and check whether the frequency of each digit in the integer is less than or equal to the digit itself.
assert validate(1234) == True
"""

def validate(num):
    num = str(num)
    for i in num:
        if num.count(i) > int(i):
            return False
    return True

print(validate(1234))
print(validate(12345))
print(validate(123456))
print(validate(1234567))
print(validate(12345678))
print(validate(123456789))
print(validate(1234567890))
print(validate(12345678901))
print(validate(123456789012))
print(validate(1234567890123))
print(validate(12345678901234))
print(validate(123456789012345))
print(validate(1234567890123456))
print(validate(12345678901234567))
print(validate(123456789012345678))
print(validate(1234567890123456789))
print(validate(12345678901234567890))
print(validate(123456789012345678901))
print(validate(1234567890123456789012))
print(validate(12345678901234567890123))
print(validate(123456789012345678901234))
print(validate(1234567890123456789012345))
print(validate(12345678901234567890123456))
print(validate(123456789012345678901234567))
print(validate(1234567890123456789012345678))
print(validate(12345678901234567890123456789))
print(validate(123456789012345678901234567890))
print(validate(1234567890123456789012345678901))
print(validate(12345678901234567890123456789012))
print(validate(123456789012345678901234567890123))
print(validate(1234567890123456789012345678901234))
print(validate(12345678901234567890123456789012345))
print(validate(123456789012345678901234567890123456))
print(validate(123456789012345678901234567