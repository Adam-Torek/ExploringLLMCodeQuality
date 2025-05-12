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
assert count_integer([1,2,'abc',1.2, 3.4]) == 3
assert count_integer([1,2,'abc',1.2, 3.4, 5.6]) == 4
assert count_integer([1,2,'abc',1.2, 3.4, 5.6, 7.8]) == 5
assert count_integer([1,2,'abc',1.2, 3.4, 5.6, 7.8, 9.10]) == 6
assert count_integer([1,2,'abc',1.2, 3.4, 5.6, 7.8, 9.10, 11.12]) == 7
assert count_integer([1,2,'abc',1.2, 3.4, 5.6, 7.8, 9.10, 11.12, 13.14]) == 8
assert count_integer([1,2,'abc',1.2, 3.4, 5.6, 7.8, 9.10, 11.12, 13.14, 15.16]) == 9
assert count_integer([1,2,'abc',1.2, 3.4, 5.6, 7.8, 9.10, 11.12, 13.14, 15.16, 17.18]) == 10
assert count_integer([1,2,'abc',1.2, 3.4, 5.6, 7.8, 9.10, 11.12, 13.14, 15.16, 17.18, 19.20]) == 11
assert count_integer([1,2,'abc',1.2, 3.4, 5.6, 7.8, 9.10, 11.12, 13.14, 15.16, 17.18, 19.20, 21.22]) == 12
assert count_integer([1,2,'abc',1.2, 3.4, 5.6, 7.8, 9.10, 11.12, 13.14, 15.16, 17.18, 19.20, 21.22, 23.24]) == 13
assert count_integer([1,2,'abc',1.2, 3.4, 5.6, 7.8, 9.10, 11.12, 13.14, 15.16, 17.18, 19.20, 21.22, 23.24, 25.26]) == 14
assert count_integer([1,2,'abc',1.2, 3.4, 5.6, 7.8, 9.10, 11.12, 13.14, 15.16, 17.18, 19.20, 21.22, 23.24, 25.26, 27.28]) == 15
assert count_integer([1,2,'abc',1.2, 3.4, 5.6, 7.8, 9.10, 11.12, 13.14, 15.16, 17.18, 19.20, 21.22, 23.24, 25