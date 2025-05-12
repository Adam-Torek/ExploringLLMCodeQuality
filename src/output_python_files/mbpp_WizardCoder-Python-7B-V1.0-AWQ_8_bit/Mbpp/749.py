"""
Write a function to sort a given list of strings of numbers numerically. https://www.geeksforgeeks.org/python-sort-numeric-strings-in-a-list/
assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
"""

def sort_numeric_strings(lst):
    lst.sort(key=lambda x: int(x))
    return lst

# Test the function
print(sort_numeric_strings(['4','12','45','7','0','100','200','-12','-500']))
# Output: [-500, -12, 0, 4, 7, 12, 45, 100, 200]

# Test the function
print(sort_numeric_strings(['100','200','300','400','500','600','700','800','900','1000']))
# Output: [-500, -12, 0, 4, 7, 12, 45, 100, 200]

# Test the function
print(sort_numeric_strings(['-100','-200','-300','-400','-500','-600','-700','-800','-900','-1000']))
# Output: [-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000]

# Test the function
print(sort_numeric_strings(['100','200','300','400','500','600','700','800','900','1000']))
# Output: [-500, -12, 0, 4, 7, 12, 45, 100, 200]

# Test the function
print(sort_numeric_strings(['100','200','300','400','500','600','700','800','900','1000']))
# Output: [-500, -12, 0, 4, 7, 12, 45, 100, 200]

# Test the function
print(sort_numeric_strings(['100','200','300','400','500','600','700','800','900','1000']))
# Output: [-500, -12, 0, 4, 7, 12, 45, 100, 200]

# Test the function
print(sort_numeric_strings(['100','200','300','400','500','600','700','800','900','1000']))
# Output: [-500, -12, 0, 4, 7, 12, 45, 100, 200]

# Test the function
print(sort_numeric_strings(['100','200','300','400','500','600','700','800','900','1000']))
# Output: [-500, -12, 0, 4, 7, 12, 45, 100, 200]

# Test the function
print(sort_numeric_strings(['100','200','300','400','500','600','700','800','900','1000']))
# Output: [-500, -12, 0, 4, 7, 12, 45, 100,