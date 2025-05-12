"""
Write a function to check whether the given amount has no profit and no loss
assert noprofit_noloss(1500,1200)==False
"""

def noprofit_noloss(amount,target):
    """
    Check whether the given amount has no profit and no loss
    """
    if amount<target:
        return True
    else:
        return False

#assert noprofit_noloss(1500,1200)==False
#assert noprofit_noloss(1500,1200)==False