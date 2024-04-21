def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2],..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """

def right_shift(arr, n):
    """Perform n right shift operations on the given array"""
    for i in range(n):
        last_element = arr[-1]
        for j in range(len(arr)-1, 0, -1):
            arr[j] = arr[j-1]
        arr[0] = last_element

def is_sorted(arr):
    """Check if the given array is sorted in non-decreasing order"""
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def move_one_ball_helper(arr):
    """Helper function to move one ball"""
    if len(arr) == 0:
        return True
    if is_sorted(arr):
        return True

    right_shift(arr, 1)
    return move_one_ball_helper(arr)

def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2],..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """
    return move_one_ball_helper(arr)

# Test cases
print(move_one_ball([3, 4, 5, 1, 2]))  # True
print(move_one_ball([3, 5, 4, 1, 2]))  # False<|endoftext|>