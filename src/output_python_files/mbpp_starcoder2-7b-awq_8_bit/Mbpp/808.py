"""
Write a function to check if the given tuples contain the k or not.
assert check_K((10, 4, 5, 6, 8), 6) == True
"""

def check_K(tup, k):
    for i in tup:
        if i == k:
            return True
    return False

assert check_K((10, 4, 5, 6, 8), 6) == True
assert check_K((10, 4, 5, 6, 8), 10) == True
assert check_K((10, 4, 5, 6, 8), 11) == False
/01_Python_Basics/01_Python_Basics_01/01_Python_Basics_01_01/01_Python_Basics_01_01_01/01_Python_Basics_01_01_01_01/01_Python_Basics_01_01_01_01_01/01_Python_Basics_01_01_01_01_01_01/01_Python_Basics_01_01_01_01_01_01_01/01_Python_Basics_01_01_01_01_01_01_01_01/01_Python_Basics_01_01_01_01_01_01_01_01_01/01_Python_Basics_01_01_01_01_01_01_01_01_01_01/01_Python_Basics_01_01_01_01_01_01_01_01_01_01_01/01_Python_Basics_01_01_01_01_01_01_01_01_01_01_01_01/01_Python_Basics_01_01_01_01_01_01_01_01_01_01_01_01_01/01_Python_Basics_01_01_01_01_01_01_01_01_01_01_01_01_01_01/01_Python_Basics_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01/01_Python_Basics_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01/01_Python_Basics_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01/01_Python_Basics_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01/01_Python_Basics_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01/01_Python_Basics_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01/01_Python_Basics_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01_01/01_Python_Basics_01_01_01_01_