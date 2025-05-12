"""
Write a function to find the maximum difference between available pairs in the given tuple list.
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""

def max_difference(list_of_tuples):
    """
    :param list_of_tuples: list of tuples
    :return: max difference
    """
    max_diff = 0
    for i in range(len(list_of_tuples)):
        for j in range(i+1, len(list_of_tuples)):
            if abs(list_of_tuples[i][0] - list_of_tuples[j][0]) > max_diff:
                max_diff = abs(list_of_tuples[i][0] - list_of_tuples[j][0])
    return max_diff

print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]))
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
    :param nums: list of integers
    :return: single number
    """
    return 2 * sum(set(nums)) - sum(nums)

print(single_number([2,2,1]))
print(single_number([4,1,2,1,2]))
/python/leetcode/easy/121_best_time_to_buy_and_sell_stock.py
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

def max_profit(prices):
    """
    :param prices: list of integers
    :return: max profit
    """
    if len(prices) == 0:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

print(max_profit([7,1,5,3,6,4]))
print(max_profit([7,6,4,3,1]))
/python/leetcode/easy/104_maximum_depth_of_binary_tree.py
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_depth(root):
    """
    :param root: root of the tree
    :return: max depth
    """
    if root is None:
        return 0
    return max(max_depth(root.left), max_depth(root.