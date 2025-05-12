"""
Write a function to check whether an element exists within a tuple.
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
"""

def check_tuplex(tuplex, x):
    if x in tuplex:
        return True
    else:
        return False

assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'z')==False

"""
Write a function to convert a list to a tuple.
assert convert_listx([1, 3, 5, 7, 9])== (1, 3, 5, 7, 9)
"""

def convert_listx(listx):
    return tuple(listx)

assert convert_listx([1, 3, 5, 7, 9])== (1, 3, 5, 7, 9)

"""
Write a function to remove an item from a tuple.
assert remove_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==("w", 3, "e", "s", "o", "u", "r", "c", "e")
"""

def remove_tuplex(tuplex, x):
    tuplex = list(tuplex)
    tuplex.remove(x)
    return tuple(tuplex)

assert remove_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==("w", 3, "e", "s", "o", "u", "r", "c", "e")

"""
Write a function to slice a tuple.
assert slice_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),2,6)==("r", "e", "s", "o")
"""

def slice_tuplex(tuplex, x, y):
    return tuplex[x:y]

assert slice_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),2,6)==("r", "e", "s", "o")

"""
Write a function to find the length of a tuple.
assert length_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"))==10
"""

def length_tuplex(tuplex):
    return len(tuplex)

assert length_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"))==10

"""
Write a function to find the minimum and maximum values in a tuple.
assert min_max_tuplex((4, 6, 2, 1, 7, 9))== (1, 9)
"""

def min_max_tuplex(tuplex):
    return (min(tuplex), max(tuplex))

assert min_max_tuplex((4, 6, 2, 1, 7, 9))== (1, 9)

"""
Write a function to find the product of all items in a tuple.
assert product_tuplex((4, 6, 2, 1, 7, 9))== 3024
"""

def product_tuplex(tuplex):
    return reduce(lambda x, y: x*y, tuplex)

assert product_tuplex((4, 6, 2, 1, 7, 9))== 3024

"""
Write a function to find the sum of all items in a tuple.
assert sum_tuplex((4, 6, 2, 1, 7, 9))== 28
"""

def sum_tuplex(tuplex):
    return reduce(lambda x, y: x+y, tuplex)