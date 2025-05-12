"""
Write a function to check whether the given amount has no profit and no loss
assert noprofit_noloss(1500,1200)==False
"""
def noprofit_noloss(amount,fee):
    if amount <= fee:
        return True
    else:
        return False

# Test cases
print(noprofit_noloss(1500,1200)) # False
print(noprofit_noloss(1000,0)) # True
print(noprofit_noloss(1000,100)) # True<|endoftext|>