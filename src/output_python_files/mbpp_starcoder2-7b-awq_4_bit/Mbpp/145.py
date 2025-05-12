"""
Write a python function to find the maximum difference between any two elements in a given array.
assert max_Abs_Diff((2,1,5,3)) == 4
"""

def max_Abs_Diff(arr):
    max_diff = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            diff = abs(arr[i] - arr[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

print(max_Abs_Diff((2,1,5,3)))
/python/leetcode/easy/136_single_number.py
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

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return 2 * sum(set(nums)) - sum(nums)

print(singleNumber([4,1,2,1,2]))
/python/leetcode/easy/125_valid_palindrome.py
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.lower()
    s = ''.join(filter(str.isalnum, s))
    return s == s[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))
/python/leetcode/easy/108_convert_sorted_array_to_bst.py
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root

print(sortedArrayToBST([-10,-3,0,5,9]))
/python/leetcode/easy/118_pascals_triangle.py
"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1,