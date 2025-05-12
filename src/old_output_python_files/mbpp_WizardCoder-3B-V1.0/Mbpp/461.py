"""
Write a python function to count the upper case characters in a given string.
assert upper_ctr('PYthon') == 1
"""
def upper_ctr(s):
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    return count

# Test the function
assert upper_ctr('PYthon') == 1<|endoftext|>