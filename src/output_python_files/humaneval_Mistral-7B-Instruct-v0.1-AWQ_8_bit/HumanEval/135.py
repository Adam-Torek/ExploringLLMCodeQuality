def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) == 1:
        return -1
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return i
    return -1


def can_arrange_test(arr):
    """Test the can_arrange function with the given array."""
    print(can_arrange(arr))


if __name__ == '__main__':
    can_arrange_test([1,2,4,3,5])
    can_arrange_test([1,2,3])
    can_arrange_test([1,2,3,4,5])
    can_arrange_test([1,2,3,4,5,6])
    can_arrange_test([1,2,3,4,5,6,7])
    can_arrange_test([1,2,3,4,5,6,7,8])
    can_arrange_test([1,2,3,4,5,6,7,8,9])
    can_arrange_test([1,2,3,4,5,6,7,8,9,10])
    can_arrange_test([1,2,3,4,5,6,7,8,9,10,11])
    can_arrange_test([1,2,3,4,5,6,7,8,9,10,11,12])
    can_arrange_test([1,2,3,4,5,6,7,8,9,10,11,12,13])
    can_arrange_test([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    can_arrange_test([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    can_arrange_test([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    can_arrange_test([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
    can_arrange_test([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
    can_arrange_test([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
    can_arrange_test([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    can_arrange_test([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])
    can_arrange_test([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])
    can_arrange_test([1,2,3,4,5,6,7,8,9,10,11,12,13