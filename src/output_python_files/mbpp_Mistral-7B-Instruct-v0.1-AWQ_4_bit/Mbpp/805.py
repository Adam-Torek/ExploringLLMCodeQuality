"""
Write a function that returns the list in a list of lists whose sum of elements is the highest.
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
"""

def max_sum_list(lst):
    max_sum = lst[0]
    max_sum_index = 0
    for i in range(1,len(lst)):
        if sum(lst[i]) > max_sum:
            max_sum = sum(lst[i])
            max_sum_index = i
    return lst[max_sum_index]

assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]