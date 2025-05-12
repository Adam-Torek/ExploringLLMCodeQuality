"""
Write a function to check whether the given number is undulating or not.
assert is_undulating(1212121) == True
"""

def is_undulating(num):
    num_str = str(num)
    for i in range(len(num_str) - 2):
        if num_str[i] == num_str[i+2]:
            return True
    return False

print(is_undulating(1212121)) # True
print(is_undulating(123456)) # False
print(is_undulating(121314121)) # True
print(is_undulating(1234567)) # False
print(is_undulating(121314151617181920)) # True
print(is_undulating(12345)) # False
print(is_undulating(12131415161718192021)) # False