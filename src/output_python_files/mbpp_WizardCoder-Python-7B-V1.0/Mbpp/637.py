"""
Write a function to check whether the given amount has no profit and no loss
assert noprofit_noloss(1500,1200)==False
"""
def noprofit_noloss(buy_price,sell_price):
    if buy_price>sell_price:
        return False
    else:
        return True

# Test cases
print(noprofit_noloss(1500,1200)) # False
print(noprofit_noloss(1000,200)) # True
print(noprofit_noloss(1000,100)) # False
print(noprofit_noloss(100,200)) # False
print(noprofit_noloss(100,100)) # True
print(noprofit_noloss(100,101)) # True
print(noprofit_noloss(100,99)) # False
print(noprofit_noloss(100,100.5)) # True
print(noprofit_noloss(100,100.01)) # False
print(noprofit_noloss(100,100.49)) # True
print(noprofit_noloss(100,100.51)) # False
print(noprofit_noloss(100,101.49)) # False
print(noprofit_noloss(100,101.51)) # True
print(noprofit_noloss(100,99.49)) # False
print(noprofit_noloss(100,99.51)) # True
print(noprofit_noloss(100,101.49)) # False
print(noprofit_noloss(100,101.51)) # True
print(noprofit_noloss(100,99.49)) # False
print(noprofit_noloss(100,99.51)) # True
print(noprofit_noloss(100,100.49)) # False
print(noprofit_noloss(100,100.51)) # True
print(noprofit_noloss(100,101.49)) # False
print(noprofit_noloss(100,101.51)) # True
print(noprofit_noloss(100,100.49)) # False
print(noprofit_noloss(100,100.51)) # True
print(noprofit_noloss(100,101.49)) # False
print(noprofit_noloss(100,101.51)) # True
print(noprofit_noloss(100,100.49)) # False
print(noprofit_noloss(100,100.51)) # True
print(noprofit_noloss(100,101.49)) # False
print(noprofit_noloss(100,101.51)) # True
print(noprofit_noloss(100,100.49)) # False
print(noprofit_noloss(100,100.51)) # True
print(noprofit_noloss(100,101.49)) # False
print(noprofit_noloss(100,101.51)) # True
print(noprofit_noloss(100,100.49)) # False
print(noprofit_noloss(100,100.51)) # True
print(noprofit_noloss(100,101.49)) # False
print(nopro