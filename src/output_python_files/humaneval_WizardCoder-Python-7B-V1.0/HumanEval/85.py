def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum(lst[1::2])


def test_add():
    assert add([4, 2, 6, 7]) == 2
    assert add([1, 2, 3, 4, 5, 6, 7, 8]) == 2
    assert add([1, 3, 5, 7, 9]) == 0
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 2
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 4
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 6
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 8
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 10
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 12
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 14
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == 16
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 18
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert add