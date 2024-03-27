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
    max_diff = abs(min(arr) - max(arr))
    return max_diff

if __name__ == "__main__":
    assert max_Abs_Diff((2,1,5,3)) == 4
    assert max_Abs_Diff((-1,1,5,3)) == 6
    assert max_Abs_Diff((1,2,3,4)) == 3
    assert max_Abs_Diff((1,2,3,4,5)) == 5
    assert max_Abs_Diff((1,2,3,4,5,6)) == 5
    assert max_Abs_Diff((1,2,3,4,5,6,7)) == 6
    assert max_Abs_Diff((1,2,3,4,5,6,7,8)) == 7
    assert max_Abs_Diff((1,2,3,4,5,6,7,8,9)) == 8
    assert max_Abs_Diff((1,2,3,4,5,6,7,8,9,10)) == 9
    assert max_Abs_Diff((1,2,3,4,5,6,7,8,9,10,11)) == 10
    assert max_Abs_Diff((1,2,3,4,5,6,7,8,9,10,11,12)) == 11
    assert max_Abs_Diff((1,2,3,4,5,6,7,8,9,10,11,12,13)) == 12
    assert max_Abs_Diff((1,2,3,4,5,6,7,8,9,10,11,12,13,14)) == 13
    assert max_Abs_Diff((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)) == 14
    assert max_Abs_Diff((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)) == 15
    assert max_Abs_Diff((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)) == 16
    assert max_Abs_Diff((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)) == 17
    assert max_Abs_Diff((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)) == 18
    assert max_Abs_Diff((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)) == 19
    assert max_Abs_Diff((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)) == 20
    assert max_Abs_Diff((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)) == 21
    assert max_Abs_Diff((1,2,3,4,5,6,7,8,9,10,11,