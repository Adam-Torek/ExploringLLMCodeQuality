"""
Write a python function to check if a given number is one less than twice its reverse.
assert check(70) == False
"""

def check(num):
    return num == (2 * num) - 1

# Test cases
print(check(70)) # False
print(check(123)) # True
print(check(1000)) # True<|endoftext|>