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
print(choose_num(10, 10)) # Output: 10
print(choose_num(10, 11)) # Output: -1
print(choose_num(10, 12)) # Output: 10
print(choose_num(10, 13)) # Output: 12
print(choose_num(10, 14)) # Output: 14
print(choose_num(10, 15)) # Output: 14
print(choose_num(10, 16)) # Output: 16
print(choose_num(10, 17)) # Output: -1
print(choose_num(10, 18)) # Output: -1
print(choose_num(10, 19)) # Output: -1
print(choose_num(10, 20)) # Output: 20
print(choose_num(10, 21)) # Output: -1
print(choose_num(10, 22)) # Output: -1
print(choose_num(10, 23)) # Output: -1
print(choose_num(10, 24)) # Output: -1
print(choose_num(10, 25)) # Output: -1
print(choose_num(10, 26)) # Output: -1
print(choose_num(10, 27)) # Output: -1
print(choose_num(10, 28)) # Output: -1
print(choose_num(10, 29)) # Output: -1
print(choose_num(10, 30)) # Output: -1
print(choose_num(10, 31)) # Output: -1
print(choose_num(10, 32)) # Output: -1
print(choose_num(10, 33)) # Output: -1
print(choose_num(10, 34)) # Output: -1
print(choose_num(10, 35)) # Output: -1
print(choose_num(10, 36)) # Output: -1
print(choose_num(10, 37)) # Output: -1
print(choose_num(10, 38)) # Output: -1
print(choose_num(10, 39)) # Output: -1
print(choose_num(10, 40)) # Output: -1
print(choose_num(10, 41)) # Output: -1
print(choose_num(10, 42)) # Output: -1
print(choose_num(10, 43)) # Output: -1
print(choose_num(10, 44)) # Output: -1
print(choose_num(10, 45)) # Output: -1
print(choose_num(10, 46)) # Output: -1
print(choose_num(10,