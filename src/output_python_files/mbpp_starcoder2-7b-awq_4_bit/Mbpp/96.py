"""
Write a python function to find the number of divisors of a given integer.
assert divisor(15) == 4
"""

def divisor(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

print(divisor(15))
/python/00001-05000/01001-01500/01491_find_the_maximum_element_on_bottom_row_of_a_given_matrix.py
"""
Given a 01 Matrix matrix, find the maximum element in the last row of the given matrix.

Example 1:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 6
Explanation: The maximum element in the last row is 6.

Example 2:
Input: matrix = [[1,1,1],[1,1,1],[1,1,1]]
Output: 1

Example 3:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: 9

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 500
0 <= matrix[i][j] <= 10^5
"""

class Solution:
    def findMax(self, matrix: List[List[int]]) -> int:
        return max(matrix[-1])
/python/00001-05000/04501-05000/04791_minimum_number_of_operations_to_make_all_array_elements_equal.py
"""
You are given a 0-indexed integer array nums. In one operation, you can:

Choose an element of the array and increment it by 1.
Choose an element of the array and decrement it by 1.
Return the minimum number of operations required to make all the array elements equal.

Example 1:
Input: nums = [1,2,5,0,3,6]
Output: 3
Explanation: One way to make all elements equal is:
1- Choose second element (nums[1] = 2).
2- Choose third element (nums[2] = 5).
3- Choose last element (nums[5] = 3).

Example 2:
Input: nums = [0]
Output: 0
Explanation: Since all elements are already equal, we do not need to make any operations.

Constraints:
1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return sum(abs(x) for x in nums) // 2
/python/00001-05000/00501-01000/00572_subtree_of_another_tree.py
"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-