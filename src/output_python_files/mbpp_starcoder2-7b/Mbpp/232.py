"""
Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
"""
def larg_nnum(lst,n):
    lst.sort(reverse=True)
    return lst[:n]

"""
Write a function that takes in a list and an integer n and returns a list containing the n smallest items from the list.
assert set(small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([10,20])
"""
def small_nnum(lst,n):
    lst.sort()
    return lst[:n]

"""
Write a function that takes in a list and returns a list containing the same items in the same order but with duplicates removed.
assert set(remove_dup([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]))==set([10, 20, 50, 70, 90, 40, 60, 80, 100])
"""
def remove_dup(lst):
    return list(set(lst))

"""
Write a function that takes in a list and returns a list containing the same items in the same order but with duplicates removed.
assert set(remove_dup([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]))==set([10, 20, 50, 70, 90, 40, 60, 80, 100])
"""
def remove_dup(lst):
    return list(set(lst))

"""
Write a function that takes in a list and returns a list containing the same items in the same order but with duplicates removed.
assert set(remove_dup([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]))==set([10, 20, 50, 70, 90, 40, 60, 80, 100])
"""
def remove_dup(lst):
    return list(set(lst))

"""
Write a function that takes in a list and returns a list containing the same items in the same order but with duplicates removed.
assert set(remove_dup([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]))==set([10, 20, 50, 70, 90, 40, 60, 80, 100])
"""
def remove_dup(lst):
    return list(set(lst))

"""
Write a function that takes in a list and returns a list containing the same items in the same order but with duplicates removed.
assert set(remove_dup([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]))==set([10, 20, 50, 70, 90, 40, 60, 80, 100])
"""
def remove_dup(lst):
    return list(set(lst))

"""
Write a function that takes in a list and returns a list containing the same items in the same order but with duplicates removed.
assert set(remove_dup([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]))==set([10, 20, 50,