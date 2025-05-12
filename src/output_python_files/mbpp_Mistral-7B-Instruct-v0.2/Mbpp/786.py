"""
Write a function to locate the right insertion point for a specified value in sorted order.
assert right_insertion([1,2,4,5],6)==4
"""
def right_insertion(arr, value):
    """
    :param arr: sorted list
    :param value: value to insert
    :return: index of the right insertion point
    """
    index = len(arr)
    for i in range(len(arr)):
        if arr[i] >= value:
            index = i
            break
    return index

assert right_insertion([1,2,4,5],6) == 4
assert right_insertion([], 1) == 0
assert right_insertion([1], 1) == 0
assert right_insertion([1,2], 1) == 1
assert right_insertion([1,2], 3) == 2
assert right_insertion([1,2,3,4], 5) == 4
assert right_insertion([1,2,3,4], 6) == 5
assert right_insertion([1,2,3,4], 7) == 5
assert right_insertion([1,2,3,4], 10) == 5
assert right_insertion([1,2,3,4], 100) == 6
assert right_insertion([1,2,3,4], -1) == 0
assert right_insertion([1,2,3,4], -5) == 0
assert right_insertion([], -1) == 0
assert right_insertion([], -5) == 0
assert right_insertion([], 1) == 0
assert right_insertion([], 10) == 0
assert right_insertion([], 100) == 0
assert right_insertion([], -100) == 0
assert right_insertion([], -1000) == 0
assert right_insertion([], -float('inf')) == 0
assert right_insertion([], float('inf')) == 0
assert right_insertion([], -float('nan')) == 0
assert right_insertion([], float('nan')) == 0
assert right_insertion([], complex(0,0)) == 0
assert right_insertion([], complex(0,1)) == 0
assert right_insertion([], complex(1,0)) == 0
assert right_insertion([], complex(1,1)) == 0
assert right_insertion([], complex(-1,0)) == 0
assert right_insertion([], complex(-1,1)) == 0
assert right_insertion([], complex(1,2)) == 0
assert right_insertion([], complex(-1,2)) == 0
assert right_insertion([], complex(1,3)) == 0
assert right_insertion([], complex(-1,3)) == 0
assert right_insertion([], complex(1,4)) == 0
assert right_insertion([], complex(-1,4)) == 0
assert right_insertion([], complex(1,5)) == 0
assert right_insertion([], complex(-1,5)) == 0
assert right_insertion([], complex(1,6)) == 0
assert right_insertion([], complex(-1,6)) == 0
assert right_insertion([], complex(1,7)) == 0
assert right_insertion([], complex(-1,7)) == 0
assert right_insertion([], complex(1,8)) == 0
assert right_insertion([], complex(-1,8)) == 0
assert right_insertion([], complex(1,9)) == 0
assert right_insertion([], complex(-1,9)) == 0
assert right_insertion([], complex(1,10)) == 0
assert right_insertion([], complex(-1,10)) == 0
assert right_insertion([], complex(1,11)) == 0
assert right_insertion([], complex(-1,11)) == 0
assert right_insertion([], complex(1,12)) == 0
assert right_insertion([], complex(-1,12)) == 0
assert right_