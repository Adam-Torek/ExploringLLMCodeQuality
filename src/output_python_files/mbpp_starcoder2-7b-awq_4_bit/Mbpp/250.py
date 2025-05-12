"""
Write a python function that takes in a tuple and an element and counts the occcurences of the element in the tuple.
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
"""

def count_X(tup, x):
    return tup.count(x)

assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),10) == 2
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),8) == 3
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),2) == 2
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),5) == 2
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),15) == 1
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),1) == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),100) == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),-1) == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),0) == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),1.5) == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),True) == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),False) == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),None) == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),"a") == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),"") == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)," ") == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),"1") == 0
assert count_X((10, 8, 5, 2,