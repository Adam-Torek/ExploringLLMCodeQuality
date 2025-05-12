"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""

def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

print(decimal_to_binary(8))
/python/leetcode/easy/136_single_number.py
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

def single_number(nums):
    single = 0
    for num in nums:
        single ^= num
    return single

print(single_number([4,1,2,1,2]))
/python/leetcode/easy/100_same_tree.py
"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val!= q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(is_same_tree(p, q))
/python/leetcode/easy/121_best_time_to_buy_and_sell_stock.py
"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
"""

def max_profit(prices):
    if len(prices) < 2:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit

print(max_profit([7,1,5,3,6,4]))
/python/leetcode/easy/108_convert_sorted_array_to_binary_search_tree.py
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    return root

nums = [1,2,3,4,5,6,7]
root = sorted_array_to_bst(nums)
print(root.val)
print(root.left.val)
print(root.right.val)
/python/leetcode/easy/119_pascals_triangle_ii.py
"""
Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3,
Return [1,3,3,1].
Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

def get_row(rowIndex):
    row = [1]
    for i in range(rowIndex):
        row = [x + y for x, y in zip