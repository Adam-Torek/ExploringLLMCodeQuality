"""
Write a python function to count number of digits in a given string.
assert number_ctr('program2bedone') == 1
"""

def number_ctr(string):
    count = 0
    for char in string:
        if char.isdigit():
            count += 1
    return count

# Test the function
assert number_ctr('program2bedone') == 1<|endoftext|>