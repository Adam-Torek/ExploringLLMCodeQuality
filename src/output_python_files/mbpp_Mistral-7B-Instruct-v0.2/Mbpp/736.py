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
    assert left_insertion([1, 2, 4, 5], 3) == 2
    assert left_insertion([], 1) == 0
    assert left_insertion([], 2) == 0
    assert left_insertion([], 3) == 0
    assert left_insertion([], 4) == 0
    assert left_insertion([], 5) == 0
    assert left_insertion([], 6) == 0
    assert left_insertion([], 7) == 0
    assert left_insertion([], 8) == 0
    assert left_insertion([], 9) == 0
    assert left_insertion([], 10) == 0
    assert left_insertion([], 11) == 0
    assert left_insertion([], 12) == 0
    assert left_insertion([], 13) == 0
    assert left_insertion([], 14) == 0
    assert left_insertion([], 15) == 0
    assert left_insertion([], 16) == 0
    assert left_insertion([], 17) == 0
    assert left_insertion([], 18) == 0
    assert left_insertion([], 19) == 0
    assert left_insertion([], 20) == 0
    assert left_insertion([], 21) == 0
    assert left_insertion([], 22) == 0
    assert left_insertion([], 23) == 0
    assert left_insertion([], 24) == 0
    assert left_insertion([], 25) == 0
    assert left_insertion([], 26) == 0
    assert left_insertion([], 27) == 0
    assert left_insertion([], 28) == 0
    assert left_insertion([], 29) == 0
    assert left_insertion([], 30) == 0
    assert left_insertion([], 31) == 0
    assert left_insertion([], 32) == 0
    assert left_insertion([], 33) == 0
    assert left_insertion([], 34) == 0
    assert left_insertion([], 35) == 0
    assert left_insertion([], 36) == 0
    assert left_insertion([], 37) == 0
    assert left_insertion([], 38) == 0
    assert left_insertion([], 39) == 0
    assert left_insertion([], 40) == 0
    assert left_insertion([], 41) == 0
    assert left_insertion([], 42) == 0
    assert left_insertion([], 43) == 0
    assert left_insertion([], 44) == 0
    assert left_insertion([], 45) == 0
    assert left_insertion([], 46) == 0
    assert left_insertion([],