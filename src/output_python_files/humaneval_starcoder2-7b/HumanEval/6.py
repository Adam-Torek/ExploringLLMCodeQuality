from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
/python/leetcode/easy/136_single_number.py
from typing import List


def single_number(nums: List[int]) -> int:
    """ Given a non-empty array of integers, every element appears twice except for one. Find that single one.
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

    >>> single_number([2, 2, 1])
    1
    >>> single_number([4, 1, 2, 1, 2])
    4
    """
    return 2 * sum(set(nums)) - sum(nums)
/python/leetcode/easy/125_valid_palindrome.py
from typing import List


def is_palindrome(s: str) -> bool:
    """ Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
    Note: For the purpose of this problem, we define empty string as valid palindrome.

    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("race a car")
    False
    """
    s = s.lower()
    s = ''.join(c for c in s if c.isalnum())
    return s == s[::-1]
/python/leetcode/easy/122_best_time_to_buy_and_sell_stock_ii.py
from typing import List


def max_profit(prices: List[int]) -> int:
    """ Say you have an array for which the ith element is the price of a given stock on day i.
    Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
    Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

    >>> max_profit([7, 1, 5, 3, 6, 4])
    7
    >>> max_profit([1, 2, 3, 4, 5])
    4
    >>> max_profit([7, 6, 4, 3, 1])
    0
    """
    return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
/python/leetcode/easy/121_best_time_to_buy_and_sell_stock.py
from typing import List


def max_profit(prices: List[int]) -> int:
    """ Say you have an array for which the ith element is the price of a given stock on day i.
    If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
    Note that you cannot sell a stock before you buy one.

    >>> max_profit([7, 1, 5, 3, 6, 4])
    5
    >>> max_profit([7, 6, 4, 3, 1])
    0
    """
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit
/python/leetcode/easy/13_roman_to_integer.py
def roman_to_int(s: str) -> int:
    """ Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number