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
    if k > len(lst) or k < 1:
        return lst
    else:
        return lst[:k-1] + lst[k+1:]