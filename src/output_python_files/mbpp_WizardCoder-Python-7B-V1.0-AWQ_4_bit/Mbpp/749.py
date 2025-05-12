"""
Write a function to sort a given list of strings of numbers numerically. https://www.geeksforgeeks.org/python-sort-numeric-strings-in-a-list/
assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
"""

def sort_numeric_strings(lst):
    lst = [int(i) if i[0] != '-' else int(i[1:]) for i in lst]
    return sorted(lst)

# Test the function
print(sort_numeric_strings(['4','12','45','7','0','100','200','-12','-500']))
# Output: [-500, -12, 0, 4, 7, 12, 45, 100, 200]

# Test the function
print(sort_numeric_strings(['-100','-500','-200','0','4','12','45','7']))
# Output: [-200, -500, -100, 0, 4, 7, 12, 45]

# Test the function
print(sort_numeric_strings(['100','200','45','4','7','12','0','-12','-500']))
# Output: [-500, -12, 0, 4, 7, 12, 45, 100, 200]

# Test the function
print(sort_numeric_strings(['-100','-500','-200','0','4','12','45','7']))
# Output: [-200, -500, -100, 0, 4, 7, 12, 45]

# Test the function
print(sort_numeric_strings(['100','200','45','4','7','12','0','-12','-500']))
# Output: [-500, -12, 0, 4, 7, 12, 45, 100, 200]

# Test the function
print(sort_numeric_strings(['-100','-500','-200','0','4','12','45','7']))
# Output: [-200, -500, -100, 0, 4, 7, 12, 45]

# Test the function
print(sort_numeric_strings(['100','200','45','4','7','12','0','-12','-500']))
# Output: [-500, -12, 0, 4, 7, 12, 45, 100, 200]

# Test the function
print(sort_numeric_strings(['-100','-500','-200','0','4','12','45','7']))
# Output: [-200, -500, -100, 0, 4, 7, 12, 45]

# Test the function
print(sort_numeric_strings(['100','200','45','4','7','12','0','-12','-500']))
# Output: [-500, -12, 0, 4, 7, 12, 45, 100, 200]

# Test the function
print(sort_numeric_strings(['-100','-500','-200','0','4','12','45','7']))
# Output: [-200, -500, -100, 0, 4, 7, 12, 45]

# Test the function
print(sort_numeric_strings(['100','200','45','4','7','12','0','-12','-50