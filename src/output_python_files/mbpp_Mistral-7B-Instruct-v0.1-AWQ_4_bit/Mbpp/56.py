"""
Write a python function to check if a given number is one less than twice its reverse.
assert check(70) == False
"""

def check(num):
    num_str = str(num)
    num_str_rev = num_str[::-1]
    if int(num_str_rev) * 2 == num - 1:
        return True
    else:
        return False