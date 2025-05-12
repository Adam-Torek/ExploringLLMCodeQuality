"""
Write a python function to find whether a number is divisible by 11.
assert is_Diff (12345) == False
"""
def is_Divisible_by_11(num):
    if num % 11 == 0:
        return True
    else:
        return False

print(is_Divisible_by_11(12345))