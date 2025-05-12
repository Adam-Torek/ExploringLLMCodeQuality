"""
Write a function to find the ratio of zeroes to non-zeroes in an array of integers.
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
"""

def zero_count(arr):
    count = 0
    for i in arr:
        if i == 0:
            count += 1
    return count / len(arr)

print(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]))/python/leetcode/easy/136_single_number.py
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return 2 * sum(set(nums)) - sum(nums)

print(single_number([4,1,2,1,2]))/python/leetcode/easy/1089_duplicate_zeros.py
"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3,0,4,5,0,0,0,0,0,0,0,0,0,0,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3,0,0,4,5,0,0,0,0,0,0,0,0,0,0]

Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""

def duplicate_zeros(arr):
    """
    :type arr: List[int]
    :rtype: None
    """
    for i in range(len(arr)):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()

print(duplicate_zeros([1,2,3,0,4,5,0,0,0,0,0,0,0,0,0,0,0]))/python/leetcode/easy/1002_find_common_characters.py
"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i] consists of lowercase letters
"""

def find_common_characters(A):
    """
    :type A: List[str]
    :rtype: List[str]
    """
    result = []
    for i in range(len(A[0])):
        char = A[0][i]
        for j in range(1, len(A)):
            if char not in A[j]:
                break
            if char in A[j]:
                if j == len(A) - 1:
                    result