"""
Write a function to find minimum of three numbers.
assert min_of_three(10,20,0)==0
"""

def min_of_three(a,b,c):
    """
    This function takes three arguments and returns the minimum of the three numbers.
    """
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c

#test the function
assert min_of_three(10,20,0)==0