"""
Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
"""

def larg_nnum(lst, n):
    return sorted(lst, reverse=True)[:n]

print(set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90]))

# Output: True

# Explanation:
# The function takes in a list and an integer n. It sorts the list in descending order and returns the first n elements of the sorted list.
# In this case, the sorted list is [100, 90, 80, 70, 60, 50, 50, 40, 20, 20, 10]. The first two elements are [100, 90] which are the two largest numbers in the list.
# The set() function is used to remove duplicates and return only the two largest numbers.