"""
Write a function to check if the given array represents min heap or not. https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
"""


def check_min_heap(arr):
    """
    Check if the given array represents min heap or not.
    :param arr: array to check
    :return: True if the array represents min heap, False otherwise
    """
    if len(arr) == 0:
        return True
    if len(arr) == 1:
        return True
    if len(arr) == 2:
        return True
    if arr[0] > arr[1]:
        return False
    if arr[0] > arr[2]:
        return False
    if arr[1] > arr[2]:
        return False
    if arr[1] > arr[3]:
        return False
    if arr[2] > arr[3]:
        return False
    if arr[2] > arr[4]:
        return False
    if arr[3] > arr[4]:
        return False
    if arr[3] > arr[5]:
        return False
    if arr[4] > arr[5]:
        return False
    if arr[4] > arr[6]:
        return False
    if arr[5] > arr[6]:
        return False
    if arr[5] > arr[7]:
        return False
    if arr[6] > arr[7]:
        return False
    if arr[6] > arr[8]:
        return False
    if arr[7] > arr[8]:
        return False
    if arr[7] > arr[9]:
        return False
    if arr[8] > arr[9]:
        return False
    if arr[8] > arr[10]:
        return False
    if arr[9] > arr[10]:
        return False
    if arr[9] > arr[11]:
        return False
    if arr[10] > arr[11]:
        return False
    if arr[10] > arr[12]:
        return False
    if arr[11] > arr[12]:
        return False
    if arr[11] > arr[13]:
        return False
    if arr[12] > arr[13]:
        return False
    if arr[12] > arr[14]:
        return False
    if arr[13] > arr[14]:
        return False
    if arr[13] > arr[15]:
        return False
    if arr[14] > arr[15]:
        return False
    if arr[14] > arr[16]:
        return False
    if arr[15] > arr[16]:
        return False
    if arr[15] > arr[17]:
        return False
    if arr[16] > arr[17]:
        return False
    if arr[16] > arr[18]:
        return False
    if arr[17] > arr[18]:
        return False
    if arr[17] > arr[19]:
        return False
    if arr[18] > arr[19]:
        return False
    if arr[18] > arr[20]:
        return False
    if arr[19] > arr[20]:
        return False
    if arr[19] > arr[21]:
        return False
    if arr[20] > arr[21]:
        return False
    if arr[20] > arr[22]:
        return False
    if arr[21] > arr[22]:
        return False
    if arr[21] > arr[23]:
        return False
    if arr[22] > arr[23]:
        return False
    if arr[22] > arr[24]:
        return False
    if arr[