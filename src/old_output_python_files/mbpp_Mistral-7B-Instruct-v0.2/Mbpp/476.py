"""
Write a python function to find the sum of the largest and smallest value in a given array.
assert big_sum([1,2,3]) == 4
"""
def big_sum(arr):
    """
    Function to find the sum of the largest and smallest value in a given array
    :param arr: list
    :return: int
    """
    if len(arr) == 0:
        return None
    min_val = min(arr)
    max_val = max(arr)
    return min_val + max_val

if __name__ == "__main__":
    assert big_sum([1,2,3]) == 4
    assert big_sum([-1,0,1]) == 0
    assert big_sum([-10, 10]) == 0
    assert big_sum([]) == None
    assert big_sum([1]) == 1
    assert big_sum([1,1,1]) == 2
    assert big_sum([1,2,3,4]) == 7
    assert big_sum([5,5,5,5]) == 20
    assert big_sum([-5,-5,-5,-5]) == -10
    assert big_sum([-5,5]) == 0
    assert big_sum([5,-5]) == 0
    assert big_sum([5,5,-5,-5]) == 0
    assert big_sum([5,5,5,-5]) == 10
    assert big_sum([5,5,5,5,5]) == 25
    assert big_sum([5,5,5,5,5,5]) == 35
    assert big_sum([5,5,5,5,5,5,5]) == 45
    assert big_sum([5,5,5,5,5,5,5,5]) == 55
    assert big_sum([5,5,5,5,5,5,5,5,5]) == 65
    assert big_sum([5,5,5,5,5,5,5,5,5,5]) == 75
    assert big_sum([5,5,5,5,5,5,5,5,5,5,5]) == 85
    assert big_sum([5,5,5,5,5,5,5,5,5,5,5,5]) == 95
    assert big_sum([5,5,5,5,5,5,5,5,5,5,5,5,5]) == 105
    assert big_sum([5,5,5,5,5,5,5,5,5,5,5,5,5,5]) == 115
    assert big_sum([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]) == 125
    assert big_sum([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]) == 135
    assert big_sum([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]) == 145
    assert big_sum([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]) == 155
    assert big_sum([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]) == 165
    assert big_sum([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]) == 175
    assert big_sum([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]) == 185
    assert big_sum([5,5,5,5,5,5,5,5,5,5,5,5,5,5,