"""
Write a function to locate the left insertion point for a specified value in sorted order. https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-24.php
assert left_insertion([1,2,4,5],6)==4
"""
def left_insertion(arr, value):
    """
    :param arr: sorted list
    :param value: value to insert
    :return: index of the left insertion point
    """
    index = 0
    while index < len(arr) and value > arr[index]:
        index += 1
    return index

if __name__ == "__main__":
    assert left_insertion([1, 2, 4, 5], 6) == 4
    assert left_insertion([1, 2, 4, 5], 1) == 0
    assert left_insertion([1, 2, 4, 5], 5) == 3
    assert left_insertion([], 5) == 0
    assert left_insertion([], 1) == 0
    assert left_insertion([1], 1) == 0
    assert left_insertion([1], 2) == 1
    assert left_insertion([1, 2], 1) == 0
    assert left_insertion([1, 2], 2) == 1
    assert left_insertion([1, 2], 3) == 2
    assert left_insertion([1, 2], 4) == 3
    assert left_insertion([1, 2], 5) == 4
    assert left_insertion([1, 2], 6) == 5
    assert left_insertion([1, 2], 7) == 6
    assert left_insertion([1, 2], 8) == 7
    assert left_insertion([1, 2], 9) == 8
    assert left_insertion([1, 2], 10) == 9
    assert left_insertion([1, 2], 11) == 10
    assert left_insertion([1, 2], 12) == 11
    assert left_insertion([1, 2], 13) == 12
    assert left_insertion([1, 2], 14) == 13
    assert left_insertion([1, 2], 15) == 14
    assert left_insertion([1, 2], 16) == 15
    assert left_insertion([1, 2], 17) == 16
    assert left_insertion([1, 2], 18) == 17
    assert left_insertion([1, 2], 19) == 18
    assert left_insertion([1, 2], 20) == 19
    assert left_insertion([1, 2], 21) == 20
    assert left_insertion([1, 2], 22) == 21
    assert left_insertion([1, 2], 23) == 22
    assert left_insertion([1, 2], 24) == 23
    assert left_insertion([1, 2], 25) == 24
    assert left_insertion([1, 2], 26) == 25
    assert left_insertion([1, 2], 27) == 26
    assert left_insertion([1, 2], 28) == 27
    assert left_insertion([1, 2], 29) == 28
    assert left_insertion([1, 2], 30) == 29
    assert left_insertion([1, 2], 31) == 30
    assert left_insertion([1, 2], 32) == 31
    assert left_insertion([1, 2], 33) == 32
    assert left_insertion([1, 2], 34) == 33
    assert left_insertion([1, 2], 35) == 34