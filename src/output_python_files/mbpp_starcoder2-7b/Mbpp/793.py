"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""

def last(arr,x):
    if len(arr) == 0:
        return -1
    if arr[len(arr)-1] == x:
        return len(arr)-1
    if arr[0] == x:
        return 0
    if arr[0] > x:
        return -1
    if arr[len(arr)-1] < x:
        return -1
    if arr[len(arr)-1] > x:
        return last(arr[0:len(arr)-1],x)

print(last([1,2,3],1))
print(last([1,2,3],2))
print(last([1,2,3],3))
print(last([1,2,3],4))
print(last([1,2,3],0))
print(last([1,2,3],5))
print(last([1,2,3],-1))
print(last([1,2,3],-2))
print(last([1,2,3],-3))
print(last([1,2,3],-4))
print(last([1,2,3],-5))
print(last([1,2,3],-6))
print(last([1,2,3],-7))
print(last([1,2,3],-8))
print(last([1,2,3],-9))
print(last([1,2,3],-10))
print(last([1,2,3],-11))
print(last([1,2,3],-12))
print(last([1,2,3],-13))
print(last([1,2,3],-14))
print(last([1,2,3],-15))
print(last([1,2,3],-16))
print(last([1,2,3],-17))
print(last([1,2,3],-18))
print(last([1,2,3],-19))
print(last([1,2,3],-20))
print(last([1,2,3],-21))
print(last([1,2,3],-22))
print(last([1,2,3],-23))
print(last([1,2,3],-24))
print(last([1,2,3],-25))
print(last([1,2,3],-26))
print(last([1,2,3],-27))
print(last([1,2,3],-28))
print(last([1,2,3],-29))
print(last([1,2,3],-30))
print(last([1,2,3],-31))
print(last([1,2,3],-32))
print(last([1,2,3],-33))
print(last([1,2,3],-34))
print(last([1,2,3],-35))
print(last([1,2,3],-36))
print(last([1,2,3],-37))
print(last([1,2,3],-38))
print(last([1,2,3],-39))
print(last([1,2,3],-40))
print(last([1,2,3],-41))
print(last([1,2,3],-42))
print(last([1,2,3],-43))
print(last([1,2,3],-44))
print(last([1,2,3],-45))
print(last([1,2,3],-46))
print(last([1,2,3],-47))
print(last([1,2,3],-48))
print(last([1,2,3],-49))
print(last([1,2,3],-50))
print(last([1,2,3],-51))
print(last([1,2,3],-52))
print(last([1,2,