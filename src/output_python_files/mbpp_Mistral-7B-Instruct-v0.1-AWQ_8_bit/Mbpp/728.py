"""
Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].
assert sum_list([10,20,30],[15,25,35])==[25,45,65]
"""

def sum_list(a,b):
    return [a[i]+b[i] for i in range(len(a))]

#test
assert sum_list([10,20,30],[15,25,35])==[25,45,65]