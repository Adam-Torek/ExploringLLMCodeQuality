def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x % 2 != 0:
        x += 1
    if y % 2 != 0:
        y += 1
    if x > y:
        return choose_num(y, x)
    else:
        return y

# Testing the function
print(choose_num(12, 15))
print(choose_num(13, 12))
print(choose_num(10, 10))
print(choose_num(1, 10))
print(choose_num(10, 1))</s>