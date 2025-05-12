"""
Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
"""

def remove_kth_element(lst, k):
    """
    Removes the kth element from the list
    """
    lst.pop(k-1)
    return lst

# Testing the function
print(remove_kth_element([1,1,2,3,4,4,5,1],3)) #[1, 1, 2, 4, 4, 5, 1]
print(remove_kth_element([1,1,2,3,4,4,5,1],0)) #[1, 1, 2, 4, 4, 5, 1]
print(remove_kth_element([1,1,2,3,4,4,5,1],6)) #[1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],-1)) #[1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],7)) #[1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],10)) #[1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],-10)) #[1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],0.5)) #[1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],"a")) #[1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],None)) #[1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],True)) #[1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],False)) #[1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],[])) #[1, 1, 2, 3, 4, 4, 5]
print(remove_kth_element([1,1,2,3,4,4,5,1],[1,2,3,4,5,6])) #[1, 1, 2, 3, 4, 4, 5]

# Testing with the given example
print(remove_kth_element([1,1,2,3,4,4,5,1],3)) #[1, 1, 2, 3, 4, 4, 5, 1]