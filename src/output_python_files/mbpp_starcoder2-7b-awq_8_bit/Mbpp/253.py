"""
Write a python function that returns the number of integer elements in a given list.
assert count_integer([1,2,'abc',1.2]) == 2
"""

def count_integer(lst):
    count = 0
    for i in lst:
        if type(i) == int:
            count += 1
    return count

assert count_integer([1,2,'abc',1.2]) == 2
assert count_integer([1,2,3,4]) == 4
assert count_integer([1,2,3,4,5]) == 5
assert count_integer([1,2,3,4,5,6]) == 6
assert count_integer([1,2,3,4,5,6,7]) == 7
assert count_integer([1,2,3,4,5,6,7,8]) == 8
assert count_integer([1,2,3,4,5,6,7,8,9]) == 9
assert count_integer([1,2,3,4,5,6,7,8,9,10]) == 10
assert count_integer([1,2,3,4,5,6,7,8,9,10,11]) == 11
assert count_integer([1,2,3,4,5,6,7,8,9,10,11,12]) == 12
assert count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13]) == 13
assert count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14]) == 14
assert count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == 15
assert count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) == 16
assert count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]) == 17
assert count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]) == 18
assert count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == 19
assert count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == 20
assert count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]) == 21
assert count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]) == 22
assert count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]) == 23
assert count_integer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]) == 24
assert count_integer([1,2,3,4,5,