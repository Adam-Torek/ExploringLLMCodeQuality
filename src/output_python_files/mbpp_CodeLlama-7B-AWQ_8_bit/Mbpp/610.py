"""
Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
"""

def remove_kth_element(lst, k):
    lst = lst[:k] + lst[k+1:]
    return lst


print(remove_kth_element([1,1,2,3,4,4,5,1],3))
print(remove_kth_element([1,1,2,3,4,4,5,1],1))
print(remove_kth_element([1,1,2,3,4,4,5,1],0))
print(remove_kth_element([1,1,2,3,4,4,5,1],8))
print(remove_kth_element([1,1,2,3,4,4,5,1],-1))
print(remove_kth_element([1,1,2,3,4,4,5,1],-8))
print(remove_kth_element([1,1,2,3,4,4,5,1],-10))
print(remove_kth_element([1,1,2,3,4,4,5,1],-100))
print(remove_kth_element([1,1,2,3,4,4,5,1],100))
print(remove_kth_element([1,1,2,3,4,4,5,1],10))
print(remove_kth_element([1,1,2,3,4,4,5,1],1000))
print(remove_kth_element([1,1,2,3,4,4,5,1],10000))
print(remove_kth_element([1,1,2,3,4,4,5,1],100000))
print(remove_kth_element([1,1,2,3,4,4,5,1],1000000))
print(remove_kth_element([1,1,2,3,4,4,5,1],10000000))
print(remove_kth_element([1,1,2,3,4,4,5,1],100000000))
print(remove_kth_element([1,1,2,3,4,4,5,1],1000000000))
print(remove_kth_element([1,1,2,3,4,4,5,1],10000000000))
print(remove_kth_element([1,1,2,3,4,4,5,1],100000000000))
print(remove_kth_element([1,1,2,3,4,4,5,1],1000000000000))
print(remove_kth_element([1,1,2,3,4,4,5,1],10000000000000))
print(remove_kth_element([1,1,2,3,4,4,5,1],100000000000000))
print(remove_kth_element([1,1,2,3,4,4,5,1],1000000000000000))
print(remove_kth_element([1,1,2,3,4,4,5,1],10000000000000000))
print(remove_kth_element([1,1,2,3,4,4,5,1],100000000000000000))
print(remove_kth_element([1,1,2,3,4,4,5,1],1000000000000000000))
print(