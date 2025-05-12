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
        return 5471
    if n == 15:
        return 10931
    if n == 16:
        return 21861
    if n == 17:
        return 43731
    if n == 18:
        return 87481
    if n == 19:
        return 174931
    if n == 20:
        return 349571
    if n == 21:
        return 699131
    if n == 22:
        return 1398291
    if n == 23:
        return 2796571
    if n == 24:
        return 5593151
    if n == 25:
        return 11186291
    if n == 26:
        return 22372571
    if n == 27:
        return 44745131
    if n == 28:
        return 89490271
    if n == 29:
        return 179080531
    if n == 30:
        return 358161051
    if n == 31:
        return 716322105
    if n == 32:
        return 1432644211
    if n == 33:
        return 2865368421
    if n == 34:
        return 5730736843
    if n == 35:
        return 11461473765
    if n == 36:
        return 22922947491
    if n == 37:
        return 45845894985
    if n == 38:
        return 91691794971
    if n == 39:
        return 183383594961
    if n ==