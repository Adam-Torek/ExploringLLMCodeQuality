"""
Write a function to locate the right insertion point for a specified value in sorted order.
assert right_insertion([1,2,4,5],6)==4
"""
def right_insertion(arr, value):
    """
    :param arr: sorted list
    :param value: value to be inserted
    :return: index of the right insertion point
    """
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid
    return left

assert right_insertion([1,2,4,5],6) == 4
assert right_insertion([1,2,4,5],3) == 2
assert right_insertion([1,2,4,5],1) == 0
assert right_insertion([],1) == 0
assert right_insertion([1],1) == 0
assert right_insertion([1],2) == 1
assert right_insertion([1],3) == 1
assert right_insertion([1],4) == 1
assert right_insertion([1],5) == 1
assert right_insertion([1],6) == 1
assert right_insertion([1],7) == 1
assert right_insertion([1],8) == 1
assert right_insertion([1],9) == 1
assert right_insertion([1],10) == 1
assert right_insertion([1],11) == 1
assert right_insertion([1],12) == 1
assert right_insertion([1],13) == 1
assert right_insertion([1],14) == 1
assert right_insertion([1],15) == 1
assert right_insertion([1],16) == 1
assert right_insertion([1],17) == 1
assert right_insertion([1],18) == 1
assert right_insertion([1],19) == 1
assert right_insertion([1],20) == 1
assert right_insertion([1],21) == 1
assert right_insertion([1],22) == 1
assert right_insertion([1],23) == 1
assert right_insertion([1],24) == 1
assert right_insertion([1],25) == 1
assert right_insertion([1],26) == 1
assert right_insertion([1],27) == 1
assert right_insertion([1],28) == 1
assert right_insertion([1],29) == 1
assert right_insertion([1],30) == 1
assert right_insertion([1],31) == 1
assert right_insertion([1],32) == 1
assert right_insertion([1],33) == 1
assert right_insertion([1],34) == 1
assert right_insertion([1],35) == 1
assert right_insertion([1],36) == 1
assert right_insertion([1],37) == 1
assert right_insertion([1],38) == 1
assert right_insertion([1],39) == 1
assert right_insertion([1],40) == 1
assert right_insertion([1],41) == 1
assert right_insertion([1],42) == 1
assert right_insertion([1],43) == 1
assert right_insertion([1],44) == 1
assert right_insertion([1],45) == 1
assert right_insertion([1],46) == 1
assert right_insertion([1],47) == 1
assert right_insertion([1],48) == 1
assert right_insertion([1],49) == 1
assert right_insertion([1],50) == 1
assert right_insertion([1],51) == 1
assert right_insertion([1],52) == 1
assert right_insertion([1],53) == 1
assert right_insertion([1],54