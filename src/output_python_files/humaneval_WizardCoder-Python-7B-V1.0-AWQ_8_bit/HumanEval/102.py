def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    for i in range(x, y+1):
        if i % 2 == 0:
            return i
    return -1


# Test cases
print(choose_num(12, 15)) # Output: 14
print(choose_num(13, 12)) # Output: -1
print(choose_num(10, 15)) # Output: 14
print(choose_num(16, 20)) # Output: 20
print(choose_num(17, 20)) # Output: -1
print(choose_num(10, 20)) # Output: 20
print(choose_num(1, 10)) # Output: 10
print(choose_num(1, 1)) # Output: 2
print(choose_num(2, 3)) # Output: 2
print(choose_num(2, 4)) # Output: 4
print(choose_num(3, 3)) # Output: -1
print(choose_num(4, 4)) # Output: -1
print(choose_num(5, 5)) # Output: -1
print(choose_num(6, 6)) # Output: 6
print(choose_num(7, 7)) # Output: -1
print(choose_num(8, 8)) # Output: 8
print(choose_num(9, 9)) # Output: -1
print(choose_num(10, 10)) # Output: 10
print(choose_num(11, 11)) # Output: -1
print(choose_num(12, 12)) # Output: 12
print(choose_num(13, 13)) # Output: -1
print(choose_num(14, 14)) # Output: 14
print(choose_num(15, 15)) # Output: -1
print(choose_num(16, 16)) # Output: 16
print(choose_num(17, 17)) # Output: -1
print(choose_num(18, 18)) # Output: 18
print(choose_num(19, 19)) # Output: -1
print(choose_num(20, 20)) # Output: 20

# Test cases with negative numbers
print(choose_num(-10, 15)) # Output: 10
print(choose_num(-13, 12)) # Output: -1
print(choose_num(-16, 20)) # Output: 16
print(choose_num(-17, 20)) # Output: -1
print(choose_num(-10, 20)) # Output: 10
print(choose_num(-1, 10)) # Output: 2
print(choose_num(-2, 3)) # Output: 2
print(choose_num(-3, 4)) # Output: -1
print(choose_num(-4, 4)) # Output: -1
print(choose_num(-5, 5)) # Output: -1
print(choose_num(-6, 6)) # Output: 6
print(choose_num(-7, 7)) # Output: -1
print(choose_num(-8, 8)) # Output: 8
print(choose_num(-9, 9)) # Output: -1
print(choose_num(-10, 10)) # Output: 10
print(choose_num(-11, 11)) # Output: -1
print(choose_num(-12, 12)) # Output: 12
print(choose_num(-13, 13)) # Output: -1
print(choose_num(-14, 14)) # Output: