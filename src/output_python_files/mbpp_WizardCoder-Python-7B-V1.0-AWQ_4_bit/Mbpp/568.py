"""
Write a function to create a list of N empty dictionaries.
assert empty_list(5)==[{},{},{},{},{}]
"""

def empty_list(n):
    return [{}]*n

print(empty_list(5))