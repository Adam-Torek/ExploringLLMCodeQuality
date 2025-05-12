"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""
def mul_even_odd(lst):
    """
    This function takes a list as an input and returns the product of first even and odd number of the list.
    """
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even*odd

# Testing the function
assert mul_even_odd([1,3,5,7,4,1,6,8])==4