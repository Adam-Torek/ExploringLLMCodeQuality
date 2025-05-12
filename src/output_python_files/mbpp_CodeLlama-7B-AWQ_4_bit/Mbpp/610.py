"""
Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
"""


def remove_kth_element(lst, k):
    return lst[:k-1] + lst[k:]


print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], 3))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], 5))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], 1))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], 8))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], 0))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -1))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -8))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -5))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -2))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -3))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -4))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -6))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -7))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -8))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -9))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -10))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -11))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -12))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -13))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -14))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -15))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -16))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -17))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -18))
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], -19))
print(