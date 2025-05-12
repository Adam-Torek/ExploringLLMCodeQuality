"""
Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
"""
def remove_kth_element(lst, k):
    """
    :param lst: list
    :param k: int
    :return: list
    """
    if k > len(lst):
        return lst
    else:
        return lst[:k] + lst[k+1:]


# assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
# assert remove_kth_element([1,1,2,3,4,4,5,1],4)==[1, 1, 2, 3, 4, 5, 1]
# assert remove_kth_element([1,1,2,3,4,4,5,1],5)==[1, 1, 2, 3, 4, 1]
# assert remove_kth_element([1,1,2,3,4,4,5,1],6)==[1, 1, 2, 3, 4, 1]