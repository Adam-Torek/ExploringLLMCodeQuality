"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""

def sum_Of_Subarray_Prod(lst):
    """
    :type lst: List[int]
    :rtype: int
    """
    n = len(lst)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            ans += lst[i]*lst[j]
    return ans


if __name__ == '__main__':
    print(sum_Of_Subarray_Prod([1,2,3]))