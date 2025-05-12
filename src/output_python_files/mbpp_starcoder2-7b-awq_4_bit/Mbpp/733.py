"""
Write a function to find the index of the first occurrence of a given number in a sorted array.
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
"""

def find_first_occurrence(arr, num):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        if arr[0] == num:
            return 0
        else:
            return -1
    if arr[0] == num:
        return 0
    if arr[len(arr) - 1] == num:
        return len(arr) - 1
    if arr[len(arr) - 1] < num:
        return -1
    if arr[0] > num:
        return -1
    if arr[len(arr) // 2] == num:
        return len(arr) // 2
    if arr[len(arr) // 2] > num:
        return find_first_occurrence(arr[:len(arr) // 2], num)
    if arr[len(arr) // 2] < num:
        return find_first_occurrence(arr[len(arr) // 2:], num)


print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))
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

def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return 2 * sum(set(nums)) - sum(nums)

print(single_number([4,1,2,1,2]))
/python/leetcode/easy/108_convert_sorted_array_to_binary_search_tree.py
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

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        if len(nums) == 2:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            return root
        if len(nums) == 3:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            root.right = TreeNode(nums[2])
            return root
        root = TreeNode(nums[len(nums) // 2])
        root.left = self.sortedArrayToBST(nums[:len(nums) // 2])
        root.right = self.sortedArrayToBST(nums[len(nums) // 2 + 1:])
        return root

def print_tree(root):
    if root is None:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

s = Solution()
print_tree(s.sortedArrayToBST([-10,-3,0,5,9]))
/python/leetcode/easy/104_maximum_depth_of