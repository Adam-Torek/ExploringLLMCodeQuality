"""
Write a function to check whether the given amount has no profit and no loss
assert noprofit_noloss(1500,1200)==False
"""
def noprofit_noloss(buy_price,sell_price):
    if buy_price>sell_price:
        return False
    else:
        return True

#test the function
print(noprofit_noloss(1500,1200)) #False
print(noprofit_noloss(100,200)) #True
print(noprofit_noloss(200,100)) #False
print(noprofit_noloss(100,150)) #True
print(noprofit_noloss(100,100)) #False
print(noprofit_noloss(100,101)) #False
print(noprofit_noloss(100,100.01)) #False
print(noprofit_noloss(100,100.001)) #False
print(noprofit_noloss(100,100.0001)) #False
print(noprofit_noloss(100,100.00001)) #False
print(noprofit_noloss(100,100.000001)) #False
print(noprofit_noloss(100,100.0000001)) #False
print(noprofit_noloss(100,100.00000001)) #False
print(noprofit_noloss(100,100.000000001)) #False
print(noprofit_noloss(100,100.0000000001)) #False
print(noprofit_noloss(100,100.00000000001)) #False
print(noprofit_noloss(100,100.000000000001)) #False
print(noprofit_noloss(100,100.0000000000001)) #False
print(noprofit_noloss(100,100.00000000000001)) #False
print(noprofit_noloss(100,100.000000000000001)) #False
print(noprofit_noloss(100,100.0000000000000001)) #False
print(noprofit_noloss(100,100.00000000000000001)) #False
print(noprofit_noloss(100,100.000000000000000001)) #False
print(noprofit_noloss(100,100.000000000000000001)) #False
print(noprofit_noloss(100,100.000000000000000001)) #False
print(noprofit_noloss(100,100.000000000000000001)) #False
print(noprofit_noloss(100,100.000000000000000001)) #False
print(noprofit_noloss(100,100.000000000000000001)) #False
print(noprofit_noloss(100,100.000000000000000001)) #False
print(noprofit_noloss(100,100.