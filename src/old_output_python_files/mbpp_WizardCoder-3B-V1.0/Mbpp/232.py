"""
Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
"""
def larg_nnum(lst, n):
    return sorted(lst, reverse=True)[:n]

# Test cases
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
assert set(larg_nnum([1, 2, 3, 4, 5],2))==set([5,4])
assert set(larg_nnum([1, 2, 3, 4, 5],3))==set([5,4,3])
assert set(larg_nnum([1, 2, 3, 4, 5],4))==set([5,4,3,2])
assert set(larg_nnum([1, 2, 3, 4, 5],5))==set([5,4,3,2,1])<|endoftext|>