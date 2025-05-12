"""
Write a python function to find the maximum difference between any two elements in a given array.
assert max_Abs_Diff((2,1,5,3)) == 4
"""
def max_Abs_Diff(arr):
    """
    Function to find the maximum absolute difference between any two elements in a given array
    :param arr: list of integers
    :return: int
    """
    if len(arr) < 2:
        return None
    min_val = min(arr)
    max_val = max(arr)
    return max_val - min_val

if __name__ == "__main__":
    assert max_Abs_Diff((2,1,5,3)) == 4
    assert max_Abs_Diff((-1,1,5,3)) == 6
    assert max_Abs_Diff((-1,1,5,3,2)) == 6
    assert max_Abs_Diff((-1,1,5,3,2,4)) == 7
    assert max_Abs_Diff((-1,1,5,3,2,4,6)) == 7
    assert max_Abs_Diff((-1,1,5,3,2,4,6,7)) == 8
    assert max_Abs_Diff((-1,1,5,3,2,4,6,7,8)) == 9
    assert max_Abs_Diff((-1,1,5,3,2,4,6,7,8,9)) == 10
    assert max_Abs_Diff((-1,1,5,3,2,4,6,7,8,9,10)) == 11
    assert max_Abs_Diff((-1,1,5,3,2,4,6,7,8,9,10,11)) == 12
    assert max_Abs_Diff((-1,1,5,3,2,4,6,7,8,9,10,11,12)) == 13
    assert max_Abs_Diff((-1,1,5,3,2,4,6,7,8,9,10,11,12,13)) == 14
    assert max_Abs_Diff((-1,1,5,3,2,4,6,7,8,9,10,11,12,13,14)) == 15
    assert max_Abs_Diff((-1,1,5,3,2,4,6,7,8,9,10,11,12,13,14,15)) == 16
    assert max_Abs_Diff((-1,1,5,3,2,4,6,7,8,9,10,11,12,13,14,15,16)) == 17
    assert max_Abs_Diff((-1,1,5,3,2,4,6,7,8,9,10,11,12,13,14,15,16,17)) == 18
    assert max_Abs_Diff((-1,1,5,3,2,4,6,7,8,9,10,11,12,13,14,15,16,17,18)) == 19
    assert max_Abs_Diff((-1,1,5,3,2,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19)) == 20
    assert max_Abs_Diff((-1,1,5,3,2,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)) == 21
    assert max_Abs_Diff((-1,1,5,3,2,4,6,7,8,9,10,11,12,13,14,15,16,17,