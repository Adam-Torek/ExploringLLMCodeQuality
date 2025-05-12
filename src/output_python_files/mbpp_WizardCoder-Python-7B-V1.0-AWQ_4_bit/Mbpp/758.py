"""
Write a function to count lists within a list. The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurencies in the original list.
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
"""

def unique_sublists(lst):
    d = {}
    for sublst in lst:
        t = tuple(sublst)
        if t in d:
            d[t] += 1
        else:
            d[t] = 1
    return d

print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])) #{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}

#Alternative solution:
def count_sublists(lst):
    d = {}
    for sublst in lst:
        t = tuple(sublst)
        d[t] = d.get(t, 0) + 1
    return d

print(count_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])) #{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}

#Alternative solution using Counter:
from collections import Counter
def count_sublists(lst):
    return Counter(tuple(sorted(sublst)) for sublst in lst)

print(count_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])) #Counter({(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}

#Alternative solution using defaultdict:
from collections import defaultdict
def count_sublists(lst):
    d = defaultdict(int)
    for sublst in lst:
        t = tuple(sublst)
        d[t] += 1
    return dict(d)

print(count_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])) #{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}

#Alternative solution using set:
def count_sublists(lst):
    d = {}
    for sublst in lst:
        t = tuple(sorted(sublst))
        d[t] = d.get(t, 0) + 1
    return d

print(count_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])) #{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}

#Alternative solution using set:
from collections import Counter
def count_sublists(lst):
    return Counter(tuple(sorted(sublst)) for sublst in lst)

print(count_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7