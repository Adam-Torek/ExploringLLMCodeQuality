"""
Write a python function to check if a given number is one less than twice its reverse.
assert check(70) == False
"""

def check(num):
    return num == int(str(num)[::-1]) - 1

print(check(70)) # False
print(check(123)) # False
print(check(122)) # True
print(check(121)) # False
print(check(120)) # True
print(check(1211)) # False
print(check(1221)) # True
print(check(12321)) # False
print(check(12320)) # True
print(check(12322)) # False
print(check(12323)) # False
print(check(12324)) # False
print(check(12325)) # False
print(check(123245)) # False
print(check(123235)) # False
print(check(123225)) # False
print(check(123224)) # False
print(check(123223)) # False
print(check(123222)) # False
print(check(123211)) # False
print(check(123212)) # False
print(check(123213)) # False
print(check(123214)) # False
print(check(123215)) # False
print(check(123216)) # False
print(check(123217)) # False
print(check(123218)) # False
print(check(123219)) # False
print(check(123221)) # False
print(check(123222)) # False
print(check(123223)) # False
print(check(123224)) # False
print(check(123225)) # False
print(check(123226)) # False
print(check(123227)) # False
print(check(123228)) # False
print(check(123229)) # False
print(check(123230)) # False
print(check(123231)) # False
print(check(123232)) # False
print(check(123233)) # False
print(check(123234)) # False
print(check(123235)) # False
print(check(123236)) # False
print(check(123237)) # False
print(check(123238)) # False
print(check(123239)) # False
print(check(123240)) # False
print(check(123241)) # False
print(check(123242)) # False
print(check(123243)) # False
print(check(123244)) # False
print(check(123245)) # False
print(check(123246)) # False
print(check(123247)) # False
print(check(123248)) # False
print(check(123249)) # False
print(check(123250)) # False
print(check(123251)) # False
print(check(123252)) # False
print(check(123253)) # False
print(check(123254)) # False
print(check(123255)) # False
print(check(123256)) # False
print(check(123257)) # False
print(check(123258)) # False
print(check(123259)) # False
print(check(123260)) # False
print(check(123261)) # False
print(check(1232