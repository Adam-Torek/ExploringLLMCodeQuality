"""
Write a function to create a list of N empty dictionaries.
assert empty_list(5)==[{},{},{},{},{}]
"""

def empty_list(n):
    """
    Create a list of N empty dictionaries.
    """
    return [{} for i in range(n)]

# assert empty_list(5)==[{},{},{},{},{}]
print(empty_list(5))