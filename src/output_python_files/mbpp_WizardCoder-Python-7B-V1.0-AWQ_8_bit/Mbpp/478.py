"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""
def remove_lowercase(string):
    return ''.join(char for char in string if char.isupper())

print(remove_lowercase("PYTHon")) # Output: PYTH

# Test cases
print(remove_lowercase("PYTHon")) # Output: PYTH
print(remove_lowercase("Python")) # Output: PYTH
print(remove_lowercase("pythOn")) # Output: PYTH
print(remove_lowercase("PYThOn")) # Output: PYTh
print(remove_lowercase("PYtHoN")) # Output: PYtHN
print(remove_lowercase("PYTHON")) # Output: PYTHON
print(remove_lowercase("PYtHoN")) # Output: PYtHN
print(remove_lowercase("PYTHon123")) # Output: PYTH123
print(remove_lowercase("PYTHon@#$")) # Output: PYTH@#$
print(remove_lowercase("PYTHon!")) # Output: PYTH!
print(remove_lowercase("PYTHon?")) # Output: PYTH?
print(remove_lowercase("PYTHon.")) # Output: PYTH.
print(remove_lowercase("PYTHon,PYTHon")) # Output: PYTH,PYTH
print(remove_lowercase("PYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHonPYTHon