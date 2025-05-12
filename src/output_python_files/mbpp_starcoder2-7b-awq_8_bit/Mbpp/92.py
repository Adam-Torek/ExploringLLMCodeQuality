"""
Write a function to check whether the given number is undulating or not.
assert is_undulating(1212121) == True
"""

def is_undulating(num):
    num = str(num)
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            return False
    return True

print(is_undulating(1212121))
print(is_undulating(1234567))
print(is_undulating(12345678))
print(is_undulating(123456789))
print(is_undulating(1234567890))
print(is_undulating(12345678901))
print(is_undulating(123456789012))
print(is_undulating(1234567890123))
print(is_undulating(12345678901234))
print(is_undulating(123456789012345))
print(is_undulating(1234567890123456))
print(is_undulating(12345678901234567))
print(is_undulating(123456789012345678))
print(is_undulating(1234567890123456789))
print(is_undulating(12345678901234567890))
print(is_undulating(123456789012345678901))
print(is_undulating(1234567890123456789012))
print(is_undulating(12345678901234567890123))
print(is_undulating(123456789012345678901234))
print(is_undulating(1234567890123456789012345))
print(is_undulating(12345678901234567890123456))
print(is_undulating(123456789012345678901234567))
print(is_undulating(1234567890123456789012345678))
print(is_undulating(12345678901234567890123456789))
print(is_undulating(123456789012345678901234567890))
print(is_undulating(1234567890123456789012345678901))
print(is_undulating(12345678901234567890123456789012))
print(is_undulating(123456789012345678901234567890123))
print(is_undulating(1234567890123456789012345678901234))
print(is_undulating(12345678901234567890123456789012345))
print(is_undulating(123456789012345678901234567890123456))
print(is_undulating(