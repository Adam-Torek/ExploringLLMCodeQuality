"""
Write a python function to check whether a list is sublist of another or not.
assert is_Sub_Array([1,4,3,5],[1,2]) == False
"""
def is_Sub_Array(arr1,arr2):
    """
    Function to check whether arr1 is sublist of arr2 or not
    :param arr1: list
    :param arr2: list
    :return: boolean value
    """
    if len(arr1) > len(arr2):
        return False
    for i in range(len(arr2)):
        if arr1 == arr2[i:i+len(arr1)]:
            return True
    return False

assert is_Sub_Array([1,4,3,5],[1,2]) == False
assert is_Sub_Array([1,4,3,5],[1,4,3,5,1,4,3,5]) == True
assert is_Sub_Array([1,4,3],[1,4,3,5]) == True
assert is_Sub_Array([1,4,3],[1,2,3,4,5]) == False