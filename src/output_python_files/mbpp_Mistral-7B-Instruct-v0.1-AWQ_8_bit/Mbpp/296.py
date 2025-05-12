"""
Write a python function to count inversions in an array.
assert get_Inv_Count([1,20,6,4,5]) == 5
"""

def get_Inv_Count(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                count += 1
    return count


if __name__ == '__main__':
    print(get_Inv_Count([1,20,6,4,5]))