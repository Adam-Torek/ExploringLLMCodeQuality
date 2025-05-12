"""
Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
"""
def remove_kth_element(lst, k):
    return lst[:k-1] + lst[k:]

print(remove_kth_element([1,1,2,3,4,4,5,1],3)) # [1, 1, 2, 4, 4, 5, 1]
print(remove_kth_element([1,1,2,3,4,4,5,1],1)) # [1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],6)) # [1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],0)) # [1, 1, 2, 3, 4, 4, 5, 1]
print(remove_kth_element([1,1,2,3,4,4,5,1],7)) # [1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],-1)) # [1, 1, 2, 3, 4, 4, 5, 1]
print(remove_kth_element([],3)) # []
print(remove_kth_element([1],1)) # []
print(remove_kth_element([1,1,2,3,4,4,5,1],0)) # [1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],1)) # [1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],2)) # [1, 1, 2, 3, 4, 5, 1]
print(remove_kth_element([1,1,2,3,4,4,5,1],4)) # [1, 1, 2, 3, 4, 5, 1]
print(remove_kth_element([1,1,2,3,4,4,5,1],5)) # [1, 1, 2, 3, 4, 4, 1]
print(remove_kth_element([1,1,2,3,4,4,5,1],6)) # [1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],7)) # [1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],8)) # [1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],-1)) # [1, 1, 2, 3, 4, 4, 5, 1]
print(remove_kth_element([1,1,2,3,4,4,5,1],0)) # [1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],1)) # [1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,