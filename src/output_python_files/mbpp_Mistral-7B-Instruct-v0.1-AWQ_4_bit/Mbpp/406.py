"""
Write a python function to find whether the parity of a given number is odd.
assert find_Parity(12) == False
"""

def find_Parity(num):
    if num % 2 == 0:
        return True
    else:
        return False