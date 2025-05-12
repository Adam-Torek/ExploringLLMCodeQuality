from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    max_so_far = float('-inf')
    for num in numbers:
        max_so_far = max(num, max_so_far)
        result.append(max_so_far)
    return result

def max_profit(prices: List[int]) -> int:
    """
    Given a list of prices, find the maximum profit that can be made from buying and selling a stock once.
    >>> max_profit([9, 11, 8, 5, 7, 12, 14, 16])
    7
    """
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

def max_profit_dp(prices: List[int]) -> int:
    """
    Given a list of prices, find the maximum profit that can be made from buying and selling a stock once.
    >>> max_profit_dp([9, 11, 8, 5, 7, 12, 14, 16])
    7
    """
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

def max_profit_with_k_transactions(prices: List[int], k: int) -> int:
    """
    Given a list of prices and a number of transactions k, find the maximum profit that can be made from buying
    and selling a stock k times.
    >>> max_profit_with_k_transactions([9, 11, 8, 5, 7, 12, 14, 16], 2)
    7
    """
    if not prices or k == 0:
        return 0
    if k >= len(prices) // 2:
        return max_profit(prices)
    profits = [0] * k
    for i in range(1, len(prices)):
        for j in range(k):
            if j == 0:
                profits[j] = max(profits[j], prices[i] - prices[i-1])
            else:
                profits[j] = max(profits[j], prices[i] - prices[i-1] + profits[j-1])
    return max(profits)

def max_profit_with_k_transactions_dp(prices: List[int], k: int) -> int:
    """
    Given a list of prices and a number of transactions k, find the maximum profit that can be made from buying
    and selling a stock k times.
    >>> max_profit_with_k_transactions_dp([9, 11, 8, 5, 7, 12, 14, 16], 2)
    7
    """
    if not prices or k == 0:
        return 0
    if k >= len(prices) // 2:
        return max_profit(prices)
    profits = [0