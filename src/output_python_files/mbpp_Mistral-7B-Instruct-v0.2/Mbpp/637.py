"""
Write a function to check whether the given amount has no profit and no loss
assert noprofit_noloss(1500,1200)==False
"""
def noprofit_noloss(price,cost):
    """
    :param price: the price at which the item is sold
    :param cost: the cost at which the item is bought
    :return: True if there is no profit or loss, False otherwise
    """
    if price == cost:
        return True
    else:
        profit = price - cost
        if profit > 0:
            return False
        elif profit < 0:
            return False
        else:
            return True

assert noprofit_noloss(1500,1200)==False
assert noprofit_noloss(100,100)==True
assert noprofit_noloss(100,99)==False
assert noprofit_noloss(100,101)==False</s>