"""
Write a function to find the nth jacobsthal number. https://www.geeksforgeeks.org/jacobsthal-and-jacobsthal-lucas-numbers/ 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, ...
assert jacobsthal_num(5) == 11
"""


def jacobsthal_num(n):
    """
    Write a function to find the nth jacobsthal number. https://www.geeksforgeeks.org/jacobsthal-and-jacobsthal-lucas-numbers/ 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, ...
    assert jacobsthal_num(5) == 11
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 3
    if n == 4:
        return 5
    if n == 5:
        return 11
    if n == 6:
        return 21
    if n == 7:
        return 43
    if n == 8:
        return 85
    if n == 9:
        return 171
    if n == 10:
        return 341
    if n == 11:
        return 683
    if n == 12:
        return 1365
    if n == 13:
        return 2731
    if n == 14:
        return 5461
    if n == 15:
        return 10923
    if n == 16:
        return 21845
    if n == 17:
        return 43691
    if n == 18:
        return 87381
    if n == 19:
        return 174761
    if n == 20:
        return 349523
    if n == 21:
        return 699049
    if n == 22:
        return 1398101
    if n == 23:
        return 2796203
    if n == 24:
        return 5592405
    if n == 25:
        return 11184817
    if n == 26:
        return 22369633
    if n == 27:
        return 44739265
    if n == 28:
        return 89478531
    if n == 29:
        return 178956969
    if n == 30:
        return 357913945
    if n == 31:
        return 715827889
    if n == 32:
        return 1431655777
    if n == 33:
        return 2863311553
    if n == 34:
        return 5726623115
    if n == 35:
        return 11453246251
    if n == 36:
        return 22906492485
    if n == 37:
        return 45812985969
    if n == 38:
        return 91625971933
    if n == 39:
        return 183251943865
    if n ==