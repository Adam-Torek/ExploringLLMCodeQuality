"""
Write a function that takes two lists and returns true if they have at least one common element.
assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
"""
def common_element(list1, list2):
    """
    :param list1: list
    :param list2: list
    :return: bool
    """
    return bool(list(set(list1) & set(list2)))

if __name__ == "__main__":
    assert common_element([1,2,3,4,5], [5,6,7,8,9]) == True
    assert common_element([1,2,3,4,5], [1,2,3,4,6]) == True
    assert common_element([1,2,3,4,5], [1,2,3,4,5]) == True
    assert common_element([1,2,3,4,5], [1,2,3,4,5,6]) == False
    assert common_element([], []) == True
    assert common_element([], [1]) == False
    assert common_element([1], []) == False
    assert common_element([], []) == True
    assert common_element([1,1], [1,1]) == True
    assert common_element([1,1], [1,2]) == False
    assert common_element([1,1], [1,1,1]) == True
    assert common_element([1,1], [1,1,1,1]) == True
    assert common_element([1,1], [1,1,1,1,1]) == True
    assert common_element([1,1], [1,1,1,1,1,1]) == True
    assert common_element([1,1], [1,1,1,1,1,1,1]) == True
    assert common_element([1,1], [1,1,1,1,1,1,1,1]) == True
    assert common_element([1,1], [1,1,1,1,1,1,1,1,1]) == True
    assert common_element([1,1], [1,1,1,1,1,1,1,1,1,1]) == True
    assert common_element([1,1], [1,1,1,1,1,1,1,1,1,1,1]) == True
    assert common_element([1,1], [1,1,1,1,1,1,1,1,1,1,1,1]) == True
    assert common_element([1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1]) == True
    assert common_element([1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == True
    assert common_element([1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == True
    assert common_element([1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == True
    assert common_element([1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == True
    assert common_element([1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == True
    assert common_element([1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == True
    assert common_element([1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == True
    assert common_element([1,1], [1,1,1,1,1,1,1,1,