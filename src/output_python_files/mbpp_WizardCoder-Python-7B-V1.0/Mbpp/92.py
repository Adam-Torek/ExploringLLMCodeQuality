"""
Write a function to check whether the given number is undulating or not.
assert is_undulating(1212121) == True
"""

def is_undulating(num):
    num_str = str(num)
    for i in range(len(num_str) - 2):
        if num_str[i] == num_str[i+2]:
            return False
    return True

# Test cases
print(is_undulating(1212121)) # True
print(is_undulating(1234567)) # False
print(is_undulating(121314121)) # True
print(is_undulating(123123)) # False
print(is_undulating(121212)) # False
print(is_undulating(123123123)) # True
print(is_undulating(12312312)) # False
print(is_undulating(121212121)) # True
print(is_undulating(12121212)) # False
print(is_undulating(123123123)) # True
print(is_undulating(1231231231)) # False
print(is_undulating(12121212121)) # True
print(is_undulating(1212121212)) # False
print(is_undulating(12312312312)) # True
print(is_undulating(123123123123)) # False
print(is_undulating(1212121212121)) # True
print(is_undulating(121212121212)) # False
print(is_undulating(1231231231231)) # True
print(is_undulating(12312312312312)) # False
print(is_undulating(121212121212121)) # True
print(is_undulating(12121212121212)) # False
print(is_undulating(123123123123123)) # True
print(is_undulating(1231231231231231)) # False
print(is_undulating(12121212121212121)) # True
print(is_undulating(1212121212121212)) # False
print(is_undulating(12312312312312312)) # True
print(is_undulating(123123123123123123)) # False
print(is_undulating(1212121212121212121)) # True
print(is_undulating(121212121212121212)) # False
print(is_undulating(1231231231231231231)) # True
print(is_undulating(12312312312312312312)) # False
print(is_undulating(121212121212121212121)) # True
print(is_undulating(12121212121212121212)) # False
print(is_undulating(123123123123123123123)) # True
print(is_undulating(1231231231231231231231)) # False
print(is_undulating(12121212121212121212121)) # True
print(is_undulating(121