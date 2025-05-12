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
    elif n == 1:
        return 1
    else:
        return jacobsthal_num(n - 1) + jacobsthal_num(n - 2)


if __name__ == "__main__":
    print(jacobsthal_num(5))
    print(jacobsthal_num(10))
    print(jacobsthal_num(15))
    print(jacobsthal_num(20))
    print(jacobsthal_num(25))
    print(jacobsthal_num(30))
    print(jacobsthal_num(35))
    print(jacobsthal_num(40))
    print(jacobsthal_num(45))
    print(jacobsthal_num(50))
    print(jacobsthal_num(55))
    print(jacobsthal_num(60))
    print(jacobsthal_num(65))
    print(jacobsthal_num(70))
    print(jacobsthal_num(75))
    print(jacobsthal_num(80))
    print(jacobsthal_num(85))
    print(jacobsthal_num(90))
    print(jacobsthal_num(95))
    print(jacobsthal_num(100))
    print(jacobsthal_num(105))
    print(jacobsthal_num(110))
    print(jacobsthal_num(115))
    print(jacobsthal_num(120))
    print(jacobsthal_num(125))
    print(jacobsthal_num(130))
    print(jacobsthal_num(135))
    print(jacobsthal_num(140))
    print(jacobsthal_num(145))
    print(jacobsthal_num(150))
    print(jacobsthal_num(155))
    print(jacobsthal_num(160))
    print(jacobsthal_num(165))
    print(jacobsthal_num(170))
    print(jacobsthal_num(175))
    print(jacobsthal_num(180))
    print(jacobsthal_num(185))
    print(jacobsthal_num(190))
    print(jacobsthal_num(195))
    print(jacobsthal_num(200))
    print(jacobsthal_num(205))
    print(jacobsthal_num(210))
    print(jacobsthal_num(215))
    print(jacobsthal_num(