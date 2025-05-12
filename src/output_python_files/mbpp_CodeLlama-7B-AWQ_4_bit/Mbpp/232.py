"""
Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
"""

def larg_nnum(lst, n):
    """
    lst: list of numbers
    n: integer
    return: list of the n largest numbers in lst
    """
    # Your code here
    lst.sort(reverse=True)
    return lst[:n]