"""
Write a python function to calculate the product of the unique numbers in a given list.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
"""

def unique_product(lst):
    """
    >>> unique_product([10, 20, 30, 40, 20, 50, 60, 40])
    720000000
    """
    return reduce(lambda x, y: x * y, set(lst))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
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
    >>> single_number([2,2,1])
    1
    >>> single_number([4,1,2,1,2])
    4
    """
    return 2 * sum(set(nums)) - sum(nums)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
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
    >>> max_profit([7,1,5,3,6,4])
    5
    >>> max_profit([7,6,4,3,1])
    0
    """
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

if __name__ == "__main__":
    import doctest
    doctest.testmod()
/python/leetcode/easy/100_same_tree.py
"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""

def is_same_tree(p, q):
    """
    >>> is_same_tree(None, None)
    True
    >>> is_same_tree(TreeNode(1), TreeNode(1))
    True
    >>> is_same_tree(TreeNode(1), TreeNode(2))
    False
    >>> is_same_tree(TreeNode(1