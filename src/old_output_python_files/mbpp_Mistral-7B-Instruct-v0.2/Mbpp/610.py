"""
Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
"""
def remove_kth_element(input_list, k):
    """
    Function to remove the k'th element from the input list
    :param input_list: list to remove element from
    :param k: index of the element to remove
    :return: list with the k'th element removed
    """
    if len(input_list) < k:
        raise IndexError("List index out of range")
    return input_list[:k] + input_list[k+1:]

if __name__ == "__main__":
    assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
    assert remove_kth_element([],3)==[]
    assert remove_kth_element([1],3)==[]
    assert remove_kth_element([1,1,2,3,4,4,5,1],0)==[1, 1, 2, 3, 4, 4, 5]
    assert remove_kth_element([1,1,2,3,4,4,5,1],7)==[1, 1, 2, 3, 4, 4, 5]
    assert remove_kth_element([1,1,2,3,4,4,5,1],8)==[1, 1, 2, 3, 4, 4, 5, 1]
    assert remove_kth_element([1,1,2,3,4,4,5,1],-1)==[1, 1, 2, 3, 4, 4, 5, 1]
    assert remove_kth_element([1,1,2,3,4,4,5,1],9)==[1, 1, 2, 3, 4, 4, 5, 1]
    assert remove_kth_element([1,1,2,3,4,4,5,1],10)==[1, 1, 2, 3, 4, 4, 5, 1]
    assert remove_kth_element([1,1,2,3,4,4,5,1],11)==[1, 1, 2, 3, 4, 4, 5, 1]
    assert remove_kth_element([1,1,2,3,4,4,5,1],12)==[1, 1, 2, 3, 4, 4, 5, 1]
    assert remove_kth_element([1,1,2,3,4,4,5,1],13)==[1, 1, 2, 3, 4, 4, 5, 1]
    assert remove_kth_element([1,1,2,3,4,4,5,1],14)==[1, 1, 2, 3, 4, 4, 5, 1]
    assert remove_kth_element([1,1,2,3,4,4,5,1],15)==[1, 1, 2, 3, 4, 4, 5, 1]
    assert remove_kth_element([1,1,2,3,4,4,5,1],16)==[1, 1, 2, 3, 4, 4, 5, 1]
    assert remove_kth_element([1,1,2,3,4,4,5,1],17)==[1, 1, 2, 3, 4, 4, 5, 1]
    assert remove_kth_element([1,1,2,3,4,4,5,1],18)==[1, 1, 2, 3, 4,