"""
Write a function to check whether the given amount has no profit and no loss
assert noprofit_noloss(1500,1200)==False
"""
def noprofit_noloss(amount,cost):
    """
    :param amount: the price of the item
    :param cost: the cost of the item
    :return: True if there is no profit or loss, False otherwise
    """
    profit = amount - cost
    return profit <= 0 and profit >= 0

assert noprofit_noloss(1500,1200)==False
assert noprofit_noloss(100,100)==True
assert noprofit_noloss(50,50)==True
assert noprofit_noloss(100,95)==False
assert noprofit_noloss(100,105)==False